---
title: "ADR-0001: Use Kafka for job dispatch"
type: architecture
status: completed
topic: distributed-systems
difficulty: advanced
tags:
  - adr
  - kafka
  - messaging
created: 2026-08-30
updated: 2026-08-30
---

# ADR: Use Kafka for job dispatch in the Distributed Job Platform

## Status

Accepted — 2026-08-30

## Context

The [Distributed Job Platform](../../05-Projects/Distributed-Job-Platform/README.md)
must move submitted jobs from the API service to a horizontally scalable pool
of workers. The requirements that constrain the choice:

- **Durability.** A job accepted by the API must never be lost, including
  during a broker restart or a worker crash mid-execution.
- **Replay.** When a bug causes jobs to be processed incorrectly, it must be
  possible to re-run the affected window after deploying a fix. This is a
  learning platform; that will happen.
- **Horizontal scaling** of workers, with a clear, observable measure of
  whether they are keeping up.
- **Backpressure visibility.** Consumer lag must be a first-class metric, since
  Week 20 is dedicated to observability and failure testing.
- **Learning value.** The project exists to make the Month 4 material concrete:
  partitions, consumer groups, offsets and delivery semantics. This is a
  legitimate and explicitly weighted criterion here, and would not be in a
  commercial system.

Expected scale is modest — 100 jobs/s sustained, jobs taking seconds to
minutes. No option is excluded on throughput grounds; every candidate below
handles this load comfortably.

## Decision

**We will use Apache Kafka (KRaft mode) as the job dispatch mechanism**, with:

- one topic `jobs`, keyed by job ID
- partition count fixed at 12 from the start, sized for future worker
  parallelism rather than current load
- `acks=all` with `min.insync.replicas=2` in any multi-broker deployment
- `enable.idempotence=true` on the producer
- workers as a single consumer group, committing offsets **after** processing
- a dead-letter topic `jobs.dlq` after 5 failed attempts

The API will **not** publish to Kafka directly. It writes the job and an outbox
row in one PostgreSQL transaction, and a relay publishes from the outbox — see
[Outbox Pattern](../../03-Concepts/Messaging/Delivery-Semantics/Outbox%20Pattern.md).
That is a separate decision and will get its own ADR.

## Alternatives

| Alternative | Why it was rejected |
| --- | --- |
| **PostgreSQL as a queue** (`SELECT ... FOR UPDATE SKIP LOCKED`) | Genuinely the best engineering fit for 100 jobs/s: one fewer system, transactional enqueue with no outbox needed, and simple operations. Rejected **only** because it would skip the Month 4 learning objectives entirely. Recorded plainly, because this is the option a commercial project at this scale should probably choose. |
| **RabbitMQ** | Excellent work queue with per-message ack and a mature DLQ. Rejected because it deletes messages on ack, so there is no replay, and it teaches less about partitioned logs. |
| **AWS SQS** | Least operational effort, and near-zero cost at this scale. Rejected for vendor lock-in in a learning project meant to stay locally runnable, and because visibility timeouts hide the offset mechanics that are the point of the exercise. |
| **Redis Streams** | Lightweight and already a plausible dependency. Rejected on durability: persistence is weaker than Kafka's, and the failure modes are exactly the ones this project must not have. |
| **Direct HTTP to workers** | No durability, no buffering, no backpressure. The API would have to own retries and worker discovery. Rejected outright. |

## Consequences

### Positive

- Durable, replayable job history with configurable retention
- Consumer lag is a direct, meaningful measure of worker health
- Partitions give a clean, bounded parallelism model with per-key ordering
- Directly exercises [Kafka](../../03-Concepts/Messaging/Kafka/Kafka.md) and
  [Message Delivery Semantics](../../03-Concepts/Messaging/Delivery-Semantics/Message%20Delivery%20Semantics.md)
- [Lab 06](../../04-Labs/06-Kafka-Delivery/README.md) can run directly against
  the real system

### Negative

- **Substantially more operational complexity** than a database queue: brokers,
  topics, consumer groups, rebalances and retention all become things that can
  break at 2 a.m.
- Kafka is the most resource-hungry component in an otherwise light stack
- Partition count is effectively permanent: raising it later breaks key-to-
  partition affinity for existing keys
- Managed Kafka has a high cost floor, so any cloud deployment is expensive
  relative to the rest of the system
- Rebalance behaviour will need tuning (`max.poll.interval.ms` against actual
  job duration) — this is the most likely source of production surprise

### Neutral

- Delivery is **at-least-once**. Workers must be idempotent regardless; that
  requirement would exist with any of these alternatives
- The outbox pattern is required because the API writes to two systems. This is
  a consequence of introducing a broker at all, not of choosing Kafka
- If the platform were ever taken to production at this scale, revisiting this
  ADR in favour of PostgreSQL would be a reasonable outcome, and the reasoning
  above is recorded so that conversation can be short

## Related Concepts

- [Kafka](../../03-Concepts/Messaging/Kafka/Kafka.md)
- [Queues and Pub-Sub](../../03-Concepts/Messaging/Queues/Queues%20and%20Pub-Sub.md)
- [Message Delivery Semantics](../../03-Concepts/Messaging/Delivery-Semantics/Message%20Delivery%20Semantics.md)
- [Outbox Pattern](../../03-Concepts/Messaging/Delivery-Semantics/Outbox%20Pattern.md)
- [Idempotency](../../03-Concepts/Distributed-Systems/Fundamentals/Idempotency.md)

---
title: Distributed System
type: concept
status: learning
topic: distributed-systems
difficulty: beginner
tags:
  - distributed-systems
  - fundamentals
created: 2026-08-30
updated: 2026-08-30
---

# Distributed System

## Learning Goals

- [ ] State what makes a system distributed rather than merely multi-process
- [ ] Name three problems that exist only once a network is involved
- [ ] Explain why "the network is reliable" is a fallacy and what it costs

## What Is It?

A system whose components run on separate machines, communicate only by
passing messages over a network, and have no shared clock or shared memory.
Lamport's definition is the sharpest: *a system in which the failure of a
computer you did not even know existed can render your own computer unusable*.

The defining property is not scale. It is that **the components fail
independently**, and no component can distinguish a failed peer from a slow
one.

## Why Does It Matter?

Every guarantee that is free in a single process — a consistent view of
memory, an ordering of events, an operation that either happened or did not —
has to be rebuilt explicitly, at a cost, once the system spans machines. Most
of this knowledge base is about what those reconstructions cost.

## Core Concepts

- **Independent failure** — one node can die while others continue
- **Unreliable network** — messages can be lost, delayed, duplicated, reordered
- **No global clock** — wall clocks drift; there is no single "now"
- **Asynchrony** — no upper bound on message delay you can safely assume
- **Concurrency** — events happen simultaneously with no natural total order

## The Fallacies of Distributed Computing

Peter Deutsch's list. Each is an assumption that is false, and each has a
matching design response.

| Fallacy | Reality | Response |
| --- | --- | --- |
| The network is reliable | Messages are lost | Retries, acknowledgements |
| Latency is zero | Every hop costs | Batching, caching, locality |
| Bandwidth is infinite | Links saturate | Compression, backpressure |
| The network is secure | It is not | TLS, authn/authz at every hop |
| Topology doesn't change | It changes constantly | Service discovery |
| There is one administrator | There are many | Automation, IaC |
| Transport cost is zero | Egress is billed | Cost-aware architecture |
| The network is homogeneous | It is not | Explicit protocols, versioning |

## Failure Scenarios

| Failure | What you observe | Why it is hard |
| --- | --- | --- |
| Node crash | Requests time out | Indistinguishable from slowness |
| Network partition | Both sides still alive | Each side thinks the other died |
| Slow node ("gray failure") | p99 latency climbs | Healthy checks still pass |
| Clock skew | Timestamps disagree | Ordering by wall clock breaks |

## Real-World Systems

Any of: Kubernetes, Kafka, PostgreSQL with replicas, S3, DNS. Pick one and
identify each of the core concepts above inside it.

## Hands-on Experiment

Run [Lab 01 — RPC](../../../04-Labs/01-RPC/README.md). Kill the server
mid-request and observe what the client can and cannot conclude.

## My Understanding

> Write this from memory, sources closed. See [Learning Principles](../../../01-Roadmap/learning-principles.md).

## Questions

- [ ] Is a single machine running two processes that talk over localhost a
      distributed system? What changes when the socket crosses a NIC?
- [ ] Which of the eight fallacies has bitten systems I already work on?

## Related Concepts

- [Partial Failure](Partial%20Failure.md)
- [Latency and Throughput](Latency%20and%20Throughput.md)
- [RPC](RPC.md)
- [CAP Theorem](../Consistency/CAP%20Theorem.md)

## Resources

- Kleppmann, *Designing Data-Intensive Applications*, ch. 8
- Lamport, "Distribution" (1987) — the one-sentence definition
- [MIT 6.5840](https://pdos.csail.mit.edu/6.5840/), Lecture 1

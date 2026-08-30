---
title: System Design
type: architecture
status: completed
topic: architecture
difficulty: intermediate
tags:
  - architecture
  - system-design
created: 2026-08-30
updated: 2026-08-30
---

# System Design

Two kinds of document live here.

## 1. Studies of real systems

Pick a system, work out how it actually functions, and write it up:
requirements, architecture, data flow, failure behaviour, and the trade-off it
chose. Use `99-Templates/Project-Note.md`.

Candidates that pay for the time:

- [ ] Kafka — why a log rather than a queue
- [ ] Kubernetes — reconciliation on top of consensus
- [ ] S3 — durability without availability
- [ ] DynamoDB — Dynamo's ideas, productised
- [ ] Spanner — TrueTime and the cost of external consistency

## 2. Practice problems

Classic design exercises, done properly: requirements first, capacity estimates
second, architecture third, and **failure analysis last and most carefully**.

- [ ] URL shortener — the read-heavy, cache-everything shape
- [ ] Rate limiter — distributed counters and their consistency needs
- [ ] Notification system — fan-out and delivery semantics
- [ ] Distributed cache — invalidation and consistent hashing
- [ ] Metrics pipeline — high-volume ingest and time-series storage

## The method

1. **Requirements** — functional, then non-functional with actual numbers
2. **Estimates** — QPS, storage, bandwidth. Order of magnitude is enough
3. **API** — the contract, before the boxes
4. **Data model** — access patterns first, schema second
5. **Architecture** — the diagram
6. **Bottlenecks** — what breaks first at 10x
7. **Failure analysis** — for each component: what happens when it dies?

Step 7 is where the learning is. Anyone can draw six boxes.

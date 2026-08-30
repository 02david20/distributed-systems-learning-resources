---
title: Job Platform — Design
type: project
status: learning
topic: distributed-systems
difficulty: advanced
tags:
  - project
  - design
created: 2026-08-30
updated: 2026-08-30
---

# Job Platform — Design

Design documents: the arguments and trade-offs behind the architecture. One
file per topic, e.g. `Job State Machine.md`, `Idempotency Scheme.md`,
`Retry Policy.md`.

A design document explores; an [ADR](../../../06-Architecture/ADRs/README.md)
records what was decided and why. When a design settles, write the ADR and link
it from here.

## Planned documents

- [ ] `Job State Machine.md` — states, transitions, who owns `status`
- [ ] `Idempotency Scheme.md` — key format, storage, retention window
- [ ] `Retry Policy.md` — per-dependency timeouts, attempts, backoff, DLQ rules
- [ ] `Data Model.md` — `jobs`, `outbox`, `idempotency_keys`, indexes
- [ ] `API Contract.md` — endpoints, status codes, error semantics

---
title: Architecture Decision Records
type: architecture
status: completed
topic: architecture
difficulty: beginner
tags:
  - architecture
  - adr
created: 2026-08-30
updated: 2026-08-30
---

# Architecture Decision Records

| ADR | Decision | Status |
| --- | --- | --- |
| [0001](0001-use-kafka-for-job-dispatch.md) | Use Kafka for job dispatch in the Distributed Job Platform | Accepted |

## Conventions

- **Filename**: `NNNN-short-kebab-case-title.md`, numbered sequentially.
  ADRs are the one place where the human-readable naming rule is relaxed — the
  number is the identity, and it needs to sort
- **Immutable**: an accepted ADR is not edited. Superseding it means writing a
  new one and setting the old one's status to `Superseded by ADR-NNNN`
- **Template**: `99-Templates/ADR.md`
- **Status**: `Proposed` → `Accepted` | `Rejected` → `Superseded`

## When to write one

Write an ADR when the decision is expensive to reverse, when it was contested,
or when a reasonable person would later ask *why*. Typical triggers here:
choosing a messaging system, a consistency model, a partition key, or a
failure-handling strategy.

Do **not** write one for a decision that is obvious, cheap to reverse, or
already implied by an earlier ADR.

---
title: MIT 6.5840 — Distributed Systems
type: course
status: learning
topic: distributed-systems
difficulty: advanced
tags:
  - course
  - mit
  - distributed-systems
  - raft
created: 2026-08-30
updated: 2026-08-30
---

# MIT 6.5840 — Distributed Systems

## Course

| Field | Value |
| --- | --- |
| Provider | MIT CSAIL (Robert Morris et al.) |
| URL | <https://pdos.csail.mit.edu/6.5840/> |
| Format | Video lectures, papers, four programming labs in Go |
| Cost | Free (materials are public) |
| Estimated effort | 6–10 h/week during Month 3 |
| Started | *not yet* |
| Target completion | End of Month 3 (Lab 3C), Lab 4 optional |

This is the single most valuable resource in the plan. The labs are the point:
reading about Raft produces a comfortable illusion of understanding that
Lab 3B removes within an hour.

## Objectives

- [ ] Implement MapReduce (Lab 1)
- [ ] Implement a fault-tolerant key/value server (Lab 2)
- [ ] Implement Raft leader election (Lab 3A)
- [ ] Implement Raft log replication (Lab 3B)
- [ ] Implement Raft persistence and crash recovery (Lab 3C)
- [ ] Read and be able to discuss the assigned papers, not just skim them

## Schedule

| Week | Planned | Actual |
| --- | --- | --- |
| 9 | Lectures 1–4; Lab 1 (MapReduce) |  |
| 10 | Raft paper; Lab 3A (elections) |  |
| 11 | Lab 3B (log replication), 3C (persistence) |  |
| 12 | Consolidate; write up |  |

## Modules

| # | Topic | Status | Note |
| --- | --- | --- | --- |
| 1 | Introduction, MapReduce | not started |  |
| 2 | RPC and threads (Go) | not started |  |
| 3 | GFS | not started |  |
| 4 | Primary/backup replication | not started |  |
| 5 | Fault tolerance: Raft (1) | not started | [Raft](../../03-Concepts/Distributed-Systems/Consensus/Raft.md) |
| 6 | Fault tolerance: Raft (2) | not started |  |
| 7 | ZooKeeper | not started |  |
| 8 | Distributed transactions | not started | [Two-Phase Commit](../../03-Concepts/Databases/Distributed-Transactions/Two-Phase%20Commit.md) |
| 9 | Spanner | not started |  |

## Progress

See [progress.md](progress.md).

`░░░░░░░░░░░░` 0%

## Notes

Per-lecture notes live in [`notes/`](notes/README.md). Durable *concepts* belong in
[03-Concepts](../../03-Concepts/README.md), not here — this folder holds
course-specific material only.

## Labs

Lab code lives in a **separate repository** — MIT asks that solutions are not
published, and this repository is public. Keep only observations and design
notes here, never solution code.

## Questions

- [ ] Go's concurrency model is assumed. Is a refresher needed first?
- [ ] Which papers are load-bearing and which can be skimmed?

## Final Assessment

Self-assessed: do the provided test suites pass, including the `-race` runs
and the repeated-run harness?

## Lessons Learned

<!-- Fill in at the end of Month 3. -->

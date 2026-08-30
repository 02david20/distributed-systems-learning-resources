---
title: Job Platform — Experiments
type: project
status: learning
topic: distributed-systems
difficulty: advanced
tags:
  - project
  - experiments
created: 2026-08-30
updated: 2026-08-30
---

# Job Platform — Experiments

Measurements against the running system. Each experiment states a question, a
prediction and a measured answer — the same discipline as
[04-Labs](../../../04-Labs/README.md), scoped to this project.

## Planned

| # | Question | Week |
| --- | --- | --- |
| E1 | What is the submission p99 at 100 jobs/s? | 17 |
| E2 | How does end-to-end latency change with partition count? | 18 |
| E3 | How many duplicates does a `kill -9` of a worker produce? | 19 |
| E4 | How long does the outbox relay take to drain a 10k backlog? | 19 |
| E5 | What is the measured recovery time after a PostgreSQL failover? | 20 |
| E6 | Which injected failure is invisible on the dashboards? | 20 |

E6 feeds directly into
[Lab 07 — Failure Testing](../../../04-Labs/07-Failure-Testing/README.md).

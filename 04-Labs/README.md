---
title: Labs
type: lab
status: completed
topic: meta
difficulty: beginner
tags:
  - lab
  - index
created: 2026-08-30
updated: 2026-08-30
---

# Labs

Each lab answers **one specific engineering question** and records a
prediction before the run. A lab is finished when **Actual Result** is filled
in and the prediction has been judged right or wrong — not when the code runs.

| # | Lab | Question | Status |
| --- | --- | --- | --- |
| 01 | [RPC](01-RPC/README.md) | What can a client conclude when an RPC times out? | not started |
| 02 | [Timeouts and Retries](02-Timeouts-Retries/README.md) | Do retries help or hurt a saturated dependency? | **worked example** |
| 03 | [Idempotency](03-Idempotency/README.md) | Does an idempotency key actually prevent duplicate side effects? | not started |
| 04 | [Replication](04-Replication/README.md) | How much data does an async replica lose on failover? | not started |
| 05 | [Leader Election](05-Leader-Election/README.md) | What happens when the leader node crashes? | not started |
| 06 | [Kafka Delivery](06-Kafka-Delivery/README.md) | Can offset commit timing lose or duplicate messages? | not started |
| 07 | [Failure Testing](07-Failure-Testing/README.md) | How does the job platform behave under injected failure? | not started |

## Rules

1. **One question per lab.** If it needs "and", it is two labs.
2. **Predict first.** Write **Expected Result** before running anything.
3. **Record raw output.** Paste it before summarising it.
4. **Judge the prediction.** Being wrong is the most valuable outcome.
5. **Clean up.** Every lab ends with a teardown, checked for anything billable.

Start from `99-Templates/Lab-Note.md`.

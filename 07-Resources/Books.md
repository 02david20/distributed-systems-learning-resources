---
title: Books
type: resource
status: completed
topic: meta
difficulty: beginner
tags:
  - resources
  - books
created: 2026-08-30
updated: 2026-08-30
---

# Books

## Essential

### Designing Data-Intensive Applications — Martin Kleppmann

O'Reilly, 2017 (2nd edition in progress).

The backbone of Months 1–4. Unusually rigorous for a practitioner book, with
a bibliography that doubles as a curated paper list. Chapters map onto the
roadmap almost exactly:

| Chapter | Roadmap week |
| --- | --- |
| 1 — Reliable, Scalable, Maintainable | Week 1 |
| 5 — Replication | Week 5 |
| 6 — Partitioning | Week 14 |
| 7 — Transactions | Week 13 |
| 8 — The Trouble with Distributed Systems | Weeks 1–2 |
| 9 — Consistency and Consensus | Weeks 6–10 |
| 11 — Stream Processing | Weeks 15–16 |

If only one book gets read, this is it.

## Strongly recommended

### Site Reliability Engineering — Google

Free online: <https://sre.google/sre-book/table-of-contents/>

Operational reality: SLOs, error budgets, cascading failures, incident
response. Chapters 3–4 and 21–22 are the load-bearing ones for this plan.

### Database Internals — Alex Petrov

O'Reilly, 2019. Part I is storage engines (B-trees, LSM trees); Part II is
distributed systems from a database perspective — failure detection, leader
election, consensus, with more implementation detail than DDIA.

### Understanding Distributed Systems — Roberto Vitillo

A more approachable on-ramp than DDIA. Good if a topic in DDIA is not landing.

## Reference

### Kafka: The Definitive Guide — Narkhede, Shapira, Palino

O'Reilly, 2nd ed. The reference for Weeks 15–16. Read the design and
delivery-semantics chapters; skim the operations chapters until needed.

### Programming Kubernetes — Hausenblas & Schimanski

For Week 22. The clearest explanation of the controller pattern, informers and
work queues in print.

### Systems Performance — Brendan Gregg

Methodology for performance work: the USE method, latency analysis, and how not
to be fooled by averages. Relevant to Week 1 and to every lab afterwards.

## Distributed Systems for Fun and Profit — Mikito Takada

Free: <https://book.mixu.net/distsys/>

Short and free. A good two-hour orientation before starting Month 1.

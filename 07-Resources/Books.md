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

## Free and short

### Distributed Systems for Fun and Profit — Mikito Takada

<https://book.mixu.net/distsys/>

A good two-hour orientation before starting Month 1. Covers the abstractions,
time and order, and replication, without asking for a month of your life.

### Distributed Systems — Tanenbaum & Van Steen (4th ed.)

<https://www.distributed-systems.net/index.php/books/ds4/>

Free PDF from the authors. The standard university textbook: broader and more
formal than DDIA, and the better reference when you want the *definition* of
something rather than the engineering trade-off.

### Scalable Web Architecture and Distributed Systems — Kate Matsudaira

<https://aosabook.org/en/v2/distsys.html>

One chapter of *The Architecture of Open Source Applications*. A compact tour
of the pieces — caches, proxies, indexes, queues — and why each exists.

### An Introduction to Distributed Systems — Kyle Kingsbury

<https://github.com/aphyr/distsys-class>

Course notes rather than a book, and unusually precise about what the words
mean. Pairs well with the [Jepsen analyses](https://jepsen.io/analyses).

## Theory

Read these if the theory becomes interesting on its own terms. None is required
by the roadmap, and none is a good first book.

| Book | What it is for |
| --- | --- |
| **Distributed Algorithms** — Nancy Lynch | The canonical formal reference. Dense, rigorous, and the place proofs actually live |
| **Distributed Computing: Fundamentals, Simulations and Advanced Topics** — Attiya & Welch | More approachable than Lynch, same territory |
| **Principles of Distributed Systems** — ETH Zurich ([free PDF](https://disco.ethz.ch/courses/podc_allstars/)) | Lecture notes; good for a single topic in isolation |
| **Impossibility Results for Distributed Computing** — Attiya & Ellen | What provably *cannot* be done, and why. Short |

## Worth knowing about

### Designing Distributed Systems — Brendan Burns

Patterns for container-based systems (sidecar, ambassador, adapter, scatter-
gather) from a Kubernetes co-founder. Thin, and useful in Month 6.

### Making reliable distributed systems in the presence of software errors — Joe Armstrong

<https://erlang.org/download/armstrong_thesis_2003.pdf>

Erlang's PhD thesis. "Let it crash" as a coherent philosophy rather than a
slogan — supervision trees, isolation and failure as a normal event. Genuinely
changes how you think about error handling.

### Systemantics: How Systems Work and Especially How They Fail — John Gall

Not a technical book. A short, funny, and uncomfortably accurate account of why
large systems fail in ways nobody designed. "A complex system that works is
invariably found to have evolved from a simple system that worked."

!!! tip "Do not buy all of these"
    Two books carry the six months: **DDIA** and the **SRE book** (free).
    Everything above is a reference to reach for when a specific question
    appears, not a reading list to work through.

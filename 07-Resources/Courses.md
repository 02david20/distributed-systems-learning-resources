---
title: Courses
type: resource
status: completed
topic: meta
difficulty: beginner
tags:
  - resources
  - courses
created: 2026-08-30
updated: 2026-08-30
---

# Courses

## Primary

### MIT 6.5840 — Distributed Systems

<https://pdos.csail.mit.edu/6.5840/>

Free, public materials: lectures, papers and four Go labs. The Raft labs are
the single highest-value exercise in the whole plan — they convert reading
comprehension into actual understanding, usually painfully.

Tracked in [02-Courses/MIT-6.5840](../02-Courses/MIT-6.5840/README.md).

### UIUC Cloud Computing Specialization

<https://www.coursera.org/specializations/cloud-computing>

Indranil Gupta's specialization. Broader and more theoretical than 6.5840:
gossip protocols, membership, key-value stores, stream processing. Good
complement; most courses can be audited free.

Tracked in [02-Courses/UIUC-Cloud-Computing](../02-Courses/UIUC-Cloud-Computing/README.md).

## Supplementary

### MIT 6.824 archives

<https://pdos.csail.mit.edu/6.824/>

The previous incarnation of 6.5840. Older lecture recordings are still
available and sometimes clearer on specific topics.

### CMU 15-445 — Database Systems

<https://15445.courses.cs.cmu.edu/>

Andy Pavlo's course. The reference for transactions, MVCC, WAL and query
execution — everything in Month 4, Week 13, done properly.

### Stanford CS 244B — Distributed Systems

<https://www.scs.stanford.edu/24sp-cs244b/>

Reading-heavy graduate course; useful as a curated paper list.

### Cambridge — Concurrent and Distributed Systems (Kleppmann)

<https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/> ·
[YouTube playlist](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB)

Lectures 9–16 are the distributed half, by the author of DDIA. Eight lectures
of ~40 minutes with free written notes. The best *structured* introduction on
this page: logical time, broadcast ordering, consensus, replication and CRDTs,
in that order. Watch these in Month 2 if DDIA chapter 9 feels dense.

### KTH — Reliable Distributed Algorithms, Parts 1 and 2

[Part 1](https://www.edx.org/learn/computer-programming/kth-royal-institute-of-technology-reliable-distributed-algorithms-part-1) ·
Part 2 on edX

The algorithms course: failure detectors, broadcast abstractions, shared
memory, consensus, replicated state machines — built up formally, layer by
layer. Closer to Lynch's book than to DDIA. Take it if the *why does this
algorithm work* question keeps recurring.

### ETH Zurich — Distributed Systems

<https://disco.ethz.ch/courses>

Strong on fault tolerance (models, consensus, agreement) and replication
(2PC, 3PC, Paxos), with free lecture notes. Useful as a second explanation when
one source has not landed.

### CMU 15-440 — Distributed Systems

<https://www.cs.cmu.edu/~dga/15-440/>

Assignments in Go, which makes it a natural companion to 6.5840. Good coverage
of RPC and naming, which most courses rush.

### Cloud provider training

Vendor certification paths (AWS Solutions Architect, Google Professional Cloud
Architect) are reasonable for breadth on managed services and pricing models.
They are weak on distributed systems fundamentals; use them for the cloud
half of the plan only.

## Cross-checked against

The course list above was cross-checked against
[awesome-distributed-systems](https://github.com/theanalyst/awesome-distributed-systems),
which also carries entries for
[distributedsystemscourse.com](http://www.distributedsystemscourse.com/) (a
beginner course by Chris Colohan, ex-Google) and Georgia Tech's Software
Defined Networking on Coursera. Neither is on the roadmap: the first overlaps
with Month 1, and the second is a specialism this plan does not need.

## Deliberately not listed

Bootcamp-style "system design interview" courses. Interview preparation is a
different goal from understanding, and optimising for it early produces
confident hand-waving. Revisit after Month 4 if interviews are the aim.

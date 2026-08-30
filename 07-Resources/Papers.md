---
title: Papers
type: resource
status: completed
topic: meta
difficulty: advanced
tags:
  - resources
  - papers
created: 2026-08-30
updated: 2026-08-30
---

# Papers

Read in roadmap order. Reading a paper properly means being able to state its
problem, its central idea, and what it gave up — three sentences, from memory.

## Consensus and replication

| Paper | Why | Week |
| --- | --- | --- |
| Ongaro & Ousterhout, [*In Search of an Understandable Consensus Algorithm*](https://raft.github.io/raft.pdf) (2014) | Raft. Read the **extended** version | 10 |
| Ongaro, *Consensus: Bridging Theory and Practice* (2014) | The thesis; the only good treatment of membership change and snapshots | 11 |
| Lamport, *Paxos Made Simple* (2001) | The classic. Read after Raft, when it makes sense | 12 |
| Hunt et al., *ZooKeeper: Wait-free Coordination* (2010) | The other coordination service; contrast with etcd | 12 |
| Schneider, *Implementing Fault-Tolerant Services Using the State Machine Approach* (1990) | The framework everything else assumes | 10 |

## Foundations

| Paper | Why | Week |
| --- | --- | --- |
| Lamport, *Time, Clocks, and the Ordering of Events* (1978) | Happens-before; the origin of logical time | 6 |
| Fischer, Lynch & Paterson, *Impossibility of Distributed Consensus with One Faulty Process* (1985) | FLP. Why consensus needs timing assumptions | 9 |
| Gilbert & Lynch, *Brewer's Conjecture...* (2002) | The formal CAP result | 7 |
| Chandra & Toueg, *Unreliable Failure Detectors for Reliable Distributed Systems* (1996) | Completeness vs. accuracy | 9 |
| Herlihy & Wing, *Linearizability* (1990) | The definition, from the source | 6 |
| Saltzer, Reed & Clark, *End-to-End Arguments in System Design* (1984) | Why the endpoints must verify | 2 |

## Systems

| Paper | Why | Week |
| --- | --- | --- |
| Ghemawat et al., *The Google File System* (2003) | Design for commodity hardware and constant failure | 5 |
| Dean & Ghemawat, *MapReduce* (2004) | 6.5840 Lab 1 | 9 |
| DeCandia et al., *Dynamo* (2007) | Consistent hashing, quorums, eventual consistency | 8 |
| Chang et al., *Bigtable* (2006) | Wide-column storage at scale | 14 |
| Corbett et al., *Spanner* (2012) | TrueTime; buying external consistency with atomic clocks | 14 |
| Kreps et al., *Kafka: a Distributed Messaging System for Log Processing* (2011) | Kafka's original design rationale | 15 |
| Verbitski et al., *Amazon Aurora* (2017) | "The log is the database" taken literally | 13 |
| Burrows, *The Chubby Lock Service* (2006) | Lock services and the lessons from operating one | 9 |

## Operations and failure

| Paper | Why | Week |
| --- | --- | --- |
| Dean & Barroso, *The Tail at Scale* (2013) | Tail latency and fan-out amplification | 1 |
| Huang et al., *Gray Failure* (2017) | Why "up" and "working" differ | 1 |
| Yuan et al., *Simple Testing Can Prevent Most Critical Failures* (2014) | Most catastrophic failures come from unhandled error paths | 20 |
| Mohan et al., *ARIES* (1992) | WAL-based recovery, in full | 13 |
| Gray & Lamport, *Consensus on Transaction Commit* (2006) | 2PC and Paxos, unified | 14 |

## Critiques worth reading

- Kleppmann, [*A Critique of the CAP Theorem*](https://arxiv.org/abs/1509.05393) (2015)
- Waldo et al., *A Note on Distributed Computing* (1994) — why RPC transparency fails
- Abadi, *Consistency Tradeoffs in Modern Distributed Database System Design* — PACELC

## Where to find them

- [Papers We Love](https://paperswelove.org/) — curated collections
- [The Morning Paper archive](https://blog.acolyer.org/) — Adrian Colyer's summaries; read the summary, then the paper
- [MIT 6.5840 schedule](https://pdos.csail.mit.edu/6.5840/schedule.html) — every assigned paper, with reading questions

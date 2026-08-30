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

The **Tier** column is the honest triage:

- **1** — read in full, more than once. These change how you think
- **2** — read in full, once, when the roadmap reaches them
- **3** — know the result and the diagram; read fully only if the topic becomes
  your problem

---

## Foundations

| Paper | Tier | Why | Week |
| --- | --- | --- | --- |
| Lamport, [*Time, Clocks, and the Ordering of Events*](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) (1978) | **1** | Happens-before and logical clocks. The origin of ordering without a global clock | 6 |
| Fischer, Lynch & Paterson, [*Impossibility of Distributed Consensus with One Faulty Process*](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf) (1985) | **1** | FLP. Consensus is impossible in a purely asynchronous system with one crash — so every real system smuggles in a timing assumption. Read [the Paper Trail walkthrough](https://www.the-paper-trail.org/post/2008-08-13-a-brief-tour-of-flp-impossibility/) alongside it | 9 |
| Gilbert & Lynch, [*Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*](https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf) (2002) | 2 | The formal CAP result — much narrower than the folklore version | 7 |
| Herlihy & Wing, *Linearizability: A Correctness Condition for Concurrent Objects* (1990) | 2 | The definition, from the source | 6 |
| Terry et al., [*Session Guarantees for Weakly Consistent Replicated Data*](https://www.cs.utexas.edu/~dahlin/Classes/GradOS/papers/SessionGuaranteesPDIS.pdf) (1994) | 2 | Where read-your-writes, monotonic reads and monotonic writes come from. Standard vocabulary in every later paper | 6 |
| Saltzer, Reed & Clark, *End-to-End Arguments in System Design* (1984) | 2 | Why only the endpoints can confirm anything | 2 |
| Schneider, *Implementing Fault-Tolerant Services Using the State Machine Approach* (1990) | 2 | The framework consensus papers assume you already know | 10 |
| Lamport, Shostak & Pease, [*The Byzantine Generals Problem*](https://lamport.azurewebsites.net/pubs/byz.pdf) (1982) | 3 | The 3f+1 bound. Mostly out of scope here, but the vocabulary is everywhere | 12 |

## Consensus

| Paper | Tier | Why | Week |
| --- | --- | --- | --- |
| Ongaro & Ousterhout, [*In Search of an Understandable Consensus Algorithm*](https://raft.github.io/raft.pdf) (2014) | **1** | Raft. Read the **extended** version. See [Raft](../03-Concepts/Distributed-Systems/Consensus/Raft.md) | 10 |
| Ongaro, [*Consensus: Bridging Theory and Practice*](https://github.com/ongardie/dissertation) (2014) | **1** | The thesis. The only good treatment of membership changes and log compaction | 11 |
| Lamport, [*Paxos Made Simple*](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf) (2001) | 2 | The readable Paxos paper. Read *after* Raft, when the problem is familiar | 12 |
| Chandra, Griesemer & Redstone, [*Paxos Made Live — An Engineering Perspective*](https://research.google/pubs/paxos-made-live-an-engineering-perspective/) (2007) | **1** | Google on everything the theory papers leave out: disk corruption, membership, testing. The best "theory meets production" paper in the field | 12 |
| Burrows, [*The Chubby Lock Service*](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/) (2006) | 2 | Paxos as a service; the direct ancestor of ZooKeeper, etcd and Consul | 9 |
| Hunt et al., *ZooKeeper: Wait-free Coordination for Internet-scale Systems* (2010) | 2 | The other coordination service; contrast its guarantees with etcd's | 12 |
| Lamport, [*The Part-Time Parliament*](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf) (1998) | 3 | The original Paxos paper, famously hard. Read for the history, not the algorithm | — |
| Castro & Liskov, [*Practical Byzantine Fault Tolerance*](http://pmg.csail.mit.edu/papers/osdi99.pdf) (1999) | 3 | BFT made practical. Relevant if blockchains or adversarial settings come up | — |
| Gray & Lamport, *Consensus on Transaction Commit* (2006) | 2 | 2PC and Paxos unified — why a replicated coordinator stops 2PC blocking | 14 |

## Storage and databases

| Paper | Tier | Why | Week |
| --- | --- | --- | --- |
| DeCandia et al., [*Dynamo: Amazon's Highly Available Key-value Store*](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) (2007) | **1** | Consistent hashing, quorums, vector clocks, read repair — the AP design, in one paper. Rare in that a production-system paper redirected academic research | 8 |
| Ghemawat, Gobioff & Leung, [*The Google File System*](https://research.google/pubs/the-google-file-system/) (2003) | 2 | Designing for constant failure on commodity hardware | 5 |
| Chang et al., [*Bigtable*](https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/) (2006) | 2 | Wide-column storage; the ancestor of HBase and Cassandra's data model | 14 |
| Corbett et al., [*Spanner*](https://research.google/pubs/spanner-googles-globally-distributed-database/) (2012) | 2 | TrueTime: buying external consistency with atomic clocks and a bounded uncertainty window | 14 |
| Lakshman & Malik, *Cassandra: A Decentralized Structured Storage System* (2010) | 3 | Dynamo's ideas plus Bigtable's data model | — |
| Verbitski et al., *Amazon Aurora: Design Considerations...* (2017) | 2 | "The log is the database" taken literally. Pairs with [Write-Ahead Log](../03-Concepts/Databases/Transactions/Write-Ahead%20Log.md) | 13 |
| Mohan et al., *ARIES: A Transaction Recovery Method* (1992) | 2 | WAL-based recovery in full detail | 13 |
| Weil et al., [*CRUSH: Controlled, Scalable, Decentralized Placement of Replicated Data*](https://www.ssrc.ucsc.edu/media/pubs/6ec6b0cd3f8c0a5b6dd8c0dfaf3f7e1b6d0d3f8b.pdf) (2006) | 3 | Placement without a central directory; the basis of Ceph | — |

## Messaging and streams

| Paper | Tier | Why | Week |
| --- | --- | --- | --- |
| Kreps, [*The Log: What every software engineer should know*](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) (2013) | **1** | Not a paper, but the clearest statement of the idea behind [Replicated Log](../03-Concepts/Distributed-Systems/Consensus/Replicated%20Log.md) | 15 |
| Kreps, Narkhede & Rao, [*Kafka: a Distributed Messaging System for Log Processing*](http://notes.stephenholiday.com/Kafka.pdf) (2011) | 2 | Kafka's original design rationale, before the ecosystem grew around it | 15 |
| Shapiro et al., [*Conflict-free Replicated Data Types*](https://pages.lip6.fr/Marc.Shapiro/papers/RR-7687.pdf) (2011) | 2 | Strong eventual consistency without coordination. Used in Riak, Redis, Akka and every collaborative editor | 6 |

## Failure, operations and observability

| Paper | Tier | Why | Week |
| --- | --- | --- | --- |
| Dean & Barroso, *The Tail at Scale* (2013) | **1** | Tail latency and fan-out amplification. Short, and it reframes performance work permanently | 1 |
| Yuan et al., *Simple Testing Can Prevent Most Critical Failures* (2014) | **1** | 92% of catastrophic failures came from incorrect handling of non-fatal errors. Read before [Lab 07](../04-Labs/07-Failure-Testing/README.md) | 20 |
| Huang et al., *Gray Failure: The Achilles' Heel of Cloud-Scale Systems* (2017) | 2 | Why "up" and "working" are different, and why health checks miss it | 1 |
| Chandra & Toueg, *Unreliable Failure Detectors for Reliable Distributed Systems* (1996) | 2 | Completeness vs. accuracy — the trade-off behind every timeout you pick | 9 |
| Das, Gupta & Motivala, *SWIM: Scalable Weakly-consistent Infection-style Process Group Membership* (2002) | 2 | Gossip-based failure detection; O(n) instead of O(n²) | 9 |
| Sigelman et al., [*Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/) (2010) | 2 | The design behind Zipkin, Jaeger and OpenTelemetry. Directly relevant to Week 20 | 20 |
| Agache et al., [*Firecracker: Lightweight Virtualization for Serverless Applications*](https://www.usenix.org/conference/nsdi20/presentation/agache) (2020) | 3 | What a serverless cold start actually is | 3 |

## Critiques and correctives

Read these *after* the paper they argue with — they are much more useful as
corrections than as introductions.

- Kleppmann, [*A Critique of the CAP Theorem*](https://arxiv.org/abs/1509.05393) (2015)
- Waldo et al., *A Note on Distributed Computing* (1994) — why RPC transparency
  cannot work, written while the industry was building RPC frameworks anyway
- Abadi, *Consistency Tradeoffs in Modern Distributed Database System Design* —
  PACELC, the formulation that applies when there is no partition
- Bailis & Ghodsi, *Eventual Consistency Today: Limitations, Extensions, and
  Beyond* — what "eventual" actually means in production

## How to read a paper

Keshav's three-pass method, which is the standard advice because it works:

1. **Pass 1 (~10 min)** — title, abstract, introduction, section headings,
   conclusion. Decide whether to continue.
2. **Pass 2 (~1 h)** — read for the argument. Skip proofs. Mark references you
   need. You should be able to summarise the paper afterwards.
3. **Pass 3 (several h)** — reconstruct the work. Challenge every assumption.
   Only for papers you need to *implement* or genuinely disagree with.

Tier 1 papers get pass 3. Tier 3 papers get pass 1.

## Finding papers

- [Papers We Love](https://paperswelove.org/) — curated, with recorded talks
- [The Morning Paper archive](https://blog.acolyer.org/) — Adrian Colyer's
  summaries. Read the summary to triage, then read the paper
- [MIT 6.5840 schedule](https://pdos.csail.mit.edu/6.5840/schedule.html) —
  every assigned paper with reading questions attached
- [awesome-consensus](https://github.com/dgryski/awesome-consensus) — deeper
  than this list on consensus specifically

!!! tip "Link rot is normal"
    Several of these are hosted on university and corporate pages that move.
    If a link 404s, search the exact title on Google Scholar or Papers We Love —
    the papers themselves are all freely available.

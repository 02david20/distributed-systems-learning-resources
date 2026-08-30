---
title: Blogs and Reading Lists
type: resource
status: completed
topic: meta
difficulty: beginner
tags:
  - resources
  - blogs
  - reading-lists
created: 2026-08-30
updated: 2026-08-30
---

# Blogs and Reading Lists

Engineering writing that meets the standard in [Resources](README.md): teams
describing their own systems, practitioners explaining something better than
the primary source does, and curated lists that lead to primary sources.

## Essential reading

### Amazon Builders' Library

<https://aws.amazon.com/builders-library/>

The single best free writing on distributed systems *practice*. Each article is
written by a principal engineer about a problem they actually operate. Start
with timeouts and retries, health checks, load shedding, and static stability.

Referenced throughout [Timeouts and Retries](../03-Concepts/Distributed-Systems/Fundamentals/Timeouts%20and%20Retries.md)
and [Load Balancing](../03-Concepts/Cloud/Networking/Load%20Balancing.md).

### Notes on Distributed Systems for Young Bloods — Jeff Hodges

<https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/>

Short, blunt, and about the operational reality rather than the theory.
"Distributed systems are different because they fail often" is the thesis, and
it is the right one. Read it in Week 1.

### Distributed systems theory for the distributed systems engineer — Henry Robinson

<https://www.the-paper-trail.org/post/2014-08-09-distributed-systems-theory-for-the-distributed-systems-engineer/>

A breadth-first reading path through the theory, with an opinion about what
matters and what can be skipped. Useful as a map of the territory before
committing six months to it.

### An Introduction to Distributed Systems — Kyle Kingsbury (aphyr)

<https://github.com/aphyr/distsys-class>

The written companion to his distributed systems course. Unusually clear on
what the words actually mean — availability, consistency, ordering — from
someone who breaks databases for a living.

## Blogs worth following

| Blog | Author | Why |
| --- | --- | --- |
| [The Paper Trail](https://www.the-paper-trail.org/) | Henry Robinson | Readable explanations of hard papers — FLP, Paxos, consensus in general |
| [aphyr](https://aphyr.com/tags/Distributed-Systems) | Kyle Kingsbury | The Jepsen posts: real databases, real violations, real evidence |
| [All Things Distributed](https://www.allthingsdistributed.com/) | Werner Vogels (Amazon CTO) | Design rationale behind AWS services, from the top |
| [Martin Kleppmann](https://martin.kleppmann.com/) | Martin Kleppmann | The author of DDIA; the distributed-locking post is required reading |
| [Marc Brooker](https://brooker.co.za/blog/) | AWS senior principal | Deep, practical writing on queues, retries, consistency and formal methods |
| [Dan Luu](https://danluu.com/) | Dan Luu | Empirical, sceptical; *Files are hard* is essential if you touch storage |
| [High Scalability](http://highscalability.com/) | various | Architecture breakdowns of large services — useful raw material for `06-Architecture/System-Design/` |

## Individual posts worth the time

| Post | Why |
| --- | --- |
| [The Log: What every software engineer should know about real-time data's unifying abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) — Jay Kreps | Long, and worth every minute. The idea behind [Replicated Log](../03-Concepts/Distributed-Systems/Consensus/Replicated%20Log.md) and [Kafka](../03-Concepts/Messaging/Kafka/Kafka.md) |
| [How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) — Kleppmann | The fencing-token argument. Changes how you think about [Leader Election](../03-Concepts/Distributed-Systems/Consensus/Leader%20Election.md) |
| [There is No Now](https://queue.acm.org/detail.cfm?id=2745385) — Justin Sheehy | Why simultaneity is not a thing you get to have |
| [Files are hard](https://danluu.com/file-consistency/) — Dan Luu | Durability assumptions that turn out to be false. Read before trusting `fsync` |
| [SWIM protocol explained](https://asafdav2.github.io/2017/swim-protocol/) | The gossip failure detector, walked through. Pairs with [Failure Detection](../03-Concepts/Distributed-Systems/Fault-Tolerance/Failure%20Detection.md) |
| [On Designing and Deploying Internet-Scale Services](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton_html/) — James Hamilton | A 2007 checklist that is still mostly correct |
| [The C10K problem](http://www.kegel.com/c10k.html) — Dan Kegel | Historical, but the clearest explanation of why concurrency models matter |

## Testing and verification

- **[Jepsen](https://jepsen.io/)** — Kyle Kingsbury's framework and, more
  importantly, the [analyses](https://jepsen.io/analyses). Reading one analysis
  of a database you use is a bracing experience. Also the best reference for
  [Consistency Models](../03-Concepts/Distributed-Systems/Consistency/Consistency%20Models.md)
- **[Testing Distributed Systems](https://asatarin.github.io/testing-distributed-systems/)**
  — Andrey Satarin's curated list: how Google, Amazon, Netflix, Microsoft and
  Dropbox actually test. Directly relevant to
  [Lab 07](../04-Labs/07-Failure-Testing/README.md)
- **[Verdi](http://verdi.uwplse.org/)** — a framework for formally verifying
  distributed systems. Read if formal methods appeal; skip otherwise

## Meta lists

Lists of lists. Useful when you want breadth on a specific subtopic.

| List | Focus |
| --- | --- |
| [awesome-distributed-systems](https://github.com/theanalyst/awesome-distributed-systems) | The general list this repository's resources were cross-checked against |
| [awesome-consensus](https://github.com/dgryski/awesome-consensus) | Consensus protocols specifically — deeper than the general lists |
| [A Distributed Systems Reading List](https://dancres.github.io/Pages/) | Dan Creswell's annotated theory-and-industry list |
| [Distributed Systems Readings](https://henryr.github.io/distributed-systems-readings/) | Henry Robinson's course-oriented list |
| [Readings in Distributed Systems](http://christophermeiklejohn.com/distributed/systems/2013/07/12/readings-in-distributed-systems.html) | Christopher Meiklejohn; strong on theory |
| [CMU 15-749 required readings](http://www.andrew.cmu.edu/course/15-749/READINGS/required/) | A university's opinion on what is mandatory |
| [Papers We Love — distributed systems](https://github.com/papers-we-love/papers-we-love/tree/main/distributed_systems) | Papers with community discussion attached |

!!! warning "Meta lists are for finding things, not for reading"
    A list of 200 links produces the feeling of progress and none of the
    substance. Use these to locate the *one* paper that answers a question you
    already have, then go read it properly — see
    [Learning Principles](../01-Roadmap/learning-principles.md).

## Research venues

For when a topic has no good secondary source yet.

- **[PODC / DISC](https://podc-disc.github.io/)** — the theory conferences
- **[OSDI and NSDI](https://www.usenix.org/conferences)** (USENIX) — where most
  of the systems papers in [Papers](Papers.md) were published
- **[SOSP](https://sosp.org/)** — biennial; Dynamo and many others
- **[Springer Distributed Computing](https://www.springer.com/journal/446)** — the journal

---
title: Videos
type: resource
status: completed
topic: meta
difficulty: beginner
tags:
  - resources
  - videos
created: 2026-08-30
updated: 2026-08-30
---

# Videos

## Lecture series

### MIT 6.5840 lectures

<https://pdos.csail.mit.edu/6.5840/schedule.html>

Robert Morris's lectures, recorded and public. The Raft lectures are the
clearest available explanation of the algorithm short of implementing it.

### Martin Kleppmann — Distributed Systems (Cambridge)

<https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB>

Eight lectures, roughly 40 minutes each, with free written notes. Excellent on
logical time, broadcast ordering and consistency models. The best structured
introduction if DDIA feels dense.

### CMU Database Group

<https://www.youtube.com/@CMUDatabaseGroup>

Andy Pavlo's 15-445 and 15-721 lectures, plus the "Database Talks" seminar
series where system authors present their own designs.

## Individual talks

| Talk | Why |
| --- | --- |
| Kyle Kingsbury, *Jepsen* talks | Watching real databases violate their advertised guarantees, with evidence. Bracing |
| Camille Fournier, *Consensus systems for the skeptical architect* | Honest treatment of when you do and do not need consensus |
| Martin Kleppmann, *Turning the database inside out* | Event logs as the primary abstraction |
| Rich Hickey, *Simple Made Easy* | Not distributed systems, but the clearest available thinking about complexity |
| Jeff Dean, *Building Software Systems at Google Scale* | Where the latency numbers everyone quotes come from |

## Conference channels

- **[Strange Loop](https://www.youtube.com/@StrangeLoopConf)** — archived; consistently high quality on distributed systems
- **[USENIX](https://www.youtube.com/@USENIX)** — OSDI, NSDI and SREcon talks, usually by the paper authors
- **[CNCF](https://www.youtube.com/@cncf)** — KubeCon; variable, but the deep-dive tracks are worth filtering for

## A caution

Video is good for intuition and bad for retention. A talk that feels
illuminating produces almost nothing a week later unless it is followed by
writing something down or running something. Pair every talk with a note or a
lab — see [Learning Principles](../01-Roadmap/learning-principles.md).

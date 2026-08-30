---
title: Job Platform — Architecture
type: project
status: learning
topic: distributed-systems
difficulty: advanced
tags:
  - project
  - architecture
created: 2026-08-30
updated: 2026-08-30
---

# Job Platform — Architecture

Diagrams and structural descriptions. Design *arguments* go in
[`design/`](../design/README.md); decisions become
[ADRs](../../../06-Architecture/ADRs/README.md).

## Component view

```mermaid
flowchart TD
    subgraph Edge
        LB[Load Balancer]
    end
    subgraph "Control path"
        API[API Service]
        PG[(PostgreSQL)]
        REL[Outbox Relay]
    end
    subgraph "Work path"
        K[Kafka]
        W[Worker pool]
        OS[(Object Store)]
    end
    LB --> API
    API --> PG
    PG --> REL
    REL --> K
    K --> W
    W --> OS
    W --> PG
```

## Job state machine

```mermaid
stateDiagram-v2
    [*] --> pending: POST /jobs (committed)
    pending --> running: worker claims
    running --> succeeded: result written
    running --> pending: worker crash (redelivery)
    running --> failed: attempts exhausted
    failed --> [*]
    succeeded --> [*]
```

The `running → pending` edge is the important one: it is not an error path, it
is the normal consequence of at-least-once delivery. Every transition must be
idempotent because it can be replayed.

## Deployment view

```mermaid
flowchart TD
    subgraph "AZ a"
        API1[API] --> PGP[(PG primary)]
        W1[Workers]
    end
    subgraph "AZ b"
        API2[API] --> PGS[(PG standby)]
        W2[Workers]
    end
    PGP -.replication.- PGS
    ALB[Load Balancer] --> API1
    ALB --> API2
```

## Open architecture questions

- [ ] How many Kafka partitions, and what is the message key?
- [ ] Outbox relay: polling or CDC? (ADR-0002)
- [ ] Where does job status live — PostgreSQL only, or also a cache?
- [ ] Do workers need leader election, or is the consumer group sufficient?

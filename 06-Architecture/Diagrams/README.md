---
title: Diagrams
type: architecture
status: completed
topic: architecture
difficulty: beginner
tags:
  - architecture
  - diagrams
  - mermaid
created: 2026-08-30
updated: 2026-08-30
---

# Diagrams

All diagrams in this repository are [Mermaid](https://mermaid.js.org/) in
fenced code blocks. They render natively in **both** Obsidian and MkDocs
Material, stay diffable in Git, and need no binary assets.

Full authoring guidance is in [docs/mermaid.md](../../docs/mermaid.md).

## Conventions used here

| Element | Convention |
| --- | --- |
| Data stores | `[(Cylinder)]` — `PG[(PostgreSQL)]` |
| Services | `[Rectangle]` |
| Decisions | `{Diamond}` |
| External actors | `((Circle))` |
| Failures / removed paths | Dotted arrows `-.->` |
| Multi-line labels | `<br/>` inside quotes |

Quote any label containing punctuation: `A["hash(key) mod n"]`.

## Reusable diagrams

### Leader/follower replication

```mermaid
flowchart LR
    C[Client] -->|writes| L[(Leader)]
    L -->|replication| F1[(Follower 1)]
    L -->|replication| F2[(Follower 2)]
    C -->|reads| F1
    C -->|reads| F2
```

### Quorum under partition

```mermaid
flowchart LR
    subgraph Majority["Majority — 3 of 5, keeps serving"]
        N1((N1)) --- N2((N2)) --- N3((N3))
    end
    subgraph Minority["Minority — 2 of 5, must refuse writes"]
        N4((N4)) --- N5((N5))
    end
    Majority -. partition .- Minority
```

### Request with retry and backoff

```mermaid
flowchart TD
    R[Request] --> A[Attempt]
    A -->|success| S[Done]
    A -->|non-retryable| F[Fail fast]
    A -->|timeout / 5xx| B{Attempts and<br/>budget left?}
    B -->|no| F
    B -->|yes| W["Wait: random(0, 2^n × base)"]
    W --> A
```

### Reconciliation loop

```mermaid
flowchart LR
    D[Desired state] --> C{Compare}
    O[Observed state] --> C
    C -->|drift| A[Act]
    A --> O
    C -->|match| W[Wait]
    W --> C
```

### Async job pipeline

```mermaid
flowchart TD
    U[User] --> API
    API --> DB[(Database)]
    DB --> Relay[Outbox relay]
    Relay --> Q[Kafka]
    Q --> W1[Worker]
    Q --> W2[Worker]
    W1 --> S[(Object store)]
    W2 --> S
```

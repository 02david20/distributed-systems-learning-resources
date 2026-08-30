---
title: Idempotency
type: concept
status: learning
topic: distributed-systems
difficulty: intermediate
tags:
  - distributed-systems
  - reliability
  - idempotency
created: 2026-08-30
updated: 2026-08-30
---

# Idempotency

## Learning Goals

- [ ] Define idempotency precisely, including what "same effect" covers
- [ ] Design an idempotency key scheme with correct storage and expiry
- [ ] Explain why exactly-once delivery is impossible but exactly-once
      *effect* is achievable

## What Is It?

An operation is idempotent if performing it more than once has the same effect
on system state as performing it once. `SET x = 5` is idempotent;
`x = x + 5` is not. `DELETE /jobs/42` is idempotent; `POST /jobs` is not.

The subtlety: "effect" means **all** effects, including emails sent, money
moved and messages published — not just the row in the database.

## Why Does It Matter?

[Partial Failure](Partial%20Failure.md) guarantees that clients will sometimes
retry requests that already succeeded. Idempotency is what makes that retry
safe, and therefore what makes [Timeouts and Retries](Timeouts%20and%20Retries.md)
usable at all. Without it, at-least-once delivery corrupts data.

## Core Concepts

### Natural vs. engineered idempotency

- **Naturally idempotent**: reads, absolute writes, deletes, `PUT` semantics
- **Engineered**: made idempotent with a client-supplied key plus server-side
  deduplication

### The idempotency key protocol

1. Client generates a unique key (UUIDv4) **once per logical operation** — not
   once per attempt
2. Client sends the key with every attempt of that operation
3. Server atomically inserts the key into a store. If the insert succeeds, this
   is the first attempt: do the work, record the response against the key
4. If the insert conflicts, this is a retry: return the stored response without
   re-executing

The atomic insert is the whole mechanism. It must be in the same transaction
as the side effect, or a crash between the two reintroduces the bug.

```sql
-- The critical section: one transaction, or nothing works.
BEGIN;
  INSERT INTO idempotency_keys (key, status)
  VALUES ($1, 'in_progress');          -- UNIQUE violation => this is a retry
  INSERT INTO jobs (id, payload) VALUES ($2, $3);
COMMIT;
```

### Key lifetime

Keys cannot be kept forever. Choose a retention window longer than the maximum
plausible retry window (24 hours is common) and expire them. State the window
in the API documentation — after it passes, a retry *will* duplicate.

## How It Works

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant D as Database
    C->>S: POST /jobs (Idempotency-Key: abc)
    S->>D: BEGIN; INSERT key abc; INSERT job; COMMIT
    D-->>S: ok
    S--xC: response lost
    C->>S: POST /jobs (Idempotency-Key: abc) [retry]
    S->>D: INSERT key abc
    D-->>S: unique violation
    S->>D: SELECT stored response
    S-->>C: 200 + original response (no new job)
```

## Failure Scenarios

| Failure | Consequence | Fix |
| --- | --- | --- |
| Key generated per attempt | Every retry is a new operation | Generate once, per logical operation |
| Key stored outside the transaction | Crash between them duplicates work | One transaction |
| Same key, different payload | Ambiguous | Reject with 422; hash the payload and compare |
| Key expired before the retry | Duplicate | Document the window; keep it > max retry window |
| Concurrent retries | Both may execute | Unique constraint makes one lose; return 409 or wait |

## Real-World Systems

- Stripe's `Idempotency-Key` header — the canonical public API design
- Kafka's idempotent producer: producer ID + monotonic sequence number per
  partition, deduplicated by the broker
- HTTP method semantics: `GET`, `PUT`, `DELETE` idempotent; `POST` not

## Hands-on Experiment

[Lab 03 — Idempotency](../../../04-Labs/03-Idempotency/README.md)

## My Understanding

> Sources closed. Explain why "exactly-once delivery" is a marketing term but
> "exactly-once processing" is achievable.

## Questions

- [ ] Where does the job platform need idempotency keys — API only, or workers too?
- [ ] How do idempotency keys interact with the [Outbox Pattern](../../Messaging/Delivery-Semantics/Outbox%20Pattern.md)?

## Related Concepts

- [Timeouts and Retries](Timeouts%20and%20Retries.md)
- [Partial Failure](Partial%20Failure.md)
- [Message Delivery Semantics](../../Messaging/Delivery-Semantics/Message%20Delivery%20Semantics.md)
- [Outbox Pattern](../../Messaging/Delivery-Semantics/Outbox%20Pattern.md)

## Resources

- [Stripe: Idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- [AWS Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- Kleppmann, *DDIA*, ch. 11 §"Exactly-once message processing"

---
title: Disaster Recovery
type: concept
status: learning
topic: cloud
difficulty: intermediate
tags:
  - cloud
  - reliability
  - disaster-recovery
  - rpo
  - rto
created: 2026-08-30
updated: 2026-08-30
---

# Disaster Recovery

## Learning Goals

- [ ] Define RPO and RTO and derive them from business requirements
- [ ] Compare the four standard DR strategies on cost and RTO
- [ ] Explain why an untested backup should be assumed not to exist

## What Is It?

Restoring service after an event that redundancy alone does not cover: region
loss, data corruption, ransomware, or an operator deleting the production
database. High availability handles component failure;
**disaster recovery handles losing the whole thing**.

## RPO and RTO

```mermaid
flowchart LR
    B[Last good backup] -->|"RPO — data you lose"| D[Disaster]
    D -->|"RTO — time you are down"| R[Service restored]
```

- **RPO — Recovery Point Objective**: how much data you can afford to lose,
  measured in time. RPO of 15 minutes means backups/replication no more than
  15 minutes behind
- **RTO — Recovery Time Objective**: how long you can afford to be down

Both are **business decisions with a price tag**, not technical preferences.
RPO = 0 requires synchronous replication and pays for it on every single write.

## The four strategies

| Strategy | RTO | RPO | Cost | How |
| --- | --- | --- | --- | --- |
| **Backup & restore** | Hours–days | Hours | Lowest | Restore from backups into new infrastructure |
| **Pilot light** | Tens of minutes | Minutes | Low | Data replicated; compute off until needed |
| **Warm standby** | Minutes | Seconds–minutes | Medium | Scaled-down copy running continuously |
| **Hot standby / multi-site** | Seconds | ~0 | Highest | Full capacity live in both places |

## The 3-2-1 rule

Three copies of the data, on two different media, one off-site. In cloud terms:
the live database, an automated backup in the same region, and a copy in a
**different region and a different account**, because a compromised or
mis-billed account can take its own backups with it.

## Failure Scenarios

| Failure | Consequence | Mitigation |
| --- | --- | --- |
| Backups never restored | Restore fails when it matters | **Scheduled restore drills**; measure the actual RTO |
| Backup in the same region/account | Lost with the primary | Cross-region, cross-account copies |
| Logical corruption replicated instantly | Replicas are corrupt too | Point-in-time recovery, delayed replica |
| Archive-tier restore | Retrieval takes hours, blowing the RTO | Keep recent backups in a hot tier |
| Runbook out of date | Recovery improvised under pressure | Version the runbook with the code; rehearse |
| DR region has no capacity | Cannot scale up during a regional event | Reserved capacity, or accept the risk explicitly |

!!! danger "A backup that has never been restored is a hypothesis"
    The only evidence that a backup works is a completed restore. Put the drill
    on a calendar and record the measured RTO next to the target.

## Real-World Systems

- PostgreSQL PITR: base backup + archived WAL restores to any second
- `etcdctl snapshot save` / `restore` — the Kubernetes equivalent
- AWS Backup, cross-region snapshot copy, S3 Cross-Region Replication

## Hands-on Experiment

Week 23: define RPO and RTO for the job platform, delete the database, restore
it from backup and **time it**. Compare the measured numbers against the
targets and write down the gap.

## My Understanding

> Sources closed. Explain why replication is not a backup.

## Questions

- [ ] What RPO/RTO do the job platform's job records genuinely need?
- [ ] What would the DR plan cost per month at each of the four strategies?

## Related Concepts

- [High Availability](High%20Availability.md)
- [Failure Recovery](../../Distributed-Systems/Fault-Tolerance/Failure%20Recovery.md)
- [Database Replication](../../Databases/Replication/Database%20Replication.md)
- [Storage Models](../Storage/Storage%20Models.md)

## Resources

- [AWS: Disaster recovery of workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [PostgreSQL: Continuous Archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)

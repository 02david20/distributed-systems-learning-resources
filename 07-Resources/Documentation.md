---
title: Documentation
type: resource
status: completed
topic: meta
difficulty: beginner
tags:
  - resources
  - documentation
created: 2026-08-30
updated: 2026-08-30
---

# Documentation

Official documentation, by system. When a question has an answer here and in a
blog post, the answer here is the one that is current.

## Kubernetes

- [Documentation home](https://kubernetes.io/docs/home/)
- [Cluster architecture](https://kubernetes.io/docs/concepts/architecture/) — Week 21
- [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) — Week 22
- [Leases and leader election](https://kubernetes.io/docs/concepts/architecture/leases/)
- [Operating etcd clusters](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- [API concepts — watch, resource versions](https://kubernetes.io/docs/reference/using-api/api-concepts/) — the part that explains how controllers really work

## etcd

- [Documentation](https://etcd.io/docs/)
- [FAQ](https://etcd.io/docs/latest/faq/) — including why cluster size should be odd
- [Hardware recommendations](https://etcd.io/docs/latest/op-guide/hardware/) — the disk-latency argument
- [Disaster recovery](https://etcd.io/docs/latest/op-guide/recovery/)
- [raft library](https://github.com/etcd-io/raft) — production reference implementation

## Kafka

- [Documentation](https://kafka.apache.org/documentation/)
- [Design](https://kafka.apache.org/documentation/#design) — read this section in full
- [Producer and consumer configuration](https://kafka.apache.org/documentation/#configuration) — `acks`, `enable.idempotence`, `max.poll.interval.ms`
- [KRaft](https://kafka.apache.org/documentation/#kraft) — Raft replacing ZooKeeper
- [Confluent: exactly-once semantics](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/)

## PostgreSQL

- [Documentation](https://www.postgresql.org/docs/current/)
- [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — Week 13
- [Concurrency control / MVCC](https://www.postgresql.org/docs/current/mvcc.html)
- [Write-ahead logging](https://www.postgresql.org/docs/current/wal-intro.html)
- [High availability and replication](https://www.postgresql.org/docs/current/high-availability.html) — Week 5
- [Continuous archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) — Week 23

## Cloud provider

> **Choose one provider and record it here.** Going deep on one beats going
> shallow on three; the concepts transfer, the console details do not.
>
> Chosen provider: *not yet chosen — decide in Week 3.*

### AWS

- [Documentation](https://docs.aws.amazon.com/)
- [Builders' Library](https://aws.amazon.com/builders-library/) — the best free writing on distributed systems practice anywhere. Timeouts and retries, health checks, load shedding, static stability
- [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) — Week 4
- [Disaster recovery whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) — Week 23

### Google Cloud

- [Documentation](https://cloud.google.com/docs)
- [Architecture Framework](https://cloud.google.com/architecture/framework)
- [VPC overview](https://cloud.google.com/vpc/docs/vpc) — global VPC differs meaningfully from AWS
- [SRE resources](https://sre.google/books/)

### Azure

- [Documentation](https://learn.microsoft.com/azure/)
- [Architecture Center](https://learn.microsoft.com/azure/architecture/)
- [Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)

## Tooling used in the labs

- [Docker Compose](https://docs.docker.com/compose/)
- [MinIO](https://min.io/docs/minio/linux/index.html) — local S3-compatible object storage
- [Toxiproxy](https://github.com/Shopify/toxiproxy) — deterministic network fault injection
- [Prometheus](https://prometheus.io/docs/) and [Grafana](https://grafana.com/docs/)
- [OpenTelemetry](https://opentelemetry.io/docs/)
- [gRPC](https://grpc.io/docs/)

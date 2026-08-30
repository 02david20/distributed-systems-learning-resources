---
title: Learning Principles
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - meta
  - learning
created: 2026-08-30
updated: 2026-08-30
---

# Learning Principles

The rules this knowledge base is built around. They exist because the
default failure mode of technical self-study is producing beautiful notes
that copy documentation and teach nothing.

## 1. Explanation beats transcription

Every concept note has a **My Understanding** section that must be written
with all sources closed. If it cannot be written, the note is not finished —
regardless of how complete the other sections look.

## 2. A lab answers exactly one question

A lab is not "learn Kafka". A lab is "does a consumer lose messages if it
commits offsets before processing?". One question, a prediction written down
*before* running anything, and a recorded verdict on whether the prediction
was right.

Being wrong in a lab is the highest-value outcome available. It is the only
signal that a mental model was broken.

## 3. Predict first, then measure

Write the **Expected Result** before the **Actual Result**. Filling in the
expectation afterwards feels the same and teaches nothing.

## 4. Failure is the subject, not an edge case

Distributed systems are defined by partial failure. Any note about a
mechanism that does not describe how it behaves when a node dies, a network
partitions, or a message is delivered twice is an incomplete note. Hence the
**Failure Scenarios** section in every template.

## 5. Notes are linked, not filed

The folder a note lives in matters far less than what it links to. Prefer
adding a link in **Related Concepts** over reorganising folders. The graph is
the structure; the folders are just storage.

## 6. Depth over coverage

Twelve concepts understood well beat sixty summarised. When behind schedule,
cut breadth, not the **My Understanding** and lab sections.

## 7. The repository must outlive the tools

Plain Markdown, YAML frontmatter, ordinary relative links, Mermaid. No
proprietary storage, no plugin database, no build step that rewrites content.
If Obsidian disappears tomorrow, everything here still opens in any editor.

## 8. Read primary sources

Papers, official documentation, and university courses over blog posts.
A blog post is acceptable as a pointer to a primary source, not as a
replacement for one.

## 9. Issues track actions, notes hold knowledge

A GitHub Issue says "read the Raft paper §5.2 and write up leader election".
The knowledge that comes out of it lives in the Markdown note, never in the
issue body. See [Git Workflow](../docs/git-workflow.md).

## 10. Review on a schedule

Every fourth week is a review week. Re-read the **My Understanding** sections
written three weeks earlier and correct the ones that now look wrong. Spaced
correction is the cheapest retention mechanism available.

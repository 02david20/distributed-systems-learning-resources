---
title: Inbox
type: concept
status: inbox
topic: meta
difficulty: beginner
tags:
  - inbox
created: 2026-08-30
updated: 2026-08-30
---

# Inbox

Capture point. Anything half-formed lands here: a question from a lecture, a
link, a paragraph that will become a note later.

**Nothing in this folder is published.** `00-Inbox/` is excluded by path in
`mkdocs.yml`, so writing here is friction-free — no need to think about whether
it is fit to read.

New notes are created here by default (`.obsidian/app.json` sets
`newFileFolderPath`).

## Processing

Empty it weekly, as part of the end-of-week review:

1. **Is it a concept?** Move it to `03-Concepts/<Area>/<Subarea>/`, apply
   `99-Templates/Learning-Note.md`, set `status: learning`, add it to
   [the concept index](../03-Concepts/README.md).
2. **Is it a question?** Move it into the **Questions** section of the note it
   belongs to.
3. **Is it a task?** Open a GitHub Issue and delete the file.
4. **Is it a resource?** Add it to the right file in `07-Resources/` — with a
   sentence on why it is worth anyone's time — and delete the file.
5. **Is it none of those?** Delete it. Most captures are not worth keeping, and
   an inbox that is never emptied stops being a capture point and becomes a
   graveyard.

The only rule: **the inbox is emptied, not archived.**

---
title: Conventions
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - handbook
  - conventions
created: 2026-08-30
updated: 2026-08-30
---

# Conventions

## File naming

**Use the concept's real name, capitalised, with spaces.**

```text
Raft.md
Leader Election.md
CAP Theorem.md
Message Delivery Semantics.md
```

Not:

```text
20260830123456.md        # timestamp IDs — unreadable in every tool
note-839201.md           # opaque
raft_consensus_v2.md     # versioning belongs in Git
```

The filename is what appears in Obsidian's search, in the graph, in link
autocomplete and in the site navigation. Optimising it for a machine costs
readability everywhere, and Git already provides the identity a timestamp ID
was invented to give.

### Exceptions

| Case | Convention | Why |
| --- | --- | --- |
| ADRs | `0001-use-kafka-for-job-dispatch.md` | The number *is* the identity, and it must sort |
| Top-level folders | `03-Concepts`, `99-Templates` | Numeric prefixes force a deliberate order |
| Repository-level files | `mkdocs.yml`, `requirements.txt` | Tooling requires these exact names |

### How spaces behave in each tool

This is the one place where readability has a real cost, so it is worth being
precise about what happens.

| Tool | Behaviour with spaces |
| --- | --- |
| **Obsidian** | Fully supported. Autocomplete inserts the correct link automatically |
| **Markdown links** | A raw space breaks the link. It must be `%20`-encoded — `[Raft](Leader%20Election.md)` — or the target wrapped in angle brackets: `[Raft](<Leader Election.md>)`. Obsidian writes the `%20` form for you |
| **MkDocs** | Builds fine. The published URL contains `%20`, e.g. `.../Consensus/Raft/` but `.../Fundamentals/Partial%20Failure/` |
| **Git / shells** | Fine, but paths need quoting: `git add "03-Concepts/.../CAP Theorem.md"` |

**The trade-off, stated plainly:** filenames with spaces produce URLs with
`%20` in them. They work correctly everywhere, and they are slightly uglier
when pasted into a chat window. Human-readable names in daily use were judged
worth that, and the site navigation is unaffected because MkDocs takes nav
labels from the `title:` frontmatter, not from the filename.

If a clean URL ever matters for a specific page, hyphenate that one filename.
Do not convert the whole vault.

## Internal links

**Use ordinary relative Markdown links.** Not wiki-links.

```markdown
[Raft](../Consensus/Raft.md)
[Quorum](../../Distributed-Systems/Replication/Quorum.md)
[Lab 02](../../04-Labs/02-Timeouts-Retries/README.md)
```

Wiki-links (`[[Raft]]`) are more convenient to type and are an Obsidian
extension that plain Markdown, GitHub's renderer and MkDocs do not understand
without a plugin. Relative links work in Obsidian, on github.com, in any
editor, and on the published site — no plugin, no build step, no lock-in.

Configure Obsidian once (see [Setup — Obsidian](setup/obsidian.md)) and its
autocomplete will produce this format for you:

- **Use `[[Wikilinks]]`** → off
- **New link format** → *Relative path to file*
- **Automatically update internal links** → on

Always include the `.md` extension: it is what makes the link work in Obsidian,
on GitHub, and in MkDocs' link validation.

## Frontmatter

Every note starts with a YAML block:

```yaml
---
title: Raft
type: concept
status: learning
topic: distributed-systems
difficulty: advanced
tags:
  - distributed-systems
  - consensus
  - raft
created: 2026-08-30
updated: 2026-08-30
---
```

### Fields

| Field | Required | Purpose |
| --- | --- | --- |
| `title` | yes | Display name in Obsidian and the site nav |
| `type` | yes | What kind of note this is |
| `status` | yes | Where it is in the pipeline — **controls publishing** |
| `topic` | yes | Broad subject area |
| `difficulty` | no | Sequencing hint |
| `tags` | no | Cross-cutting themes; keep to 2–5 |
| `created` | yes | `YYYY-MM-DD`, never changed |
| `updated` | yes | `YYYY-MM-DD`, bumped on substantive edits |

### `type`

```text
concept | course | lab | project | architecture | resource
```

### `status`

```text
inbox | learning | draft | review | completed | archived
```

| Status | Meaning | Published? |
| --- | --- | --- |
| `inbox` | Captured, not processed | **no** |
| `draft` | Being written, not fit to read | **no** |
| `learning` | Actively studying; genuine but incomplete | yes |
| `review` | Complete, awaiting a re-read | yes |
| `completed` | Finished, including **My Understanding** | yes |
| `archived` | Superseded, kept for history | yes |

See [Publishing](publishing.md) for the mechanism.

### `topic`

```text
distributed-systems | cloud | databases | messaging | kubernetes |
architecture | meta
```

### `difficulty`

```text
beginner | intermediate | advanced
```

## Keep the metadata small

Seven fields, all of which are read by a human or by the publishing hook. The
temptation is to add `source`, `confidence`, `review_date`, `related_count`,
`time_spent` — and then to spend the study time maintaining a database instead
of learning. **A note is a document, not a record.** Add a field only when
something concretely breaks without it.

## Folder placement

Folders are storage; links are structure. Put a note where you would look for
it, and do not agonise — a wrong folder costs nothing because search and
backlinks both ignore folders entirely.

| Content | Folder |
| --- | --- |
| Quick capture, unprocessed | `00-Inbox/` |
| A concept that is true independently of any course | `03-Concepts/<Area>/<Subarea>/` |
| Course-specific material | `02-Courses/<Course>/notes/` |
| An experiment answering one question | `04-Labs/NN-Name/` |
| Build work | `05-Projects/<Project>/` |
| A decision | `06-Architecture/ADRs/` |

## Headings

One `# H1` per note, matching `title`. Sections follow the relevant template so
that notes are comparable and skimmable. Do not skip heading levels.

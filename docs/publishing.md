---
title: Publishing
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - handbook
  - publishing
  - mkdocs
created: 2026-08-30
updated: 2026-08-30
---

# Publishing

## The strategy

**The repository root *is* the MkDocs docs directory.** There is one copy of
every Markdown file: Obsidian edits it, MkDocs publishes it. No duplication, no
sync step, no export.

MkDocs normally refuses to let `docs_dir` be the directory containing
`mkdocs.yml`. [`mkdocs-same-dir`](https://github.com/oprypin/mkdocs-same-dir)
lifts that restriction, and `docs_dir` is then set explicitly:

```yaml
docs_dir: .

plugins:
  - same-dir     # must come first
```

Both lines are required — the plugin alone does not change `docs_dir`.

The `docs/` folder therefore holds only pages that belong to the *site and the
handbook* — this document, the setup guides, the conventions — not copies of
notes.

## What gets excluded, and how

Two independent filters, deliberately kept separate.

### 1. Path-based — `exclude_docs` in `mkdocs.yml`

Native to MkDocs 1.6+, gitignore-style syntax. Whole directories that should
never be published:

```yaml
exclude_docs: |
  .obsidian/
  .github/
  .venv/
  hooks/
  site/
  00-Inbox/
  99-Templates/
  requirements.txt
```

Excluded files are neither rendered nor copied into the site, which matters:
without this, `.obsidian/` and `.github/` would be copied verbatim into the
published output.

### 2. Frontmatter-based — `hooks/publishing.py`

A ~40-line MkDocs hook. A note is held back when its frontmatter has:

- `status: draft`, or
- `status: inbox`, or
- `publish: false`

Everything else is published.

```python
UNPUBLISHED_STATUSES = {"draft", "inbox"}

def on_files(files, config):
    return Files([f for f in files if _is_publishable(_read_frontmatter(f.abs_src_path))])
```

That is the entire mechanism. No index, no database, no build step that
rewrites files. Change one line of frontmatter and the note appears or
disappears on the next build.

## How to keep a note private

Three options, in order of preference:

1. **Leave it in `00-Inbox/`.** Excluded by path.
2. **Set `status: draft`.** Works anywhere in the vault.
3. **Set `publish: false`.** For a finished note that is deliberately private —
   personal reflections, employer-specific material.

```yaml
---
title: Notes on our internal architecture
status: completed
publish: false
---
```

!!! danger "Private is not secret"
    These files are still **committed to Git**. If the repository is public,
    anyone can read them in the repository even though they are not on the
    website. For anything genuinely confidential — credentials, employer
    internals, personal data — keep it outside the repository entirely. See the
    security section of the [README](../README.md).

## Verifying what will publish

```bash
mkdocs build --strict 2>&1 | grep "held back"
```

The hook logs every file it drops. To see the whole list:

```bash
mkdocs build --strict --verbose 2>&1 | grep -A50 "publishing hook"
```

Or inspect the built site directly:

```bash
mkdocs build --strict
find site -name '*.html' | sort
```

## Navigation

There is no hand-maintained `nav:` block. The navigation is generated from the
folder structure by
[`mkdocs-awesome-pages-plugin`](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin),
with per-folder `.pages` files supplying titles and order:

```yaml
# 03-Concepts/.pages
title: Concepts
nav:
  - README.md
  - Distributed-Systems
  - Databases
  - ...          # everything else, alphabetically
```

The `...` token means "everything not listed above", so **a new note appears in
the navigation automatically** with no configuration change. That is the
property that makes this maintainable over years.

Page titles come from the `title:` frontmatter, so folder names like
`03-Concepts` never appear in the published navigation.

## Strict mode

CI runs `mkdocs build --strict`, which turns warnings into errors. The warnings
that matter:

| Warning | Cause | Fix |
| --- | --- | --- |
| `Doc file contains a link ... not found` | Broken relative link, usually a typo or a moved file | Fix the path |
| Link to an excluded file | Linking to something in `00-Inbox/` or a `status: draft` note | Publish the target, or remove the link |
| `Anchor not found` | `#heading` that no longer exists | Fix the anchor |

**Linking from a published note to an unpublished one breaks the build.** This
is intentional: it is the mechanism that stops the site from shipping dead
links. Either finish the target note or drop the link.

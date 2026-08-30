---
title: Setup — MkDocs Locally
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - handbook
  - setup
  - mkdocs
created: 2026-08-30
updated: 2026-08-30
---

# Setup — MkDocs Locally

## Install

Python 3.9 or newer. Use a virtual environment so the toolchain cannot collide
with anything else on the machine.

```bash
cd distributed-systems-learning-resources
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

`.venv/` is git-ignored.

What gets installed:

| Package | Role |
| --- | --- |
| `mkdocs` | The static site generator |
| `mkdocs-material` | Theme: search, dark mode, admonitions, Mermaid, tabs |
| `mkdocs-same-dir` | Lets the repository root be the docs directory |
| `mkdocs-awesome-pages-plugin` | Navigation from the folder structure |
| `PyYAML` | Frontmatter parsing in the publishing hook |

## Preview while writing

```bash
mkdocs serve
```

Then <http://127.0.0.1:8000>. The server watches for changes and reloads the
browser on save, so Obsidian in one window and the browser in the other gives
a live preview of the published result.

```bash
mkdocs serve -a 0.0.0.0:8000    # reachable from another device on the network
mkdocs serve --dirtyreload      # faster rebuilds on a large vault; nav may lag
```

## Build

```bash
mkdocs build --strict
```

Output goes to **`site/`** at the repository root. It is git-ignored and
regenerated on every build — never edit it, and never commit it. GitHub Actions
produces its own copy; the local `site/` is only for inspection.

`--strict` turns warnings into errors, which is what CI runs. Build locally
before pushing and CI will not surprise you.

```bash
# Discard a local build
rm -rf site/
```

## Checking what will publish

```bash
# Which notes were held back?
mkdocs build --strict 2>&1 | grep -A20 "held back"

# What actually shipped?
mkdocs build --strict && find site -name '*.html' | sort
```

See [Publishing](../publishing.md).

## A note on the MkDocs 2.0 banner

`mkdocs-material` prints a long red banner warning that a future MkDocs 2.0
will break plugins and themes, and suggesting `properdocs` as a replacement.

It is not an error, and it is not about this repository's configuration.
`requirements.txt` pins `mkdocs>=1.6,<2.0`, so the incompatible release it
warns about cannot be installed here. To silence it locally:

```bash
export DISABLE_MKDOCS_2_WARNING=true
```

CI sets this already. If the upstream situation changes, the migration path is
a one-line swap — `properdocs` is a drop-in for MkDocs 1.x and the same
`mkdocs.yml` works — so this is worth being aware of, not worth acting on now.

## Common problems

| Error | Cause | Fix |
| --- | --- | --- |
| `Config value 'plugins': The "same-dir" plugin is not installed` | Dependencies missing, or the venv is not active | `source .venv/bin/activate && pip install -r requirements.txt` |
| `contains a link '...' which is not found` | Broken relative link, or a link to an unpublished note | Fix the path, or publish the target |
| Mermaid shows as plain text | `pymdownx.superfences` custom fence missing | Confirm the `markdown_extensions` block in `mkdocs.yml` |
| Navigation looks wrong | `.pages` file mistake | Check the `.pages` in that folder; `...` includes the remainder |
| `Address already in use` | A previous `mkdocs serve` is running | `mkdocs serve -a 127.0.0.1:8001`, or kill it |
| Note not on the site | `status: draft`/`inbox`, or excluded by path | [Publishing](../publishing.md) |

## Upgrading

```bash
source .venv/bin/activate
pip install --upgrade -r requirements.txt
mkdocs build --strict          # verify before committing
```

`requirements.txt` pins major versions, so upgrades stay within a compatible
range. If a major version bump is wanted, change the pin deliberately and
confirm the build.

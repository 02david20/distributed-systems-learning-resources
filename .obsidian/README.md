# .obsidian — shared vault configuration

These files are **deliberately committed** so that every clone of this
repository behaves identically. They are small, stable, and portable.

| File | Purpose |
| --- | --- |
| `app.json` | Link format (relative Markdown links, wikilinks OFF), new-note location. **The most important file here** — if link settings differ between machines, notes end up with links that work in Obsidian and break on the published site |
| `core-plugins.json` | Which built-in features are enabled |
| `templates.json` | Points the Templates plugin at `99-Templates/` |
| `appearance.json` | Theme set to follow the system |
| `hotkeys.json` | `Cmd/Ctrl + T` inserts a template |
| `community-plugins.json` | The *list* of community plugins (empty by default) — not their code |

Per-machine state is git-ignored: `workspace.json`, `workspace-mobile.json`,
`graph.json`, caches, and `plugins/` (third-party JavaScript, reinstalled per
machine).

Obsidian rewrites these files when settings change in the UI. That is fine —
`git diff` will show what changed, and you decide whether to commit it.

Full rationale: [`docs/setup/obsidian.md`](../docs/setup/obsidian.md) and
[`docs/git-workflow.md`](../docs/git-workflow.md).

> This file is excluded from the published site: `.obsidian/` is listed in
> `exclude_docs` in `mkdocs.yml`.

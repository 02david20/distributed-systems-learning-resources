---
title: Setup — Obsidian
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - handbook
  - setup
  - obsidian
created: 2026-08-30
updated: 2026-08-30
---

# Setup — Obsidian

Everything on this page is **manual**. The repository ships the folder
structure, templates, configuration files and CI; installing software, granting
credentials and choosing personal preferences cannot be automated safely from
inside a repository, and should not be.

Budget about 20 minutes.

---

## Step 1 — Install Obsidian

Download from <https://obsidian.md> and install.

- **macOS**: drag to Applications, or `brew install --cask obsidian`
- **Windows**: run the installer, or `winget install Obsidian.Obsidian`
- **Linux**: AppImage, Flatpak, Snap or `.deb` from the same page

Free for personal use. No account is required, and you should not create one:
Obsidian Sync is a paid service that this setup replaces with Git.

---

## Step 2 — Clone the repository

```bash
git clone https://github.com/02david20/distributed-systems-learning-resources.git
cd distributed-systems-learning-resources
```

Put it somewhere permanent and **not inside a cloud-sync folder**. Dropbox,
iCloud Drive and OneDrive all corrupt `.git` directories eventually by syncing
partial writes. Git is the sync mechanism here; a second one is a liability.

Good: `~/vaults/`, `~/projects/`, `~/Documents/` (if not synced).

---

## Step 3 — Open the repository as a vault

1. Launch Obsidian.
2. **Open folder as vault**.
3. Select the cloned `distributed-systems-learning-resources` directory.
4. Obsidian asks whether to trust the author of the vault — this is about
   whether to allow community plugins to run. Since the vault ships no plugin
   code, either answer is safe; **Trust author and enable plugins** is
   convenient if you plan to install the Git plugin in Step 6.

The repository *is* the vault. There is no import and no separate Obsidian
folder — Obsidian's only footprint is the `.obsidian/` directory that is
already committed.

!!! success "What you should see"
    The file explorer shows `00-Inbox` through `99-Templates`, `docs/` and
    `README.md`. Open
    `03-Concepts/Distributed-Systems/Consensus/Raft.md` — the Mermaid diagrams
    should render in preview mode (`Cmd/Ctrl + E`).

---

## Step 4 — Enable core features

**Settings → Core plugins.** The repository ships
`.obsidian/core-plugins.json` with these already on, so this step is
verification rather than configuration.

| Feature | Why |
| --- | --- |
| **File explorer** | Folder tree |
| **Search** | Full-text across the vault. `Cmd/Ctrl + Shift + F` |
| **Quick switcher** | Jump to a note by name. `Cmd/Ctrl + O` — the fastest thing in Obsidian |
| **Backlinks** | *What links here* — the single most valuable feature for learning |
| **Outgoing links** | What this note references |
| **Graph view** | Visualise the concept network |
| **Tags** | Browse by tag |
| **Templates** | Insert the note templates |
| **Daily notes** | Optional — useful for a study log |
| **Outline** | Heading navigation in long notes |

Turn **off** anything not listed. Fewer moving parts, faster startup.

### Verify the link settings

**Settings → Files and links.** These three matter more than anything else on
this page, because they determine whether the links Obsidian writes work
outside Obsidian:

| Setting | Value | Why |
| --- | --- | --- |
| **Use [[Wikilinks]]** | **OFF** | Wiki-links are an Obsidian extension. Plain Markdown links work in Obsidian, on GitHub *and* in MkDocs |
| **New link format** | **Relative path to file** | Absolute paths break when the site is served from a subdirectory |
| **Automatically update internal links** | ON | Renaming a note fixes every link to it |
| **Default location for new notes** | `00-Inbox` | Capture first, file later |

These ship in the committed `.obsidian/app.json`, so they should already be
correct. Check them anyway — getting this wrong produces links that work
locally and break on the published site, which is a slow, annoying failure to
diagnose. See [Conventions](../conventions.md).

---

## Step 5 — Configure templates

**Settings → Templates → Template folder location** → `99-Templates`

Ships in `.obsidian/templates.json`; verify it.

### Assign a hotkey

**Settings → Hotkeys** → search "Templates: Insert template" → bind
`Cmd/Ctrl + T`. Templates that take three clicks to insert do not get used.

### Using a template

1. `Cmd/Ctrl + N` for a new note
2. Name it properly — `Consistent Hashing`, not `Untitled`
3. `Cmd/Ctrl + T` → pick `Learning-Note`
4. Fill in the frontmatter; delete sections that genuinely do not apply

The templates use `{{title}}` and `{{date:YYYY-MM-DD}}`, which the core
Templates plugin expands on insert.

---

## Step 6 — Configure Git

### Option A — Git CLI (recommended)

The fallback that is also the primary recommendation. Nothing to install beyond
Git itself, nothing that can surprise you.

```bash
git config user.name  "Your Name"
git config user.email "you@example.com"

# Authenticate once. GitHub CLI is the least painful route:
gh auth login
# or set up an SSH key: https://docs.github.com/authentication
```

Daily rhythm:

```bash
git pull --rebase        # start of session
# ... write in Obsidian ...
git status
git diff                 # read this
git add -A
git commit -m "Week 5: add Replication and Quorum notes"
git push
```

See [Git Workflow](../git-workflow.md).

**Why this is the recommendation:** committing is a deliberate act. You read
the diff, you write a message describing what you learned, and the history
becomes a study log rather than a stream of `vault backup: 2026-08-30T14:23`.

### Option B — the Obsidian Git community plugin

Convenient on mobile and for people who will otherwise never commit. It is
**not** bundled — Obsidian ships with no community plugins, and it must be
installed by hand on every machine.

**Installation:**

1. **Settings → Community plugins**
2. **Turn on community plugins** (disables Restricted Mode — read the warning;
   community plugins are third-party code with full access to your vault)
3. **Browse** → search **"Git"** → the one by *Vinzent03* → **Install** → **Enable**
4. **Settings → Git** and configure:

| Setting | Suggested | Reason |
| --- | --- | --- |
| Vault backup interval | `0` (disabled) | Automatic commits produce a useless history |
| Auto pull on startup | ON | Cheap, avoids most conflicts |
| Auto push | OFF | Push deliberately |
| Commit message | `vault backup: {{date}}` | Only used if auto-commit is ever enabled |
| Disable notifications | OFF | You want to see failures |

Then bind hotkeys for **Git: Commit all changes** and **Git: Push**.

**Authentication caveat:** the plugin uses `isomorphic-git` on desktop, which
does not read your SSH agent the way the CLI does. HTTPS with a personal access
token is the path of least resistance. If it fails to authenticate, use the CLI
— that is not a workaround, it is the better option anyway.

!!! danger "The risks of automatic commit and push"
    - **A timer-driven commit history is unreadable.** 400 commits called
      `vault backup: <timestamp>` destroy `git log`'s value as a study record,
      which is one of the main reasons for using Git here.
    - **You never read the diff.** The habit of reviewing changes before
      committing is the main thing standing between you and a pushed API key.
      Automatic push removes that step entirely.
    - **Conflicts happen unattended.** Auto-pull can leave conflict markers in
      a note while you are typing in it.
    - **Half-written notes get published.** A commit fires mid-sentence,
      Actions deploys, and the site shows an unfinished thought. (Setting
      `status: draft` while writing prevents this — see
      [Publishing](../publishing.md).)

    If you enable the plugin, enable **auto-pull** and leave **auto-commit and
    auto-push off**. Use it as a convenient button, not as a robot.

### Option C — mobile

Obsidian's mobile apps cannot run Git natively. The realistic options are the
Git plugin on mobile (works, occasionally fragile), Working Copy on iOS, or
simply treating mobile as capture-only into `00-Inbox` and committing from a
desktop later.

---

## Step 7 — Create a test note and verify the whole pipeline

This confirms every link in the chain.

**1. In Obsidian**, create `00-Inbox/Pipeline Test.md`:

````markdown
---
title: Pipeline Test
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - test
created: 2026-08-30
updated: 2026-08-30
---

# Pipeline Test

Verifying Obsidian → Git → GitHub → Actions → Pages.

```mermaid
flowchart LR
    Obsidian --> Git --> GitHub --> Actions --> Pages
```

A link to [Raft](../03-Concepts/Distributed-Systems/Consensus/Raft.md).
````

**2. Verify in Obsidian:** the diagram renders in preview, and the Raft link
resolves (`Cmd/Ctrl + click`).

**3. Move it out of the Inbox** — `00-Inbox/` is excluded from publishing.
Drag it to `03-Concepts/`. Obsidian will offer to update links; accept.

**4. Build locally:**

```bash
mkdocs serve
```

Open <http://127.0.0.1:8000>, find the note, confirm the diagram renders.

**5. Commit and push:**

```bash
git add "03-Concepts/Pipeline Test.md"
git commit -m "Add pipeline test note"
git push
```

**6. Watch the deploy:** GitHub → **Actions** tab → the *Deploy documentation*
run. It should go green in one to two minutes.

**7. Confirm on the live site:**
`https://02david20.github.io/distributed-systems-learning-resources/`

**8. Test the private path:** change the frontmatter to `status: draft`,
commit, push. After the rebuild the note is gone from the site — and still in
the repository.

**9. Delete it.** The pipeline works; the note has served its purpose.

---

## Recommended community plugins

The vault is designed to need **none**. Everything essential — links,
backlinks, search, graph, templates, Mermaid — is core Obsidian.

Consider these only when a specific need appears:

| Plugin | When it earns its place | What it costs |
| --- | --- | --- |
| **Git** (Vinzent03) | You want commits from inside Obsidian, or you write on mobile | See the risks above |
| **Templater** | The core Templates plugin's `{{title}}`/`{{date}}` stop being enough — e.g. auto-filling `updated:` | A second templating syntax; templates stop being readable without it |
| **Excalidraw** | You need hand-drawn diagrams beyond Mermaid | **Proprietary format.** Always export SVG alongside |
| **Dataview** | You want live queries over frontmatter, e.g. "every `status: learning` note" | **Queries render only in Obsidian.** They appear as raw code blocks on the site. Portability-compromising — use sparingly and never as the only way to find something |

### Plugins to avoid here

| Plugin | Why not |
| --- | --- |
| Anything storing content outside Markdown | Breaks the portability principle outright |
| Kanban | Progress tracking belongs in GitHub Projects; two systems means neither is trusted |
| Note refactoring / auto-linking tools | They rewrite files in bulk; the diffs are unreviewable |
| Publishing plugins (Obsidian Publish, digital garden exporters) | MkDocs already does this, from the same files |

The general test: **if uninstalling the plugin would make content unreadable
or unfindable, do not install it.**

---

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| Links written as `[[Note]]` | Wikilinks on | Settings → Files and links → **Use [[Wikilinks]]** off |
| Links break on the published site | Absolute link format | Set **New link format** to *Relative path to file* |
| Templates option greyed out | Template folder not set | Settings → Templates → `99-Templates` |
| Mermaid not rendering in Obsidian | Source mode | `Cmd/Ctrl + E` to toggle preview |
| Mermaid renders in Obsidian, not on the site | Unsupported diagram type | Stick to the seven types in [Mermaid](../mermaid.md) |
| Note missing from the site | `status: draft`/`inbox`, or in `00-Inbox/` | See [Publishing](../publishing.md) |
| `mkdocs build --strict` fails on a link | Link to an excluded or missing file | Fix the path, or publish the target |
| Vault feels slow | Large binaries in the vault | Keep media out of the repository |

---

## What was automated, and what was not

### Shipped by the repository

- Folder structure and `.pages` navigation files
- Five note templates
- `.obsidian/` shared settings (link format, core plugins, template folder)
- `mkdocs.yml`, `requirements.txt`, the publishing hook
- GitHub Actions workflow, issue templates, PR template
- `.gitignore` covering secrets, build output and per-machine Obsidian state
- This documentation, and ~40 seeded notes

### Yours to do

- Install Obsidian
- Create the GitHub repository and push
- Open the folder as a vault, and answer the trust prompt
- Verify the Obsidian settings above
- Install any community plugin you decide you want
- Configure Git credentials
- [Enable GitHub Pages and configure the repository](github.md)
- Replace `02david20` in `mkdocs.yml` with your GitHub username
- Decide your own preferences — theme, hotkeys, daily notes

None of the second list can be done safely from inside a repository. Software
installation, credentials and account configuration are yours by definition.

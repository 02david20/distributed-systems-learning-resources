---
title: Setup — GitHub
type: concept
status: completed
topic: meta
difficulty: beginner
tags:
  - handbook
  - setup
  - github
created: 2026-08-30
updated: 2026-08-30
---

# Setup — GitHub

Manual configuration on GitHub's side. About 15 minutes, once.

---

## Step 1 — Create the repository

```bash
cd cloud-distributed-systems-learning
git init
git add -A
git commit -m "Bootstrap knowledge base"
gh repo create cloud-distributed-systems-learning --public --source=. --push
```

Or create it in the web UI and:

```bash
git remote add origin https://github.com/USERNAME/cloud-distributed-systems-learning.git
git branch -M main
git push -u origin main
```

**Public or private?** Public if the site should be reachable without a paid
plan — GitHub Pages on private repositories requires GitHub Pro or an
organisation plan. Public also means *everything committed is world-readable*,
including notes marked `publish: false`. See [Publishing](../publishing.md).

---

## Step 2 — Replace the placeholders

`mkdocs.yml` ships with `USERNAME` in three places:

```yaml
site_url: https://USERNAME.github.io/cloud-distributed-systems-learning/
repo_url: https://github.com/USERNAME/cloud-distributed-systems-learning
extra:
  social:
    - link: https://github.com/USERNAME
```

```bash
sed -i '' 's/USERNAME/your-github-username/g' mkdocs.yml   # macOS
sed -i    's/USERNAME/your-github-username/g' mkdocs.yml   # Linux
```

Do the same in `README.md` and `docs/git-workflow.md` if you want those links
live.

---

## Step 3 — Enable GitHub Pages

**Settings → Pages → Build and deployment → Source → `GitHub Actions`.**

This is the current recommended method and the one the shipped workflow uses.
Do **not** select "Deploy from a branch" — there is no `gh-pages` branch, and
the workflow publishes an artifact directly.

The site appears at:

```text
https://USERNAME.github.io/cloud-distributed-systems-learning/
```

The first deploy can take a few minutes to become reachable after the workflow
goes green.

---

## Step 4 — Check Actions permissions

**Settings → Actions → General → Workflow permissions**

The workflow declares what it needs:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

Nothing extra is required — `deploy-pages` uses OIDC, so there is no token to
create or store. If the deploy job fails with a permissions error, confirm
Actions are enabled for the repository at all.

---

## Step 5 — Create labels

```bash
gh label create learning            --color 0E8A16 --description "Learn a concept"
gh label create course              --color 1D76DB --description "Course work"
gh label create reading             --color 5319E7 --description "Paper or book"
gh label create lab                 --color FBCA04 --description "Hands-on experiment"
gh label create project             --color D93F0B --description "Build work"
gh label create distributed-systems --color 006B75
gh label create cloud               --color 0075CA
gh label create database            --color B60205
gh label create messaging           --color C2E0C6
gh label create kubernetes          --color 326CE5
gh label create architecture        --color BFD4F2
gh label create review              --color E4E669 --description "Spaced review"
```

The first five are *what kind of work*; the middle six are *subject area*;
`review` marks spaced-repetition revisits. Issue templates apply the type label
automatically.

---

## Step 6 — Create the Project board

**Your profile → Projects → New project → Board.**

Columns:

```text
Backlog → This Month → This Week → Learning → Practicing → Review → Done
```

| Column | Meaning | WIP limit |
| --- | --- | --- |
| **Backlog** | Everything not yet scheduled | — |
| **This Month** | Committed to the current month | — |
| **This Week** | Committed to this week | ~5 |
| **Learning** | Reading and note-writing in progress | **2** |
| **Practicing** | Lab or project work in progress | **2** |
| **Review** | Written; awaiting a spaced re-read | — |
| **Done** | Note has a **My Understanding** section; lab has an **Actual Result** | — |

The WIP limits are the point of the board. Three concepts half-learned is worse
than one finished.

### Suggested automation

**Project → Workflows**: enable *Item closed → Done* and
*Auto-add to project* filtered to this repository. Nothing more — automation
that moves cards on your behalf makes the board stop reflecting reality.

### How Issues and notes divide the work

> **The Issue is the action. The note is the knowledge.**

| Belongs in the Issue | Belongs in the note |
| --- | --- |
| "Read Raft §5.2 and write up leader election" | The explanation of leader election |
| Links to resources to use | What the resources said |
| Definition of done | The **My Understanding** section |
| A link to the note | Everything else |

Never paste note content into an Issue. Issues are closed and forgotten; notes
are the artefact. Each Issue links to the note it will produce.

---

## Step 7 — Verify the first deploy

```bash
git commit --allow-empty -m "Trigger first deploy"
git push
gh run watch
```

Then open the Pages URL. If the workflow is green but the page 404s, wait a
minute — the first publish takes a moment to propagate.

---

## Optional — branch protection

For a single-author knowledge base this is usually unnecessary friction. If you
want CI to gate `main`:

**Settings → Rules → Rulesets → New branch ruleset** → target `main` →
require a pull request and require the `build` status check.

The workflow builds on pull requests without deploying, so a broken link is
caught before it can reach the live site.

---

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| Workflow fails: `Get Pages site failed` | Pages not enabled, or source is not "GitHub Actions" | Step 3 |
| Deploy succeeds, site 404s | Propagation delay, or wrong `site_url` | Wait; then check `site_url` in `mkdocs.yml` |
| CSS missing, links broken on the live site | `site_url` does not match the real URL | Fix `site_url` — the subdirectory path matters |
| Build fails only in CI | Local build was not run with `--strict` | `mkdocs build --strict` locally |
| Pages unavailable on a private repo | Requires a paid plan | Make the repository public, or host elsewhere |

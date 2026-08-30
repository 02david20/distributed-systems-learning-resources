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
cd distributed-systems-learning-resources
git init
git add -A
git commit -m "Bootstrap knowledge base"
gh repo create distributed-systems-learning-resources --public --source=. --push
```

Or create it in the web UI and:

```bash
git remote add origin https://github.com/02david20/distributed-systems-learning-resources.git
git branch -M main
git push -u origin main
```

**Public or private?** Public if the site should be reachable without a paid
plan — GitHub Pages on private repositories requires GitHub Pro or an
organisation plan. Public also means *everything committed is world-readable*,
including notes marked `publish: false`. See [Publishing](../publishing.md).

---

## Step 2 — Replace the placeholders

Already done for this repository. If you fork it, these are the values to
change:

```yaml
site_url: https://blogs.sentinelnodes.cc/            # or the github.io URL
repo_url: https://github.com/02david20/distributed-systems-learning-resources
extra:
  social:
    - link: https://github.com/02david20
```

Plus the `CNAME` file at the repository root, which holds the custom domain.

```bash
sed -i '' 's/02david20/your-github-username/g' mkdocs.yml   # macOS
sed -i    's/02david20/your-github-username/g' mkdocs.yml   # Linux
```

Do the same in `README.md` and `docs/git-workflow.md` if you want those links
live.

---

## Step 3 — Enable GitHub Pages

The workflow tries to do this for you: `actions/configure-pages` is invoked
with `enablement: true`, which creates the Pages site with the build type set
to `workflow` on the first run.

If that succeeds, there is nothing to do here. If it fails — some accounts and
organisation policies do not permit the API to enable Pages — set it by hand:

**Settings → Pages → Build and deployment → Source → `GitHub Actions`.**

Do **not** select "Deploy from a branch" — there is no `gh-pages` branch, and
the workflow publishes an artifact directly.

The site appears at:

```text
https://02david20.github.io/distributed-systems-learning-resources/
```

…until a custom domain is configured, after which that URL redirects to it.
See Step 4.

The first deploy can take a few minutes to become reachable after the workflow
goes green.

---

## Step 4 — Custom domain

This site is served from **`blogs.sentinelnodes.cc`**. A subdomain was chosen
over the apex deliberately: it needs one ordinary CNAME record, it leaves
`sentinelnodes.cc` free for other services, and the apex can only ever point at
one Pages site.

### 4a. The CNAME file

The repository root holds a `CNAME` file containing exactly:

```text
blogs.sentinelnodes.cc
```

It must end up in the built site. `mkdocs-same-dir` passes `CNAME` through
explicitly, so `site/CNAME` appears on every build — verify with:

```bash
mkdocs build --strict && cat site/CNAME
```

!!! warning "Do not delete this file"
    With Actions-based publishing, each deployment replaces the whole site. If
    `CNAME` is missing from the artifact, GitHub can clear the custom domain
    setting and the site silently reverts to the `github.io` URL.

### 4b. DNS at Cloudflare

One record. `sentinelnodes.cc` is on Cloudflare DNS
(`molly`/`etienne.ns.cloudflare.com`).

| Type | Name | Target | Proxy | TTL |
| --- | --- | --- | --- | --- |
| `CNAME` | `blogs` | `02david20.github.io` | **DNS only (grey cloud)** | Auto |

Note the target is the **user** host `02david20.github.io`, with no repository
path — GitHub routes to the right project by the `CNAME` file's contents.

!!! danger "The proxy must be off — grey cloud, not orange"
    With Cloudflare proxying enabled, GitHub cannot complete the HTTP
    validation needed to issue the TLS certificate, so **Enforce HTTPS stays
    greyed out**. Worse, if Cloudflare's SSL/TLS mode is *Flexible*, enabling
    Enforce HTTPS later produces an infinite redirect loop: Cloudflare talks
    HTTP to GitHub, GitHub redirects to HTTPS, forever.

    Turn the proxy off, get the certificate, and only then consider turning it
    back on — and if you do, set SSL/TLS mode to **Full (strict)** first.

### 4c. Tell GitHub

**Settings → Pages → Custom domain** → enter `blogs.sentinelnodes.cc` → **Save**.

GitHub runs a DNS check. Once it passes it requests a Let's Encrypt
certificate, which usually takes a few minutes and occasionally up to an hour.

When **Enforce HTTPS** becomes tickable, tick it.

### 4d. Verify

```bash
# DNS resolves to GitHub Pages, not Cloudflare
dig +short blogs.sentinelnodes.cc
# expect: 02david20.github.io. then 185.199.10[8-11].153

# Certificate is issued and the site is served
curl -sSI https://blogs.sentinelnodes.cc/ | head -3

# The old URL redirects to the new one
curl -sS -o /dev/null -w '%{http_code} %{url_effective}\n' -L \
  https://02david20.github.io/distributed-systems-learning-resources/
```

### Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| "Domain does not resolve to the GitHub Pages server" | DNS not propagated, or proxy is on | Wait; set the record to DNS only |
| Enforce HTTPS greyed out | Certificate not issued yet | Wait; confirm grey cloud, then re-save the domain |
| Redirect loop after enabling HTTPS | Cloudflare SSL mode is Flexible | Set Full (strict), or turn the proxy off |
| Custom domain empties itself after a deploy | `CNAME` missing from the build | Confirm `site/CNAME` exists |
| Certificate valid for `github.io`, not the domain | Domain saved before DNS resolved | Remove the custom domain, save, re-add it |

---

## Step 5 — Check Actions permissions

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

## Step 6 — Create labels

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

## Step 7 — Create the Project board

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

## Step 8 — Verify the first deploy

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
| Workflow fails: `Get Pages site failed ... Not Found` | No Pages site exists yet, and `enablement: true` could not create one | Set Settings → Pages → Source → GitHub Actions by hand, then re-run |
| Workflow warns about Node 20 deprecation | Informational only — every action here is a current major already running on Node 24 | Nothing to do |
| Deploy succeeds, site 404s | Propagation delay, or wrong `site_url` | Wait; then check `site_url` in `mkdocs.yml` |
| CSS missing, links broken on the live site | `site_url` does not match the real URL | Fix `site_url` — the subdirectory path matters |
| Build fails only in CI | Local build was not run with `--strict` | `mkdocs build --strict` locally |
| Pages unavailable on a private repo | Requires a paid plan | Make the repository public, or host elsewhere |

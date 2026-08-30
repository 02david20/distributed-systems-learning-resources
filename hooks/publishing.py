"""MkDocs build hook: keep unfinished notes out of the published site.

The Obsidian vault and the published documentation are the same Markdown
files, so something has to decide which notes are public. That decision is
made here, from YAML frontmatter, and nowhere else.

Rules
-----
A documentation page is EXCLUDED from the built site when either:

  * its frontmatter has ``status: draft`` or ``status: inbox``, or
  * its frontmatter has ``publish: false``.

Everything else is published, including notes with no frontmatter at all.
Path-based exclusions (00-Inbox/, 99-Templates/, .obsidian/, ...) are handled
separately by ``exclude_docs`` in mkdocs.yml.

This is intentionally the whole mechanism. There is no database, no index and
no build step that rewrites files: flip one line of frontmatter and the note
appears on, or disappears from, the next build.
"""

from __future__ import annotations

import logging
import re
from typing import Any

import yaml
from mkdocs.structure.files import Files

log = logging.getLogger("mkdocs.hooks.publishing")

#: Frontmatter ``status`` values that are never published.
UNPUBLISHED_STATUSES = {"draft", "inbox"}

#: Matches a YAML frontmatter block at the very start of a file.
_FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)


def _read_frontmatter(path: str) -> dict[str, Any]:
    """Return the YAML frontmatter of ``path`` as a dict, or ``{}``."""
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError):
        return {}

    match = _FRONTMATTER_RE.match(text)
    if match is None:
        return {}

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        log.warning("Could not parse frontmatter in %s: %s", path, exc)
        return {}

    return data if isinstance(data, dict) else {}


def _is_publishable(meta: dict[str, Any]) -> bool:
    if meta.get("publish") is False:
        return False
    status = meta.get("status")
    if status is None:
        return True
    return str(status).strip().lower() not in UNPUBLISHED_STATUSES


def _is_path_excluded(file) -> bool:  # noqa: ANN001 - MkDocs File
    """True if `exclude_docs` in mkdocs.yml already dropped this file."""
    inclusion = getattr(file, "inclusion", None)
    try:
        return bool(inclusion is not None and inclusion.is_excluded())
    except AttributeError:
        return False


def on_files(files: Files, config) -> Files:  # noqa: ANN001 - MkDocs signature
    """Drop unpublished documentation pages before the nav is built."""
    kept: list = []
    dropped: list[str] = []

    for file in files:
        if not file.is_documentation_page() or _is_path_excluded(file):
            # Non-pages, and pages already excluded by `exclude_docs` in
            # mkdocs.yml, are passed through untouched. Templates in
            # 99-Templates/ deliberately contain `{{date:...}}` placeholders
            # that are not valid YAML, so they must not be parsed at all.
            kept.append(file)
            continue

        if _is_publishable(_read_frontmatter(file.abs_src_path)):
            kept.append(file)
        else:
            dropped.append(file.src_uri)

    if dropped:
        log.info(
            "publishing hook: %d note(s) held back (status: draft/inbox or "
            "publish: false):\n  %s",
            len(dropped),
            "\n  ".join(sorted(dropped)),
        )

    return Files(kept)

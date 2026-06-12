# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Status

This repository is greenfield: at the time of writing it contains no code, only this guidance. The notes below describe the intended system. As the codebase materializes, replace planned descriptions with concrete commands and file references, and keep this file in sync with reality.

## Purpose

A personal CV system for Oscar Esteban (ORCID-backed academic CV) with three pillars:

1. **ORCID synchronization** — bidirectional sync between the local records and the user's ORCID profile (publications, grants, employment, education). Treat ORCID and the local YAML database as two replicas that must converge; any sync logic needs a conflict story (which side wins, how divergence is detected and surfaced).
2. **A YAML publication database** — the source of truth for all scholarly output, stratified by record type: journal papers, oral conference presentations, poster presentations, invited talks, software contributions, Stage 1 registered reports, preprints, and similar. The stratification is a first-class concept — record type drives how an item is rendered, deduplicated, and matched against ORCID.
3. **PDF/LaTeX CV generation** — tooling that compiles CV variants (e.g., long-form, short-form, topic-tailored) to PDF from the YAML database via LaTeX. This tooling is expected to be tested.

When designing data structures, the YAML schema is the architectural center of gravity: ORCID sync reads/writes it, and the LaTeX generator reads it. Changes to the schema ripple into both. Keep one canonical schema and avoid letting the generator or the sync layer accrete their own divergent representations.

## Commit conventions

Use [Conventional Commits](https://www.conventionalcommits.org/): a type prefix on every subject line, e.g. `enh:`, `fix:`, `chore:`, `docs:`, `test:`, `refactor:`. Keep the body as short as the change allows — omit it for trivial changes. Always add yourself as a co-author trailer:

```
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
```

## Pull request conventions

All changes land through PRs — do not push directly to the default branch.

- **Title**: conventional-commit type in ALLCAPS, e.g. `FIX: Correct publication date of Esteban et al. (2019)`.
- **Body**: more descriptive than a commit body but not over-explained; state what changed and why, skip the play-by-play.
- **Issue linkage**: when a PR closes an issue, include the closing keyword, e.g. `Fixes: #340`.

## Working notes

- The data is biographical and citation-bearing — correctness of dates, DOIs, author lists, and venue names matters more than throughput. Prefer surfacing a suspected discrepancy over silently "fixing" a record.
- The LaTeX toolchain (pdflatex/lualatex/latexmk, BibTeX/biblatex) is a build dependency for PDF generation; reach for the `latex` skill when writing or debugging `.tex` sources, and the `zotero` skill if reference management connects to a Zotero library.

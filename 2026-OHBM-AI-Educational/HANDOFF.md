# Handoff — re-found the OHBM 2026 "LLMs for Coding" talk with fresh eyes

You're taking over a conference talk that has gone stale. The previous assistant
and Oscar both agree the current deck drifted into generic, templated mush. Your
job is **fresh eyes with a point of view** — not a polish pass. Read this once,
then read Oscar's *real* talks, then **talk with him before touching a slide.**

## Who you're working with
Oscar Esteban — neuroimaging methods researcher (fMRIPrep / NiPreps), open-science
advocate, UNIL Lausanne. Blunt, allergic to predictable output, wants a real
collaborator who brings ideas — not a yes-machine that hands back a finished plan
or a multiple-choice menu. If a draft smells like a template, he says so (he
described the last attempt as "a rancid old smoker's house with the windows shut").
Think out loud, take positions, argue with him. Don't flatter, don't hedge, don't
bury him in options.

## The talk
- OHBM 2026 Educational, "Using LLMs in Neuroimaging Research — LLMs for Coding."
  ~30 min, single speaker.
- Format: remark.js Markdown deck. Slides live inside `<textarea id="source">` in
  `2026-OHBM-AI-Educational/index.html`. Engine is the `remark/` git submodule —
  **do not edit it**. House rules in `CLAUDE.md` at the repo root.
  Repo: `~/workspace/nipreps-presentations`.
- Subject: Oscar's real experience using agentic coding (Claude Code / Codex) for
  neuroimaging — building small "skills," running one large experiment, and
  grounding models so they stop hallucinating.

## What went wrong (do not repeat)
The current `index.html` IS the stale artifact. Its tics:
- Every slide has the identical shape: **bold claim → punchy fragment →
  `.center[*italic kicker*]`**. The same rhythm ~30 times. This sameness is the
  core problem.
- Over-bolding, nested bold/italic, em-dash aphorisms; one phrase ("Structure —
  not vigilance") repeated six times; prose and meta-commentary crammed onto
  slides that should be terse.
Treat this file as a **content quarry** — the facts in it are real and verified —
**not** a style reference.

## Oscar's real voice — read these yourself; don't take anyone's word
Before proposing anything, read several of his actual decks and internalize how he
presents:
- `~/workspace/nipreps-presentations/2025-esmrmb/index.html` — note the **fictional
  personas** he uses for a mixed audience (Thảo, Amine, Lucas).
- `~/workspace/nipreps-presentations/2025-MRITogether/index.html`
- `.../2024-BrainHack/index.html`, `.../2023-EPFL/index.html`, `.../2022-OHBM/index.html`
- `~/workspace/talks/` — many more (202412-OSU, 20260210-ISC, 202504-CDT-UCL,
  20250401-labmeeting, 20260420-RRI, …).

What you'll likely notice (verify, then form your own view): slides are
**economical — the narrative lives in the `???` speaker notes**. He leans on ONE
load-bearing metaphor that recurs *without fanfare* (sushi / "analysis-grade" data;
the Swiss-cheese QC model; a genomics-standardization timeline; the dead-salmon
fMRI study; "truck factor"). Titles are declarative and information-bearing, never
puns. Humor is dry and embedded ("113 members + a robot"; "he's coming because his
manager made him"). He hedges honestly on his own results ("unfortunately, we had
to conclude…"). Diagrams and **stepwise-SVG reveals** carry the argument, not
bullet aphorisms. Data-forward, opinionated about open science.

## Content that must survive (real & verified — mine it from the current deck's notes)
1. **Skills story (Act ①):** Claude Code fabricated references, so he built
   `/s2-query` (Semantic Scholar search; stdlib script; JSON to stdout) and
   `/zotero` (CSL-JSON library sync; CrossRef-verifies every DOI). Real skills at
   `~/.claude/skills/s2-query/` and `~/.claude/skills/zotero/`; `skill-creator`
   exists too. A natural place to show *real code*.
2. **ABIDE experiment (Act ②):** he drove ~2,200 subjects (ABIDE I+II, 43 sites)
   through fMRIPrep on the Curnagl HPC cluster via Claude Code **without ever
   logging into the cluster himself**. YODA/DataLad provenance. Real human-in-the-
   loop steering moments: a shell-glob bug; "ghost subjects" (data stranded after a
   push race); an F0080 motion/distortion ordering bug. Replicated Abraham et al.
   2017 (autism classification); preprocessing choice explained <1% of the accuracy
   gap. ~480 commits, 62 with an AI co-author trailer.
3. **Grounding (Act ③):** models hallucinate API details (invented a QSIPrep
   `--output-spaces` flag that's actually fMRIPrep's). Framed precisely as an
   **imitative falsehood** (Lin, Hilton & Evans 2022, *TruthfulQA*, DOI
   10.18653/v1/2022.acl-long.229 — note inverse scaling: bigger models were *less*
   truthful), compounded by false-premise compliance. Fix = grounding via a
   curated, cited LLM-wiki. Benchmark (Sonnet) memory vs web vs wiki: memory =
   instant/cheap/always-wrong; web = right but slow & costly; wiki = right, fast,
   cheap. Assets: `images/qsiprep-hallucination.cast`, `images/qsiprep-grounding.svg`.

## Constraints Oscar has set
- Keep **Slido** audience polls and the **three-act** structure (his explicit call).
  You may argue for something better, but don't silently remove them.
- Rendering polish is not the priority; voice and structure are.
- Conventional-commits house style; don't edit `remark/`.

## How to start (please don't immediately rewrite)
1. Read this, then 3–4 of his real decks above.
2. Skim the current deck as a fact source.
3. Come back to Oscar with a genuine point of view and 2–4 **fresh** framings —
   your own, not a menu of his recycled metaphors. Then discuss. He explicitly
   wants to think it through together before any slides are written.

## Prior assistant's ideas (react or discard — you are NOT bound)
Floated last session; Oscar didn't reject them, didn't commit either:
1. **Open on the wreckage, not the wins** — a forensic autopsy of the times the
   agent confidently lied (fabricated citation, hallucinated flag, glob bug, ghost
   subjects, F0080), letting the trust argument fall out of the bodies.
2. **The "phantom" echo** — Oscar once scanned himself as a calibration phantom
   (HCPh); in the ABIDE run he was the human reference the drifting agent is
   measured against. Self-as-instrument is a signature move of his.
3. **A counter-thesis** — agentic coding lets everyone spin up bespoke pipelines
   again, in tension with the whole NiPreps standardization mission. Uncomfortable,
   and only he can credibly say it.
4. **Reframe AI as a new source of analytical variability** — his core research
   theme — rather than a productivity-tools talk.
Bring your own. Surprise him.

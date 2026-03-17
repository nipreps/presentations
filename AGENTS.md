<!--
Copyright The NiPreps Developers <nipreps@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

We support and encourage derived works from this project, please read
about our expectations at

    https://www.nipreps.org/community/licensing/
-->

# AGENTS instructions

This project's purpose is to generate GitHub pages that contain only NiPreps-related presentations and educational materials.

Presentations will generally use our custom fork of remark.js and will be written in Markdown.

Under `remark/`, we can find the base JavaScript code for the slides, as well as some "extensions" to play asciicasts, show SVGs step-by-step, or play a roulette of names.

## Previewing presentations

Serve from the repo root so that relative paths to the `remark/` submodule resolve correctly:

```bash
python -m http.server 8000
# Then visit http://localhost:8000/2025-MRITogether/
```

## Presentation structure

Each presentation lives in a `<YYYY-EventName>/` directory containing an `index.html`. Slides are written as Markdown inside a `<textarea id="source">` block. The HTML boilerplate loads CSS and JS from the `remark/` submodule via relative paths (e.g., `../remark/core/base.css`, `../remark/core/engine.js`).

- **Presentation-specific images** go in `<YYYY-EventName>/images/`.
- **Shared assets** (logos, SVGs, videos used across talks) go in `assets/`.

## The `remark/` submodule

`remark/` is a git submodule pointing to `oesteban/remark-engine`. **Do not edit files inside `remark/` directly** — changes to the engine must be made in that repository.

### Available macros (defined in `core/engine.js`)

- `![:img Alt text, 50%](image.png)` — image with alt text and width
- `![:video 80%](file.mp4)` — embedded video with width
- `![:doi](10.xxxx/yyyy)` — DOI link

### Extensions (load after `engine.js`)

- `ext/stepwise-svg.js` — progressive SVG element reveal
- `ext/roulette.js` + `ext/roulette.css` — timed speaking roulette and group formation
- `ext/asciicasts.js` — auto-discover and mount `.cast` terminal recordings
- `ext/timer.js` — countdown timer

### Theming

Available themes: `themes/nipreps.css`, `themes/chuv.css`, `themes/hes-so.css`. Override CSS custom properties (`--accent`, `--accent-dim`, `--accent-dark`, `--heading-color`, `--logo-url`) in a theme file or an inline `<style>` block.

To override remark defaults (ratio 16:9, Monokai highlighting, etc.), set `window.remarkEngineConfig = { ... }` before loading `engine.js`.

## Codex instructions

- Always plan first
- Think harder in the planning phase
- When proposing tasks, highlight potential critical points that could lead to side effects.

## Branches, Commits and PRs

- Commit messages should follow the semantic commit conventions of Conventional Commits (https://www.conventionalcommits.org/en/v1.0.0/).
  - At least, they MUST contain one line with the following format: `<type-code>: <message>` where `<type-code>` indicates the type of comment. Type of comments can be fixes and bugfixes (`fix:`), enhancements and new features (`enh:`), style (`sty:`), documentation (`doc:`), maintenance (`mnt:`), etc.
- PR titles should also be semantic, and use the same Type codes but in all caps (e.g., `FIX:`, `ENH:`, `STY:`, `DOC:`, `STY:`, `MNT:`)
- Branch names should start with a type code too, with pattern `<type-code>/<branch-name>`. If addressing a specific issue, the issue number will be included at the end of `<branch-name>`, e.g., `fix/display-glitch-123` for issue #123.

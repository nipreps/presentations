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

## Codex instructions

- Always plan first
- Think harder in the planning phase
- When proposing tasks, highlight potential critical points that could lead to side effects.

## Branches, Commits and PRs

- Commit messages should follow the semantic commit conventions of Conventional Commits (https://www.conventionalcommits.org/en/v1.0.0/).
  - At least, they MUST contain one line with the following format: `<type-code>: <message>` where `<type-code>` indicates the type of comment. Type of comments can be fixes and bugfixes (`fix:`), enhancements and new features (`enh:`), style (`sty:`), documentation (`doc:`), maintenance (`mnt:`), etc.
- PR titles should also be semantic, and use the same Type codes but in all caps (e.g., `FIX:`, `ENH:`, `STY:`, `DOC:`, `STY:`, `MNT:`)
- Branch names should start with a type code too, with pattern `<type-code>/<branch-name>`. If addressing a specific issue, the issue number will be included at the end of `<branch-name>`, e.g., `fix/display-glitch-123` for issue #123.

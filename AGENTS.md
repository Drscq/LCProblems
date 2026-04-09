# Repository Guidelines

## Project Structure & Module Organization
`README.md` is the top-level index for the repository. Problem writeups are organized by source or topic in folders such as `Meta/`, `Google/`, `Uber/`, `Practices/`, `Category/`, and `LearningMaterial/`. Contest work lives in `Contest/Weekly/848/` and pairs `Question<N>.py` scripts with `Question<N>.md` notes. Images belong under `Figures/` and usually mirror the content folder, for example `Figures/Meta/...` or `Figures/google/...`. Add new material to the closest existing directory and keep file names aligned with the current pattern.

## Build, Test, and Development Commands
There is no repository-wide build system, dependency manifest, or CI workflow. Use simple local checks:

```bash
python3 Contest/Weekly/848/Question1.py
python3 Contest/Weekly/848/Question4.py
rg --files
git diff --stat
```

Run Python scripts directly to exercise the embedded sample cases. Use `rg --files` to navigate the content quickly, and `git diff --stat` before committing to confirm you did not touch unrelated notes or figures.

## Coding Style & Naming Conventions
Use 4-space indentation in Python. Keep contest scripts runnable with a small `if __name__ == "__main__":` block that prints sample inputs and expected outputs. Follow the existing naming scheme: Markdown notes use `<number> <Problem Title>.md`, while contest scripts use `Question<N>.py`.

In Markdown, start with `# <number>. <Title>` when the file is problem-specific. Prefer short, consistent sections such as `Examples`, `Constraints`, `Solution`, and `Complexity Analysis`. Add language tags to fenced code blocks, for example `cpp`, `python`, or `javascript`.

## Testing Guidelines
There is no automated test suite or coverage target. For Python files, run the script and verify the printed results still match the documented expectations. For Markdown-only changes, check that relative links, figure paths, and complexity claims are still accurate.

## Commit & Pull Request Guidelines
Recent history uses short, imperative commit subjects such as `Add problem description and C++ solution for "20 Valid Parentheses"`. Keep commits focused on one problem set or topic. Pull requests should summarize the directories changed, list newly added problems or figures, and mention any manual verification performed. Include screenshots only when updating rendered assets or diagrams.

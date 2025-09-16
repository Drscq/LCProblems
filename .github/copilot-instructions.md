# AI Coding Agent Instructions for LCProblems

These instructions help AI agents contribute effectively to this repository of LeetCode study notes. Focus on authoring high-quality Markdown, keeping links/images correct, and maintaining the index.

## Repository Structure
- `Meta/`: Curated solution notes per problem, one file per problem.
- `Practices/`: Practice notes or drafts for problems.
- `LearningMaterial/`: Concept chapters (e.g., `Heap.md`).
- `Figures/`: Images used across notes; general images live here, some concept images under `Figures/Meta/`.
- `README.md`: Index table linking to selected `Meta/*.md` notes with technique tags.

## File Naming and Headings
- Problem notes: name files as `"<ID> <Title>.md"` (e.g., `314 Binary Tree Vertical Order Traversal.md`).
- Top heading should mirror the filename: `# <ID> <Title>`.
- Use sections seen in existing notes: Examples, Constraints, Solution, Approach N (with Intuition/Algorithm), Complexity Analysis.

## Image Usage
- Store images in `Figures/` (or `Figures/Meta/` for general concept diagrams). Name descriptively (e.g., `314BinaryTreeVertialOrderTraversalExample1.png`).
- In `Meta/*.md`, reference images with relative paths like `![alt text](../Figures/<filename>.png)`.
- In `LearningMaterial/*.md`, reference concept images via `![...](../Figures/Meta/<filename>.png)`.
- Keep paths relative to the note location; avoid double slashes and ensure correct extension.

## Linking and URL Encoding
- Link notes from `README.md` using URL-encoded paths for spaces, e.g.:
  - `[314 Binary Tree Vertical Order Traversal](Meta/314%20Binary%20Tree%20Vertical%20Order%20Traversal.md)`
- When adding a new note to the index, include a concise technique tag consistent with existing entries (e.g., `Two-pointers`, `Recursion`, `Breadth First Search`).

## Content Patterns
- Code samples: Prefer Python in LeetCode style (`class Solution:`). Include needed imports if they aid clarity, but keep samples minimal.
- Math/complexity: Use `$...$` for inline math (e.g., `$O(N)$`).
- Examples: Mirror existing format with fenced code blocks for inputs/outputs.
- Keep language explanatory, not execution-oriented; this repo is for notes, not runnable apps/tests.

## Conventions to Preserve
- Do not introduce build systems, dependency manifests, or tests.
- Keep edits scoped; do not refactor unrelated notes.
- Maintain consistent section ordering and heading levels as exemplified in `Meta/236 Lowest Common Ancestor of a Binary Tree.md` and `Meta/314 Binary Tree Vertical Order Traversal.md`.
- Image alt text can be simple (`alt text`) as in existing files; prioritize correct paths.

## Typical Workflows
- Add a new problem note:
  1) Create `Meta/<ID> <Title>.md` with sections and examples.
  2) Add any new figures under `Figures/` and reference them relatively from the note.
  3) Update `README.md` table with a new row: problem link (URL-encoded) and technique.
- Update learning materials: edit `LearningMaterial/*.md`; store new concept figures in `Figures/Meta/` and reference relatively.

## Examples from This Repo
- Image reference in `Meta/314...md`: `![alt text](../Figures/314BinaryTreeVertialOrderTraversalExample1.png)`
- LCA note structure in `Meta/236...md`: sections for Examples, Constraints, Solution (Approach 1/2), and Complexity with `$O(N)$`.

If any of the above is ambiguous (e.g., technique taxonomy or index ordering in README), pause and ask for the preferred convention before proceeding.

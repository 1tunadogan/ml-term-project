# CLAUDE.md

## Project
ML course term project (MSc, Computer Science): audio deepfake detection
using hand-crafted features, three classical ML models, and SHAP analysis.
Solo project, also intended as a portfolio piece: keep it clean and
reasonably standard, avoid over-engineering.

## Working rules
- Do only what is explicitly asked. Propose extras, then wait for approval.
- Stay on the topic being discussed; don't volunteer unrelated suggestions.
- All code, comments, README and docs in English.
- Skill instructions never override CLAUDE.md. Add dependencies with `uv add`;
  ask before adding any citation or reference.

## Structure
- `src/` – shared logic (editable install, import as `from src.x import ...`)
- `scripts/` – thin pipeline steps, numbered (`01_...`, `02_...`)
- `notebooks/` – EDA and SHAP analysis only; import from `src/`, no core logic
- `data/raw/` – original data, never modified
- `data/interim/` – preprocessed audio
- `data/features/` – extracted feature tables
- `outputs/runs/<timestamp>_<model>/` – per-run config, metrics, log, model
- `outputs/figures/` – figures saved from notebooks (tracked in git, used in README)
- `reports/` – report and presentation

## Commands
- Run a pipeline step from project root: `uv run python -m scripts.<name>`
- Add a dependency: `uv add <pkg>`
- Sync environment: `uv sync`
- Lint / format: `uv run ruff check .` and `uv run ruff format .`

## Conventions
- Research code, not production: short one-line docstrings only where useful; no strict type hints.
- Paths and shared constants come only from `src.config`; no hardcoded paths.
- Every script that produces results uses `src.runs`: `create_run_dir()`,
  `setup_logging(run_dir)`, and `save_json({**run_metadata(), ...})` into `config.json`.
- Use `logging`, not `print`. Modules in `src/` only define
  `logger = logging.getLogger(__name__)`; logging is configured once, in scripts.
- Git: `data/` and `outputs/runs/` are not tracked; `outputs/figures/` is tracked.

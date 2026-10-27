"""File-based experiment tracking helpers."""

import json
import logging
import platform
from datetime import datetime

from src.config import RUNS_DIR, SEED


def create_run_dir(name):
    """Create outputs/runs/<timestamp>_<name>/."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = RUNS_DIR / f"{timestamp}_{name}"
    run_dir.mkdir(parents=True)
    return run_dir


def setup_logging(run_dir=None, level=logging.INFO):
    """Log to console and, if run_dir is given, to run_dir/run.log."""
    handlers = [logging.StreamHandler()]
    if run_dir is not None:
        handlers.append(logging.FileHandler(run_dir / "run.log"))
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
        force=True,
    )


def save_json(data, path):
    path.write_text(json.dumps(data, indent=2, default=str))


def load_json(path):
    return json.loads(path.read_text())


def run_metadata():
    """Timestamp, Python version and seed of a run."""
    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "python_version": platform.python_version(),
        "seed": SEED,
    }

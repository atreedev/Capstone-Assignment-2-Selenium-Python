from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> int:
    (ROOT / "reports" / "html").mkdir(parents=True, exist_ok=True)
    (ROOT / "reports" / "screenshots").mkdir(parents=True, exist_ok=True)

    completed = subprocess.run(
        [sys.executable, "-m", "pytest", "-v"],
        cwd=ROOT,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())

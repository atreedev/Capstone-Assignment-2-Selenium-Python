from __future__ import annotations

import logging
from pathlib import Path


def get_logger(name: str = "automation") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    log_dir = Path("reports/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "automation.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger

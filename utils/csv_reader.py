from __future__ import annotations

import csv
from pathlib import Path


class CSVReader:
    """Small dependency-free CSV reader for test data."""

    @staticmethod
    def read_rows(path: str | Path) -> list[dict[str, str]]:
        csv_path = Path(path)
        if not csv_path.exists():
            raise FileNotFoundError(f"CSV test data not found: {csv_path}")
        with csv_path.open("r", newline="", encoding="utf-8-sig") as handle:
            return list(csv.DictReader(handle))

    @staticmethod
    def find_row(path: str | Path, test_case: str) -> dict[str, str]:
        rows = CSVReader.read_rows(path)
        for row in rows:
            if row.get("test_case", "").strip().casefold() == test_case.strip().casefold():
                return row
        raise KeyError(f"No CSV row found for test_case={test_case!r}")

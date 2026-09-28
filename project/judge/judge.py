from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

RUBRIC = [
    ("F01", "Project structure and separation of concerns", 10),
    ("F02", "Selenium WebDriver / browser factory", 10),
    ("F03", "Page Object Model", 15),
    ("F04", "Configuration management", 10),
    ("F05", "CSV test-data handling", 10),
    ("F06", "PyTest login/search coverage", 15),
    ("F07", "unittest coverage", 10),
    ("F08", "Failure screenshots", 10),
    ("F09", "HTML reporting", 5),
    ("F10", "Maintainability / documentation", 5),
]

REQUIRED_PATHS = [
    "config/config.ini",
    "data/test_data.csv",
    "docs/ARCHITECTURE.md",
    "docs/FEATURE_BACKLOG.md",
    "docs/JUDGING.md",
    "pages/base_page.py",
    "pages/home_page.py",
    "pages/login_page.py",
    "pages/products_page.py",
    "tests/test_login_pytest.py",
    "tests/test_login_unittest.py",
    "tests/test_product_search_pytest.py",
    "utils/config_manager.py",
    "utils/csv_reader.py",
    "utils/driver_factory.py",
    "utils/screenshot.py",
    "conftest.py",
    "pytest.ini",
    "requirements.txt",
    "README.md",
]


def syntax_errors() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.py"):
        if any(part in {".venv", "__pycache__"} for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            errors.append(f"{path.relative_to(ROOT)}:{exc.lineno}:{exc.offset}: {exc.msg}")
    return errors


def score_presence(paths: Iterable[str]) -> tuple[bool, list[str]]:
    missing = [path for path in paths if not (ROOT / path).exists()]
    return not missing, missing


def score_framework() -> dict:
    results = {}

    results["F01"] = (score_presence(REQUIRED_PATHS)[0], "Required project files present")
    results["F02"] = (exists_with("utils/driver_factory.py", ["class DriverFactory", "webdriver.Chrome"]), "DriverFactory exists")
    results["F03"] = (all(exists_with(path, ["class "]) for path in [
        "pages/base_page.py", "pages/home_page.py", "pages/login_page.py", "pages/products_page.py"
    ]), "Page objects present")
    results["F04"] = (exists_with("utils/config_manager.py", ["class ConfigManager", "os.getenv"]), "Config manager + environment override present")
    results["F05"] = (exists_with("utils/csv_reader.py", ["class CSVReader", "csv.DictReader"]) and (ROOT / "data/test_data.csv").exists(), "CSV reader and data present")
    results["F06"] = (all(exists_with(path, ["pytest", "assert"]) for path in [
        "tests/test_login_pytest.py", "tests/test_product_search_pytest.py"
    ]), "PyTest login/search tests present")
    results["F07"] = (exists_with("tests/test_login_unittest.py", ["unittest.TestCase", "setUpClass"]), "unittest test class present")
    results["F08"] = (exists_with("conftest.py", ["pytest_runtest_makereport", "capture_screenshot"]), "Failure screenshot hook present")
    results["F09"] = (exists_with("pytest.ini", ["--html"]) and exists_with("requirements.txt", ["pytest-html"]), "HTML report plugin and configuration present")
    results["F10"] = (all((ROOT / p).exists() for p in ["README.md", "docs/ARCHITECTURE.md", "docs/FEATURE_BACKLOG.md", "docs/JUDGING.md"]), "Documentation present")
    return results


def exists_with(relative: str, needles: list[str]) -> bool:
    path = ROOT / relative
    if not path.exists():
        return False
    content = path.read_text(encoding="utf-8")
    return all(needle in content for needle in needles)


def main() -> int:
    syntax = syntax_errors()
    results = score_framework()
    total = sum(points for _, _, points in RUBRIC)
    earned = 0
    print("=" * 72)
    print("CAPSTONE ASSIGNMENT 2 — PROJECT JUDGE")
    print("=" * 72)
    for feature_id, description, points in RUBRIC:
        passed, evidence = results[feature_id]
        awarded = points if passed else 0
        earned += awarded
        status = "PASS" if passed else "FAIL"
        print(f"{feature_id} [{status:4}] {awarded:>2}/{points:<2}  {description}")
        print(f"       Evidence: {evidence}")

    print("-" * 72)
    if syntax:
        print("SYNTAX ERRORS:")
        for error in syntax:
            print(f"  - {error}")
        print("Syntax gate: FAIL")
        earned = 0
    else:
        print("Syntax gate: PASS — all Python files parsed successfully")

    print(f"Framework evidence score: {earned}/{total}")
    print("Runtime browser tests are intentionally not replaced by this static judge.")
    print("Run `python run_tests.py` for execution evidence.")
    return 0 if earned == total and not syntax else 1


if __name__ == "__main__":
    raise SystemExit(main())

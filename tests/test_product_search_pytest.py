from __future__ import annotations

from pathlib import Path

import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.csv_reader import CSVReader


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data" / "test_data.csv"
SEARCH_CASES = [row for row in CSVReader.read_rows(CSV_PATH) if row.get("test_case") == "product_search"]


@pytest.mark.search
@pytest.mark.smoke
@pytest.mark.parametrize("case", SEARCH_CASES, ids=lambda case: f"search={case['search_term']}")
def test_product_search_from_csv(driver, base_url, case):
    """Assignment 2 core scenario driven entirely by external CSV test data."""
    home = HomePage(driver, base_url)
    products = ProductsPage(driver, timeout=15)

    home.open_home_page()
    assert home.is_loaded(), "Home page should be visible after launch"

    home.go_to_products()
    assert products.is_loaded(), "Products page should be visible"

    products.search(case["search_term"])
    assert products.is_search_results_visible(), "Searched Products heading should be visible"

    actual_heading = products.get_text(products.SEARCHED_PRODUCTS_HEADING)
    assert actual_heading.casefold() == case["expected_heading"].casefold(), (
        f"Expected heading {case['expected_heading']!r}; got {actual_heading!r}"
    )

    product_names = products.get_product_names()
    assert product_names, "At least one product should be returned for the search"

    # The application may return related products whose displayed names do not
    # contain the exact search string. Validate the data-driven expectation
    # instead of incorrectly requiring every returned name to contain it.
    expected_fragment = case["expected_product_fragment"].casefold().strip()
    assert any(expected_fragment in name.casefold() for name in product_names), (
        f"Expected at least one result containing {case['expected_product_fragment']!r}; got {product_names!r}"
    )


@pytest.mark.search
def test_search_reader_returns_expected_fields(test_data_path):
    """Unit-level data contract check: CSV rows contain the fields used by UI tests."""
    rows = CSVReader.read_rows(test_data_path)
    assert rows, "CSV should contain at least one test-data row"
    required_fields = {
        "test_case",
        "search_term",
        "expected_heading",
        "expected_product_fragment",
        "invalid_email",
        "invalid_password",
    }
    assert required_fields.issubset(rows[0].keys())

# Shared set-up for the tests. You don't need to change this file.
# matplotlib's Agg backend draws charts in memory only, so no window opens while the tests run. Each test that
# asks for creamery gets its own fresh copy of Hilltop Creamery's three files, made by seed.py in a temporary
# folder and read with pandas, so the tests check your code against the same data even if you changed the CSV
# files in your folder.
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import pytest

from seed import write_creamery


@pytest.fixture
def creamery(tmp_path):
    """The three seeded files, read into DataFrames: creamery["daily"], creamery["flavors"] and creamery["orders"]."""
    folder = write_creamery(tmp_path)
    return {
        "daily": pd.read_csv(folder / "daily.csv", parse_dates=["date"]),
        "flavors": pd.read_csv(folder / "flavors.csv"),
        "orders": pd.read_csv(folder / "orders.csv"),
    }


@pytest.fixture(autouse=True)
def close_charts():
    """Closes every chart a test made, so charts don't pile up in memory."""
    yield
    plt.close("all")

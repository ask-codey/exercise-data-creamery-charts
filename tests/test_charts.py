# Tests for charts.py. Run them with: python -m pytest (in the exercise folder, with the virtual environment active).
# Each test calls one of your chart functions, on the data seed.py makes (in a temporary folder) or on a small table
# written in the test, and reads the chart it returns: its title, its axis labels and the data it draws. Nothing is
# compared by pixels. A failing test says what it read, what it expected and what it found. You don't need to change
# this file.
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from charts import cones_over_time, flavor_bars, order_totals_histogram, temperature_vs_cones


def check(call, got, expected):
    """Fails with a message that says what the chart showed and what it should show."""
    assert got == expected, f"{call} should give {expected!r}, but it gave {got!r}."


def chart(result, name):
    """Checks that a chart function returned (fig, ax), and returns them."""
    assert isinstance(result, tuple) and len(result) == 2, (
        f"{name} should return two things, fig and ax (return fig, ax), but it returned {result!r}.")
    fig, ax = result
    assert isinstance(fig, Figure), f"The first thing {name} returns should be the Figure, but it was {fig!r}."
    assert isinstance(ax, Axes), f"The second thing {name} returns should be the Axes, but it was {ax!r}."
    return fig, ax


def labels(ax):
    """The chart's title, x-axis label and y-axis label."""
    return ax.get_title(), ax.get_xlabel(), ax.get_ylabel()


def numbers(values):
    """Plotted values as a plain list of numbers, whole numbers shown without .0."""
    return [int(v) if float(v).is_integer() else float(v) for v in values]


def bar_heights(ax):
    return numbers(bar.get_height() for bar in ax.patches)


def small_daily(cones, temps=None):
    """A small daily table for one test: one row a day from January 1, 2025."""
    days = len(cones)
    return pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=days),
        "high_temp_f": temps or [50] * days,
        "cones_sold": cones,
        "rainy": [False] * days,
    })


# cones_over_time

def test_1_cones_over_time_returns_fig_and_ax_titled_cones_sold_each_day_2025_with_date_and_cones_sold_labels(creamery):
    fig, ax = chart(cones_over_time(creamery["daily"]), "cones_over_time(daily)")
    check("cones_over_time(daily)'s title, x label and y label", labels(ax),
          ("Cones sold each day, 2025", "Date", "Cones sold"))


def test_2_cones_over_time_draws_one_line_of_365_points(creamery):
    fig, ax = chart(cones_over_time(creamery["daily"]), "cones_over_time(daily)")
    check("the number of lines on cones_over_time(daily)", len(ax.get_lines()), 1)
    check("the number of points on the line", len(ax.get_lines()[0].get_ydata()), 365)


def test_3_cones_over_time_line_starts_4_6_4_and_ends_on_december_31(creamery):
    fig, ax = chart(cones_over_time(creamery["daily"]), "cones_over_time(daily)")
    line = ax.get_lines()[0]
    check("the line's first three y values", numbers(line.get_ydata()[:3]), [4, 6, 4])
    check("the line's last date", str(pd.Series(line.get_xdata()).iloc[-1].date()), "2025-12-31")


def test_4_cones_over_time_draws_12_30_and_21_for_a_three_day_table():
    fig, ax = chart(cones_over_time(small_daily([12, 30, 21])), "cones_over_time(df)")
    check("cones_over_time(df)'s y values for cones 12, 30, 21", numbers(ax.get_lines()[0].get_ydata()), [12, 30, 21])


def test_5_cones_over_time_tilts_the_dates(creamery):
    fig, ax = chart(cones_over_time(creamery["daily"]), "cones_over_time(daily)")
    rotation = ax.get_xticklabels()[0].get_rotation()
    assert rotation != 0, "The dates on cones_over_time(daily) should be tilted with fig.autofmt_xdate(), but they're flat."


# flavor_bars

def test_6_flavor_bars_is_titled_scoops_sold_by_flavor_2025_with_flavor_and_scoops_sold_labels(creamery):
    fig, ax = chart(flavor_bars(creamery["flavors"]), "flavor_bars(flavors)")
    check("flavor_bars(flavors)'s title, x label and y label", labels(ax),
          ("Scoops sold by flavor, 2025", "Flavor", "Scoops sold"))


def test_7_flavor_bars_draws_12_bars_from_8573_down_to_2030(creamery):
    fig, ax = chart(flavor_bars(creamery["flavors"]), "flavor_bars(flavors)")
    check("flavor_bars(flavors)'s bar heights, left to right", bar_heights(ax),
          [8573, 7836, 7018, 6431, 6308, 5342, 4878, 4383, 3757, 3332, 2521, 2030])


def test_8_flavor_bars_puts_900_4000_2500_in_order_4000_2500_900_with_their_names():
    flavors = pd.DataFrame({"flavor": ["Pistachio", "Vanilla Bean", "Strawberry"], "scoops_sold": [900, 4000, 2500]})
    fig, ax = chart(flavor_bars(flavors), "flavor_bars(df)")
    check("flavor_bars(df)'s bar heights for 900, 4000, 2500", bar_heights(ax), [4000, 2500, 900])
    fig.canvas.draw()
    check("flavor_bars(df)'s names under the bars", [t.get_text() for t in ax.get_xticklabels()],
          ["Vanilla Bean", "Strawberry", "Pistachio"])


def test_9_flavor_bars_leaves_the_table_it_was_given_in_menu_order():
    flavors = pd.DataFrame({"flavor": ["Pistachio", "Vanilla Bean", "Strawberry"], "scoops_sold": [900, 4000, 2500]})
    flavor_bars(flavors)
    check("the table's flavors after flavor_bars(df)", flavors["flavor"].tolist(),
          ["Pistachio", "Vanilla Bean", "Strawberry"])


# temperature_vs_cones

def test_10_temperature_vs_cones_is_titled_hotter_days_sell_more_cones_with_temperature_and_cones_labels(creamery):
    fig, ax = chart(temperature_vs_cones(creamery["daily"]), "temperature_vs_cones(daily)")
    check("temperature_vs_cones(daily)'s title, x label and y label", labels(ax),
          ("Hotter days sell more cones", "High temperature (°F)", "Cones sold"))


def test_11_temperature_vs_cones_draws_365_dots_at_alpha_0_5(creamery):
    fig, ax = chart(temperature_vs_cones(creamery["daily"]), "temperature_vs_cones(daily)")
    check("the number of dot sets on temperature_vs_cones(daily)", len(ax.collections), 1)
    dots = ax.collections[0]
    check("the number of dots", len(dots.get_offsets()), 365)
    check("the dots' alpha", dots.get_alpha(), 0.5)


def test_12_temperature_vs_cones_puts_days_of_50_80_65_degrees_at_40_300_150_cones():
    daily = small_daily([40, 300, 150], temps=[50, 80, 65])
    fig, ax = chart(temperature_vs_cones(daily), "temperature_vs_cones(df)")
    dots = [numbers(point) for point in ax.collections[0].get_offsets()]
    check("temperature_vs_cones(df)'s dots as [temperature, cones]", dots, [[50, 40], [80, 300], [65, 150]])


# order_totals_histogram

def test_13_order_totals_histogram_is_titled_most_orders_are_under_15_with_total_and_count_labels(creamery):
    fig, ax = chart(order_totals_histogram(creamery["orders"], 10), "order_totals_histogram(orders, 10)")
    check("order_totals_histogram(orders, 10)'s title, x label and y label", labels(ax),
          ("Most orders are under $15", "Order total ($)", "Number of orders"))


def test_14_order_totals_histogram_with_bins_10_draws_10_bars_holding_all_5000_orders(creamery):
    fig, ax = chart(order_totals_histogram(creamery["orders"], 10), "order_totals_histogram(orders, 10)")
    check("the number of bars for bins=10", len(ax.patches), 10)
    check("the orders in all the bars together", sum(bar_heights(ax)), 5000)


def test_15_order_totals_histogram_with_5_dollar_bins_from_0_to_50_counts_1301_1425_1106_on_down_to_12(creamery):
    edges = list(range(0, 55, 5))
    fig, ax = chart(order_totals_histogram(creamery["orders"], edges), "order_totals_histogram(orders, [0, 5, ..., 50])")
    check("the bars' heights for bins of $5 from $0 to $50", bar_heights(ax),
          [1301, 1425, 1106, 489, 294, 182, 76, 70, 45, 12])


def test_16_order_totals_histogram_counts_4_25_6_50_12_00_14_75_as_1_1_2_in_bins_0_5_10_15():
    orders = pd.DataFrame({"order_id": ["HC-1", "HC-2", "HC-3", "HC-4"], "items": [1, 1, 2, 3],
                           "order_total": [4.25, 6.50, 12.00, 14.75]})
    fig, ax = chart(order_totals_histogram(orders, [0, 5, 10, 15]), "order_totals_histogram(df, [0, 5, 10, 15])")
    check("the bars' heights for $4.25, $6.50, $12.00, $14.75 in bins 0-5, 5-10, 10-15", bar_heights(ax), [1, 1, 2])

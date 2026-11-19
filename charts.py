"""Hilltop Creamery's year in four charts: four chart functions for you to finish.

The docstring under each function says exactly what its chart must show: the kind of chart, the
data, the title and the two axis labels, word for word. Replace each
raise NotImplementedError("Not built yet.") line with your own code.

Every function starts its chart with
    fig, ax = plt.subplots()
draws on ax, and ends with
    return fig, ax
so the tests can read the chart: its title, its labels and the data it draws. Don't call
plt.show() or fig.savefig() in these functions; report.py saves the charts for you. The table a
function is given must stay exactly as it was.
"""
import matplotlib.pyplot as plt


def cones_over_time(daily):
    """A line chart of the cones sold each day of the year.

    daily has one row a day, with a date column (dates, not text) and cones_sold.
    x: daily["date"], y: daily["cones_sold"], one line, in date order.
    Title: "Cones sold each day, 2025"
    x-axis label: "Date"
    y-axis label: "Cones sold"
    Tilt the dates with fig.autofmt_xdate() so they don't overlap.
    """
    raise NotImplementedError("Not built yet.")


def flavor_bars(flavors):
    """A bar chart of the scoops sold of each flavor, largest first.

    flavors has a flavor column and a scoops_sold column, in menu order.
    One vertical bar a flavor (ax.bar), sorted from the most scoops on the left to the fewest on
    the right, with each flavor's name under its bar.
    Title: "Scoops sold by flavor, 2025"
    x-axis label: "Flavor"
    y-axis label: "Scoops sold"
    Turn the flavor names on their side with ax.tick_params(axis="x", labelrotation=90) so they fit.

    Flavors with 900, 4000 and 2500 scoops: the bars' heights, left to right, are 4000, 2500, 900.
    """
    raise NotImplementedError("Not built yet.")


def temperature_vs_cones(daily):
    """A scatter plot of each day's high temperature against the cones sold that day.

    One dot a day: x is daily["high_temp_f"], y is daily["cones_sold"]. Make the dots
    see-through with alpha=0.5, so the crowded parts show darker.
    Title: "Hotter days sell more cones"
    x-axis label: "High temperature (°F)"
    y-axis label: "Cones sold"
    """
    raise NotImplementedError("Not built yet.")


def order_totals_histogram(orders, bins):
    """A histogram of July's order totals, with the number of bars that bins says.

    orders has an order_total column (dollars). Pass bins straight to ax.hist, so bins=10
    draws 10 bars and bins=[0, 5, 10] draws two bars, $0 to $5 and $5 to $10.
    Title: "Most orders are under $15"
    x-axis label: "Order total ($)"
    y-axis label: "Number of orders"
    """
    raise NotImplementedError("Not built yet.")

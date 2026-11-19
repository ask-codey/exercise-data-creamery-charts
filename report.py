# Makes Hilltop Creamery's four charts with your functions from charts.py, saves each one as a PNG in a charts
# folder, and prints what each chart holds, so you can see them at work. Ready to use.
# Make the data first with: python seed.py
# Run it with: python report.py
from pathlib import Path

import matplotlib

matplotlib.use("Agg")   # draw the charts in memory and save them; no window opens

import pandas as pd

from charts import cones_over_time, flavor_bars, order_totals_histogram, temperature_vs_cones

daily = pd.read_csv("daily.csv", parse_dates=["date"])
flavors = pd.read_csv("flavors.csv")
orders = pd.read_csv("orders.csv")
folder = Path("charts")
folder.mkdir(exist_ok=True)

fig, ax = cones_over_time(daily)
fig.savefig(folder / "cones-over-time.png")
print("1) points on the line:", len(ax.get_lines()[0].get_ydata()))

fig, ax = flavor_bars(flavors)
fig.savefig(folder / "flavor-bars.png", bbox_inches="tight")
fig.canvas.draw()
names = [label.get_text() for label in ax.get_xticklabels()]
heights = [round(bar.get_height()) for bar in ax.patches]
print("2) tallest bar:", names[0], heights[0])
print("3) shortest bar:", names[-1], heights[-1])

fig, ax = temperature_vs_cones(daily)
fig.savefig(folder / "temperature-vs-cones.png")
print("4) dots on the scatter plot:", len(ax.collections[0].get_offsets()))

fig, ax = order_totals_histogram(orders, range(0, 55, 5))
fig.savefig(folder / "order-totals.png")
counts = [round(bar.get_height()) for bar in ax.patches]
print("5) histogram bars:", len(counts))
print("6) orders in the tallest bar:", max(counts))
print("7) charts saved in:", folder)

"""Makes Hilltop Creamery's three data files: our own made-up data. Ready to use.

Run it with: python seed.py

It writes three CSV files in this folder:

- daily.csv: one row for each day of 2025 (365 rows): date, high_temp_f (the day's high
  temperature in degrees Fahrenheit), cones_sold, and rainy (True or False).
- flavors.csv: the shop's 12 flavors in menu order, with the scoops of each sold in 2025.
- orders.csv: every order rung up in July 2025 (5,000 orders): order_id, items (how many
  things were in the order) and order_total (in dollars).

It uses a fixed random seed, so every run, on every computer, writes exactly the same files.
The tests make their own copies the same way.
"""
import csv
import math
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 2025
FIRST_DAY = date(2025, 1, 1)
DAYS = 365
ORDERS = 5000

# The flavors in the order the menu board lists them, with each one's share of the scoops.
FLAVORS = [
    ("Vanilla Bean", 0.138),
    ("Chocolate Fudge", 0.124),
    ("Strawberry", 0.071),
    ("Mint Chocolate Chip", 0.097),
    ("Cookie Dough", 0.115),
    ("Salted Caramel Swirl", 0.103),
    ("Butter Pecan", 0.041),
    ("Rocky Road", 0.058),
    ("Pistachio", 0.034),
    ("Coffee Toffee Crunch", 0.079),
    ("Black Raspberry", 0.088),
    ("Lemon Sorbet", 0.052),
]
SCOOPS = 62_000   # about this many scoops in the year

# What an order's items cost: a single cone, a double cone, a cup, a sundae, a milkshake.
PRICES = [4.25, 5.75, 4.50, 7.50, 6.50]
PRICE_SHARES = [0.42, 0.20, 0.16, 0.10, 0.12]
# How many items an order has: most orders are one or two people.
ITEM_COUNTS = [1, 2, 3, 4, 5, 6, 7, 8]
ITEM_SHARES = [0.44, 0.27, 0.12, 0.08, 0.04, 0.02, 0.015, 0.015]


def make_daily(rng):
    """One row a day: a high temperature that follows the seasons, some rainy days, and the cones sold."""
    rows = []
    for n in range(DAYS):
        day = FIRST_DAY + timedelta(days=n)
        season = math.sin(2 * math.pi * (n - 105) / 365)   # coldest in mid-January, warmest in mid-July
        high = round(58 + 26 * season + rng.gauss(0, 5))
        rain_chance = 0.30 if day.month in (3, 4, 5, 11) else 0.20
        rainy = rng.random() < rain_chance
        cones = max(0, 5.2 * (high - 32)) + rng.gauss(0, 18)
        if day.weekday() >= 5:      # Saturday and Sunday
            cones *= 1.35
        if rainy:
            cones *= 0.55
        rows.append({
            "date": day.isoformat(),
            "high_temp_f": high,
            "cones_sold": max(4, round(cones)),
            "rainy": rainy,
        })
    return rows


def make_flavors(rng):
    """The 12 flavors in menu order, each with the scoops sold in the year."""
    return [{"flavor": name, "scoops_sold": round(SCOOPS * share * rng.uniform(0.95, 1.05))}
            for name, share in FLAVORS]


def make_orders(rng):
    """July's orders: how many items each had and what it came to."""
    rows = []
    for number in range(1, ORDERS + 1):
        items = rng.choices(ITEM_COUNTS, weights=ITEM_SHARES)[0]
        total = sum(rng.choices(PRICES, weights=PRICE_SHARES, k=items))
        rows.append({"order_id": f"HC-{number:04d}", "items": items, "order_total": round(total, 2)})
    return rows


def make_creamery():
    """Every file's rows, as a dictionary of file name to rows."""
    rng = random.Random(SEED)
    return {
        "daily": make_daily(rng),
        "flavors": make_flavors(rng),
        "orders": make_orders(rng),
    }


def write_creamery(folder):
    """Writes daily.csv, flavors.csv and orders.csv into folder (a folder name or a Path) and returns the folder as a Path."""
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    for name, rows in make_creamery().items():
        with (folder / f"{name}.csv").open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    return folder


if __name__ == "__main__":
    write_creamery(Path(__file__).parent)
    for name, rows in make_creamery().items():
        print(f"Wrote {name}.csv: {len(rows)} rows.")

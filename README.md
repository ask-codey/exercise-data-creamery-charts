# Exercise: Hilltop Creamery Charts

Exercise code for the lesson **Exercise: Hilltop Creamery Charts** in the Python for Data Analysis course on [ask-codey.com](https://www.ask-codey.com).

Hilltop Creamery, an ice cream shop, wants its year on four charts: how many cones it sold each day, which flavors sell best, whether hot days sell more cones, and what a typical order comes to. You'll write the four chart functions in `charts.py`, and tests call each one and read the chart it returns: its title, its axis labels and the data it draws.

## What's here

- `seed.py`: makes the shop's three data files, our own made-up data: `daily.csv` (one row for each day of 2025, 365 rows), `flavors.csv` (12 flavors) and `orders.csv` (July's 5,000 orders). It uses a fixed random seed, so it writes the same files on every computer. Ready to use.
- `charts.py`: the four functions, `cones_over_time`, `flavor_bars`, `temperature_vs_cones` and `order_totals_histogram`. Each one stops with `NotImplementedError: Not built yet.` for now. The docstring under each says exactly what its chart must show. For you to finish.
- `explore.ipynb`: a notebook for looking at the data and trying your charts as you write them. The tests don't read it. Ready to use, and yours to change.
- `report.py`: makes the four charts with your functions, saves each one as a PNG in a `charts` folder, and prints what each chart holds. Ready to use.
- `tests/test_charts.py`: tests that call your functions and read the charts they return. You don't need to change this file.
- `tests/conftest.py`: sets matplotlib's `Agg` backend, which draws charts in memory without opening a window, and gives each test a fresh copy of the data, made by `seed.py` in a temporary folder, so the tests use the same data even if you changed the CSV files. Ready to use.
- `requirements.txt`: the packages this exercise needs, each at an exact version: pandas, matplotlib, ipykernel (so VS Code can run the notebook) and pytest. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `charts.py` and `seed.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment, the files Python and pytest make as they run, the three CSV files, which `seed.py` makes again whenever they're needed, and the `charts` folder `report.py` writes. Ready to use.

## Before you start

The packages go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

Then make the data, once:

```bash
python seed.py
```

It prints one line for each file it wrote. To look at the data, open `explore.ipynb`, choose the `.venv` kernel with **Select Kernel** (top right), and run the cells.

## Check your work

```bash
python -m pytest
```

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it read from your chart, what it expected and what it found, for example *flavor_bars(df)'s bar heights for 900, 4000, 2500 should give [4000, 2500, 900], but it gave [900, 4000, 2500].*

To see your charts, run:

```bash
python report.py
```

It saves them as PNG files in the `charts` folder; open any of them in VS Code to look.

## The rules

Each function makes its chart with `fig, ax = plt.subplots()`, draws on `ax`, and ends with `return fig, ax`. The titles and labels must match these exactly, capital letters and punctuation included:

| Function | Chart | Data | Title | x-axis label | y-axis label |
|---|---|---|---|---|---|
| `cones_over_time(daily)` | One line (`ax.plot`), dates tilted with `fig.autofmt_xdate()` | x `date`, y `cones_sold`, in date order | `Cones sold each day, 2025` | `Date` | `Cones sold` |
| `flavor_bars(flavors)` | Vertical bars (`ax.bar`), the most scoops on the left, names turned with `ax.tick_params(axis="x", labelrotation=90)` | x `flavor`, height `scoops_sold`, sorted largest first | `Scoops sold by flavor, 2025` | `Flavor` | `Scoops sold` |
| `temperature_vs_cones(daily)` | Dots (`ax.scatter`) with `alpha=0.5` | x `high_temp_f`, y `cones_sold` | `Hotter days sell more cones` | `High temperature (°F)` | `Cones sold` |
| `order_totals_histogram(orders, bins)` | A histogram (`ax.hist`), `bins` passed straight to it | `order_total` | `Most orders are under $15` | `Order total ($)` | `Number of orders` |

- Keep each function's name and parameters as they are.
- Don't change the table a function is given: `sort_values` hands back a sorted copy, which is what `flavor_bars` needs.
- Don't call `plt.show()` or `fig.savefig()` in these functions: `report.py` saves the charts.
- Don't change the tests, `conftest.py`, `seed.py` or `report.py`.

## Tips

- Try each chart in `explore.ipynb` first, on the real data, then move the lines that work into `charts.py`.
- In the notebook, the chart a function makes shows under the cell, so `fig, ax = flavor_bars(flavors)` is enough to see it.
- `flavors.sort_values("scoops_sold", ascending=False)` puts the most scoops first.
- `ax.tick_params(axis="x", labelrotation=90)` turns the flavor names on their side, so they don't run into each other.
- `°` is the degree sign. If it's hard to type, copy it from this README or from the docstring.
- After you change `charts.py`, restart the notebook's kernel before you try it there, so the notebook imports your newest code.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.

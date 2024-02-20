import matplotlib.pyplot as plt
from load_csv import load
from pint import UnitRegistry
import numpy as np


class Convert:
    """Class for converting short scale values to raw numbers"""
    def __init__(self):
        """Constructor for the Convert class"""
        self.ureg = UnitRegistry()
        self.ureg.define("thousand = 1e3 = k")
        self.ureg.define("million = 1e6 = M")
        self.ureg.define("billion = 1e9 = B")

    def short_to_raw(self, val):
        """Converts a short scale value to a raw number"""
        try:
            return float(val)
        except ValueError:
            return self.ureg(val).to_base_units().magnitude


def main():
    convert = Convert()
    csv = load("population_total.csv")

    data = csv.loc[csv["country"] == "France"]
    years = data.columns[1:]
    values = data.values[0][1:]
    values = np.array([convert.short_to_raw(val) for val in values])
    plt.plot(years.astype(int), values.astype(float))

    data = csv.loc[csv["country"] == "Belgium"]
    years = data.columns[1:]
    values = data.values[0][1:]
    values = np.array([convert.short_to_raw(val) for val in values])
    plt.plot(years.astype(int), values.astype(float))

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xlim(1800, 2050)
    plt.legend(["Belgium", "France"], loc="lower right")
    plt.show()
    return


if __name__ == "__main__":
    main()

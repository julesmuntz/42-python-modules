import matplotlib.pyplot as plt
from load_csv import load
from pint import UnitRegistry
import mplcursors


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
    csv_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    csv_le = load("life_expectancy_years.csv")

    values_gdp = csv_gdp["1900"].apply(convert.short_to_raw).astype(float)
    values_le = csv_le["1900"].apply(convert.short_to_raw).astype(float)
    plt.scatter(values_gdp.astype(float), values_le.astype(float))
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    cursor = mplcursors.cursor(
        plt.scatter(values_gdp.astype(float), values_le.astype(float))
    )
    cursor.connect(
        "add",
        lambda sel: sel.annotation.set_text(
            "Country: {}\nGDP: {}\nLife expectancy: {}".format(
                csv_gdp["country"][sel.index], sel.target[0], sel.target[1]
            )
        ),
    )
    plt.show()
    return


if __name__ == "__main__":
    main()

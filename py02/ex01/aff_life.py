import matplotlib.pyplot as plt
from load_csv import load


def main():
    csv = load("life_expectancy_years.csv")
    if csv is None:
        print("File not found")
        return
    data = csv.loc[csv["country"] == "France"]
    years = data.columns[1:]
    values = data.values[0][1:]
    plt.plot(years.astype(int), values.astype(float))
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()
    return


if __name__ == "__main__":
    main()

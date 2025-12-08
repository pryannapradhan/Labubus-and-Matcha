import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_individual_figs():
    dfs = ld_cln_data()  # load in cleaned datasets

    # loop through dictionary and generate individual graphs for each dataset
    for name, df in dfs.items():
        plt.figure(figsize=(12, 5))
        plt.plot(df["Date"], df["Price"])
        plt.title(f"{name.capitalize()} Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    plot_individual_figs()
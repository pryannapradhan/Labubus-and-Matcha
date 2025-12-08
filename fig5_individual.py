import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_individual_figs():
    dfs = ld_cln_data()  # load in cleaned datasets

    for name, df in dfs.items():
        plt.figure(figsize=(12, 5))

        # loop through dictionary and generate individual graphs for each dataset
        if 'Price' in df.columns:
            y_col = 'Price'
        elif 'TotalSales' in df.columns:
            y_col = 'TotalSales'
        elif 'CPI' in df.columns:
            y_col = 'CPI'
        elif 'GDP' in df.columns:
            y_col = 'GDP'
        elif 'UnemploymentRate' in df.columns:
            y_col = 'UnemploymentRate'

        plt.plot(df["Date"], df[y_col])
        plt.title(f"{name.capitalize()} Over Time")
        plt.xlabel("Date")
        plt.ylabel(y_col)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    plot_individual_figs()
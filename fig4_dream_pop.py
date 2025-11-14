import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig4():
    dfs = ld_cln_data()

    df_dreams = dfs["dreams"]
    df_pop = dfs["pop"]

    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(df_dreams['Date'], df_dreams['Close'], color='blue', label='Dreams Inc.')
    ax1.set_ylabel("Dreams Inc.", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(df_pop['Date'], df_pop['Price'], color='red', linestyle='--', label='PopMart')
    ax2.set_ylabel("PopMart", color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title("Dual-Axis: Dreams Inc. vs PopMart")
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig4()
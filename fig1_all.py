import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig1():
    stock_data = ld_cln_data()

    df_dollar = stock_data["dollar"]
    df_dreams = stock_data["dreams"]
    df_estee = stock_data["estee"]
    df_pop = stock_data["pop"]
    df_pvh = stock_data["pvh"]
    df_starbucks = stock_data["starbucks"]
    df_target = stock_data["target"]
    df_tjx = stock_data["tjx"]
    df_ulta = stock_data["ulta"]
    df_walmart = stock_data["walmart"]

    fig, axes = plt.subplots(5, 2, figsize=(14, 18))
    fig.suptitle("Stock Price History (2021–2025)", fontsize=20)

    # Plot Dollar Tree
    axes[0, 0].plot(df_dollar['Date'], df_dollar['Price'], color="blue")
    axes[0, 0].set_title("Dollar Tree")
    # Plot Dreams
    axes[0, 1].plot(df_dreams['Date'], df_dreams['Close'], color="purple")
    axes[0, 1].set_title("Dreams Incorporated")
    # Plot Estee
    axes[1, 0].plot(df_estee['Date'], df_estee['Close'], color="brown")
    axes[1, 0].set_title("Estée Lauder")
    # Plot PopMart
    axes[1, 1].plot(df_pop['Date'], df_pop['Price'], color="red")
    axes[1, 1].set_title("PopMart")
    # Plot PVH
    axes[2, 0].plot(df_pvh['Date'], df_pvh['Price'], color="pink")
    axes[2, 0].set_title("PVH")
    # Plot Starbucks
    axes[2, 1].plot(df_starbucks['Date'], df_starbucks['Price'], color="green")
    axes[2, 1].set_title("Starbucks")
    # Plot Target
    axes[3, 0].plot(df_target['Date'], df_target['Price'], color="orange")
    axes[3, 0].set_title("Target")
    # Plot TJX
    axes[3, 1].plot(df_tjx['Date'], df_tjx['Price'], color="cyan")
    axes[3, 1].set_title("TJX")
    # Plot Ulta Beauty
    axes[4, 0].plot(df_ulta['Date'], df_ulta['Price'], color="magenta")
    axes[4, 0].set_title("Ulta Beauty")
    # Plot Walmart
    axes[4, 1].plot(df_walmart['Date'], df_walmart['Price'], color="black")
    axes[4, 1].set_title("Walmart")

    # label axes
    for ax in axes.flat:
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig1()
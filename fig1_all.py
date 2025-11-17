import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig1():
    stock_data = ld_cln_data()

    df_dreams = stock_data["dreams"]
    df_pop = stock_data["pop"]
    df_starbucks = stock_data["starbucks"]
    df_ulta = stock_data["ulta"]
    df_cars = stock_data["cars"]
    df_estee_21_25 = stock_data["estee_21_25"]

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle("Stock Price History (2021–2025)", fontsize=20)

    # plot dreams
    axes[0, 0].plot(df_dreams['Date'], df_dreams['Close'], color = "purple")
    axes[0, 0].set_title('Dreams Incorporated')

    # plot popmart
    axes[0, 1].plot(df_pop['Date'], df_pop['Price'], color = "red")
    axes[0, 1].set_title('PopMart')

    # plot starbucks
    axes[0, 2].plot(df_starbucks['Date'], df_starbucks['Price'], color = "green")
    axes[0, 2].set_title('Starbucks')

    # plot ulta
    axes[1, 0].plot(df_ulta['Date'], df_ulta['Price'], color = "orange")
    axes[1, 0].set_title('Ulta Beauty')

    # plot car sales
    axes[1, 1].plot(df_cars['Date'], df_cars['Price'], color = "black")
    axes[1, 1].set_title('Car Sales')

    # plot estee
    axes[1, 2].plot(df_estee_21_25['Date'], df_estee_21_25['Close'], color = "brown")
    axes[1, 2].set_title('Estee Lauder')

    # label aces
    for ax in axes.flat:
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig1()
import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig3():
    stock_data = ld_cln_data()

    df_dreams = stock_data["dreams"]
    df_pop = stock_data["pop"]
    df_starbucks = stock_data["starbucks"]
    df_ulta = stock_data["ulta"]
    df_cars = stock_data["cars"]
    df_estee_21_25 = stock_data["estee_21_25"]   # use only 2021–2025

    # plot overlay
    plt.figure(figsize=(14, 7))

    plt.plot(df_dreams['Date'], df_dreams['Price'], label='Dreams Inc.', color = "purple")
    plt.plot(df_pop['Date'], df_pop['Price'], label='PopMart', color = "red")
    plt.plot(df_starbucks['Date'], df_starbucks['Price'], label='Starbucks', color = "green")
    plt.plot(df_ulta['Date'], df_ulta['Price'], label='Ulta Beauty', color = "orange")
    plt.plot(df_cars['Date'], df_cars['Price'], label='Car Sales', color = "black")
    plt.plot(df_estee_21_25['Date'], df_estee_21_25['Price'], label='Estee Lauder (2021–2025)', color = "brown")

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("All Companies: Stock Price Overlay")
    plt.legend(title="Company", loc="upper left")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig3()
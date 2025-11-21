import matplotlib.pyplot as plt
import pandas as pd
from data_cleaning import ld_cln_data

def plot_fig7():
    stock_data = ld_cln_data()

    df_dreams = stock_data["dreams"]
    df_pop = stock_data["pop"]
    df_starbucks = stock_data["starbucks"]
    df_ulta = stock_data["ulta"]
    df_cars = stock_data["cars"]
    df_estee_97_01 = stock_data["estee_97_01"]

    # Sshift estee dates from 1997-2001 to 2021-2025 for plotting purposes
    df_estee_shifted = df_estee_97_01.copy()
    df_estee_shifted["Date"] = df_estee_shifted["Date"] + pd.DateOffset(years=24)

    plt.figure(figsize=(14, 7))

    plt.plot(df_dreams['Date'], df_dreams['Close'], label='Dreams Inc.', color="purple")
    plt.plot(df_pop['Date'], df_pop['Price'], label='PopMart', color="red")
    plt.plot(df_starbucks['Date'], df_starbucks['Price'], label='Starbucks', color="green")
    plt.plot(df_ulta['Date'], df_ulta['Price'], label='Ulta Beauty', color="orange")
    plt.plot(df_cars['Date'], df_cars['TotalSales'], label='Car Sales', color="black")

    # shifted estee
    plt.plot(df_estee_shifted['Date'], df_estee_shifted['Close'],
             label='Estee Lauder (97–01 shifted)', color="brown", linestyle='dashed')

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Small Luxury (Dreams, PopMart, Ulta, Estee) vs. Car Sales")
    plt.legend(title="Company/Item", loc="upper left")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # plot just estee
    plt.figure(figsize=(10, 5))
    plt.plot(df_estee_97_01['Date'], df_estee_97_01['Close'], color="brown")

    plt.title("Estee Lauder Stock Price (1997–2001)")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig7()
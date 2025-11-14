import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_individual_figs():
    stock_data = ld_cln_data()

    df_dreams = stock_data["dreams"]
    df_pop = stock_data["pop"]
    df_starbucks = stock_data["starbucks"]
    df_ulta = stock_data["ulta"]
    df_cars = stock_data["cars"]
    df_estee = stock_data["estee_21_25"]   # only 2021–2025

    # plot dreams
    plt.figure(figsize=(10,5))
    plt.plot(df_dreams["Date"], df_dreams["Close"], color="purple")
    plt.title("Dreams Incorporated (2021–2025)")
    plt.xlabel("Date"); plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # plot popmart
    plt.figure(figsize=(10,5))
    plt.plot(df_pop["Date"], df_pop["Price"], color="red")
    plt.title("PopMart (2021–2025)")
    plt.xlabel("Date"); plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # plot starbucks
    plt.figure(figsize=(10,5))
    plt.plot(df_starbucks["Date"], df_starbucks["Price"], color="green")
    plt.title("Starbucks (2021–2025)")
    plt.xlabel("Date"); plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # plot ulta
    plt.figure(figsize=(10,5))
    plt.plot(df_ulta["Date"], df_ulta["Price"], color="orange")
    plt.title("Ulta Beauty (2021–2025)")
    plt.xlabel("Date"); plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # plot car sales
    plt.figure(figsize=(10,5))
    plt.plot(df_cars["Date"], df_cars["Price"], color="black")
    plt.title("Car Sales Over Time")
    plt.xlabel("Date"); plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # plot estee
    plt.figure(figsize=(10,5))
    plt.plot(df_estee["Date"], df_estee["Close"], color="brown")
    plt.title("Estee Lauder (2021–2025)")
    plt.xlabel("Date"); plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_individual_figs()
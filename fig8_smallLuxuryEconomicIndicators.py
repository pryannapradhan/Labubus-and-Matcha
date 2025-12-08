import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig8():
    data = ld_cln_data() # load cleaned data

    df_dreams = data["dreams"]
    df_pop = data["pop"]
    df_starbucks = data["starbucks"]
    df_ulta = data["ulta"]

    # unemployment (already filtered to 21-25_)
    df_unemp = data["unemployment_21_25"]

    # Create figure
    plt.figure(figsize=(14, 7))

    ax1 = plt.gca() # left axis for stock prices
    ax2 = ax1.twinx()  # right axis for unemployment rate

    # graph stock market price data
    ax1.plot(df_dreams['Date'], df_dreams['Price'],
             label="Dreams", color="purple")
    ax1.plot(df_pop['Date'], df_pop['Price'],
             label="PopMart", color="red")
    ax1.plot(df_starbucks['Date'], df_starbucks['Price'],
             label="Starbucks", color="green")
    ax1.plot(df_ulta['Date'], df_ulta['Price'],
             label="Ulta Beauty", color="orange")

    ax1.set_xlabel("Date")
    ax1.set_ylabel("Stock Price")

    # graph unemployment rate data
    ax2.plot(df_unemp['Date'], df_unemp['UnemploymentRate'],
             label="Unemployment Rate", color="black", linewidth=2)
    ax2.set_ylabel("Unemployment Rate (%)")

    # set title
    plt.title("Small Luxury Spending vs Unemployment Rate (2021–2025)")

    # combine legends
    lines = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc="upper right")

    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_fig8()
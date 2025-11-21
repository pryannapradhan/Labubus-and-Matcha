import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig9():
    stock_data = ld_cln_data()

    df_dollar = stock_data["dollar"]
    df_pvh = stock_data["pvh"]
    df_tjx = stock_data["tjx"]
    df_walmart = stock_data["walmart"]
    df_target = stock_data["target"]

    plt.figure(figsize=(14, 7))

    plt.plot(df_dollar['Date'], df_dollar['Price'], label='Dollar Tree', color="blue")
    plt.plot(df_pvh['Date'], df_pvh['Price'], label='PVH', color="green")
    plt.plot(df_tjx['Date'], df_tjx['Price'], label='TJX', color="red")
    plt.plot(df_walmart['Date'], df_walmart['Price'], label='Walmart', color="orange")
    plt.plot(df_target['Date'], df_target['Price'], label='Target', color="purple")

    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title("Retail Company Stock Prices")
    plt.legend(title="Company", loc="upper left")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig9()

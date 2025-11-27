import matplotlib.pyplot as plt
from data_cleaning import ld_cln_data

def plot_fig2():
    stock_data = ld_cln_data()

    df_estee = stock_data["estee"]
    df_estee_21_25 = stock_data["estee_21_25"]
    df_estee_95_03 = stock_data["estee_95_03"]

    fig = plt.figure(figsize=(14, 10))

    # plot estee 95-03
    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax1.plot(df_estee_95_03['Date'], df_estee_95_03['Price'])
    ax1.set_title('Estee Lauder (1995–2003)')

    # plot estee 21-25
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax2.plot(df_estee_21_25['Date'], df_estee_21_25['Price'])
    ax2.set_title('Estee Lauder (2021–2025)')

    # pot full estee
    ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
    ax3.plot(df_estee['Date'], df_estee['Price'])
    ax3.set_title('Estee Lauder — Full History')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fig2()
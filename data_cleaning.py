import pandas as pd


def ld_cln_data():
    # Load CSV files
    df_dreams = pd.read_csv('DreamsIncorporatedStockPrices.csv')
    df_pop = pd.read_csv('PopMartStockPrices.csv')
    df_starbucks = pd.read_csv('StarbucksStockPriceHistory.csv')
    df_ulta = pd.read_csv('UltaBeautyStockPriceHistory.csv')
    df_cars = pd.read_csv('CarSales.csv')
    df_estee = pd.read_csv('EsteeLauderStockPriceHistory.csv')

    # adjust based on format of data in csv file
    df_dreams['Date'] = pd.to_datetime(df_dreams['Date'], format='%m/%Y')
    df_pop['Date'] = pd.to_datetime(df_pop['Date'], format='%m/%d/%Y')
    df_starbucks['Date'] = pd.to_datetime(df_starbucks['Date'], format='%m/%d/%Y')
    df_ulta['Date'] = pd.to_datetime(df_ulta['Date'], format='%m/%d/%Y')
    df_cars['Date'] = pd.to_datetime(df_cars['observation_date'], format='%Y-%m-%d')
    df_estee['Date'] = pd.to_datetime(df_estee['date'], format='%Y-%m-%d')

    # sort the data - should all be sorted, just double check
    df_dreams = df_dreams.sort_values('Date')
    df_pop = df_pop.sort_values('Date')
    df_starbucks = df_starbucks.sort_values('Date')
    df_ulta = df_ulta.sort_values('Date')
    df_cars = df_cars.sort_values('Date')
    df_estee = df_estee.sort_values('Date')

    # make sure price/close(if data doesn't have price col) is in float
    df_dreams['Close'] = df_dreams['Close'].astype(float)
    df_pop['Price'] = df_pop['Price'].astype(float)
    df_starbucks['Price'] = df_starbucks['Price'].astype(float)
    df_ulta['Price'] = df_ulta['Price'].astype(float)
    df_cars['Price'] = df_cars['TOTALSA'].astype(float)
    df_estee['Close'] = df_estee['close'].astype(float)

    # estee subsets for figure 2
    df_estee_21_25 = df_estee[
        (df_estee['Date'] >= '2021-01-01') &
        (df_estee['Date'] <= '2025-10-01')
    ]

    df_estee_95_03 = df_estee[
        (df_estee['Date'] >= '1995-01-01') &
        (df_estee['Date'] <= '2003-12-31')
    ]

    # return dictionary
    return {
        "dreams": df_dreams,
        "pop": df_pop,
        "starbucks": df_starbucks,
        "ulta": df_ulta,
        "cars": df_cars,
        "estee": df_estee,
        "estee_21_25": df_estee_21_25,
        "estee_95_03": df_estee_95_03
    }
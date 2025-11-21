import pandas as pd


def ld_cln_data():
    # Load Stock CSV files
    df_dollar = pd.read_csv('StockHistoryData/DollarTreeStock.csv')
    df_dreams = pd.read_csv('StockHistoryData/DreamsIncorporatedStock.csv')
    df_estee = pd.read_csv('StockHistoryData/EsteeLauderStock.csv')
    df_pop = pd.read_csv('StockHistoryData/PopMartStock.csv')
    df_pvh = pd.read_csv('StockHistoryData/PVHStock.csv')
    df_starbucks = pd.read_csv('StockHistoryData/StarbucksStock.csv')
    df_target = pd.read_csv('StockHistoryData/TargetStock.csv')
    df_tjx = pd.read_csv('StockHistoryData/TJXStock.csv')
    df_ulta = pd.read_csv('StockHistoryData/UltaStock.csv')
    df_walmart = pd.read_csv('StockHistoryData/WalmartStock.csv')

    # Load Economic Indicator CSV files
    df_cars = pd.read_csv('EconomicIndicatorData/CarSales.csv')
    df_cpi = pd.read_csv('EconomicIndicatorData/CPIData.csv')
    df_gdp = pd.read_csv('EconomicIndicatorData/GDPData.csv')
    df_unemployment = pd.read_csv('EconomicIndicatorData/UnemploymentData.csv')


    # Adjust Stock Price Data Date
    df_dollar['Date'] = pd.to_datetime(df_dollar['Date'], format='%m/%d/%Y')
    df_dreams['Date'] = pd.to_datetime(df_dreams['Date'], format='%m/%Y')
    df_estee['Date'] = pd.to_datetime(df_estee['date'], format='%Y-%m-%d')
    df_pop['Date'] = pd.to_datetime(df_pop['Date'], format='%m/%d/%Y')
    df_pvh['Date'] = pd.to_datetime(df_pvh['Date'], format='%m/%d/%Y')
    df_starbucks['Date'] = pd.to_datetime(df_starbucks['Date'], format='%m/%d/%Y')
    df_target['Date'] = pd.to_datetime(df_target['Date'], format='%m/%d/%Y')
    df_tjx['Date'] = pd.to_datetime(df_tjx['Date'], format='%m/%d/%Y')
    df_ulta['Date'] = pd.to_datetime(df_ulta['Date'], format='%m/%d/%Y')
    df_walmart['Date'] = pd.to_datetime(df_walmart['Date'], format='%m/%d/%Y')


    # Adjust Economic Indicator Data Date
    df_cars['Date'] = pd.to_datetime(df_cars['observation_date'], format='%Y-%m-%d')
    df_cpi['Date'] = pd.to_datetime(df_cpi['DATE'], format='%Y-%m-%d')
    df_gdp['Date'] = pd.to_datetime(df_gdp['DATE'], format='%Y-%m-%d')
    df_unemployment['Date'] = pd.to_datetime(df_unemployment['DATE'], format='%Y-%m-%d')

    # sort the data - should all be sorted, just double check
    df_dollar = df_dollar.sort_values('Date')
    df_dreams = df_dreams.sort_values('Date')
    df_estee = df_estee.sort_values('Date')
    df_pop = df_pop.sort_values('Date')
    df_pvh = df_pvh.sort_values('Date')
    df_starbucks = df_starbucks.sort_values('Date')
    df_target = df_target.sort_values('Date')
    df_tjx = df_tjx.sort_values('Date')
    df_ulta = df_ulta.sort_values('Date')
    df_walmart = df_walmart.sort_values('Date')

    df_cars = df_cars.sort_values('Date')
    df_cpi = df_cpi.sort_values('Date')
    df_gdp = df_gdp.sort_values('Date')
    df_unemployment = df_unemployment.sort_values('Date')


    # make sure price/close(if data doesn't have price col) is in float
    df_dollar['Price'] = df_dollar['Price'].astype(float)
    df_dreams['Close'] = df_dreams['Close'].astype(float)
    df_estee['Close'] = df_estee['close'].astype(float)
    df_pop['Price'] = df_pop['Price'].astype(float)
    df_pvh['Price'] = df_pvh['Price'].astype(float)
    df_starbucks['Price'] = df_starbucks['Price'].astype(float)
    df_target['Price'] = df_target['Price'].astype(float)
    df_tjx['Price'] = df_tjx['Price'].astype(float)
    df_ulta['Price'] = df_ulta['Price'].astype(float)
    df_walmart['Price'] = df_walmart['Price'].astype(float)


    df_cars['TotalSales'] = df_cars['TOTALSA'].astype(float)
    df_cpi['CPI'] = df_cpi['CPIAUCSL'].astype(float)
    df_gdp['GDP'] = df_gdp['GDP'].astype(float)
    df_unemployment['UnemploymentRate'] = df_unemployment['UNRATE'].astype(float)


    # estee subsets for figure 2
    df_estee_21_25 = df_estee[
        (df_estee['Date'] >= '2021-01-01') &
        (df_estee['Date'] <= '2025-10-01')
    ]

    df_estee_97_01 = df_estee[
        (df_estee['Date'] >= '1997-01-01') &
        (df_estee['Date'] <= '2001-12-31')
    ]

    df_unemployment_21_25 = df_unemployment[
        (df_unemployment['Date'] >= '2021-01-01') &
        (df_unemployment['Date'] <= '2025-12-31')
        ]

    # return dictionary
    return {
        "dollar": df_dollar,
        "dreams": df_dreams,
        "estee": df_estee,
        "pop": df_pop,
        "pvh": df_pvh,
        "starbucks": df_starbucks,
        "target": df_target,
        "tjx": df_tjx,
        "ulta": df_ulta,
        "walmart": df_walmart,

        "cars": df_cars,
        "cpi": df_cpi,
        "gdp": df_gdp,
        "unemployment": df_unemployment,

        "estee_21_25": df_estee_21_25,
        "estee_97_01": df_estee_97_01,
        "unemployment_21_25": df_unemployment_21_25
    }
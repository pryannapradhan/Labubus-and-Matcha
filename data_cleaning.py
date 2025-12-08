import pandas as pd

def clean_stock_csv(file_path):
    df = pd.read_csv(file_path, dtype=str) # read in csv file using pandas

    if 'date' in df.columns:
        df.rename(columns={'date': 'Date'}, inplace=True) # rename any columns 'date' -> 'Date'

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date']) # convert dates to format datetime

    # if there is a Close column instead of price column, rename that to Price
    if 'Close' in df.columns:
        df.rename(columns={'Close': 'Price'}, inplace=True)
    elif 'close' in df.columns:
        df.rename(columns={'close': 'Price'}, inplace=True)

    # make sure the price is a numeric value
    df['Price'] = pd.to_numeric(df['Price'])

    # if the percent change is already calculate, make sure it is the right numeric format
    if 'Change %' in df.columns:
        df['Change %'] = df['Change %'].str.replace('%', '', regex=False)
        df['Change %'] = pd.to_numeric(df['Change %'])
    # if the percent change isn't calculated, add that as a column
    else:
        df['Change %'] = df['Price'].pct_change() * 100
        df['Change %'] = df['Change %'].round(2)

    # make sure columns are in a standard order
    columns_order = ['Date', 'Open', 'High', 'Low', 'Price', 'Vol.', 'Change %']
    df = df[[col for col in columns_order if col in df.columns]]

    # save the cleaned file version
    new_file = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(new_file, index=False, date_format='%m/%d/%Y', quotechar='"')
    print(f"Cleaned CSV saved to {new_file}")
    return df

def ld_cln_data():
    # Load and clean stock CSVs
    df_dollar = clean_stock_csv('StockHistoryData/CompanyComparison/DollarTreeStock.csv')
    df_dreams = clean_stock_csv('StockHistoryData/ItemComparison/DreamsIncorporatedStock.csv')
    df_estee = clean_stock_csv('StockHistoryData/ItemComparison/EsteeLauderStock.csv').resample('MS', on='Date').first().reset_index()
    df_pop = clean_stock_csv('StockHistoryData/ItemComparison/PopMartStock.csv')
    df_pvh = clean_stock_csv('StockHistoryData/CompanyComparison/PVHStock.csv')
    df_starbucks = clean_stock_csv('StockHistoryData/ItemComparison/StarbucksStock.csv')
    df_target = clean_stock_csv('StockHistoryData/CompanyComparison/TargetStock.csv')
    df_tjx = clean_stock_csv('StockHistoryData/CompanyComparison/TJXStock.csv')
    df_ulta = clean_stock_csv('StockHistoryData/ItemComparison/UltaStock.csv')
    df_walmart = clean_stock_csv('StockHistoryData/CompanyComparison/WalmartStock.csv')

    df_dollar['Price'] = df_dollar['Price'].astype(float)
    df_dreams['Price'] = df_dreams['Price'].astype(float)
    df_estee['Price'] = df_estee['Price'].astype(float)
    df_pop['Price'] = df_pop['Price'].astype(float)
    df_pvh['Price'] = df_pvh['Price'].astype(float)
    df_starbucks['Price'] = df_starbucks['Price'].astype(float)
    df_target['Price'] = df_target['Price'].astype(float)
    df_tjx['Price'] = df_tjx['Price'].astype(float)
    df_ulta['Price'] = df_ulta['Price'].astype(float)
    df_walmart['Price'] = df_walmart['Price'].astype(float)

    # Load other economic data
    df_cars = pd.read_csv('EconomicIndicatorData/CarSales.csv')
    df_cpi = pd.read_csv('EconomicIndicatorData/CPIData.csv')
    df_gdp = pd.read_csv('EconomicIndicatorData/GDPData.csv')
    df_unemployment = pd.read_csv('EconomicIndicatorData/UnemploymentData.csv')


    # convert all indicator columns (sales, CPI, etc.) to numeric values
    df_cars['TotalSales'] = df_cars['TOTALSA'].astype(float)
    df_cpi['CPI'] = df_cpi['CPIAUCSL'].astype(float)
    df_gdp['GDP'] = df_gdp['GDP'].astype(float)
    df_unemployment['UnemploymentRate'] = df_unemployment['UNRATE'].astype(float)

    # convert date columns to datetime
    df_cars['Date'] = pd.to_datetime(df_cars['observation_date'])
    df_cpi['Date'] = pd.to_datetime(df_cpi['DATE'])
    df_gdp['Date'] = pd.to_datetime(df_gdp['DATE'])
    df_unemployment['Date'] = pd.to_datetime(df_unemployment['DATE'])

    # make sure all the datasets are sorted by the date
    dfs_to_sort = [
        df_dollar, df_dreams, df_estee, df_pop, df_pvh,
        df_starbucks, df_target, df_tjx, df_ulta, df_walmart,
        df_cars, df_cpi, df_gdp, df_unemployment
    ]

    for df in dfs_to_sort:
        df.sort_values('Date', inplace=True)

    # Create subsets of the estee lauder data
    df_estee_21_25 = df_estee[
        (df_estee['Date'] >= '01/01/2021') & (df_estee['Date'] <= '10/01/2025')
    ]
    df_estee_97_01 = df_estee[
        (df_estee['Date'] >= '01/01/1997') & (df_estee['Date'] <= '12/31/2001')
    ]

    # Create subset of the unemployment data
    df_unemployment_21_25 = df_unemployment[
        (df_unemployment['Date'] >= '01/01/2021') & (df_unemployment['Date'] <= '12/31/2025')
    ]

    # return dictionary of cleaned datasets
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

if __name__ == "__main__":
    data = ld_cln_data()
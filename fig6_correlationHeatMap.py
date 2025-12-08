import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import ld_cln_data

def plot_correlation_heatmap():

    stock_data = ld_cln_data() # load in cleaned datasets

    # Dictionary of datasets to include in correlation
    economicData = {
        'DollarTree': stock_data['dollar'],
        'Dreams': stock_data['dreams'],
        'Estee': stock_data['estee'],
        'PopMart': stock_data['pop'],
        'PVH': stock_data['pvh'],
        'Starbucks': stock_data['starbucks'],
        'Target': stock_data['target'],
        'TJX': stock_data['tjx'],
        'Ulta': stock_data['ulta'],
        'Walmart': stock_data['walmart'],
        'CarSales': stock_data['cars'],
        'CPI': stock_data['cpi'],
        'GDP': stock_data['gdp'],
        'Unemployment': stock_data['unemployment']
    }

    combined_list = []

    for name, df in economicData.items():
        # Identify numeric column
        if 'Close' in df.columns:
            val_col = 'Close'
        elif 'Price' in df.columns:
            val_col = 'Price'
        elif 'CPI' in df.columns:
            val_col = 'CPI'
        elif 'GDP' in df.columns:
            val_col = 'GDP'
        elif 'UnemploymentRate' in df.columns:
            val_col = 'UnemploymentRate'
        elif 'TotalSales' in df.columns:
            val_col = 'TotalSales'

        # Resample to monthly frequency for alignment
        temp = df[['Date', val_col]].copy()
        temp = temp.set_index('Date').resample('ME').last() # take last value of each month
        temp.rename(columns={val_col: name}, inplace=True)
        combined_list.append(temp)

    # Merge all datasets on Date
    combined_df = pd.concat(combined_list, axis=1).dropna()

    # Compute correlation matrix
    corr_matrix = combined_df.corr()

    # Plot heatmap using seaborn
    plt.figure(figsize=(14, 12))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f",
                cmap='coolwarm', linewidths=0.5)

    # format heatmap and display
    plt.title("Correlation Matrix HeatMap for Stock History and Economic Indicators",
              fontsize=18)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return combined_df, corr_matrix

if __name__ == "__main__":
    combined_df, corr_matrix = plot_correlation_heatmap()

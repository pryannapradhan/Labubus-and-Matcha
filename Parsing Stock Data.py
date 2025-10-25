import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df1 = pd.read_csv('DreamsIncorporatedStockPrices.csv')
df2 = pd.read_csv('PopMartStockPrices.csv')

# Format Date Column and Sort as needed
df1['Date'] = pd.to_datetime(df1['Date'], format='%m/%Y')
df1 = df1.sort_values('Date')

df2['Date'] = pd.to_datetime(df2['Date'], format='%m/%d/%Y')
df2 = df2.sort_values('Date')

# Convert Price Columns to Float
df1['Close'] = df1['Close'].astype(float)
df2['Price'] = df2['Price'].astype(float)

# Create dual y-axis plot
fig, ax1 = plt.subplots(figsize=(14,6))

# Left axis for Dreams Incorporated
ax1.plot(df1['Date'], df1['Close'], marker='o', linestyle='-', color='blue', label='Dreams Inc.')
ax1.set_xlabel('Date')
ax1.set_ylabel('Dreams Inc. Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Right axis for POP Mart
ax2 = ax1.twinx()
ax2.plot(df2['Date'], df2['Price'], marker='x', linestyle='--', color='red', label='POP Mart')
ax2.set_ylabel('POP Mart Price', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Stock Prices Comparison')
fig.tight_layout()
plt.show()
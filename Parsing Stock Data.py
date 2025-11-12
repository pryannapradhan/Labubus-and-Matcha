import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df1 = pd.read_csv('DreamsIncorporatedStockPrices.csv')
df2 = pd.read_csv('PopMartStockPrices.csv')
df3 = pd.read_csv('StarbucksStockPriceHistory.csv')
df4 = pd.read_csv('UltaBeautyStockPriceHistory.csv')

# Format Date Column and Sort as needed
df1['Date'] = pd.to_datetime(df1['Date'], format='%m/%Y')
df1 = df1.sort_values('Date')

df2['Date'] = pd.to_datetime(df2['Date'], format='%m/%d/%Y')
df2 = df2.sort_values('Date')

df3['Date'] = pd.to_datetime(df3['Date'], format='%m/%d/%Y')
df3 = df3.sort_values('Date')

df4['Date'] = pd.to_datetime(df4['Date'], format='%m/%d/%Y')
df4 = df4.sort_values('Date')

# Convert Price Columns to Float
df1['Close'] = df1['Close'].astype(float)
df2['Price'] = df2['Price'].astype(float)
df3['Price'] = df3['Price'].astype(float)
df4['Price'] = df4['Price'].astype(float)

#-----------FIGURE 1-----------------

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot DreamsIncorporated
axes[0, 0].plot(df1['Date'], df1['Close'], color='blue')
axes[0, 0].set_title('Dreams Incorporated')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Price')

# Plot PopMart
axes[0, 1].plot(df2['Date'], df2['Price'], color='red')
axes[0, 1].set_title('PopMart')
axes[0, 1].set_xlabel('Date')
axes[0, 1].set_ylabel('Price')

# Plot Starbucks
axes[1, 0].plot(df3['Date'], df3['Price'], color='green')
axes[1, 0].set_title('Starbucks')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Price')

# Plot UltaBeauty
axes[1, 1].plot(df4['Date'], df4['Price'], color='orange')
axes[1, 1].set_title('Ulta Beauty')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Price')

# Adjust layout
plt.tight_layout()
plt.show()

#-----------FIGURE 2---------------

# Plot all companies on one graph
plt.figure(figsize=(12, 6))

plt.plot(df1['Date'], df1['Close'], label='Dreams Incorporated', color='blue')
plt.plot(df2['Date'], df2['Price'], label='PopMart', color='red')
plt.plot(df3['Date'], df3['Price'], label='Starbucks', color='green')
plt.plot(df4['Date'], df4['Price'], label='Ulta Beauty', color='orange')

plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price Comparison Over Time')
plt.legend(title='Company')
plt.grid(True)
plt.tight_layout()
plt.show()

#-----------FIGURE 3---------------

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
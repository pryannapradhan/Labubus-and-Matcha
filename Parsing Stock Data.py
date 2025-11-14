import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df_dreams = pd.read_csv('DreamsIncorporatedStockPrices.csv')
df_pop = pd.read_csv('PopMartStockPrices.csv')
df_starbucks = pd.read_csv('StarbucksStockPriceHistory.csv')
df_ulta = pd.read_csv('UltaBeautyStockPriceHistory.csv')
df_cars = pd.read_csv('CarsSales.csv')
df_estee = p

# Format Date Column and Sort as needed
df_dreams['Date'] = pd.to_datetime(df_dreams['Date'], format='%m/%Y')
df_dreams = df_dreams.sort_values('Date')

df_pop['Date'] = pd.to_datetime(df_pop['Date'], format='%m/%d/%Y')
df_pop = df_pop.sort_values('Date')

df_starbucks['Date'] = pd.to_datetime(df_starbucks['Date'], format='%m/%d/%Y')
df_starbucks = df_starbucks.sort_values('Date')

df_ulta['Date'] = pd.to_datetime(df_ulta['Date'], format='%m/%d/%Y')
df_ulta = df_ulta.sort_values('Date')

# Convert Price Columns to Float
df_dreams['Close'] = df_dreams['Close'].astype(float)
df_pop['Price'] = df_pop['Price'].astype(float)
df_starbucks['Price'] = df_starbucks['Price'].astype(float)
df_ulta['Price'] = df_ulta['Price'].astype(float)

#-----------FIGURE 1-----------------

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot DreamsIncorporated
axes[0, 0].plot(df_dreams['Date'], df_dreams['Close'], color='blue')
axes[0, 0].set_title('Dreams Incorporated')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Price')

# Plot PopMart
axes[0, 1].plot(df_pop['Date'], df_pop['Price'], color='red')
axes[0, 1].set_title('PopMart')
axes[0, 1].set_xlabel('Date')
axes[0, 1].set_ylabel('Price')

# Plot Starbucks
axes[1, 0].plot(df_starbucks['Date'], df_starbucks['Price'], color='green')
axes[1, 0].set_title('Starbucks')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Price')

# Plot UltaBeauty
axes[1, 1].plot(df_ulta['Date'], df_ulta['Price'], color='orange')
axes[1, 1].set_title('Ulta Beauty')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Price')

# Adjust layout
plt.tight_layout()
plt.show()

#-----------FIGURE 2---------------

# Plot all companies on one graph
plt.figure(figsize=(12, 6))

plt.plot(df_dreams['Date'], df_dreams['Close'], label='Dreams Incorporated', color='blue')
plt.plot(df_pop['Date'], df_pop['Price'], label='PopMart', color='red')
plt.plot(df_starbucks['Date'], df_starbucks['Price'], label='Starbucks', color='green')
plt.plot(df_ulta['Date'], df_ulta['Price'], label='Ulta Beauty', color='orange')

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
ax1.plot(df_dreams['Date'], df_dreams['Close'], marker='o', linestyle='-', color='blue', label='Dreams Inc.')
ax1.set_xlabel('Date')
ax1.set_ylabel('Dreams Inc. Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Right axis for POP Mart
ax2 = ax1.twinx()
ax2.plot(df_pop['Date'], df_pop['Price'], marker='x', linestyle='--', color='red', label='POP Mart')
ax2.set_ylabel('POP Mart Price', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Stock Prices Comparison')
fig.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df_dreams = pd.read_csv('DreamsIncorporatedStockPrices.csv')
df_pop = pd.read_csv('PopMartStockPrices.csv')
df_starbucks = pd.read_csv('StarbucksStockPriceHistory.csv')
df_ulta = pd.read_csv('UltaBeautyStockPriceHistory.csv')
df_cars = pd.read_csv('CarSales.csv')
df_estee = pd.read_csv('EsteeLauderStockPriceHistory.csv')

# Format Date Column and Sort as needed
df_dreams['Date'] = pd.to_datetime(df_dreams['Date'], format='%m/%Y')
df_dreams = df_dreams.sort_values('Date')

df_pop['Date'] = pd.to_datetime(df_pop['Date'], format='%m/%d/%Y')
df_pop = df_pop.sort_values('Date')

df_starbucks['Date'] = pd.to_datetime(df_starbucks['Date'], format='%m/%d/%Y')
df_starbucks = df_starbucks.sort_values('Date')

df_ulta['Date'] = pd.to_datetime(df_ulta['Date'], format='%m/%d/%Y')
df_ulta = df_ulta.sort_values('Date')

df_cars['Date'] = pd.to_datetime(df_cars['observation_date'], format='%Y-%m-%d')
df_cars = df_cars.sort_values('Date')

df_estee['Date'] = pd.to_datetime(df_estee['date'], format='%Y-%m-%d')
df_estee = df_estee.sort_values('Date')

# Convert Price Columns to Float
df_dreams['Close'] = df_dreams['Close'].astype(float)
df_pop['Price'] = df_pop['Price'].astype(float)
df_starbucks['Price'] = df_starbucks['Price'].astype(float)
df_ulta['Price'] = df_ulta['Price'].astype(float)
df_cars['Price'] = df_cars['TOTALSA'].astype(float)
df_estee['Close'] = df_estee['close'].astype(float)

# match estee time range to other sales
df_estee_21_25 = df_estee[
    (df_estee['Date'] >= '2021-01-01') &
    (df_estee['Date'] <= '2025-10-01')
]

#-----------FIGURE 1: All 6 plot together-----------------

# Create a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Stock Price History (2021-2025)', fontsize = 20)

# Plot Dreams Incorporated
axes[0, 0].plot(df_dreams['Date'], df_dreams['Close'])
axes[0, 0].set_title('Dreams Incorporated')

# Plot PopMart
axes[0, 1].plot(df_pop['Date'], df_pop['Price'])
axes[0, 1].set_title('PopMart')

# Plot Starbucks
axes[0, 2].plot(df_starbucks['Date'], df_starbucks['Price'])
axes[0, 2].set_title('Starbucks')

# Plot Ulta Beauty
axes[1, 0].plot(df_ulta['Date'], df_ulta['Price'])
axes[1, 0].set_title('Ulta Beauty')

# Plot Car Sales
axes[1, 1].plot(df_cars['Date'], df_cars['Price'])
axes[1, 1].set_title('Car Sales')

# Plot Estee Lauder
axes[1, 2].plot(df_estee_21_25['Date'], df_estee_21_25['Close'])
axes[1, 2].set_title('Estee Lauder')

#loop through plot to set labels
for ax in axes.flat:
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')

#Adjust Layout
plt.tight_layout()
plt.show()

#-----------FIGURE 2: Estee Lauder Analysis---------------
df_estee_95_03 = df_estee[
    (df_estee['Date'] >= '1995-01-01') &
    (df_estee['Date'] <= '2003-12-31')
]


fig = plt.figure(figsize=(14, 10))

# --- Top Left (1995–2003) ---
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax1.plot(df_estee_95_03['Date'], df_estee_95_03['Close'])
ax1.set_title('Estee Lauder (1995–2003)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')

# --- Top Right (2021–2025) ---
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax2.plot(df_estee_21_25['Date'], df_estee_21_25['Close'])
ax2.set_title('Estee Lauder (2021–2025)')
ax2.set_xlabel('Date')
ax2.set_ylabel('Price')

# --- Bottom Full-Width (All Years) ---
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
ax3.plot(df_estee['Date'], df_estee['Close'])
ax3.set_title('Estee Lauder — Full')
ax3.set_xlabel('Date')
ax3.set_ylabel('Price')

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
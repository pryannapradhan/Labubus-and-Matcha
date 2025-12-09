## Introduction
**Title:** The Lipstick Phenomenon of 2025  
**Authors:** Pryanna Pradhan and Karen Liang

**Background:** The Lipstick Phenomenon (coined by Estee Lauder in 2001) is the pattern 
of people purchasing small, affordable luxury items during a time of economic decline.

## Overview
This capstone project analyzes stock market and economic indicator data to explore 
correlations and patterns amongst datasets. The goal is to see which products in 2025 
seem to follow the "lipstick phenomenon" discovered by Estee Lauder in 2001.

## File Tree
Labubus-and-Matcha/  
├── EconomicIndicatorData/  
│   ├── CarSales.csv  
│   ├── CPIData.csv  
│   ├── GDPData.csv  
│   └── UnemploymentData.csv  
│  
├── StockHistoryData/  
│   ├── CompanyComparison/  
│   │   ├── DollarTreeStock.csv  
│   │   ├── DollarTreeStock_cleaned.csv  
│   │   ├── PVHStock.csv  
│   │   ├── PVHStock_cleaned.csv  
│   │   └── ... (other company overall stock market data)
│   │  
│   └── ItemComparison/  
│       │ ├── DreamsIncorporatedStock.csv  
│       │ ├── DreamsIncorporatedStock_cleaned.  
│       │ ├── EsteeLauderStock.csv  
│       │ ├── EsteeLauderStock_cleaned.csv  
│       │ └──... (other company item focused stock market data) 
│      
│  
├── data_cleaning.py  
├── fig1_allStockPrice.py  
├── fig2_estee.py  
├── fig3_overlay.py  
├── ... (other figures)  
│   
└── README.md  

## Economic Indicators
`CarSales.csv`
- Car Sale Data (1/1/21 - 8/1/25)
- Data that shows the date when a car was sold, and the price of the car. We needed a dataset that could display quantaties of cars sold, as well as for what prices, in order to compare it to the sale of our "lipsticks".

`CPIData.csv `
- CPI Data (1/1/1974 - 1/1/24)
- Consumer Price Index (CPI) shows the change of price of a constant group of everyday items as time passes. It accounts for inflation and cost of living. This information helps us see how normal consumers are impacted by inflation and rising prices.

`GDPData.csv  `
- GDP Data (1/1/1974 - 1/1/24)
- Gross Domestic Product (GDP) measures the total value of goods and services produced in a country. This dataset had the GDP of the U.S., which allowed us to see how successful production was in the country- if GDP was low, it's more likely that there will be more "lipstick" items.

`UnemploymentData.csv`  
- Unemployment Rate % (1/1/1974 - 1/1/24)
- Unemployment rate measures how much unemployment there is (excluding minors and those not searching for work) in a country. The higher the unemployment, the less stable the economy is.

## Stock History Data
**Note about _cleaned files:** Each of the 10 stock market CSV files has a corresponding _cleaned version.
The _cleaned version is created using the `clean_stock_csv(file_path)` function in `data_cleaning.py`.
It reformats the CSV files to a standardized structure for easier analysis.

`DollarTreeStock.csv `
- Dollar Tree Stock Data (1/1/21 - 11/1/25)
- Dollar Tree is a discount store known to sell a variety of goods anywhere from everyday household goods to party supplies
to even food. Although prices have since increased beyond $1, it remains a relatively inexpensive store.

`DreamsIncorporatedStock.csv ` 
- Dreams Incorporated Stock Data (1/21 - 10/25)
- Dreams Incorporated produces home goods and accessories, but is most popular for their blind box figurines (Smiskis, Sonny Angels, etc.)

`EsteeLauderStock.csv  ` 
- Estée Lauder Stock Data (11/17/95 - 11/12/25)
- Estée Lauder is a high performance skincare, makeup, and fragrance brand.

`PopMartStock.csv ` 
- Pop Mart Stock Data (1/1/21 - 10/1/25)
- Pop Mart sells small, collectible toys and figurines. In particular, they are most well known for the 
sale of a product called "Labubus".

`PVHStock.csv `  
- Phillips-Van Heusen Corporation Stock Data (1/1/21 - 11/1/25)
- PVH owns high-end brands such as Tommy Hilfiger and Calvin Klein.

`StarbucksStock.csv`   
- Starbucks Stock Data (1/1/21 - 10/1/25)
- Starbucks operates the largest coffeehouse chain in the world. They sell a variety of teas, coffees, baked goods, and more.

`TargetStock.csv `  
- Target Stock Data (2/1/21 - 11/1/25)
- Target is a general merchandise retailer that sells both groceries and household goods.

`TJXStock.csv `  
- TJX Companies, Inc. Stock Data (1/1/21 - 11/1/25)
- TJX owns off-price apparel and home fashions retailer stores such as T.J. Maxx, Marshalls, and HomeGoods.

`UltaStock.csv ` 
- Ulta Stock Data (10/1/25 - 11/1/25)
- Ulta is a beauty retailer for cosmetics, fragrance, skin care, and hair care products.

`WalmartStock.csv `  
- Walmart Stock Data (1/1/21 - 11/1/25)
- Walmart is a retail corporation that sells a variety of goods. It is similar to Target but less expensive.

## Figures
`fig1_allStockPrice.py ` 
- 5 x 2 grid graph of the stock prices for all 10 sets of stock market graph.

`fig2_estee.py`  
- 3 graphs of Estee Lauder stock market data on one plot. (1) 1997-2001,
  (2) 2021-2025, (3) Full History 1995-2025

`fig3_overlay.py`  
- 1 graph of all possible lipstick indicator stock market history data against the
economic indicator of unemployment rate.

`fig4_dream_pop.py ` 
- Dreams Inc. and Popmart stock market data plotted on a dual axis.

`fig5_individual.py ` 
- All datasets (both stock market history and economic indicator data) plotted on their 
own individual graph.

`fig6_correlationHeatMap.py`  
- Heatmap of the correlations between the different datasets.

`fig7_smallLuxuryBigPurchase.py ` 
- 2 graphs. The first one is an overlay of purchases of small luxury items (makeup, starbucks, etc.) and
the bigger purchase of a car. The second graph is just the Estée Lauder data 1997-2001.

`fig8_smallLuxuryEconomicIndicators.py ` 
- 1 graph of small luxury spending data (e.g. stock market history from popmart) v. unemployment rate.

`fig9_BudgetLuxury.py  `
- 1 graph of company comparison (cheaper companies v. luxury companies).

`fig10_allStockPercentChange.py`
- 5 x 2 grid of the percent change in stock market for the companies in figure 1.



## Packages
`pandas` 
- **Import:** pandas as pd  
- **Usage:** Work with csv files and clean/manipulate data

`matplotlib ` 
- **Import:** matplotlib.pyplot as plt  
- **Usage:** Plotting graphs  

`seaborn `
- **Import:** seaborn as sns  
- **Usage:** Heatmap

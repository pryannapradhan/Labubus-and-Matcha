## Introduction
**Title:** The Lipstick Phenomenon of 2025  
**Authors:** Pryanna Pradhan and Karen Liang

**Background:** The Lipstick Phenomenon (coined by Estee Lauder in 2001) is the pattern 
of people purchasing small, affordable luxury items during a time of economic decline.

## Overview
This capstone project analyzes stock market and economic indicator data to explore 
correlations and patterns among datasets. The goal is to see which products in 2025 
seem to follow the lipstick phenomenon Estee Lauder noticed in 2001.

## File Tree
Labubus-and-Matcha/  
├── EconomicIndicatorData/  
│   ├── CarSales.csv  
│   ├── CPIData.csv  
│   ├── GDPData.csv  
│   └── UnemploymentData.csv  
│  
├── StockHistoryData/  
│   ├── DollarTreeStock.csv  
│   ├── DollarTreeStock_cleaned.csv 
│   ├── DreamsIncorporatedStock.csv  
│   ├── DreamsIncorporatedStock_cleaned.csv
│   └── ... (other stocks)  
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
- Add more info here

`CPIData.csv `
- CPI Data (1/1/1974 - 1/1/24)
- Add more info here

`GDPData.csv  `
- GDP Data (1/1/1974 - 1/1/24)
- Add more info here

`UnemploymentData.csv`  
- Unemployment Rate % (1/1/1974 - 1/1/24)
- Add more info here

## Stock History Data
**Note about _cleaned files:** Each of the 10 stock market CSV files has a corresponding _cleaned version.
The _cleaned version is created using the `clean_stock_csv(file_path)` function in `data_cleaning.py`.
It reformats the CSV files to a standardized structure for easier analysis.

`DollarTreeStock.csv `
- Dollar Tree Stock Data (1/1/21 - 11/1/25)
- Dollar Tree is a discount store known too sell a variety of goods anywhere from everyday household goods to party supplie
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
sale of a product called Labubus.

`PVHStock.csv `  
- Phillips-Van Heusen Corporation Stock Data (1/1/21 - 11/1/25)
- PVH owns high-end brands such as Tommy Hilfiger abd Calvin Klein

`StarbucksStock.csv`   
- Starbucks Stock Data (1/1/21 - 10/1/25)
- Starbucks operates the largest coffeehouse chain in the world. They sell a variety of teas, coffees, baked goods, and more.

`TargetStock.csv `  
- Target Stock Data (2/1/21 - 11/1/25)
- Target is a general merchandise retailer that sells both groceries and household goods

`TJXStock.csv `  
- TJX Companies, Inc. Stock Data (1/1/21 - 11/1/25)
- TJX owns off price apparel and home fashions retailer stores such as T.J. Maxx, Marshalls, and HomeGoods

`UltaStock.csv ` 
- Ulta Stock Data (10/1/25 - 11/1/25)
- Ulta is a beauty retailer for cosmetics, fragrance, skin care, and hair care products.

`WalmartStock.csv `  
- Walmart Stock Data (1/1/21 - 11/1/25)
- Walmart is a retail corporation that sells a variety of goods. It is similar to target but generally less expensive.

## Figures
`fig1_allStockPrice.py ` 
- add explanation  

`fig2_estee.py`  
- add explanation  

`fig3_overlay.py`  
- add explanation  

`fig4_dream_pop.py ` 
- add explanation  

`fig5_individual.py ` 
- add explanation  

`fig6_correlationHeatMap.py`  
- add explanation  

`fig7_smallLuxuryBigPurchase.py ` 
- add explanation  

`fig8_smallLuxuryEconomicIndicators.py ` 
- add explanation  

`fig9_BudgetLuxury.py  `
- add explanation  

`fig10_allStockPercentChange.py`
- add explanation  



## Packages
`pandas` 
- **Import:** pandas as pd  
- **Usage:** work with csv files and clean/manipulate data

`matplotlib ` 
- **Import:** matplotlib.pyplot as plt  
- **Usage:** plotting graphs  

`seaborn `
- **Import:** seaborn as sns  
- **Usage:** heatmap

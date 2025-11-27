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

`CPIData.csv `

`GDPData.csv  `

`UnemploymentData.csv`  


## Stock History Data
**Note about _cleaned files:** Each of the 10 stock market CSV files has a corresponding _cleaned version.
The _cleaned version is created using the `clean_stock_csv(file_path)` function in `data_cleaning.py`.
It reformats the CSV files to a standardized structure for easier analysis.

`DollarTreeStock.csv `
- add explanation  

`DreamsIncorporatedStock.csv ` 
- add explanation  

`EsteeLauderStock.csv  ` 
- add explanation  

`PopMartStock.csv ` 
- add explanation  

`PVHStock.csv `  
- add explanation  

`StarbucksStock.csv`   
- add explanation  

`TargetStock.csv `  
- add explanation  

`TJXStock.csv `  
- add explanation  

`UltaStock.csv ` 
- add explanation  

`WalmartStock.csv `  
- add explanation  

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

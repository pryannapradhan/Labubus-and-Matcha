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
<u>CarSales.csv</u>

<u>CPIData.csv</u>  

<u>GDPData.csv</u>  

<u>UnemploymentData.csv</u>  


## Stock History Data
**Note about _cleaned files:** Each of the 10 stock market CSV files has a corresponding _cleaned version.
The _cleaned version is created using the `clean_stock_csv(file_path)` function in `data_cleaning.py`.
It reformats the CSV files to a standardized structure for easier analysis.

<u>DollarTreeStock.csv</u> 

<u>DreamsIncorporatedStock.csv</u>  

<u>EsteeLauderStock.csv</u>   

<u>PopMartStock.csv</u>   

<u>PVHStock.csv</u>   

<u>StarbucksStock.csv</u>   

<u>TargetStock.csv</u>   

<u>TJXStock.csv</u>   

<u>UltaStock.csv</u>  

<u>WalmartStock.csv</u>   

## Figures
<u>fig1_allStockPrice.py</u>  

<u>fig2_estee.py</u>  

<u>fig3_overlay.py</u>  

<u>fig4_dream_pop.py</u>  

<u>fig5_individual.py</u>  

<u>fig6_correlationHeatMap.py</u>  

<u>fig7_smallLuxuryBigPurchase.py</u>  

<u>fig8_smallLuxuryEconomicIndicators.py</u>  

<u>fig9_BudgetLuxury.py</u>  

<u>fig10_allStockPercentChange.py</u>



## Packages
<u>pandas</u>   
- **Import:** pandas as pd  
- **Usage:** work with csv files and clean/manipulate data

<u>matplotlib</u>  
- **Import:** matplotlib.pyplot as plt  
- **Usage:** plotting graphs  

<u>seaborn</u>  
- **Import:** seaborn as sns  
- **Usage:** heatmap

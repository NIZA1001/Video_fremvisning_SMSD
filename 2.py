from matplotlib.pyplot import figure
import numpy as np
import tidyfinance as td
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.optimize as sc

Data = td.download_data(
    domain="Stock Prices",
    symbols="^GSPC",
    start_date="2012-01-01",
    end_date="2026-10-01"
)

Stock = Data.pivot(index="date", on="symbol",values="adjusted_close")

Stock = Stock.to_pandas()

Stock = Stock.set_index("date")

Stock["S&P-500.log"] = np.log(Stock["^GSPC"])
Stock["diff"] = Stock["S&P-500.log"].diff(1)

print(Stock.isna().sum())

Stock = Stock.dropna()

print(Stock.head())

plt.clf()

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(Stock["S&P-500.log"])
plt.legend(Stock)
plt.grid()
ax[1].plot(Stock["diff"])
plt.legend(Stock)
plt.grid()
plt.show()
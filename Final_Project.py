import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 72)
pd.options.display.width = 0

df = pd.read_csv('Liquer_Sales_2016_till_ 2019.csv')

BottlesSold = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
BottlesSold = BottlesSold.sort_values(ascending=False)
MostPopularItem = BottlesSold.groupby('zip_code').head(1).reset_index()

MostPopularItem.columns = ['Zip Code', 'Item Name', 'Bottles Sold']
print('Most Popular Item Sold Per Zip Code:')
print(MostPopularItem)

print()


StoreSales = df.groupby(['store_number', 'store_name', 'item_description'])['bottles_sold'].sum()
MostPopularOfStore = StoreSales.sort_values(ascending=False)
TotalStoreSales = StoreSales.groupby('store_number').sum()
PercentageOfSales = MostPopularOfStore/TotalStoreSales * 100
PercentageOfSalesPerStore = PercentageOfSales.groupby('store_number').head(1)

PercentageOfSalesPerStore.columns = ['Store Number', 'Store Name', 'Item Name', 'Percentage of Total Sales']

print('Most Popular Item\'s Percentage of Sales Per Store')
print(PercentageOfSalesPerStore)



colors = np.random.randint(74, size=74)
plt.scatter(df['zip_code'], df['bottles_sold'], c=colors, cmap='nipy_spectral_r')
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold Per Zip Code')
plt.show()


PercentageOfSalesPerStore.plot(kind='bar')
plt.title('Most Popular Item Sales Percentage By Store')
plt.xlabel('Store Name')
plt.ylabel('Percentage Based on Total Sales')
plt.show()

#1.Importing libraries and Loading dataset

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("OnlineRetail.csv", encoding='latin1')
print(df.head())
print(df.info())

#2.Data Cleaning

df= df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
print(df.info())

#3.Creating Revenue Column

df['TotalRevenue'] = df['Quantity']* df['UnitPrice']
print(df.info())

#4.Top 10 Products

top_products = df.groupby('Description')['Quantity'].sum()
top_products = top_products.sort_values(ascending=False).head(10)
print(top_products)

#5.Revenue by country

revenue_country = df.groupby('Country')['TotalRevenue'].sum()
top_countries = revenue_country.sort_values(ascending=False).head(5)
print(top_countries)

#6.Bar chart(Top products)

plt.figure()
top_products.plot(kind='bar')
plt.title("Top 10 products")
plt.xlabel("product")
plt.ylabel("Quantity sold")
plt.show()

#7.Pie Chart(Country Revenue)

plt.figure()
top_countries.plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 5 Countries by Revenue")
plt.show()



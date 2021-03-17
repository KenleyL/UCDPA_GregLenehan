
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


Property_Prices = pd.read_csv("form_41c-price-sh-property-area-by_year_1_test.csv")

#dropping duplicates





#showing column names
print (Property_Prices.columns)

#List - only showing the Dublin and National columns
Dub_Nat = Property_Prices[["YEAR", "Dublin ", "National"]]

#sorting values by national


#printing the last 10 rows
print(Dub_Nat.tail(10))




Dub_Nat[Dub_Nat["YEAR"] >= 2005].head()

fig, ax = plt.subplots()



x= Property_Prices["National"].tail(5)
y= Property_Prices["YEAR"].tail(5)

plt.plot(x,y)
plt.show()

fig, ax = plt.subplots()



x= Property_Prices["National"].tail(5)
y= Property_Prices["Dublin "].tail(5)


plt.xlabel('National')
plt.plot(x,y)
plt.show()

#dropping rows that contain null values
droprows = Property_Prices.dropna()
print(Property_Prices.shape, droprows.shape)

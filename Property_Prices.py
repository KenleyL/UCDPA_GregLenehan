
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


Property_Prices = pd.read_csv("form_41c-price-sh-property-area-by_year_1_test.csv")

#showing column names
print (Property_Prices.columns)

#dropping rows that contain null values
droprows = Property_Prices.dropna()
print(Property_Prices.shape, droprows.shape)

#Only showing the Dublin and National columns
Dub_Nat = Property_Prices[["YEAR", "Dublin ", "National"]]

#iterrow created to show data from Dub_Nat
for i, row in Dub_Nat.iterrows():
    print(i, row[0], row[1], row[2])

#merging a dataset
df1 =pd.DataFrame({
    "Year":[2001, 2006, 2009, 2015],
    "City":["Dublin", "Dublin", "Dublin", "Dublin"],
    "Price": [267939, 512461, 345444, 335013]
})
print(df1)

df2 =pd.DataFrame({
    "Year":[2001, 2006, 2009, 2015],
    "City":["National", "National", "National", "National"],
    "Price": [206117, 371447, 275250, 264565]
})
print(df2)

print(pd.merge(df1,df2,on="Year"))

df1

list1 = ('Dublin_one', 'Dublin_six','Dublin_nine', 'Dublin_fifteen')
list2 = (267939, 512461, 345444, 335013)

fig, ax = plt.subplots()

x= list1
y= list2

plt.xlabel('Region', color='red')
plt.ylabel('Price', color='red')
ax.set_title('Dublin House Prices 2001-2015')
plt.grid(True)
plt.ylim(250000, 550000)
plt.plot(x,y)

plt.show()


list3 = ('Dublin', 'National', "Cork")
list4 = (335013, 264565, 221723)

print(Property_Prices.iloc[39])

fig, ax = plt.subplots()

x= list3
y= list4

plt.xlabel('County', color='green')
plt.ylabel('Price', color='green')
ax.set_title('House Prices 2015 Comparison')
plt.grid(True)
plt.ylim(200000, 350000)
plt.plot(x,y)

plt.show()












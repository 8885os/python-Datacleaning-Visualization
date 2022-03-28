import pandas as pd
from matplotlib import pyplot as plt
fontdict = {
    "font1": {"family": "Verdana",
    "color": "black",
    "weight": 700,
    "size": 20},
    "font2": {"family": "Verdana","color": "black","weight": 700,"size": 20,}}


sample_data = pd.read_csv('sample_data.csv')
print(sample_data.column_c.iloc[0])
plt.scatter(sample_data.column_a, sample_data.column_b)
plt.scatter(sample_data.column_a, sample_data.column_c)
plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c)
plt.suptitle("Sample Graph")
plt.title("sample",fontdict["font2"])
plt.legend(["this is x", "this is z"])
plt.show()
data = pd.read_csv('countries.csv')
us = data[data.country == 'United States']
china = data[data.country == 'China']
us.population / us.population.iloc[0] * 100
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(["united States", "China"])
plt.xlabel("Year")
plt.ylabel("Percentage growth of population(%)")
plt.show()
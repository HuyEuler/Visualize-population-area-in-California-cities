import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

cities = pd.read_csv("data/california_cities.csv")
# print(cities.head())
# print(cities.info)

# 1. Get latitude, longitude
latd, longd = cities["latd"], cities["longd"]
population, area = np.log10(cities["population_total"]), cities["area_total_km2"]
# print(area[: 5])


# 2. Visuazlize data in scatter plot
plt.scatter(latd, longd, s=area, c=population, alpha=0.5)
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.title("Visualize area, population in California cities")
plt.axis("equal")
color_bar = plt.colorbar()
color_bar.set_label("log10() (millions person)")
plt.show()


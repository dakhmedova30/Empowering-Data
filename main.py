# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util
import mpl_toolkits.mplot3d as mplot3d

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")

fig = plt.figure()
ax = plt.axes(projection='3d')

# Add Step 1 code here:
oneCountryBooleanList = lwd["country_name"] == "Indonesia"
oneCountryData = lwd.loc[oneCountryBooleanList]

twoCountryBooleanList = lwd["country_name"] == "Philippines"
twoCountryData = lwd.loc[twoCountryBooleanList]

# Print out the number of rows and columns
#print(lwd.shape)

print("The Philippines is a tropical country with a population of 113.9 million people. It typically has high humidity, high temperatures, and abundant rainfall. The Philippines is an archipelagic nation with 7,000 islands, having relatively lower diversity, and it is predominantly Christian.\n")

input("Press enter to continue.\n")

print("Indonesia has a population of 273.8 million people and is also characterized by a hot and humid climate. Rainfall occurs mostly in low-lying areas and in mountainous regions with cooler temperatures. The Indonesian archipelago has roughly 17,500 islands, having greater diversity, and it is predominantly Muslim.\n")

input("Press enter to continue.\n")

print("The median age in the Philippines is 25 years old, while the median age in Indonesia is 29.9 years. The Philippines have a higher average birth rate, at 2.78 births per woman, than Indonesia, which has 2.19 births per woman.\n")

input("Press enter to continue.\n")

print("Similarly, the average household size in the Philippines, 4.1 people, is larger than the average household size in Indonesia, which is 2.8 people per household. This might imply that Filipinos are expected to have more children on average, which can explain why women in the Philippines tend to give birth later in life.\n")

input("Press enter to continue.\n")

print("Filipinos might also be expected to raise more children due to the differences in the average incomes of families between the Philippines and Indonesia. In the Philippines, the average income of families is at 149.98 thousand Philippine pesos, which is approximately 8,781.80 US Dollars. On the other hand, the average annual salary in Indonesia is 146,000,000 Indonesian Rupiah (IDR) or 9,872 US Dollars, which is greater than in the Philippines.\n")

input("Press enter to continue.\n")

print("Lastly, the fluctuation in the number of children born based on the average age of women in Indonesia can be explained by the average age of childbirthing changing from 22.4 years in 2017 to 28.17 years in 2020. If this trend continues, it is likely to see the graph of Indonesia being more skewed to the right. As for the Philippines, the median age of mothers typically stayed at around 27 years old, which aligns with the graph.")

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
x1 = oneCountryData["DM_age_mean"]
y1 = oneCountryData["RH_children_born_mean"]
z1 = oneCountryData["year"]

# ax.scatter(x="DM_age_mean", y="RH_children_born_mean", z="year", color="red", data=oneCountryData)
ax.scatter(x1, y1, z1, color="red")

x2 = twoCountryData["DM_age_mean"]
y2 = twoCountryData["RH_children_born_mean"]
z2 = twoCountryData["year"]

# ax.scatter(x="DM_age_mean", y="RH_children_born_mean", z="year", color="blue", data=twoCountryData)
ax.scatter(x2, y2, z2, color="blue")

# add a title to the plot
plt.title("Number of Children Born over Age of Women")

#Label the x-axis
plt.xlabel("Average age of women")

# label the y-axis
plt.ylabel("Average number of children ever born")

# cmap = plt.get_cmap("viridis")
# plt.set_cmap(cmap)

# show the plot
plt.show()
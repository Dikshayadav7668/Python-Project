import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv('IPL_Matches_2008-2020.csv')

# Counting the number of matches played in each city
matches_per_city = df['city'].value_counts()


matches_per_city.plot(kind='bar')


plt.xlabel('City')
plt.ylabel('Number of Matches Played')
plt.title('Number of Matches Played in Each City')


plt.xticks(rotation=45)


plt.show()
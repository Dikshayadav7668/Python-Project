import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv('IPL_Matches_2008-2020.csv')

# Extracting the year from the date column
df['year'] = pd.to_datetime(df['date']).dt.year

# Grouping the data by year and team, and calculating the number of matches won
team_wins = df.groupby(['year', 'winner']).size().unstack().fillna(0)

# Plotting the stacked bar chart
team_wins.plot(kind='bar', stacked=True)

# Setting labels and title
plt.xlabel('Year')
plt.ylabel('Number of Matches Won')
plt.title('Matches Won by Teams over all IPL years')

# Display the plot
plt.show()
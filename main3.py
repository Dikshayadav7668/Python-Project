import pandas as pd
import matplotlib.pyplot as plt

# Read the first file
df1 = pd.read_csv('IPL_Matches_2008-2020.csv')

# Read the second file
df2 = pd.read_csv('IPL_Ball-by-Ball 2008-2020.csv')

# Extract the relevant columns from df2
df2_extra_runs = df2.loc[df2['inning'] == 1, ['id', 'bowling_team', 'extra_runs']]

# Merge the data from df1 and df2
merged_df = pd.merge(df1, df2_extra_runs, on='id')

# Extract the year from the date column
merged_df['year'] = pd.to_datetime(merged_df['date']).dt.year

# Filter the data for the year 2016
extra_runs_2016 = merged_df.loc[merged_df['year'] == 2016]

# Calculate the total extra runs conceded per team in 2016
team_extra_runs = extra_runs_2016.groupby('bowling_team')['extra_runs'].sum()

# Plotting the bar chart
team_extra_runs.plot(kind='bar')

# Setting labels and title
plt.xlabel('Team')
plt.ylabel('Extra Runs Conceded')
plt.title('Extra Runs Conceded per Team in 2016')

# Display the plot
plt.show()
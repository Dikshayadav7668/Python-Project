# first i an inserting neccsory libraries
import pandas as pd # this is to read files 
import matplotlib.pyplot as plt # this to plot graphs

# reading data in  adtaframe 
data = pd.read_csv('IPL_MATCHES_2008-2020.csv') # your file name conating the column yu are  going to use
data['year'] = pd.to_datetime(data['date']).dt.year

mathces_per_year = data['year'].value_counts().sort_index() # counting the number of matches played and sorting them in asscending order of year
# now plotting the data 
plt.bar(mathces_per_year.index, mathces_per_year.values)
plt.xlabel("Year")
plt.ylabel("number of matches")
plt.title("matches in years")
#showing graph
plt.show()
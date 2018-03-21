# Import libraries and artwork data
import numpy as np
import pandas as pd

artworks = pd.read_csv('data/artworks.csv')
print(artworks.shape)
print(artworks.head())

# Count the number of pieces each artist has on display and show the top 10 artists
df = pd.DataFrame(artworks)
print(df['Name'].value_counts().head(10))

# Use matplotlib to create a bar graph to display the 10 artists with the most pieces on display 
import matplotlib.pyplot as plt
top_10_artists = df['Name'].value_counts()[:20]
top_10_artists.plot(kind='barh').invert_yaxis()
plt.ylabel('Artist') 
plt.xlabel('Number of Pieces on Display')
plt.suptitle('Artists With the Most Pieces on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()

# Import artist data
artists = pd.read_csv('data/artists.csv')
print(artists.shape)
print(artists.head())

# Find the proportion of male to female artists who have works on display at the MoMA
df2 = pd.DataFrame(artists)
print(df2['Gender'].value_counts())

# Clean up missing values and capitalization inconsistencies in the artist data
df2['Gender'].replace('male', 'Male',inplace=True)
df2['Gender'].replace(np.nan, 'Unknown', inplace=True)
print(df2['Gender'].value_counts())  

# Check that all artists have been accounted for
print(sum(df2['Gender'].value_counts()) == artists.shape[0])

# Graph the proportion of male to female artists on display
labels = 'Male', 'Female', 'Unknown'
sizes = [9826, 3072, 2193]
colors = ['gold', 'lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.suptitle('Artists with Pieces on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()











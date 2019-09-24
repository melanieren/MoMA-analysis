# Import libraries and data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_artworks = pd.read_csv('data/artworks.csv')
print(df_artworks.shape)
print(df_artworks.head())

df_artists = pd.read_csv('data/artists.csv')
print(df_artists.shape)
print(df_artists.head())


# 1. Artists with most pieces on display
# Count the number of pieces each artist has on display and show the top 20 artists
print(df_artworks['Name'].value_counts().head(20))

# Use matplotlib to create a bar graph to display the 20 artists with the most pieces on display 
top_10_artists = df_artworks['Name'].value_counts()[:20]
top_10_artists.plot(kind='barh').invert_yaxis()
plt.ylabel('Artist') 
plt.xlabel('Number of Pieces on Display')
plt.suptitle('Artists With the Most Pieces on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()


# 2. Proportion of male to female artists with pieces on display 
# Find the proportion of male to female artists who have works on display at the MoMA
print(df_artists['Gender'].value_counts())

# Clean up missing values and capitalization inconsistencies in the artist data
df_artists['Gender'].replace('male', 'Male', inplace=True)
df_artists['Gender'].replace(np.nan, 'Unknown', inplace=True)

# Check that all artists have been accounted for
print(sum(df_artists['Gender'].value_counts()) == df_artists.shape[0])

# Graph the proportion of male to female artists
labels = df_artists['Gender'].value_counts().index
sizes = df_artists['Gender'].value_counts().values
colors = ['gold', 'lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.suptitle('Artists with Pieces on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()


# 3. Artists by nationality 
# Find the proportion of artists of each nationality 
most_common_nationalities = df_artists['Nationality'].value_counts()[:20]
most_common_nationalities.plot(kind='barh').invert_yaxis()
plt.ylabel('Nationality') 
plt.xlabel('Number of Artists')
plt.suptitle('Most Common Nationalities of the Artists on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()

# Classify the 20 most common nationalities of the artists by continent 
df_artists['Continent'] = np.nan

north_america = ['American', 'Canadian', 'Mexican']
south_america = ['Brazilian', 'Argentine']
europe = ['German', 'French', 'British', 'Italian', 'Swiss', 'Dutch', 'Austrian', 
            'Russian', 'Spanish', 'Polish', 'Danish', 'Belgian']
asia = ['Japanese']

def classify_nationality(row_index) :
    if df_artists.loc[row_index,'Nationality'] in north_america:
        df_artists.loc[row_index, 'Continent'] = 'North America'
    elif df_artists.loc[row_index,'Nationality'] in south_america:
        df_artists.loc[row_index, 'Continent'] = 'South America'
    elif df_artists.loc[row_index,'Nationality'] in europe:
        df_artists.loc[row_index, 'Continent'] = 'Europe'
    elif df_artists.loc[row_index,'Nationality'] in asia:
        df_artists.loc[row_index, 'Continent'] = 'Asia'
    elif (df_artists.loc[row_index,'Nationality'] == 'Nationality unknown') :
        df_artists.loc[row_index, 'Continent'] = 'Unknown'
            
for index, row in df_artists.iterrows() : 
    classify_nationality(index)

# Graph the proportion of continents represented by the 20 most common nationalities of the artists at the MoMA
labels = df_artists['Continent'].value_counts().index
sizes = df_artists['Continent'].value_counts().values
colors = ['gold', 'lightcoral', 'lightskyblue', 'mediumslateblue', 'firebrick']
plt.pie(sizes, colors=colors, autopct='%1.1f%%', pctdistance=1.2, shadow=False, startangle=140)
plt.axis('equal')
plt.suptitle('Top 20 Most Common Artist Nationalities by Continent', fontsize=14, fontweight='bold')
plt.legend(labels,loc=4)
plt.show()


# 4. When were the pieces on display added to the collection at MoMA?
# Sort the artworks data by 'Acquisition Date'
df_artworks['Acquisition Date'] = pd.to_datetime(df_artworks['Acquisition Date'], errors='coerce')
acquisitions = df_artworks['Acquisition Date'].value_counts()
acquisitions_sorted = acquisitions.sort_index()

# Show the data as a time series
acquisitions_sorted_cumsum = acquisitions_sorted.cumsum()
ts = acquisitions_sorted_cumsum.plot()
ts.set_title('Total Number of Artworks Acquired by the MoMA Over Time', fontsize=14, fontweight='bold')
ts.set_xlabel("Year")
ts.set_ylabel("Total Number of Artworks Acquired")

            












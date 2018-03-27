# Import libraries and artwork data
import numpy as np
import pandas as pd

artworks = pd.read_csv('data/artworks.csv')
print(artworks.shape)
print(artworks.head())

# Count the number of pieces each artist has on display and show the top 10 artists
df_artworks = pd.DataFrame(artworks)
print(df_artworks['Name'].value_counts().head(10))

# Use matplotlib to create a bar graph to display the 10 artists with the most pieces on display 
import matplotlib.pyplot as plt
top_10_artists = df_artworks['Name'].value_counts()[:20]
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
df_artists = pd.DataFrame(artists)
print(df_artists['Gender'].value_counts())

# Clean up missing values and capitalization inconsistencies in the artist data
df_artists['Gender'].replace('male', 'Male',inplace=True)
df_artists['Gender'].replace(np.nan, 'Unknown', inplace=True)
print(df_artists['Gender'].value_counts())  

# Check that all artists have been accounted for
print(sum(df_artists['Gender'].value_counts()) == artists.shape[0])

# Graph the proportion of male to female artists on display
labels = 'Male', 'Female', 'Unknown'
sizes = [9826, 3072, 2193]
colors = ['gold', 'lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.suptitle('Artists with Pieces on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()

# Find the proportion of artists of each nationality 
print(df_artists['Nationality'].value_counts())
most_common_nationalities = df_artists['Nationality'].value_counts()[:20]
most_common_nationalities.plot(kind='barh').invert_yaxis()
plt.ylabel('Nationality') 
plt.xlabel('Number of Artists')
plt.suptitle('Most Common Nationalities of the Artists on Display at the MoMA', fontsize=14, fontweight='bold')
plt.show()

# Classify the 20 most common nationalities of the artists by continent 
df_artists['Continent'] = np.nan

def classify_nationality(row_index) :
    if (df_artists.loc[row_index,'Nationality'] == 'American' or
        df_artists.loc[row_index,'Nationality'] == 'Canadian' or
        df_artists.loc[row_index,'Nationality'] == 'Mexican') :
        df_artists.loc[row_index, 'Continent'] = 'North America'
    elif (df_artists.loc[row_index,'Nationality'] == 'Brazilian' or
        df_artists.loc[row_index,'Nationality'] == 'Argentine') :
        df_artists.loc[row_index, 'Continent'] = 'South America'
    elif (df_artists.loc[row_index,'Nationality'] == 'German' or
        df_artists.loc[row_index,'Nationality'] == 'French' or
        df_artists.loc[row_index,'Nationality'] == 'British' or
        df_artists.loc[row_index,'Nationality'] == 'Italian' or
        df_artists.loc[row_index,'Nationality'] == 'Swiss' or
        df_artists.loc[row_index,'Nationality'] == 'Dutch' or
        df_artists.loc[row_index,'Nationality'] == 'Austrian' or
        df_artists.loc[row_index,'Nationality'] == 'Russian' or
        df_artists.loc[row_index,'Nationality'] == 'Spanish' or
        df_artists.loc[row_index,'Nationality'] == 'Polish' or
        df_artists.loc[row_index,'Nationality'] == 'Danish' or
        df_artists.loc[row_index,'Nationality'] == 'Belgian') :
        df_artists.loc[row_index, 'Continent'] = 'Europe'
    elif (df_artists.loc[row_index,'Nationality'] == 'Japanese') :
        df_artists.loc[row_index, 'Continent'] = 'Asia'
    elif (df_artists.loc[row_index,'Nationality'] == 'Nationality unknown') :
        df_artists.loc[row_index, 'Continent'] = 'Unknown'
            
for index, row in df_artists.iterrows() : 
    classify_nationality(index)
    
print(df_artists['Continent'].value_counts())

# Graph the proportion of continents represented by the 20 most common nationalities 
labels = 'North America', 'Europe', 'Asia', 'South America'
sizes = [5522, 4597, 498, 294]
colors = ['gold', 'lightcoral', 'lightskyblue', 'red', 'blue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.suptitle('Top 20 Most Common Nationalities by Continent', fontsize=14, fontweight='bold')
plt.show()
            












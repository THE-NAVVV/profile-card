import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 1 
print("Starting Task 1...")

df = pd.read_csv('netflix_titles.csv')

print(df.head(10))
print(df.shape)
print(df.info())
print(df.describe(include='all'))

df.drop_duplicates(subset='show_id', inplace=True)
df.drop(columns=['description'], inplace=True)

print("Task 1 Completed")
 

# step 2
print("Starting Task 2...")

df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('No Director Listed')

def get_minutes(val):
if isinstance(val, str) and 'min' in val:
 return int(val.split(' ')[0])
return np.nan

def get_seasons(val):
 if isinstance(val, str) and 'Season' in val:
        return int(val.split(' ')[0])
return np.nan

df['duration_minutes'] = df['duration'].apply(get_minutes)
df['seasons'] = df['duration'].apply(get_seasons)

df['Is_Recent'] = df['release_year'].apply(lambda x: 1 if x >= 2015 else 0)

print("Task 2 Completed")

#step 3  

print("Starting Task 3...")

sns.set_style("whitegrid")

plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=df)
plt.title('Movies vs TV Shows')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['release_year'], bins=30, kde=True, color='blue')
plt.title('Release Year Distribution')
plt.show()

top_countries = df['country'].value_counts().head(10).index
plt.figure(figsize=(12, 6))
sns.countplot(y='country', data=df, order=top_countries, palette='viridis')
plt.title('Top 10 Countries')
plt.show()

movies_data = df[df['type'] == 'Movie']
plt.figure(figsize=(8, 5))
sns.boxplot(x='Is_Recent', y='duration_minutes', data=movies_data)
plt.title('Duration: Recent vs Old')
plt.show()

plt.figure(figsize=(8, 6))
numeric_cols = df[['release_year', 'duration_minutes', 'seasons', 'Is_Recent']]
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()

print("All step Finished")
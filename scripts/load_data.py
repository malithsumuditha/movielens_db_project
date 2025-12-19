import mysql.connector
import pandas as pd

# DB connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD", # replace with your MySQL root password
    database="movielens_db"
)

cursor = db.cursor()

# Load movies.csv
movies = pd.read_csv("../data/movies.csv")
for _, row in movies.iterrows():
    cursor.execute("""
        INSERT INTO movies (movieId, title, genres)
        VALUES (%s, %s, %s)
    """, (row['movieId'], row['title'], row['genres']))

db.commit()
print("movies imported")

# Load ratings.csv
ratings = pd.read_csv("../data/ratings.csv")
for _, row in ratings.iterrows():
    cursor.execute("""
        INSERT INTO ratings (userId, movieId, rating, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (row['userId'], row['movieId'], row['rating'], row['timestamp']))

db.commit()
print("ratings imported")

# Load tags.csv
tags = pd.read_csv("../data/tags.csv")
for _, row in tags.iterrows():
    cursor.execute("""
        INSERT INTO tags (userId, movieId, tag, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (row['userId'], row['movieId'], row['tag'], row['timestamp']))

db.commit()
print("tags imported")


# Load links.csv
links = pd.read_csv("../data/links.csv")
for _, row in links.iterrows():
    cursor.execute("""
        INSERT INTO links (movieId, imdbId, tmdbId)
        VALUES (%s, %s, %s)
    """, (row['movieId'], row['imdbId'], row['tmdbId']))

db.commit()
print("links imported")
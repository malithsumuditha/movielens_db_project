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

# Normalize raw genres into movie_genres table
movies = pd.read_csv("movies.csv")

for _, row in movies.iterrows():
    genres = str(row['genres']).split("|")
    for g in genres:
        cursor.execute("""
            INSERT INTO movie_genres (movieId, genre)
            VALUES (%s, %s)
        """, (row['movieId'], g))

db.commit()
print("genre normalization completed")

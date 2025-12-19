import pandas as pd
import matplotlib.pyplot as plt

# 1. Popularity vs Quality per movie
df_movies = pd.read_csv("../results/results_by_movie.csv")

plt.figure(figsize=(10,6))
plt.scatter(df_movies['rating_count'], df_movies['avg_rating'])
plt.title("Popularity vs Quality (Per Movie)")
plt.xlabel("Rating Count (Popularity)")
plt.ylabel("Average Rating (Quality)")
plt.tight_layout()
plt.show()


# 2. Genre-level Average Rating + Popularity
df_genre = pd.read_csv("../results/results_by_genre.csv")

# avg rating per genre
plt.figure(figsize=(12,6))
plt.bar(df_genre['genre'], df_genre['avg_rating'])
plt.xticks(rotation=45)
plt.title("Average Rating per Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# popularity per genre (rating count)
plt.figure(figsize=(12,6))
plt.bar(df_genre['genre'], df_genre['total_ratings'])
plt.xticks(rotation=45)
plt.title("Rating Count per Genre (Popularity)")
plt.xlabel("Genre")
plt.ylabel("Rating Count")
plt.tight_layout()
plt.show()

# 3. Top 10 filtered movies (>= 50 ratings)
df_filtered = pd.read_csv("../results/rating_count_threshold.csv")
top_10 = df_filtered.sort_values(by="avg_rating", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_10['title'], top_10['avg_rating'])
plt.title("Top Rated Movies (min 50 ratings)")
plt.xlabel("Average Rating")
plt.tight_layout()
plt.show()

# 4. Tag Frequency Visualization
df_tags = pd.read_csv("../results/tag_frequency.csv")
top_tags = df_tags.sort_values(by="tag_frequency", ascending=False).head(15)

plt.figure(figsize=(10,6))
plt.barh(top_tags['tag'], top_tags['tag_frequency'])
plt.title("Most Frequent User Tags")
plt.xlabel("Tag Usage Frequency")
plt.tight_layout()
plt.show()

# 5. Monthly Rating Trend
df_time = pd.read_csv("../results/time_trend.csv")

plt.figure(figsize=(14,6))
plt.plot(df_time['month'], df_time['monthly_count'])

# show one tick per year (every 12 rows)
plt.xticks(df_time.index[::12], df_time['month'][::12], rotation=45)

plt.title("Monthly Rating Activity Over Time")
plt.xlabel("Month")
plt.ylabel("Ratings per Month")
plt.tight_layout()
plt.show()

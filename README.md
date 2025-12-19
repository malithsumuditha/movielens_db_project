MovieLens Genre + Rating Analysis – SQL + Python Project
📌 Objective

This project investigates how movie genres and user rating behavior relate to movie popularity and perceived quality using analytical SQL queries, normalization, and Python-based visualization.

📂 Dataset

MovieLens Latest Small Dataset
Download link:
https://grouplens.org/datasets/movielens/latest/

Required CSVs:

movies.csv

ratings.csv

tags.csv

links.csv

🔧 Project Structure
MovieLens-DB-Project/
│
├── data/                     # raw CSV files
├── sql/
│   ├── create_schema.sql
│   ├── genre_normalization.sql
│   ├── query1_popularity_vs_quality.sql
│   ├── query2_genre_rating.sql
│   ├── query3_threshold_filter.sql
│   ├── query4_tag_frequency.sql
│   └── query5_temporal_trend.sql
├── scripts/
│   ├── load_data.py
│   ├── normalize_genres.py
│   └── visualize_results.py
├── results/
│   ├── results_by_movie.csv
│   ├── results_by_genre.csv
│   ├── rating_count_threshold.csv
│   ├── tag_frequency.csv
│   └── time_trend.csv
├── visuals/
│   ├── fig_avg_rating_per_genre.png
│   ├── fig_popularity_vs_quality.png
│   ├── fig_monthly_rating_trend.png
│   └── ...
├── diagrams/
│   └── er_diagram.png
├── requirements.txt
└── README.md

⚙️ Installation

Install Python packages:

pip install -r requirements.txt

🚀 How to Reproduce
1️⃣ Create database + schema
run sql/create_schema.sql

2️⃣ Load raw data into DB
python scripts/load_data.py

3️⃣ Normalize genres from pipe-separated list
python scripts/normalize_genres.py


(Or execute sql/genre_normalization.sql)

4️⃣ Run analytical SQL queries
run each file in /sql/query*.sql

5️⃣ Generate visualizations
python scripts/visualize_results.py


Charts saved to /visuals.

📊 Analysis Overview

Analytical queries extract:

popularity vs perceived quality

genre-level aggregation

bias filtering with rating thresholds

tag frequency behavior

monthly rating activity trends

Visualizations demonstrate:

weak correlation between popularity + quality

genre differences in perceived value

temporal usage spikes indicating engagement cycles

🔁 Reproducibility Guarantee

All results in this project are reproducible via:

public dataset

SQL schema + constraints

ingestion scripts

query execution files

deterministic analysis flow

🧑‍💻 Contributors

Malith Sumuditha Udara Hewa Puhulwellage

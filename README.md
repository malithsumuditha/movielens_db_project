# MovieLens Genre + Rating Analysis  
### SQL + Python Project  

## Objective  
This project investigates how movie genres and user rating behavior relate to movie popularity and perceived quality using SQL analytical queries, normalization, bias filtering, and Python visualizations.

## Dataset  
MovieLens Latest Small Dataset  
Download link: https://grouplens.org/datasets/movielens/latest/  
Select this: ml-latest-small.zip (size: 1 MB)

Required CSVs: movies.csv, ratings.csv, tags.csv, links.csv  

## Database + Ingestion  
- Created relational schema in MySQL  
- Defined PKs + FKs, and M–M genres via bridge table  
- Imported raw CSVs using Python ingestion script  
- Normalized genre column by splitting pipe-separated lists  
- Verified row counts and referential integrity  

## SQL Queries Used  
The project executes five analytical queries that contribute directly to the research question:  
1. Popularity vs Quality (count vs average rating per movie)  
2. Genre-level avg rating + popularity  
3. Threshold filtering to reduce biased low-rating-count movies  
4. Tag frequency aggregation  
5. Temporal trend in rating activity  

Each query exports results to CSV for reproducibility.

## Visualization + Interpretation  
Python scripts were used to visualize results from SQL queries.  
Key plots include:  
- Scatter plot: popularity vs quality  
- Bar chart: avg rating per genre  
- Line plot: monthly rating activity trend  

Key observed patterns:  
- Film-Noir + War genres show highest avg rating  
- Popularity (rating count) does not strongly correlate with rating quality  
- Threshold filtering improves fairness vs small sample bias  
- Temporal spikes indicate bursts of user activity  

## 🔁 Full Reproducibility Steps

Follow the steps below to fully reproduce all results and visualizations from this MovieLens genre–rating analysis project.

1. Download dataset  
   - MovieLens Latest Small dataset  
   - https://grouplens.org/datasets/movielens/latest/  
   - Required CSV files: movies.csv, ratings.csv, tags.csv, links.csv  

2. Install required Python dependencies  
   - Requires Python 3.8+  
   - Run: pip install -r requirements.txt  

3. Create database and schema in MySQL  
   - Open MySQL Workbench  
   - Execute: SOURCE sql/create_schema.sql;  
   - This creates tables, PKs, and FK relationships  

4. Load CSV data into database tables  
   - Run: python scripts/load_data.py  
   - Script connects to DB and inserts rows into movies, ratings, tags, and links  

5. Normalize movie genres  
   - Run python scripts/normalize_genres.py  
   - This splits pipe-separated genres into rows in movie_genres table  

6. Execute analytical SQL queries  
   - Run each SQL file in /sql:  
     q1_popularity_vs_quality.sql  
     q2_genres_avg_rating.sql  
     q3_threshold_filter.sql  
     q4_tag_frequency.sql  
     q5_monthly_trend.sql  
   - Each script generates a CSV file saved in /results  

7. Generate visualizations  
   - Run: python scripts/visualize.py  
   - Script reads result CSVs and outputs charts to /visuals  

8. Reproduction complete  
   - Database created  
   - Data ingested and normalized  
   - Analytical queries executed  
   - Results exported and visualized  
   - Final figures match project presentation


These steps reproduce all final figures and results deterministically.

## Contributors
Dulanjana Hewa Wickramathunga  
Malith Sumuditha Udara Hewa Puhulwellage

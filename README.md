# MovieLens Genre + Rating Analysis  
### SQL + Python Project  

## Objective  
This project investigates how movie genres and user rating behavior relate to movie popularity and perceived quality using SQL analytical queries, normalization, bias filtering, and Python visualizations.

## Dataset  
MovieLens Latest Small Dataset  
Download link: https://grouplens.org/datasets/movielens/latest/  

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

## Reproducibility Instructions  
1. Download MovieLens dataset  
2. Create schema by executing provided SQL file  
3. Import raw CSVs into MySQL  
4. Run the normalization SQL / Python script for genres  
5. Execute SQL analytical queries  
6. Run visualization script to recreate plots  

These steps reproduce all final figures and results deterministically.

## Contributors
Dulanjana Hewa Wickramathunga  
Malith Sumuditha Udara Hewa Puhulwellage

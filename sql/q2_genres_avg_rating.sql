SELECT g.genre,
       COUNT(*) AS total_ratings,
       AVG(r.rating) AS avg_rating
FROM movie_genres g
JOIN ratings r ON r.movieId = g.movieId
GROUP BY g.genre
ORDER BY avg_rating DESC;

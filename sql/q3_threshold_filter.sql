SELECT m.title,
       COUNT(*) AS rating_count,
       AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON m.movieId = r.movieId
GROUP BY m.movieId
HAVING COUNT(*) >= 50
ORDER BY avg_rating DESC;

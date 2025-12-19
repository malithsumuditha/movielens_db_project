SELECT DATE_FORMAT(FROM_UNIXTIME(timestamp), '%Y-%m') AS month,
       COUNT(*) AS monthly_count
FROM ratings
GROUP BY month;

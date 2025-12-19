SELECT tag,
       COUNT(*) AS tag_frequency
FROM tags
GROUP BY tag
ORDER BY tag_frequency DESC;

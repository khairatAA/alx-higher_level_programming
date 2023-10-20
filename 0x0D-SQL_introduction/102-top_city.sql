-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)

USE hbtn_0c_0;

SELECT city, MAX(value) AS avg_temp
FROM temperature
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

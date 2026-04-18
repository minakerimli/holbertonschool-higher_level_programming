-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- The table 'temperatures' should already be imported into the database
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

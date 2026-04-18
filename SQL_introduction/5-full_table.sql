-- Script that shows the full description of the table first_table
SELECT CREATE TABLE
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'first_table'
AND TABLE_SCHEMA = DATABASE();

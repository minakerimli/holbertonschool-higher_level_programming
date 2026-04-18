-- Converts hbtn_0c_0 database, first_table, and field name to UTF8
-- The script converts the database, then the table which includes the name field
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database to ensure the table alter applies to the correct context
USE hbtn_0c_0;

-- Converting the table to utf8mb4 will automatically convert all its string columns
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

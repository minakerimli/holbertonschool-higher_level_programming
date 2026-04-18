-- Converts hbtn_0c_0 database, first_table, and field name to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Use the database
USE hbtn_0c_0;

-- Convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field name in first_table
-- Note: CONVERT TO CHARACTER SET on the table level usually handles columns, 
-- but explicit conversion ensures requirements are met.
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

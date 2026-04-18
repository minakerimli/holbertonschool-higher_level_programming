-- Convert hbtn_0c_0 database and its content to UTF8 (utf8mb4)

-- Convert database charset and collation
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert table charset and collation
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert column name charset and collation
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert database hbtn_0c_0 to UTF8 (utf8mb4)

-- Convert database charset and collation
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert table charset and collation
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert only column collation (no CHARACTER SET here)
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;

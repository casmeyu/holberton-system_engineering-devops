-- 4. never empty
-- Creates a table with an attribute that wont be empty
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);

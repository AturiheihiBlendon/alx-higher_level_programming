-- lists all records of the table second_table with score >= 10 of the database hbtn_0c_0
-- Records should be ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC

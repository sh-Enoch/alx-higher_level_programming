-- Updates the score of Bob to 10.
UPDATE second_table
SET IF EXISTS score = 10 WHERE name = "Bob";

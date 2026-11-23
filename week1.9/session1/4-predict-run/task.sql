.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

SELECT name 
FROM restaurants
WHERE (cuisine = 'Italian' OR cuisine = 'Thai') AND hygiene_rating = 5;

-- A shows 11 restaurants with a hygiene rating of 5.
-- B shows 8 restaurants with a postcode starting with LS6.
-- C shows 0 restaurants when the cuisine was 'italian' but 4 when the cuisine was 'Italian'.
-- D shows 5 restaurants where (cuisine = 'Italian') OR (cuisine = 'Thai' AND hygiene_rating = 5).
-- If you add parentheses around the cuisine conditions, D shows 2 restaurants where (cuisine = 'Italian' OR cuisine = 'Thai') AND (hygiene_rating = 5).
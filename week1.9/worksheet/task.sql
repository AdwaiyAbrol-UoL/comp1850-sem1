.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

SELECT COUNT(*)
FROM stations
WHERE capacity > 16;

-- Q1: 3) The cardinality of the table stations is:
-- .tables
-- .schema stations
-- SELECT COUNT(*) as Cardinality FROM stations; 

-- Q1: 4) The degree of the table members is:
-- .tables
-- .schema stations
-- SELECT COUNT(*) as Cardinality FROM stations; 

-- Q4:
-- SELECT capacity
-- FROM stations
-- WHERE name = 'Briggate';

-- Q5:
-- SELECT year_added
-- FROM bikes
-- WHERE bike_id = 5;

-- Q6:
-- SELECT COUNT(*)
-- FROM stations
-- WHERE capacity = 16;

-- Q7:
-- SELECT COUNT(*)
-- FROM stations
-- WHERE capacity > 16;
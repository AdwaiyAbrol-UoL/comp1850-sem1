.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- To see all the tables in a database
.tables

-- To see the attributes belonging to each table
.schema reviews

-- And to see a count of the total number of tuples
SELECT COUNT(*) as Cardinality FROM reviews; 

-- 'customers' has cardinality of 180 and degree of 7. 
-- 'restaurants' has cardinality of 30 and degree of 5. 
-- 'menu_items' has cardinality of 270 and degree of 5. 
-- 'drivers' has cardinality of 18 and degree of 4. 
-- 'orders' has cardinality of 1300 and degree of 7. 
-- 'order_items' has cardinality of 2693 and degree of 3. 
-- 'reviews' has cardinality of 412 and degree of 4. 
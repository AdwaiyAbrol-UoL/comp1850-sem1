.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

--5
SELECT name, price
FROM menu_items
WHERE is_vegetarian = 1 AND price < 8
ORDER BY price ASC;

--6
SELECT name, hygiene_rating
FROM restaurants
WHERE hygiene_rating < 4
ORDER BY hygiene_rating ASC;

--7 : a postcode match doesn’t guarantee a restaurant is actually nearby. LS6 covers an area, and a restaurant could be at the far end of it; a postcode is only a rough location, not the student’s exact location or travel distance.
SELECT name, hygiene_rating, postcode
FROM restaurants
WHERE postcode LIKE 'LS6%'
ORDER BY hygiene_rating DESC;

--8 : I believe that the email should be sent but before that there needs to be a small check. Having a University of Leeds address doesn't prove someone agreed to receive marketing emails. So, I would suggest that the email should be sent to those customers who have a University of Leeds address and have opted in to receive marketing emails.
SELECT name, email, joined_date
FROM customers
WHERE email LIKE '%@leeds.ac.uk'
ORDER BY joined_date DESC;

--9
SELECT customer_id, order_id, order_time
FROM orders
WHERE status = 'cancelled'
ORDER BY order_time DESC LIMIT 10;

--10: vegetarian dishes
SELECT name, price
FROM menu_items
WHERE restaurant_id = 4 AND is_vegetarian = 1;

--10: most expensive dish
SELECT name, price
FROM menu_items
WHERE restaurant_id = 4
ORDER BY price DESC LIMIT 1;

--11: order_id to identify the specific order, restaurant_id to identify the restaurant involved, order_time to see when the order was placed, and status to see if the order was placed. 
SELECT order_id, restaurant_id, order_time, status
FROM orders
WHERE status = 'placed' AND order_time >= '2026-10-01 00:00:00' AND order_time < '2026-11-01 00:00:00';

--12: First query gives an error because the SQL clause order expects the 'WHERE' clause to come before the 'ORDER BY' clause. The second query is wrong because without 'ORDER BY price', you just get five vegetarian dishes, not necessarily the cheapest. 
SELECT name, price 
FROM menu_items  
WHERE is_vegetarian = 1
ORDER BY price ASC LIMIT 5;

--13: LIMIT 1 will select only one item where potentially there are several items with the same lowest price. LIMIT 5 will select more items with the same lowest price, which is a step towards a fairer approach.
SELECT name, price
FROM menu_items
ORDER BY price ASC LIMIT 1;

-- 13b: Being completely fair, Leeds Eats should list all items listed at the minimum price and not claim that one arbitrary item is the cheapest. 
SELECT name, price
FROM menu_items
ORDER BY price ASC LIMIT 5;

--14: A count alone is not enough evidence to launch the feature. Leeds Eats should also check whether late-night orders are consistently high across multiple restaurants, rather than just occasional spikes.
SELECT COUNT (*)
FROM orders
WHERE order_time LIKE '%21:%' OR order_time LIKE '%22:%' OR order_time LIKE '%23:%';

SELECT COUNT (*)
FROM orders;
-- Query 1: Top 5 customers who purchased the most books in the last year
SELECT c.customer_id, c.name, SUM(od.quantity) AS total_books
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.customer_id
ORDER BY total_books DESC
LIMIT 5;

-- Query 2: Total revenue generated from book sales by each author
SELECT b.author, SUM(b.price * od.quantity) AS total_revenue
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.author;

-- Query 3: All books that have been ordered more than 10 times
SELECT b.title, SUM(od.quantity) AS total_ordered
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.title
HAVING total_ordered > 10;

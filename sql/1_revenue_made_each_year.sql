-- 2. The most expensive 10 order
-- Which orders generated the highest total revenue?

SELECT
	order_id,
	SUM(price) AS order_total
FROM dw.fact_order_items
GROUP BY order_id
ORDER BY order_total DESC
LIMIT 10;
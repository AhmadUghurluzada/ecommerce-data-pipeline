-- Top 5 Categories
-- What categories of products are the most dominant?

SELECT 
	p.product_category_name,
	SUM(f.price) AS revenue
FROM dw.fact_order_items f 
JOIN dw.dim_products p
	ON f.product_key = p.product_key
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 5;
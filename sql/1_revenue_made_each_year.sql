-- 1. Revenue made each year
-- How much total revenue was generated each year?

SELECT 
	t.year, 
	SUM(f.price) as total_revenue
FROM dw.fact_order_items f
JOIN dw.dim_time t
	ON f.date_key = t.date_key
GROUP BY t.year
ORDER BY t.year;

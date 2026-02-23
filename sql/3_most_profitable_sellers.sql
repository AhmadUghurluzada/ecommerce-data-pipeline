-- 3. The most profitable sellers by revenue
-- Which sellers generate the highest revenue

SELECT 
	s.seller_key, 
	SUM(f.price) AS seller_revenue
FROM dw.fact_order_items f
JOIN dw.dim_sellers s
	ON f.seller_key = s.seller_key
GROUP BY s.seller_key
ORDER BY seller_revenue DESC
LIMIT 10;

-- 5. Revenue growth over the years
-- How much has revenue increased compared to previous year?

WITH yearly_revenue AS (
	SELECT 
		t.year,
		SUM(price) as revenue
	FROM dw.fact_order_items f
	JOIN dw.dim_time t
		on f.date_key = t.date_key
	GROUP BY t.year
)
SELECT 
	year,
	revenue,
	revenue - LAG(revenue) OVER (ORDER BY year) AS revenue_change,
	ROUND(
		(revenue - LAG(revenue) OVER (ORDER BY year))
		* 100 / LAG(revenue) OVER (ORDER BY year),
		2
	) AS growth_percentage
FROM yearly_revenue
ORDER BY year;
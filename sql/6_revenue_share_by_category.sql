-- 6. Revenue share by each product category
-- What category contibutes the most revenue and how much?

WITH category_revenue AS (
    SELECT 
        p.product_category_name,
        SUM(f.price) AS revenue
    FROM dw.fact_order_items f
    JOIN dw.dim_products p
        ON f.product_key = p.product_key
    GROUP BY p.product_category_name
)
SELECT 
    product_category_name,
    revenue,
    ROUND(
        revenue * 100.0 / SUM(revenue) OVER (),
        2
    ) AS revenue_percentage
FROM category_revenue
ORDER BY revenue DESC
LIMIT 10;

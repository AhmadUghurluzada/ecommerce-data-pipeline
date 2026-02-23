-- 7. Sellers ranking by dense rank
-- What are the top 10 sellers?

SELECT 
    seller_key,
    SUM(price) AS seller_revenue,
    DENSE_RANK() OVER (
        ORDER BY SUM(price) DESC
    ) AS seller_rank
FROM dw.fact_order_items
GROUP BY seller_key
ORDER BY seller_rank
LIMIT 10;
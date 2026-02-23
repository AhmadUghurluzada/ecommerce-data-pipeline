-- 8. Average review score by order status
-- How much does order status affect reviews?

SELECT 
    order_status,
    ROUND(AVG(review_score), 2) AS avg_review_score,
    COUNT(*) AS total_orders
FROM dw.fact_orders
GROUP BY order_status
ORDER BY avg_review_score DESC;
# Business Insights
## Query 1: Revenue madde each year
**Goal:** To analyze the total volume of payments processed by the platform on a yearly basis.

**SQL Code:** View Query in [Query 1](..\sql\1_revenue_made_each_year.sql)

**Result:**

![Query 1](/analytics/results_screenshots/query1.png)

**Key Insights:** The revenue jump from approximate 50K to 6.15M represents 12,200% increase. This indicates 2016 was launch  phase, while 2017 was the year of massive market growth across Brazil. There is still noticable growth (20%) in 2018, even though the dataset ends in October 2018. 2018 was on track to exceed 7.6M.

## Query 2: Most expensive orders

**Goal:** To identify the most expensive transactions and understand the maximum spending capacity of the customer base.

**SQL Code:** View Query in [Query 2](..\sql\2_most_expensive_orders.sql)

**Result:**:

![Query 2](/analytics/results_screenshots/query2.png)

**Key Insights:** The top order (13,440 BRL) is nearly double the value of the second hightest order. This can be a bulk purchase, professional machinery or computing hardware in marketplace environment. Others being consistent means ultra high transactions are rare.

## Query 3: Most profitable sellers
**Goal:** To identify the platform's power sellers and evaluate revenue among the merchant base.

**SQL Code:** View Query in [Query 3](..\sql\3_most_profitable_sellers.sql)

**Result:**

![Query 3](/analytics/results_screenshots/query3.png)

**Key Insights:** Top 5 sellers are relatively close in performance, each making between 187K and 229K BRL. This suggests a healthy competition among top-tier merchants rather than a single monopoly seller.

## Query 4: Top 5 Product categories by revenue
**Goal:** To identify the dominant product categories and understand which drive the highest financial volume.

**SQL Code:** View Query in [Query 4](..\sql\4_top_5_categories.sql)

**Result:**

![Query 4](/analytics/results_screenshots/query4.png)

**Key Insights:** Top three categories (Health & Beauty, Wacthes, Bed&Bath) have each generated over 1 million BRL in revenue. Beleza_saude (Health & Beauty) suggests a customer base that prioritizes care, meanwhile relogios_presentes (Watches & Gifts) suggests that Olist is a major destination for high-magin, giftable luxury items.


## Query 5: Revenue growth over years
**Goal:** To quantify the platform's growth by comparing annual revenue and calculating percentage increase between consecutive years. 

**SQL Code:** View Query in [Query 5](..\sql\5_revenue_growth_over_years.sql)

**Result:**

![Query 5](/analytics/results_screenshots/query5.png)

**Key Insights:** The platform transitioned from a 2016 launch phase to an impressive 12,259% revenue increase in 2017, signaling rapid market penetration across Brazil. While 2018 shows a more moderate 20.03% growth, this figure only accounts for 10 months of data. This shift from "exponential startup" to "stable scaler" highlights a maturing business model that successfully navigated throug Brazilian e-commerce.


## Query 6: Revenue share by category
**Goal:** To determine the market share of each category and identify which segments are the primary revenue drivers

**SQL Code:** View Query in [Query 6](..\sql\6_revenue_share_by_category.sql)

**Result:**

![Query 6](/analytics/results_screenshots/query6.png)

**Key Insights:** The platform has a diverse revenue stream. Top 10 categories account roughly 62.5% of total sales.The relatively balanced distribution across categories suggests that the marketplace is not dependent on single niche. This reduces the risk of a total revenue collapse if one specific industry faces a downturn.


## Query 7: Sellers rank
**Goal:** To provide a ranking of the top 10 merchants based on their revenue contribution.

**SQL Code:** View Query in [Query 7](..\sql\7_sellers_rank.sql)

**Result:**

![Query 7](/analytics/results_screenshots/query7.png)

**Key Insights:** DENSE_RANK() allows to rank merchants based on their revenue contribution. Seller 2618 has earned over 229,000 BRL, setting a high bar for others. Small diffeence between top 3 rank is a sign of tough competition. 


## Query 8: Average review score by order status
**Goal:** To analyze how the final state of an order impacts customer satisfaction

**SQL Code:** View Query in [Query 8](..\sql\8_average_review_score_by_order_status.sql)

**Result:**

![Query 8](/analytics/results_screenshots/query8.png)

**Key Insights:** Customer satisfaction clearly depends on delivery status. Delivered orders have a high average rating (4.16) and make up most orders. But ratings drop sharply for shipped but not delivered (2.00), canceled (1.80), processing (1.27), and unavailable (1.53) orders. Customers are most unhappy when orders are delayed, stuck, or out of stock, so better communication during these stages could improve satisfaction.
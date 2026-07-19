# Write your MySQL query statement below
# Approach: ROUND, AVG, Subquery, MIN, Count
-- select ROUND(AVG(order_date=customer_pref_delivery_date)*100,2) as immediate_percentage from Delivery where (customer_id,order_date) in (select customer_id,min(order_date) from Delivery group by customer_id)
 select ROUND(SUM(IF(order_date=customer_pref_delivery_date,1,0))*100/count(delivery_id),2) as immediate_percentage from Delivery where (customer_id,order_date) in (select customer_id,min(order_date) from Delivery group by customer_id)
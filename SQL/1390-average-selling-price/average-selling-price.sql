# Write your MySQL query statement below
# Approach: ROUND, IFNULL, SUM, Joins, Between, Group By
select p.product_id , IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0) as average_price
from Prices p left join UnitsSold u on p.product_id=u.product_id where u.purchase_date
BETWEEN p.start_date AND p.end_date or u.units is NULL group by product_id
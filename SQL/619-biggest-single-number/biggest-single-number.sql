# Write your MySQL query statement below
# Approach: MAX(), Subquery, GROUP BY, ORDER BY, CASE WHEN, LIMIT
-- select max(num) as num from (select num from MyNumbers group by num having count(num)=1) as unq_nos
select case when count(num)=1 then num else NULL end as num from MyNumbers group by num order by num desc limit 1
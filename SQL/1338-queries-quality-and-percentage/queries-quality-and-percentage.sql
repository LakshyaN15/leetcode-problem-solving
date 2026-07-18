# Write your MySQL query statement below
# Approach: ROUND, CAST, CASE WHEN THEN 1 ELSE 0 END, SUM, IF, GROUP BY, IS NOT NULL
-- select query_name, ROUND(avg(cast(rating as decimal)/position),2) as quality, ROUND(sum(case when rating<3 then 1 else 0 end)*100/count(*),2) as poor_query_percentage from Queries where query_name is not null group by query_name
select query_name, round(avg(rating/position),2) as quality, round(avg(if(rating<3,1,0))*100,2) as poor_query_percentage from Queries group by query_name
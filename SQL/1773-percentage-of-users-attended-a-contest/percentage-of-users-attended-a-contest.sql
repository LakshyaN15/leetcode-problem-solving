# Write your MySQL query statement below
# Approach: ROUND, COUNT, GROUP BY , ORDER BY DESC and ASC, Subquery
select contest_id , ROUND((COUNT(user_id)/(select count(1) from users) *100),2) as percentage from Register group by contest_id order by percentage desc,contest_id;

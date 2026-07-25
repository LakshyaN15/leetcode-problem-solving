# Write your MySQL query statement below
# Approach: COUNT, DISTINCT, DATE_SUB, INTERVAL, GROUPBY
-- select activity_date as day,count(distinct user_id) as active_users from Activity a where activity_date between DATE_SUB('2019-07-28', INTERVAL 30 DAY) and '2019-07-28' group by day

SELECT activity_date AS day, count(distinct user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;
# Write your MySQL query statement below
# Approach: COUNT, GROUP BY, ORDER BY
select user_id, count(follower_id) as followers_count from Followers group by user_id order by user_id
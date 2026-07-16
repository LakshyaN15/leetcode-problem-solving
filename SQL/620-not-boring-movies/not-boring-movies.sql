# Write your MySQL query statement below
# Approach: %, !=
select * from Cinema where id%2=1 and description!='boring' order by rating desc;
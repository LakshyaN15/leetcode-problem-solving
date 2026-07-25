# Write your MySQL query statement below
# Approach: HAVING
select class from Courses group by class having count(class)>=5 
# Write your MySQL query statement below
# Approach: COUNT, DISTINCT, Group by
select teacher_id, count(distinct subject_id) as cnt from Teacher group by teacher_id
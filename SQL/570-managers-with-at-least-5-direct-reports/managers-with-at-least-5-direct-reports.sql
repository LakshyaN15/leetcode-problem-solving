# Write your MySQL query statement below
select e.name from Employee e join Employee e2 on e.id=e2.managerId group by e2.managerId having count(*)>=5
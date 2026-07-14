# Approach: Subquery, Joins
-- select e.name from Employee e join Employee e2 on e.id=e2.managerId group by e2.managerId having count(*)>=5

select e.name from Employee e join (select managerId, count(*) as directReports from Employee group by managerId having count(*)>=5)
e2 on e.id=e2.managerId

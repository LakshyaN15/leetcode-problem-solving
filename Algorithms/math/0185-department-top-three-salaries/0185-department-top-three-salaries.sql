# Write your MySQL query statement below
-- select e.name as Employee, e.salary as Salary, e.departmendId from Employee e
-- inner join Department d on e.departmentId=d.id 

WITH CTE AS (
    select e.name as Employee, e.salary as Salary, d.name as Department , 
    DENSE_RANK() OVER(Partition by d.id order by salary desc) as rnk
    from Department d join Employee e on d.id=e.departmentId
)
select Department, Employee, Salary
from CTE
where rnk<=3
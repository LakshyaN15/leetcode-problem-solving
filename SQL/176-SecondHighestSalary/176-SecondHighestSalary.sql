-- Last updated: 6/27/2026, 8:32:43 PM
# Write your MySQL query statement below
select Max(salary) as SecondHighestSalary 
from employee where salary<>(select max(salary) from employee)
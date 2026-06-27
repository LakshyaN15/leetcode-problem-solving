-- Last updated: 6/27/2026, 8:32:10 PM
# Write your MySQL query statement below
select eu.unique_id, e.name from Employees e left join
EmployeeUNI eu on e.id=eu.id
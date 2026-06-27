-- Last updated: 6/27/2026, 8:32:11 PM
# Write your MySQL query statement below
select distinct author_id as id from Views where author_id=viewer_id
order by id asc
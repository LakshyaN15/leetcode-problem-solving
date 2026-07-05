# Write your MySQL query statement below

# Approach: Self joins and round
-- select a1.machine_id , round(avg(a2.timestamp-a1.timestamp),3) as processing_time
-- from Activity a1 join Activity a2 on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id and a1.activity_type='start' and a2.activity_type='end'
-- group by a1.machine_id

select a1.machine_id, round ( (select avg(a2.timestamp) from Activity a2 where
a2.activity_type='end' and a1.machine_id=a2.machine_id) - (select avg(a2.timestamp) from Activity a2 where
a2.activity_type='start' and a1.machine_id=a2.machine_id),3 ) as processing_time
from Activity a1 group by a1.machine_id
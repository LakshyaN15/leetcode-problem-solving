# Write your MySQL query statement below
# Approach: LEFT (takes char from left accroding to numbers/str), SUM, CASE WHEN
# %Y-> 2025
# %y-> 25
# %M-> September
# %m-> 09
# %d-> 12
# Capital = full form (%Y = 2025, %M = September).
# Small = short form (%y = 25, %b = Sep).

select left(trans_date, 7) as month, country, count(id) as trans_count,
sum(state='approved') as approved_count,sum(amount) as trans_total_amount,
sum((state='approved')*amount) as approved_total_amount from Transactions
group by month, country 
# or can use DATE_FORMAT(trans_date, '%Y-%m') as month and case when state='approved' then 1 else 0 end
# group by month and country very imp
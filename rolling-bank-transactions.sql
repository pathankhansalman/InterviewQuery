select date_format(t1.created_at, '%Y-%m-%d') dt,
round(avg(t2.transaction_value)) rolling_three_day from
(select date(created_at) created_at,
sum(transaction_value) transaction_value
from bank_transactions
where transaction_value > 0
group by date(created_at)) t1,
(select date(created_at) created_at_2,
sum(transaction_value) transaction_value
from bank_transactions
where transaction_value > 0
group by date(created_at)) t2
where datediff(t1.created_at, t2.created_at_2) <= 2 and
datediff(t1.created_at, t2.created_at_2) >= 0
group by t1.created_at
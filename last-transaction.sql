select created_at, transaction_value, id
from (
select created_at, transaction_value, id,
DATE(created_at) as created_date,
rank() over (partition by created_date order by created_at desc) as created_rank
from 
(select created_at, transaction_value, id,
DATE(created_at) as created_date
from bank_transactions) as t) as t1
where created_rank = 1
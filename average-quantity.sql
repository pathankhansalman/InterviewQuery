select year(created_at) as year, product_id, round(avg(quantity), 2) avg_quantity
from transactions
group by year(created_at), product_id
order by year(created_at), product_id
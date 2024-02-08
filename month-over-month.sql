select t1.mon month, round((t1.revenue - t2.revenue)/t2.revenue, 2) month_over_month
from
(select month(created_at) mon, sum(quantity*price) revenue
from transactions t1
inner join products t2
on t1.product_id = t2.id
where year(created_at) = 2019
group by month(created_at)
order by month(created_at)) t1
left join
(select month(created_at) mon, sum(quantity*price) revenue
from transactions t1
inner join products t2
on t1.product_id = t2.id
where year(created_at) = 2019
group by month(created_at)
order by month(created_at)) t2
on t1.mon = t2.mon + 1
select sum(percent_first) percent_first, sum(percent_last) percent_last
from
(select
case when kind = 'first' then pct_rev else 0 end as percent_first,
case when kind = 'last' then pct_rev else 0 end as percent_last
from
(select rev_yr, round(t.amount*100/t2.amount, 2) pct_rev
from
(select sum(amount) amount, year(created_at) rev_yr
from annual_payments
group by year(created_at)) t,
(select sum(amount) amount from annual_payments) t2) t1
left join
(select min(year(created_at)) rev_yr, 'first' kind from annual_payments
union
select max(year(created_at)) rev_yr, 'last' kind from annual_payments) t2
on t1.rev_yr = t2.rev_yr) t
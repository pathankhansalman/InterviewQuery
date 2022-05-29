select (mu1 - mu2)/power(var1/n1 + var2/n2, 0.5) t_stat
from
(select
sum(case when other_id = 'Yes' then mu else 0 end) as mu1,
sum(case when other_id = 'No' then mu else 0 end) as mu2,
sum(case when other_id = 'Yes' then var else 0 end) as var1,
sum(case when other_id = 'No' then var else 0 end) as var2,
sum(case when other_id = 'Yes' then n else 0 end) as n1,
sum(case when other_id = 'No' then n else 0 end) as n2
from
(select other_id,
avg(num_trans) mu,
avg(power(num_trans, 2)) - power(avg(num_trans), 2) var,
count(num_trans) n
from
(select user_id,
case
when other_id = 'No' then 'No'
else 'Yes' end as other_id,
num_trans from
(select t1.user_id, ifnull(t2.user_id, 'No') other_id,
count(ifnull(t2.user_id, 'No')) num_trans
from transactions t1
left join (select distinct user_id from events) t2
on t1.user_id = t2.user_id
group by t1.user_id, ifnull(t2.user_id, 'No')) t) t
group by other_id) t) t

/*t-stat suggests no statistical difference*/
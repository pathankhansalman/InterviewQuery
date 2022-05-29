select (mu1 - mu2)/power(power(std1, 2)/n1 + power(std2, 2)/n2, 0.5) T_value,
n1 + n2 - 2 D_o_F
from
(select sum(mu1) mu1, sum(mu2) mu2, sum(std1) std1, sum(std2) std2,
sum(n1) n1, sum(n2) n2
from
(select
case when cat9 = 'Yes' then mu else 0 end as mu1,
case when cat9 = 'No' then mu else 0 end as mu2,
case when cat9 = 'Yes' then std else 0 end as std1,
case when cat9 = 'No' then std else 0 end as std2,
case when cat9 = 'Yes' then n else 0 end as n1,
case when cat9 = 'No' then n else 0 end as n2
from
(select cat9, avg(price) as mu,
power(avg(power(price, 2)) - power(avg(price), 2), 0.5) as std,
count(price) as n from
(select case when category_id = 9 then 'Yes'
else 'No' end as cat9, t.*
from products t) t
group by cat9) t) t) t
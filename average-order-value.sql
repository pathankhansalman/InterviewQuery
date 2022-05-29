select t2.sex sex, round(avg(ov), 2) aov
from
(select t1.*, t1.quantity*t2.price ov from transactions t1
inner join products t2
on t1.product_id = t2.id) t1
inner join users t2
on t1.user_id = t2.id
group by t2.sex
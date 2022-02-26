select P1, P2, count(t1.user_id) as 'count(*)' from
(select distinct t1.user_id, t2.name as P1 from transactions as t1
inner join products as t2 on t1.product_id = t2.id) as t1
inner join (select distinct t1.user_id, t2.name as P2 from transactions as t1
inner join products as t2 on t1.product_id = t2.id) as t2
on t1.user_id = t2.user_id and P1 < P2
group by P1, P2
order by 'count(*)' desc
limit 5
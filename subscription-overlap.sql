select t3.user_id, count(t.end_date) as overlap
	from subscriptions as t3
	left join (select distinct t1.user_id, t1.end_date
					from subscriptions as t1, subscriptions as t2
					where t1.user_id != t2.user_id and
					((t2.end_date >= t1.end_date and
					  t1.end_date >= t2.start_date) or
					 (t2.end_date >= t1.start_date and
					  t1.start_date >= t2.start_date))) as t
	on t3.user_id = t.user_id
	group by t3.user_id

select t.comment_count, count(t.id) as frequency
	from (select t1.id, count(t2.user_id) as comment_count
			from users as t1
			left outer join comments as t2
			on t1.id = t2.user_id
			and t2.created_at BETWEEN '2020-01-01' AND '2020-01-31'
			group by t1.id) as t
	group by t.comment_count
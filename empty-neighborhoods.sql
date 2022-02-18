select t.name from
	(select t2.id, t2.name, count(t1.name) as n_count
		from neighborhoods as t2
		left outer join users as t1 on t2.id = t1.neighborhood_id
		group by t2.id) as t
	where n_count = 0

select t.one_student, t.other_student, t.score_diff from
	(SELECT t1.student as one_student, t2.student as other_student, abs(t1.score - t2.score) as score_diff
		FROM `scores` as t1
		inner join `scores` as t2 on t1.id != t2.id
		ORDER BY score_diff ASC, one_student ASC, other_student ASC
		limit 1)
	as t

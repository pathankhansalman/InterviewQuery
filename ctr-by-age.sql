select t1.age_group, sum(t1.has_clicked)/count(t1.has_clicked) crt
from
(select t1.has_clicked,
floor(floor((datediff(date(t1.search_time), t2.birthdate) + 1)/365)/10)
as age_group
from search_events as t1
inner join users as t2
on t1.user_id = t2.id
and year(t1.search_time) = 2021) t1
group by t1.age_group
order by crt desc, age_group desc
limit 3
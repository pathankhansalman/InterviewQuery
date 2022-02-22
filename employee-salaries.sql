select * from
(select (t3.emp_count/t4.emp_count) as percentage_over_100K,
t4.name as department_name, t4.emp_count as number_of_employees from
(select t1.name, count(t2.id) as emp_count
from departments as t1
left join employees as t2
on t2.department_id = t1.id
where t2.salary > 100000
group by t1.name) as t3
right join
(select t1.name, count(t2.id) as emp_count
from departments as t1
left join employees as t2
on t2.department_id = t1.id
group by t1.name) as t4
on t3.name = t4.name
where t4.emp_count >= 10) t
order by t.percentage_over_100K
limit 3
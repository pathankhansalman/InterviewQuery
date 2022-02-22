select max(salary) as salary from (select t3.*, t4.sal_count from
(select t1.id, t1.salary
from employees as t1 inner join departments as t2
on t1.department_id = t2.id
where t2.name = 'engineering'
order by t1.salary desc) as t3 left join
(select count(t1.id) as sal_count, t1.salary
from employees as t1 inner join departments as t2
on t1.department_id = t2.id
where t2.name = 'engineering'
group by t1.salary) as t4
on t3.salary = t4.salary
where t3.salary < (select max(t1.salary)
from employees as t1 inner join departments as t2
on t1.department_id = t2.id
where t2.name = 'engineering')
order by t3.salary desc) as t where sal_count = 1
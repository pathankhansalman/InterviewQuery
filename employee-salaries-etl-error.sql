select t1.first_name, t1.last_name, t1.salary from
(select first_name, last_name, salary,
row_number() OVER (PARTITION BY first_name, last_name) AS rn
from employees) as t1 inner join
(select first_name, last_name, max(rn) as rn from
    (select first_name, last_name, salary,
    row_number() OVER (PARTITION BY first_name, last_name) AS rn
    from employees) t
    group by first_name, last_name) as t2
on t1.first_name = t2.first_name
and t1.last_name = t2.last_name
and t1.rn = t2.rn
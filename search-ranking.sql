select round(1 - count(distinct t1.query)/count(distinct t2.query), 2) as percentage_less_than_3 from
(select distinct query from search_results where rating >= 3) as t1,
(select distinct query from search_results) as t2
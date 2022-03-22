select query, round(avg_rating, 2) avg_rating, prec from
(select query,
coalesce(sum(diff_prod)/((count(diff_prod) - 1)*avg(std_pos*std_rating)), 0) as prec,
avg(mean_rating) as avg_rating
from
(select t1.query,
(t1.position - t2.mean_pos)*(t1.rating - t2.mean_rating) as diff_prod,
t2.std_pos, t2.std_rating, t2.mean_rating
from search_results as t1 left join
(select query, avg(position) as mean_pos, avg(rating) as mean_rating,
stddev_samp(position) as std_pos,
stddev_samp(rating) as std_rating from search_results
group by query) as t2
on t1.query = t2.query) as t
group by query) as t
order by prec desc

select query, round(sum(position*rating)/sum(position), 2) as avg_rating
from search_results
group by query
order by avg_rating
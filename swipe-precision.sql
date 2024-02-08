select variant, avg(num_right_swipes) mean_right_swipes,
10 swipe_threshold, count(t2.user_id) num_users
from
variants t1
inner join
(select user_id,
sum(case when is_right_swipe = TRUE then 1 else 0 end) num_right_swipes
from swipes
group by user_id
having count(id) >= 10) t2
on t1.user_id = t2.user_id
group by variant
union
select variant, avg(num_right_swipes) mean_right_swipes,
50 swipe_threshold, count(t2.user_id) num_users
from
variants t1
inner join
(select user_id,
sum(case when is_right_swipe = TRUE then 1 else 0 end) num_right_swipes
from swipes
group by user_id
having count(id) >= 50) t2
on t1.user_id = t2.user_id
group by variant
union
select variant, avg(num_right_swipes) mean_right_swipes,
100 swipe_threshold, count(t2.user_id) num_users
from
variants t1
inner join
(select user_id,
sum(case when is_right_swipe = TRUE then 1 else 0 end) num_right_swipes
from swipes
group by user_id
having count(id) >= 100) t2
on t1.user_id = t2.user_id
group by variant
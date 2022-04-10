select t1.dt, ifnull(submit_count/enter_count, 0) post_success_rate from
(select DATE(created_at) dt, count(id) enter_count
from events
where action = 'post_enter'
group by DATE(created_at)) t1
left join
(select DATE(created_at) dt, count(id) submit_count
from events
where action = 'post_submit'
group by DATE(created_at)) t2
on t1.dt = t2.dt
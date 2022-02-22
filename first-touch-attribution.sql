select user_id, channel from (select t2.user_id, t1.channel,
rank() over (partition by user_id order by created_at) as channel_rank
from attribution as t1
inner join user_sessions as t2
on t1.session_id = t2.session_id) as t
where channel_rank = 1 and user_id in 
(select distinct user_id
from attribution as t1
inner join user_sessions as t2
on t1.session_id = t2.session_id
and t1.conversion = true)
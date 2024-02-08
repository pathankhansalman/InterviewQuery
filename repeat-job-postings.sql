select sum(multiple_posts) multiple_posts,
sum(single_post) single_post
from
(select 
case when max(count_id) > 1 then 1 else 0 end as multiple_posts,
case when max(count_id) > 1 then 0 else 1 end as single_post
from
(select user_id, count(id) count_id
from job_postings
group by user_id, job_id) t
group by user_id) t
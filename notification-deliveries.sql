select not_ct total_pushes, count(not_ct) frequency
from
(select count(notification) not_ct from
notification_deliveries t1
right join
users t2
on t1.user_id = t2.id
and t1.created_at <= t2.conversion_date
where conversion_date is not NULL
group by id) t
group by not_ct
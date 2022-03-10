select count(distinct user_id) as num_users_gave_like from events
where created_at = '2020-06-06 00:00:00' and action = 'like'
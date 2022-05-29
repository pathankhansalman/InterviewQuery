select count(distinct user_id) num_users_open_email from events
where action = 'email_opened'
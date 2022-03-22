select user_id, datediff(max(created_at), min(created_at)) no_of_days
from user_sessions where year(created_at) = 2020
group by user_id
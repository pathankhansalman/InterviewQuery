select daily_rank, user_id, date, downloads from
(select user_id, date, downloads,
rank() over (partition by date order by downloads desc) as daily_rank
from download_facts) as t
where daily_rank <= 3 order by date, daily_rank
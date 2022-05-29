select t1.id, t1.goal, sum(ifnull(t2.imp_count, 0))/t1.goal full_pct,
7/datediff(t1.end_dt, t1.start_dt) exp_pct
from
campaigns t1
left join
(select dt, campaign_id, count(impression_id) imp_count
from ad_impressions
group by dt, campaign_id) t2
on t1.id = t2.campaign_id
and datediff(t2.dt, t1.start_dt) >= 0
and datediff(t2.dt, t1.start_dt) <= 7
group by t1.id

/*
This shows how both the campaigns are doing in the first 7 days,
comparing the expected pct of impressions and the pct of impressions
we got. We can change the proportion of the ads accordingly (Assuming
the num of total impressions needs to be constant).
*/
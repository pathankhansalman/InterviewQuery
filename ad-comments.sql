select t1.name,
t1.ad_count/(t1.ad_count + t2.ad_count) as percentage_feed,
t2.ad_count/(t1.ad_count + t2.ad_count) as percentage_moments
from (select t2.name, count(t1.ad_id) as ad_count from feed_comments as t1
left join ads as t2 on t1.ad_id = t2.id
group by t2.name) as t1 left join
(select t2.name, count(t1.ad_id) as ad_count from moments_comments as t1
left join ads as t2 on t1.ad_id = t2.id
group by t2.name) as t2 on t1.name = t2.name
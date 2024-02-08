select var(mean)/avg(variance) f_stat
from
(select rating, var(ctr) variance, avg(ctr) mean
from
(select rating, 
sum(
    case when has_clicked is TRUE then 1 else 0 end
)/count(has_clicked) ctr
from search_results t1
inner join search_events t2
on t1.result_id = t2.search_id
and t1.query = t2.query
group by rating, t1.query) t group by rating) t
/*
Mean CTR needs to be checked across positions: one Way ANOVA.
Data needed: Mean of class variances, variance of class means
*/
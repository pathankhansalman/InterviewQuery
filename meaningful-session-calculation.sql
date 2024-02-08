/*
We first measure the time between two consecutive sessions and form
a distribution of this value. Depending on this, we consider different
visits to be different sessions if they are separated by at least some
time (bottom decile perhaps). This is because sessions can be chained.
We then run a counter to count the average number of sessions per day
*/
select avg(num_sessions) from
(select date(sess_time),
sum(
    case when minutes(datediff(sess_time, lag(sess_time))) <=
    (
        select percentile_disc(0.1)
        within group (order by minutes(datediff(sess_time, lag(sess_time))))
        from user_sessions
    )
    then 0 else 1 end
) num_sessions
group by date(sess_time)) t
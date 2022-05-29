/*
We want users to start a session after the email is sent. Since we can't
reliably know when the email is read, we can assume that it's at least 10
minutes after it's sent. So any session started at least 10 minutes after
the email is sent can be attributed to the email. The upper limit is 6 hours,
for the attribution to work.
# We can see the percentage of such "conversions" to measure the success
*/
select t1.sent_at, min(t2.created_at) created,
time_to_sec(timediff(t2.created_at, t1.sent_at)) from emails t1
left join
user_sessions t2
on t1.user_id = t2.user_id
and time_to_sec(timediff(t2.created_at, t1.sent_at)) >= 60
and time_to_sec(timediff(t2.created_at, t1.sent_at)) <= 21600
group by t1.sent_at
order by t1.sent_at
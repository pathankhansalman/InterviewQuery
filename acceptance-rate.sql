select round(count(t2.requester_id)/count(t1.requester_id), 4)
as acceptance_rate from
(select distinct * from friend_requests) as t1
left join (select distinct * from friend_accepts) as t2
on t1.requester_id = t2.requester_id and
t1.requested_id = t2.acceptor_id
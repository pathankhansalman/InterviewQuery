select 'inner_join' as join_type, 3 as number_of_rows
union
select 'right_join' as join_type, 3 as number_of_rows
union
select 'left_join' as join_type, count(*) as number_of_rows
from ads
union
select 'cross_join' as join_type, 3*count(*) as number_of_rows
from ads
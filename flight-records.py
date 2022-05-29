select distinct
case when source_location < destination_location
then source_location else destination_location end as destination_one,
case when source_location > destination_location
then source_location else destination_location end as destination_two
from flights
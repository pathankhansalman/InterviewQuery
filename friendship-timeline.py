import pandas as pd
def friendship_timeline(friends_added, friends_removed):
    time_dict = {}
    for item in friends_added:
        first_id = min(item['user_ids'])
        second_id = max(item['user_ids'])
        if first_id not in time_dict:
            time_dict[first_id] = {}
        if second_id not in time_dict[first_id]:
            time_dict[first_id][second_id] = {}
        if 'added' not in time_dict[first_id][second_id]:
            time_dict[first_id][second_id]['added'] = []
        time_dict[first_id][second_id]['added'].\
            append(pd.to_datetime(item['created_at'], format='%Y-%m-%d'))
    for item in friends_removed:
        first_id = min(item['user_ids'])
        second_id = max(item['user_ids'])
        if first_id not in time_dict:
            time_dict[first_id] = {}
        if second_id not in time_dict[first_id]:
            time_dict[first_id][second_id] = {}
        if 'removed' not in time_dict[first_id][second_id]:
            time_dict[first_id][second_id]['removed'] = []
        time_dict[first_id][second_id]['removed'].\
            append(pd.to_datetime(item['created_at'], format='%Y-%m-%d'))
    retval = []
    for first_id in time_dict.keys():
        for second_id in time_dict[first_id].keys():
            if 'removed' not in time_dict[first_id][second_id].keys():
                continue
            time_dict[first_id][second_id]['added'] =\
                time_dict[first_id][second_id]['added'][:len(time_dict[first_id][second_id]['removed'])]
            time_dict[first_id][second_id]['added'] =\
                list(sorted(time_dict[first_id][second_id]['added']))
            time_dict[first_id][second_id]['removed'] =\
                list(sorted(time_dict[first_id][second_id]['removed']))
            for i in range(len(time_dict[first_id][second_id]['removed'])):
                retval.append(
                    {
                        'user_ids': [first_id, second_id],
                        'start_date' : time_dict[first_id][second_id]['added'][i].strftime('%Y-%m-%d'),
                        'end_date' : time_dict[first_id][second_id]['removed'][i].strftime('%Y-%m-%d')
                    }
                )
    return retval
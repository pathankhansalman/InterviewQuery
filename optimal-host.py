import pandas as pd
import numpy as np
def pick_host(friends):
    df = pd.DataFrame([[x['name'],
                        x['location'][0],
                        x['location'][1],
                        x['location'][2]] for x in friends],
                      columns=['name', 'x', 'y', 'z'])
    names = list(df['name'])
    min_dist = 999999999999
    min_name = ''
    for name in names:
        ser = df.loc[df['name'] == name, ['x', 'y', 'z']].iloc[0, :].copy()
        # print(ser)
        # print(df.loc[~(df['name'] == name), ['x', 'y', 'z']])
        # print(df.loc[~(df['name'] == name), ['x', 'y', 'z']].sub(ser, axis=1))
        curr_dist = np.sqrt(np.power(df.loc[~(df['name'] == name), ['x', 'y', 'z']].sub(ser, axis=1), 2).sum(axis=1)).sum()
        if curr_dist < min_dist:
            min_dist = curr_dist
            min_name = name
    return min_name
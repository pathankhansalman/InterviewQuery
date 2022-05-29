import pandas as pd

def previous_nan_values(clients_df):
    unique_ids = list(clients_df['client_id'].unique())
    clients_df = clients_df.sort_values(by=['client_id', 'ranking'],
                                        ascending=True)
    for client_id in unique_ids:
        clients_df.loc[clients_df['client_id'] == client_id,
                       'value'] =\
            clients_df.loc[clients_df['client_id'] == client_id,
                           'value'].ffill(axis=0)
    return clients_df.sort_values(by=['ranking', 'client_id'],
                                  ascending=True)
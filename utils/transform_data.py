import json
import pandas as pd

def transform_data(df):
    new_df_list = []  # Create an empty list to store DataFrames
    if not df.empty:
        for index, row in df.iterrows():
            base_code = row['code']
            date = index
            rates = row['rates']
            normalized_df = pd.json_normalize(rates)
            normalized_df['code'] = base_code
            normalized_df['date'] = date[:10]
            normalized_df['period'] = date[:7]
            new_df_list.append(normalized_df)
    new_df = pd.concat(new_df_list, ignore_index=True)
    return new_df
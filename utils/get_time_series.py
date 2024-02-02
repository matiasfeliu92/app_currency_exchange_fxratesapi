import pandas as pd
import requests
import json

from utils.constants import BASE_URL

def get_series_times(base_code, currencies, start_date, end_date):
    try:
        query = {
            'base': base_code,
            'start_date': start_date,
            'end_date': end_date,
            'currencies': currencies
        }
        r = requests.get(BASE_URL+'/timeseries', params=query)
        time_series = r.json()
        df = pd.DataFrame(time_series)
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None, None, None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None
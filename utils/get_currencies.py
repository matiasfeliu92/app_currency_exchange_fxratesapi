import pandas as pd
import requests

from utils.constants import BASE_URL

def get_currencies():
    try:
        df_currencies = pd.DataFrame()
        r = requests.get(BASE_URL+'/currencies')
        currencies = r.json()
        for key, value in currencies.items():
            df = pd.json_normalize(value)
            df_currencies = pd.concat([df_currencies, df], ignore_index=True)
        return df_currencies
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
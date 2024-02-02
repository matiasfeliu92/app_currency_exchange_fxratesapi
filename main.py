import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta, timezone, date

from utils.get_currencies import get_currencies
from utils.get_time_series import get_series_times
from utils.transform_data import transform_data

st.set_page_config(
    page_title="Currency exchanges app",
    page_icon=":chart_with_upwards_trend:",
    layout = "wide"
)

df_currencies = get_currencies()
currency_code_selector = st.multiselect('Select the currency codes', list(df_currencies['code']))
currency_code_selector = ",".join(currency_code_selector)
print(currency_code_selector)

date_range = st.date_input("Selecciona el rango de fechas", (date.today() - timedelta(days=364), date.today()))
start_date = date_range[0].strftime('%Y-%m-%dT%H:%M:%S.%fZ')
end_date = date_range[1].strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print({'start_date': start_date, 'end_date': end_date})

rates_currencies_selector = st.multiselect('Select the currency codes for the rates', list(df_currencies['code']))
rates_currencies_selector = ",".join(rates_currencies_selector)
print(rates_currencies_selector)

df_time_series = get_series_times(currency_code_selector, rates_currencies_selector, start_date, end_date)
df_time_series.rename(columns={'base': 'code'}, inplace=True)

df_time_series_values = transform_data(df_time_series).sort_values('date', ascending=False)
# print(df_time_series_values.select_dtypes(include='float64'))
if currency_code_selector and rates_currencies_selector:
    st.dataframe(df_time_series_values[0:10])
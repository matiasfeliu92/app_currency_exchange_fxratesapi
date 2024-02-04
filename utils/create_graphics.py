import pandas as pd
import plotly.express as px

def create_graphics(df:pd.DataFrame(), code: str, rate_col:str):
    print({'df': df[0:1], 'code': code, 'rate_col': rate_col})
    fig = px.line(df, x='date', y=f'{rate_col}', title=f"{df['code'][0]} to {rate_col}")
    return fig
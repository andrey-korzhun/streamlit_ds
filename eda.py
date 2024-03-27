import time

import pandas as pd
import streamlit as st
import plotly.express as px

from PIL import Image


image = Image.open('data/header.png')
st.set_page_config(
    page_title="Home Credit",
    page_icon=image,
)
st.image(image)
st.write(
    """
    # Home Credit Competition - EDA
    ### Data sample
    """
)

n_rows = st.slider(
        "N rows for display",
        min_value=1, max_value=10, value=5, step=1)

path_train_base = f'data/train_base.csv'
df = pd.read_csv(path_train_base)
df['year'] = df['MONTH'] // 100
df['month'] = df['MONTH'] % 100
df = df.drop(columns=['MONTH'])

st.write(df.sample(n_rows))

st.write(
    """
    ### Event rate per month
    """
)
year = st.radio(
    "Select year",
    [2019, 2020],
    index=0, )

gpd_df = df[['target', 'month']].loc[
    df['year'] == year].groupby(['month']).mean()
with st.status("Grouping...",) as status:
    time.sleep(1)
    status.update(label="Complete!", state="complete")
st.bar_chart(gpd_df)

st.write(
    """
    ### Total target
    """
)
st.write(df['target'].value_counts())
color = st.color_picker('Pick A Color', '#00f900')
st.bar_chart(df['target'].value_counts(),
             color=color)

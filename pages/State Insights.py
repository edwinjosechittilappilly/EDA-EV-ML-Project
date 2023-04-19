import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

import os

os.listdir()
path = "./"
df = pd.read_pickle(path + 'combined_DataCleaned.pkl')



# df.describe()

# df.info()
# create a streamlit tab
import streamlit as st
import streamlit as st
width=1080
height=720

# st.write(df.head(10))

# pie chart of state counts
#     df_bodyStle=df["BodyStyle"].value_counts().rename_axis('BodyStyle').reset_index(name='counts')

df_state=df["State"].value_counts().rename_axis('State').reset_index(name='counts')
# plotly pie chart
import plotly.express as px
fig = px.pie(df_state, values='counts', names='State', title='State Counts')
fig.update_traces(pull=[0.1, 0, 0, 0])
fig.update_layout(
    autosize=False,width=width,height=height,
    font=dict(
        size=18,  # Set the font size here
    ))
fig.update_layout(legend=dict(font=dict(size= 20)))

st.plotly_chart(fig)

fig = px.choropleth(df_state,
                    locations='State',
                    color='counts',
                    color_continuous_scale='spectral_r',
                    hover_name='State',
                    locationmode='USA-states',
                    labels={'Number of Vehicles'},
                    scope='usa',title="State Counts")
fig.update_layout(
    autosize=False,width=width,height=height,
    font=dict(
        size=18,  # Set the font size here
    ))
fig.update_layout(legend=dict(font=dict(size= 20)))

st.plotly_chart(fig)


df_vehicleMake=df["Vehicle Make"].value_counts().rename_axis('Vehicle Make').reset_index(name='counts')

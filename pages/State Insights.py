import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

import plotly.express as px
import streamlit as st
import us

import os

os.listdir()
path = "./"
# df = pd.read_pickle(path + 'combined_DataCleaned.pkl')
df_state=pd.read_pickle(path + 'df_state.pkl')
# df_state["State"]=df_state["State"].apply(lambda x: us.states.lookup((x)).name)
df_VehicleMake=pd.read_pickle(path + 'df_VehicleMake.pkl')
df_state_VehicleMake=pd.read_pickle(path + 'df_state_VehicleMake.pkl')
df_StateMakeModel=pd.read_pickle(path + 'df_StateMakeModel.pkl')

# create a streamlit tab
tab1, tab2, tab3,tab4,tab5 = st.tabs(["Vehicle Population", " Brand and Model", "","",""])


# df.describe()

# df.info()
# create a streamlit tab

width=1080
height=720

# st.write(df.head(10))

# pie chart of state counts
#     df_bodyStle=df["BodyStyle"].value_counts().rename_axis('BodyStyle').reset_index(name='counts')

# df_state=df["State"].value_counts().rename_axis('State').reset_index(name='counts')
# plotly pie chart
with tab1:

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

    df_state["State"]=df_state["State"].apply(lambda x: us.states.lookup((x)).name)
    fig = px.pie(df_state, values='counts', names='State', title='State Counts')
    fig.update_traces(pull=[0.1, 0, 0, 0])
    fig.update_layout(
        autosize=False,width=width,height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    fig.update_layout(legend=dict(font=dict(size= 20)))

    st.plotly_chart(fig)

    df_state_VehicleMake=df_state_VehicleMake.sort_values(by=['counts'],ascending=False)
    df_state_VehicleMake["State"]=df_state_VehicleMake["State"].apply(lambda x: us.states.lookup((x)).name)
    fig = px.bar(df_state_VehicleMake, x="State", y="counts", color="Vehicle Make", title="Vehicle Make by State")

    fig.update_layout(
        autosize=False,width=width,height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    fig.update_layout(legend=dict(font=dict(size= 20)))
    st.plotly_chart(fig)

with tab2:
    state=st.selectbox('State',
                           df_StateMakeModel['State'].apply(lambda x: us.states.lookup((x)).name).unique(),
                           index=0)
    state=us.states.lookup(state).abbr
    df_selected=df_StateMakeModel[df_StateMakeModel['State']==state]
    fig = px.sunburst(df_selected, path=['State','Vehicle Make',"Vehicle Model"], values='counts')

    fig.update_layout(
        autosize=False,width=width,height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    fig.update_layout(legend=dict(font=dict(size= 20))) 
    st.plotly_chart(fig)

    # fig.show()

# df_vehicleMake=df["Vehicle Make"].value_counts().rename_axis('Vehicle Make').reset_index(name='counts')

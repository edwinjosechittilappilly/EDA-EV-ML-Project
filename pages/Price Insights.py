import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

import plotly.express as px
import streamlit as st
import us

import os

width = 1080
height = 720

os.listdir()
path = "./"
df = pd.read_csv(path + "FullData.csv")



StateVsLiving, StateVsEV, GasePrice, Combined = st.tabs(
    ["StateVsLiving", "StateVsEV", "GasPrice", "Combined"])

# plotl
import plotly.express as px

with StateVsLiving:
    # fig = px.scatter(df, x="CofE", y="CofL",title="CofE vs CofL")
    # st.plotly_chart(fig)

    # fig=px.bar(df.sort_values(by="CofL",ascending=False),x="States",y="CofL",title="Cost of Living by State")
    # fig.update_layout(
    #         autosize=False,width=width,height=height,
    #         font=dict(
    #             size=18,  # Set the font size here
    #         ))
    # st.plotly_chart(fig)
    fig = px.bar(df.sort_values(by="CofL", ascending=False),
                 x="States",
                 y="CofL",
                 title="Cost of Living Index by State")
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

    fig = px.bar(df.sort_values(by="GDP Per Capita", ascending=False),
                 x="States",
                 y="GDP Per Capita",
                 title="GDP Per Capita per State")
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

with StateVsEV:
    fig = px.bar(df.sort_values(by="CofE", ascending=False),
                 x="States",
                 y="CofE",
                 title="Cost of EV by State")
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

with GasePrice:
    fig = px.bar(df.sort_values(by="Avg Gas Price", ascending=False),
                 x="States",
                 y="Avg Gas Price",
                 title="Cost of EV by State")
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

with Combined:
    import plotly.graph_objects as go
    fig = go.Figure(data=[
        go.Bar(name='Avg Gas Price', x=df.States, y=df["Avg Gas Price"]),
        # go.Bar(name='Cost of EV', x=df.States, y=df["CofE"]),
        # go.Bar(name='GDP Per Capita', x=df.States, y=df["GDP Per Capita"]), 
        go.Bar(name='Cost of Living', x=df.States, y=df["CofL"]),
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    st.plotly_chart(fig)



st.title("Data")
st.write(df)
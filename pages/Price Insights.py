import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

import plotly.express as px
import streamlit as st
import us

import os
width=1080
height=720

os.listdir()
path = "./"
df=pd.read_csv(path+"FullData.csv")

st.write(df.head())

StateVsLiving,StateVsEV,Living=st.tabs(["StateVsLiving","StateVsEV","Living"])

# plotl
import plotly.express as px



with StateVsLiving:
    fig = px.scatter(df, x="CofE", y="CofL",title="CofE vs CofL")
    st.plotly_chart(fig)

    fig=px.bar(df.sort_values(by="CofL",ascending=False),x="States",y="CofL",title="Cost of Living by State")
    fig.update_layout(
            autosize=False,width=width,height=height,
            font=dict(
                size=18,  # Set the font size here
            ))
    st.plotly_chart(fig)
    fig=px.bar(df.sort_values(by="CofL",ascending=False),x="States",y="CofL",title="Cost of Living Index by State")
    fig.update_layout(
            autosize=False,width=width,height=height,
            font=dict(
                size=18,  # Set the font size here
            ))
    st.plotly_chart(fig)


with StateVsEV:
    fig=px.bar(df.sort_values(by="CofE",ascending=False),x="States",y="CofE",title="Cost of EV by State")
    fig.update_layout(
            autosize=False,width=width,height=height,
            font=dict(
                size=18,  # Set the font size here
            ))
    st.plotly_chart(fig)

# basic streamlit app to get values from user and display the most similar car
import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import pickle
# https://edwinjosechittilappilly-eda-ev-ml-project-app-7xuxar.streamlit.app/
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Electric Car Recommender System", page_icon="📈")

st.markdown("Electric Car Recommender System")
st.sidebar.header("Recommender System")


st.title('Electric Car Recommender System')

st.write(
    'This is a simple recommender system that recommends electric cars based on user input'
)
st.write('Please enter the following details of the car you are looking for')

# code to get user input from dropdown
# get the data
path = "./"
#read dataframe from pickle
print(os.listdir(path))
df = pd.read_pickle(path + "/df_sample.pkl")

# open the scaler dicktioonary file that is saved as pickle
with open(path + "/scaler.pkl", 'rb') as f:
    scaler = pickle.load(f)

# open the config dicktioonary file that is saved as pickle
with open(path + "/config.pkl", 'rb') as f:
    config = pickle.load(f)

print(config.keys())

cols = st.columns(4)
BrandNames = df['Brand'].unique()
Brand = st.selectbox('Brand',
                     np.append(["All"], df['Brand'].unique()),
                     index=0)

if Brand == "All":
    BrandCode = -1
else:
    BrandCode = config["Brand_dict"][Brand]
ModelNames = df['Model'].unique()
Model = st.selectbox('Model',
                     np.append(["All"], df['Model'].unique()),
                     index=0)

if Model == "All":
    ModelCode = -1
else:
    ModelCode = config["Model_dict"][Model]
BodyStyleNames = df['BodyStyle'].unique()
BodyStyle = st.selectbox('BodyStyle',
                            np.append(["All"], df['BodyStyle'].unique()),
                            index=0)

if BodyStyle == "All":
    BodyStyleCode = -1
else:
    BodyStyleCode = config["BodyStyle_dict"][BodyStyle]

with cols[0]:
    RapidChargeNames = df['RapidCharge'].unique()
    RapidCharge = st.selectbox('RapidCharge',
                               np.append(["All"], df['RapidCharge'].unique()),
                               index=0)

    if RapidCharge == "All":
        RapidChargeCode = -1
    else:
        RapidChargeCode = config["RapidCharge_dict"][RapidCharge]

    PowerTrainNames = df['PowerTrain'].unique()
    PowerTrain = st.selectbox('PowerTrain',
                              np.append(["All"], df['PowerTrain'].unique()),
                              index=0)

    if PowerTrain == "All":
        PowerTrainCode = -1
    else:
        PowerTrainCode = config["PowerTrain_dict"][PowerTrain]

with cols[1]:
    PlugTypeNames = df['PlugType'].unique()
    PlugType = st.selectbox('PlugType',
                            np.append(["All"], df['PlugType'].unique()),
                            index=0)

    if PlugType == "All":
        PlugTypeCode = -1
    else:
        PlugTypeCode = config["PlugType_dict"][PlugType]


    SegmentNames = df['Segment'].unique()
    Segment = st.selectbox('Segment',
                           np.append(["All"], df['Segment'].unique()),
                           index=0)

    if Segment == "All":
        SegmentCode = -1
    else:
        SegmentCode = config["Segment_dict"][Segment]

# 'AccelSec',
#  'TopSpeed_KmH',
#  'Range_Km',
#  'Efficiency_WhKm',
#  'FastCharge_KmH',
#  'Seats',
with cols[2]:
    AccelSec = st.slider('AccelSec', 0.0, df["AccelSec"].max())
    FastCharge_KmH = st.slider('FastCharge_KmH', 0,
                               int(df["FastCharge_KmH"].max()))


with cols[3]:
    Range_Km = st.slider('Range_Km', 0, int(df["Range_Km"].max()))
    Efficiency_WhKm = st.slider('Efficiency_WhKm', 0.0,
                                df["Efficiency_WhKm"].max())

PriceEuro = st.slider('PriceEuro', 0, int(df["PriceEuro"].max()))
Seats = st.slider('Seats', 0, int(df["Seats"].max()))
TopSpeed_KmH = st.slider('TopSpeed_KmH', 0, int(df["TopSpeed_KmH"].max()))

x_given = [
    AccelSec, TopSpeed_KmH, Range_Km, Efficiency_WhKm, FastCharge_KmH, Seats,
    BrandCode, RapidChargeCode, PowerTrainCode, PlugTypeCode, BodyStyleCode,
    SegmentCode, PriceEuro, ModelCode
]

x_given_scaled = scaler.transform([x_given])
# print(x_given_scaled)
x_df = df[[
    'AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm',
    'FastCharge_KmH', 'Seats', 'BrandCode', 'RapidChargeCode',
    'PowerTrainCode', 'PlugTypeCode', 'BodyStyleCode', 'SegmentCode',
    'PriceEuro', "ModelCode"
]]
x = x_df.values
x_scaled = scaler.transform(x)
# get the cosine similarity matrix
cosine_sim = cosine_similarity(x_scaled, x_given_scaled)

# print(cosine_sim)
df["score"] = cosine_sim
df_sorted = df.sort_values(by="score", ascending=False)
if Brand != "All":
    df_sorted = df_sorted[df_sorted["Brand"] == Brand]
if Model != "All":
    df_sorted = df_sorted[df_sorted["Model"] == Model]

df_sorted.head(10)

# display a dataframe with the top 10 cars
st.write(df_sorted.head(10))

# set deafult value for select box  in streamlit

# run streamlit app

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

import os

os.listdir()
path = "./"
df = pd.read_csv(path + '/datasets/evCarsData/ElectricCarData_Clean.csv')

# print(df.head())/

df.isnull().sum()

# df.describe()

# df.info()
# create a streamlit tab
import streamlit as st
import streamlit as st

tab1, tab2, tab3 = st.tabs(["HeatMap", "Brand", "Model"])
path = "./"
df = pd.read_pickle(path + "/df_sample.pkl")
width=1080
height=500,
with tab1:
    # path = "./"
    # df = pd.read_pickle(path + "/df_sample.pkl")
    import plotly.express as px
    df_new = df.select_dtypes(exclude=['object'])
    print(df_new.columns)
    df_new.drop(["score"], inplace=True, axis=1)

    fig = px.imshow(df_new.corr().round(2), text_auto=True, aspect="auto")
    fig.update_layout(
        autosize=True,
        width=1080,
        height=1080,
        font=dict(
            size=18,  # Set the font size here
        ))
    # fig.update_xaxes()
    st.plotly_chart(fig)

with tab2:
    a=np.arange(1,df['Brand'].value_counts()[0])
    print(a)
    new_df = df['Brand'].value_counts().rename_axis('Brand').reset_index(name='counts')
    fig = px.bar(new_df, x="Brand",y="counts",title="Frequency of models for Each Brand",text_auto=True)

    fig.update_layout(
        autosize=False,width=width,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

    df_speed = df[['Brand', 'TopSpeed_KmH']]
    df_grp=df_speed.groupby('Brand',as_index=False).max().sort_values("TopSpeed_KmH", axis=0, ascending=False)
    fig = px.bar(df_grp, x="Brand",y="TopSpeed_KmH",title='Top Speed achieved by a brand',text_auto=True)

    fig.update_layout(
        autosize=False,width=width,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

    df_range = df[['Brand', 'Range_Km']]
    df_grp=df_range.groupby('Brand',as_index=False).max().sort_values("Range_Km", axis=0, ascending=False)
    fig = px.bar(df_grp, x="Brand",y="Range_Km",title='Maximum Range achieved by a brand',text_auto=True)
    fig.update_layout(
        autosize=False,width=width,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

    df_Efficiency_WhKm = df[['Brand', 'Efficiency_WhKm']]
    df_grp=df_Efficiency_WhKm.groupby('Brand',as_index=False).max().sort_values("Efficiency_WhKm", axis=0, ascending=False)
    fig = px.bar(df_grp, x="Brand",y="Efficiency_WhKm",title='Efficiency achieved by a brand',text_auto=True)
    fig.update_layout(
        autosize=False,width=width,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

    df_seat = df[['Brand', 'Seats']]
    df_grp=df_seat.groupby('Brand',as_index=False).max().sort_values("Seats", axis=0, ascending=False)
    fig = px.bar(df_grp, x="Brand",y="Seats",title='Maximum Seats achieved by a brand',text_auto=True)
    fig.update_layout(
        autosize=False,width=width,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)

    df_price = df[['Brand', 'PriceEuro']]
    df_grp=df_price.groupby('Brand',as_index=False).max().sort_values("PriceEuro", axis=0, ascending=False)
    fig = px.bar(df_grp, x="Brand",y="PriceEuro",title='Maximum Price achieved by a brand in Euro',text_auto=True)
    fig.update_layout(
        autosize=False,width=width,
        font=dict(
            size=18,  # Set the font size here
        ))
    st.plotly_chart(fig)


# # df_new=df.copy()

# # %%
# # ax= plt.figure(figsize=(15,8))
# # sb.heatmap(df.corr(),linewidths=1,linecolor='white',annot=True)

# # %% [markdown]
# # **Frequency of the Brands in the dataset**

# # %%
# ax= plt.figure(figsize=(20,5))
# sb.barplot(x='Brand',y=a,data=df)
# plt.grid(axis='y')
# plt.title('Brands in the datset')
# plt.xlabel('Brand')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45)

# # %% [markdown]
# # Byton , Fiat and smart are the prominent brands and Polestar being the least

# # %% [markdown]
# # **Top speeds achieved by the cars of a brand**

# # %%
# ax= plt.figure(figsize=(20,5))
# sb.barplot(x='Brand',y='TopSpeed_KmH',data=df,palette='Paired')
# plt.grid(axis='y')
# plt.title('Top Speed achieved by a brand')
# plt.xlabel('Brand')
# plt.ylabel('Top Speed')
# plt.xticks(rotation=45)

# # %% [markdown]
# # Porsche, Lucid and Tesla produce the fastest cars and Smart the lowest
# #
# #

# # %% [markdown]
# # **Range a car can achieve**

# # %%
# ax= plt.figure(figsize=(20,5))
# sb.barplot(x='Brand',y='Range_Km',data=df,palette='tab10')
# plt.grid(axis='y')
# plt.title('Maximum Range achieved by a brand')
# plt.xlabel('Brand')
# plt.ylabel('Range')
# plt.xticks(rotation=45)

# # %% [markdown]
# # Lucid, Lightyear and Tesla have the highest range and Smart the lowest
# #

# # %% [markdown]
# # **Car efficiency**

# # %%
# ax= plt.figure(figsize=(20,5))
# sb.barplot(x='Brand',y='Efficiency_WhKm',data=df,palette='hls')
# plt.grid(axis='y')
# plt.title('Efficiency achieved by a brand')
# plt.xlabel('Brand')
# plt.ylabel('Efficiency')
# plt.xticks(rotation=45)

# # %% [markdown]
# # Byton , Jaguar and Audi are the most efficient and Lightyear the least

# # %% [markdown]
# # **Number of seats in each car**

# # %%
# ax= plt.figure(figsize=(20,5))
# sb.barplot(x='Brand',y='Seats',data=df,palette='husl')
# plt.grid(axis='y')
# plt.title('Seats in a car')
# plt.xlabel('Brand')
# plt.ylabel('Seats')
# plt.xticks(rotation=45)

# # %% [markdown]
# # Mercedes, Tesla and Nissan have the highest number of seats and Smart the lowest

# # %% [markdown]
# # **Price of cars (in Euro)**

# # %%
# ax= plt.figure(figsize=(20,5))
# sb.barplot(x='Brand',y='PriceEuro',data=df,palette='Set2')
# plt.title('Price of a Car')
# plt.xlabel('Price in Euro')
# plt.grid(axis='y')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45)

# # %% [markdown]
# # Lightyear, Porsche and Lucid are the most expensive and SEAT and Smart the least

# # %% [markdown]
# # **Type of Plug used for charging**

# # %%
# df['PlugType'].value_counts().plot.pie(figsize=(8,15),autopct='%.0f%%',explode=(.1,.1,.1,.1))
# plt.title('Plug Type')

# # %% [markdown]
# # Most companies use Type 2 CCS and Type 1 CHAdeMo the least

# # %% [markdown]
# # **Cars and their body style**

# # %%
# df['BodyStyle'].value_counts().plot.pie(figsize=(8,15),autopct='%.0f%%',explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1))
# plt.title('Body Style')

# # %% [markdown]
# # Most cars are eiher SUV or Hatchback

# # %% [markdown]
# # **Segment in which the cars fall under**

# # %%
# df['Segment'].value_counts().plot.pie(figsize=(8,15),autopct='%.0f%%',explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1))
# plt.title('Segment')

# # %% [markdown]
# # Most cars are either C or B type
# #

# # %% [markdown]
# # **Number of Seats**

# # %%
# df['Seats'].value_counts().plot.pie(figsize=(8,15),autopct='%.0f%%',explode=(0.1,0.1,0.1,0.1,0.1))
# plt.title('Seats')

# # %% [markdown]
# # Majority of cars have 5 seats

# # %% [markdown]
# # **Putting independent variables as x and dependent variable as y**

# # %%
# x=df[['AccelSec','Range_Km','TopSpeed_KmH','Efficiency_WhKm']]
# y=df['PriceEuro']

# # %% [markdown]
# # **Finding out the linear regression using OLS method**

# # %%
# x= sm.add_constant(x)
# results = sm.OLS(y,x)

# # %% [markdown]
# # **Fitting the model and summarizing**

# # %%
# model=results.fit()
# model.summary()

# # %% [markdown]
# # Only Top Speed and Efficieny are the two variables related to price

# # %% [markdown]
# # **Importing train test split from Scikit Learn**

# # %%
# from sklearn.model_selection import train_test_split

# # %%
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=365)

# # %% [markdown]
# # **Importing Linear regression**

# # %%
# from sklearn.linear_model import LinearRegression
# lr= LinearRegression()

# # %%
# lr.fit(X_train, y_train)
# pred = lr.predict(X_test)

# # %% [markdown]
# # **Finding out the R-squared value**

# # %%
# from sklearn.metrics import r2_score
# r2=(r2_score(y_test,pred))
# print(r2*100)

# # %% [markdown]
# # Around 78% of the dependant variable has been explained by the independant variables

# # %% [markdown]
# # **Putting Yes value as 1 and No value as 0 for Logistic Regression**

# # %%
# df['RapidCharge'].replace(to_replace=['No','Yes'],value=[0, 1],inplace=True)

# # %%
# y1=df[['RapidCharge']]
# x1=df[['PriceEuro']]

# # %%
# from sklearn.model_selection import train_test_split
# X1_train, X1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.2,random_state=365)

# # %% [markdown]
# # **Importing Logistic Regression**

# # %%
# from sklearn.linear_model import LogisticRegression

# # %%
# log= LogisticRegression()

# # %%
# log.fit(X1_train, y1_train)
# pred1 = log.predict(X1_test)
# pred1

# # %% [markdown]
# # **Confusion Matrix of the regression**

# # %%
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y1_test, pred1)
# cm

# # %% [markdown]
# # **Finding out the accuracy score**

# # %%
# from sklearn.metrics import accuracy_score
# score=accuracy_score(y1_test,pred1)
# score*100

# # %% [markdown]
# # The data is accurate upto 95%

import streamlit as st 
from matplotlib import image
import pandas as pd
import plotly.express as px
import os 

# absolute path to this file 
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absloute path to this files root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absloute path to the directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "Image","titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data2","titanic.csv")


st.title("Dashboard - Titanic Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Alive = st.selectbox("Select the surviours :",df['alive'].unique())
col1,col2 = st.columns(2)

fig_1 = px.histogram(df[df['alive'] == Alive],x="who")
col1.plotly_chart(fig_1, use_container_width = True)

fig_2 = px.box(df[df['alive'] == Alive],y="who")
col2.plotly_chart(fig_2, use_container_width = True)
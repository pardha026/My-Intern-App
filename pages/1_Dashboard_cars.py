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

IMAGE_PATH = os.path.join(dir_of_interest, "Image","car.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data2","car_data.csv")

st.title("Dashboard - [cars] Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.subheader(":blue[Car Data]")
st.dataframe(df)

brand = st.selectbox("Select the Brand :",df['make'].unique())
col1,col2 = st.columns(2)

fig_1 = px.histogram(df[df['make'] == brand],x="body_style")
col1.plotly_chart(fig_1, use_container_width = True)

fig_2 = px.box(df[df['make'] == brand],y="body_style")
col2.plotly_chart(fig_2, use_container_width = True)
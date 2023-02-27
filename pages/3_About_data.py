import streamlit as st
import pandas as pd

df=pd.read_csv('resources/data2/car_data.csv')

st.subheader("Information about the :red[cars] data set")
option = st.radio("",('Head','Tail','check null values','shape'))


if option == 'Head':
    st.markdown('**Head of the dataframe**')
    st.dataframe(df.head())
elif option == 'Tail':
    st.markdown('**Tail of the dataframe**')
    st.dataframe(df.tail())
elif option == 'shape':
    st.text('Number of rows: {}'.format(df.shape[0]))
    st.text('Number of Columns: {}'.format(df.shape[1]))
elif option == 'check null values':
    st.markdown('**As we can see that there is no null values in dataset**')
    st.text(df.isna().sum())
elif option == 'info':
    st.markdown('**Information of data frame**')
    st.text(df.info())
# elif option =='describe':
st.subheader('Statistical Information')

btn_click = st.button('Describe')

if btn_click == True:
    st.dataframe(df.describe())
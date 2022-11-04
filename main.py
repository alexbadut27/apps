import streamlit as st
import pandas as pd
from pathlib import Path

data_ship = Path(__file__).parents[1] / 'data\ship_data.csv'
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.markdown("<h1 style='text-align: center; color: Green;'>Ships tracker around the globe</h1>",
                unsafe_allow_html=True)
    # allign the title and make it how i wanted
    st.markdown("<h2 style='text-align: center; color: black;'>Aerospace team </h2>", unsafe_allow_html=True)
    st.text('Using this app we can see the shipments that are going in real time across the GLOBE')
with dataset:
    st.header('Port data across the globe')
    st.text('The data has been provided by the local carriers')

    st.write(data_ship.head())
    number_one = pd.DataFrame(data_ship['Country'].value_counts())
    st.text('The most used country')
    st.bar_chart(number_one)


with features:
    st.header('Aici as vrea sa pun ceva ML')
    st.markdown('* **Daca am reusit** Bem o bere de fericire')
    st.markdown('* **Daca nu am reusit** Tot bem o bere')
    st.map()


with model_training:
    st.header('Aici am vrut sa fac un buton')
    if st.button('Apasa-ma'):

        st.write('Sugi pula')  # displayed when the button is clicked

    else:

        st.write('un mic cadou')  # displayed when the button is unclicked

sel_col, disp_col = st.columns(2)
max_depth = sel_col.slider('Da si mie o nota',min_value=1,max_value=5,value=1)



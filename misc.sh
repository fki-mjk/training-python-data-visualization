#!/bin/bash

pip install streamlit

streamlit run app.py



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Error Log")

# Sidebar - Filter Jenis Error
with st.sidebar:
    st.header("Filter")
    pilihan_jenis_error = st.multiselect(
        'Filter Jenis Error:',
        df['Jenis Error'].unique(),
        df['Jenis Error'].unique()
    )

# Membaca data
df = pd.read_csv('data/error_log_updated.csv')

# Filter DataFrame
if pilihan_jenis_error:
    df_filtered = df[df['Jenis Error'].isin(pilihan_jenis_error)]
else:
    df_filtered = df

# Menampilkan DataFrame
st.dataframe(df_filtered)

# Bar chart frekuensi jenis error
st.bar_chart(df_filtered['Jenis Error'].value_counts())

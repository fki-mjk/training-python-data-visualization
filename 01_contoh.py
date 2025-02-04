import streamlit as st
import pandas as pd

# Baca data error log
df = pd.read_csv('data/error_log_updated.csv')

# Tampilkan 5 baris pertama data
st.write(df.head())



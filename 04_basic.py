import streamlit as st
import pandas as pd

st.title("Analisis Error Log")
st.header("Data Error Log")

df = pd.read_csv('data/error_log_updated.csv')

st.write("Halo, ini aplikasi Streamlit pertamaku!")
st.write(df.head())


nama_user = st.text_input("Masukkan nama Anda:")

if (nama_user == "Trisna") :
    st.write("Selamat datang Pak Trisna")


if st.button("Klik aku!"):
    st.write("Tombol diklik!")

nilai = st.slider("Pilih nilai:", 0, 100, 50)  # Nilai awal 50

st.dataframe(df)

st.line_chart(df['Response Time (ms)'])
st.bar_chart(df['Jenis Error'].value_counts())

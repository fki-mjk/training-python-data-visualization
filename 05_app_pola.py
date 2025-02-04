import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Membaca Data ---
df = pd.read_csv('data/error_log_updated.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# --- Judul Aplikasi ---
st.title("Pola Error")

# --- 1. Visualisasi Jumlah Error per Jam ---

st.header("Jumlah Error per Jam")
error_per_jam = df.set_index('Timestamp').resample('H').size()
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(error_per_jam.index, error_per_jam.values)
plt.xlabel("Waktu")
plt.ylabel("Jumlah Error")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# --- 2. Visualisasi Jumlah Error per Hari dalam Seminggu ---

st.header("Jumlah Error per Hari dalam Seminggu")
error_per_hari = df.groupby(df['Timestamp'].dt.day_name()).size()
fig, ax = plt.subplots()
ax.bar(error_per_hari.index, error_per_hari.values)
plt.xlabel("Hari")
plt.ylabel("Jumlah Error")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# --- 3. Tabel Jumlah Error per Jam ---

st.header("Tabel Jumlah Error per Jam")
st.write(error_per_jam.to_frame(name='Jumlah Error'))

# --- 4. Tabel Jumlah Error per Hari ---

st.header("Tabel Jumlah Error per Hari")
st.write(error_per_hari.to_frame(name='Jumlah Error'))
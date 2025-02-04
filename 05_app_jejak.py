import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Membaca Data ---
df = pd.read_csv('data/error_log_updated.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# --- Judul Aplikasi ---
st.title("Jejak Error")

# --- 1. Input User ID ---

user_id = st.text_input("Masukkan User ID:")

# --- 2. Menampilkan Error Log User ---

if user_id:
    user_errors = df[df['User ID'] == user_id].sort_values('Timestamp')
    if len(user_errors) > 0:
        st.subheader(f"Error Log untuk User {user_id}")
        st.dataframe(user_errors)

        # --- a. Visualisasi Timeline Error ---
        st.subheader("Timeline Error")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(user_errors['Timestamp'], user_errors['Jenis Error'], marker='o')
        plt.xlabel("Waktu")
        plt.ylabel("Jenis Error")
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

        # --- b. Informasi Tambahan ---
        st.subheader("Informasi Tambahan")
        st.write(f"Browser/User Agent: {user_errors['Browser/User Agent'].iloc}")
        st.write(f"Sistem Operasi: {user_errors['Sistem Operasi'].iloc}")
        st.write(f"Lokasi: {user_errors['Lokasi'].iloc}")
    else:
        st.write(f"Tidak ada error log ditemukan untuk User ID {user_id}")
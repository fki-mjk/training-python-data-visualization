import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Membaca Data ---
df = pd.read_csv('data/error_log_updated.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# --- Judul Aplikasi ---
st.title("Analisis Error Log")

# --- Sidebar - Pilihan Halaman ---
page = st.sidebar.selectbox("Pilih Halaman", ["Visualisasi 1", "Visualisasi 2", "Visualisasi 3"])

# --- Conditional Rendering ---
if page == "Visualisasi 1":
    st.header("Visualisasi 1: Frekuensi Jenis Error")
    jenis_error_counts = df['Jenis Error'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(jenis_error_counts.index, jenis_error_counts.values)
    plt.xlabel("Jenis Error")
    plt.ylabel("Frekuensi")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

elif page == "Visualisasi 2":
    st.header("Visualisasi 2: Response Time vs. CPU Usage")
    fig, ax = plt.subplots()
    ax.scatter(df['Response Time (ms)'], df['CPU Usage (%)'])
    plt.xlabel("Response Time (ms)")
    plt.ylabel("CPU Usage (%)")
    st.pyplot(fig)

elif page == "Visualisasi 3":
    st.header("Visualisasi 3: Network Latency per Platform")
    fig, ax = plt.subplots()
    sns.boxplot(x='Platform', y='Network Latency (ms)', data=df, ax=ax)
    st.pyplot(fig)

# --- (Tambahkan kode untuk visualisasi lainnya) ---

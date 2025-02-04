import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Membaca Data ---
df = pd.read_csv('data/error_log_updated.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# --- Judul Aplikasi ---
st.title("Dashboard Detektif Error")

# --- 1. Ringkasan Statistik ---

st.header("Ringkasan Statistik")

# --- a. Jumlah total error ---
total_errors = len(df['Timestamp'])
st.metric("Jumlah Total Error", total_errors)

# --- b. Jenis error terbanyak ---
top_error_type = df['Jenis Error'].value_counts().index
st.metric("Jenis Error Terbanyak", top_error_type[0])

# --- c. Platform yang paling terdampak ---
most_affected_platform = df['Platform'].value_counts().index
st.metric("Platform Terdampak", most_affected_platform[0])

# --- d. Severity level yang paling sering muncul ---
most_frequent_severity = df['Severity Level'].value_counts().index
st.metric("Severity Level Terbanyak", most_frequent_severity[0])

# --- e. Visualisasi ringkasan ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribusi Jenis Error")
    fig, ax = plt.subplots()
    df['Jenis Error'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Distribusi Platform")
    fig, ax = plt.subplots()
    df['Platform'].value_counts().plot(kind='bar', ax=ax)
    plt.xlabel("Platform")
    plt.ylabel("Jumlah Error")
    st.pyplot(fig)

# --- 2. Sidebar dengan Filter ---

st.sidebar.header("Filter")

# --- a. Filter Jenis Error ---
pilihan_jenis_error = st.sidebar.multiselect(
    'Filter Jenis Error:',
    df['Jenis Error'].unique(),
    df['Jenis Error'].unique()
)

# --- b. Filter Platform ---
pilihan_platform = st.sidebar.multiselect(
    'Filter Platform:',
    df['Platform'].unique(),
    df['Platform'].unique()
)

# --- c. Filter Severity Level ---
pilihan_severity = st.sidebar.multiselect(
    'Filter Severity Level:',
    df['Severity Level'].unique(),
    df['Severity Level'].unique()
)

# --- d. Filter Rentang Waktu ---
min_timestamp = df['Timestamp'].min().timestamp()  # Konversi ke unix timestamp
max_timestamp = df['Timestamp'].max().timestamp()  # Konversi ke unix timestamp
start_time, end_time = st.sidebar.slider(
    "Pilih Rentang Waktu:",
    min_value=min_timestamp,
    max_value=max_timestamp,
    value=(min_timestamp, max_timestamp)
)

# --- 3. Filtering Data ---

# Filter DataFrame berdasarkan pilihan di sidebar
filtered_df = df.copy()
if pilihan_jenis_error:
    filtered_df = filtered_df[filtered_df['Jenis Error'].isin(pilihan_jenis_error)]
if pilihan_platform:
    filtered_df = filtered_df[filtered_df['Platform'].isin(pilihan_platform)]
if pilihan_severity:
    filtered_df = filtered_df[filtered_df['Severity Level'].isin(pilihan_severity)]

# Konversi kolom 'Timestamp' ke unix timestamp
filtered_df['Timestamp Unix'] = filtered_df['Timestamp'].apply(lambda x: x.timestamp())

# Filter DataFrame
filtered_df = filtered_df[
    (filtered_df['Timestamp Unix'] >= start_time) & (filtered_df['Timestamp Unix'] <= end_time)
]

# Hapus kolom 'Timestamp Unix' jika tidak diperlukan lagi
filtered_df = filtered_df.drop(columns=['Timestamp Unix'])

# --- 4. Menampilkan Data ---
st.header("Data Error Log")
st.dataframe(filtered_df)
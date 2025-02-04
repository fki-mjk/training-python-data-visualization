import pandas as pd

df = pd.read_csv('data/error_log_updated.csv')

# Mengubah kolom 'Timestamp' ke tipe data datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Menghapus baris dengan nilai null (jika ada)
df.dropna(inplace=True)

#... (tambahkan kode pembersihan data lainnya jika diperlukan)

jenis_error_counts = df['Jenis Error'].value_counts()
print(jenis_error_counts)

import matplotlib.pyplot as plt

plt.bar(jenis_error_counts.index, jenis_error_counts.values)
plt.xlabel("Jenis Error")
plt.ylabel("Frekuensi")
plt.xticks(rotation=45, ha='right')
plt.show()


# Grouping data berdasarkan jam
error_per_jam = df.groupby(df['Timestamp'].dt.hour).size()
print(error_per_jam)

# Visualisasi dengan line chart
plt.plot(error_per_jam.index, error_per_jam.values)
plt.xlabel("Jam")
plt.ylabel("Jumlah Error")
plt.show()


# Crosstab antara Jenis Error dan Platform
crosstab = pd.crosstab(df['Jenis Error'], df['Platform'])
print(crosstab)

rata_rata_response_time = df.groupby('Jenis Error')['Response Time (ms)'].mean()
print(rata_rata_response_time)

import seaborn as sns

sns.boxplot(x='Jenis Error', y='Response Time (ms)', data=df)
plt.show()


correlation = df['Response Time (ms)'].corr(df['CPU Usage (%)'])
print(f"Korelasi: {correlation}")

# Visualisasi dengan scatter plot
plt.scatter(df['Response Time (ms)'], df['CPU Usage (%)'])
plt.xlabel("Response Time (ms)")
plt.ylabel("CPU Usage (%)")
plt.show()



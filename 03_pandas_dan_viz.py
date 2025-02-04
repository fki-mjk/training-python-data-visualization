import pandas as pd

df = pd.read_csv('data/error_log_updated.csv')

jenis_error = df['Jenis Error']  # Mengambil kolom 'Jenis Error'
response_time = df['Response Time (ms)']  # Mengambil kolom 'Response Time (ms)'

print(df.head().to_markdown(index=False, numalign="left", stralign="left"))  # 5 baris pertama
print(df.tail(10).to_markdown(index=False, numalign="left", stralign="left"))  # 10 baris terakhir

print(df.info())

print(df.describe().to_markdown(numalign="left", stralign="left"))

high_cpu_usage = df[df['CPU Usage (%)'] > 80]  # Memilih data dengan CPU Usage di atas 80%

sorted_df = df.sort_values('Response Time (ms)')  # Mengurutkan berdasarkan Response Time (ascending)

error_per_platform = df.groupby('Platform').size()  # Menghitung jumlah error per platform


import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart frekuensi jenis error dengan Matplotlib
jenis_error_counts = df['Jenis Error'].value_counts()
plt.bar(jenis_error_counts.index, jenis_error_counts.values)
plt.xlabel("Jenis Error")
plt.ylabel("Frekuensi")
plt.xticks(rotation=45, ha='right')
plt.show()

# Scatter plot Response Time vs. CPU Usage dengan Seaborn
sns.scatterplot(x='Response Time (ms)', y='CPU Usage (%)', data=df)
plt.show()


plt.grid(True)  # Menambahkan grid
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.show()


fig, axes = plt.subplots(nrows=2, ncols=2)  # Membuat 2x2 grafik

# axes.plot(...)  # Menambahkan plot ke grafik pertama
# axes.scatter(...)  # Menambahkan scatter plot ke grafik kedua
#...


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Baca data
df = pd.read_csv('error_log_updated.csv')

# Membuat 2x1 grafik
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Bar chart frekuensi jenis error
jenis_error_counts = df['Jenis Error'].value_counts()
axes.bar(jenis_error_counts.index, jenis_error_counts.values)
axes.set_xlabel("Jenis Error")
axes.set_ylabel("Frekuensi")
axes.tick_params(axis='x', rotation=45, ha='right')
axes.grid(True)

# Scatter plot Response Time vs. CPU Usage
axes.scatter(df['Response Time (ms)'], df['CPU Usage (%)'])
axes.set_xlabel("Response Time (ms)")
axes.set_ylabel("CPU Usage (%)")
axes.grid(True)

plt.tight_layout()  # Mengatur jarak antar grafik
plt.show()

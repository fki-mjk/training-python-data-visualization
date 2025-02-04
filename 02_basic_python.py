response_time = 2000  # int, contoh nilai dari kolom 'Response Time (ms)'
cpu_usage = 85.5  # float, contoh nilai dari kolom 'CPU Usage (%)'
jenis_error = "NullPointerException"  # str, contoh nilai dari kolom 'Jenis Error'
user_id = "user456"  # str, contoh nilai dari kolom 'User ID'
lokasi = "Jakarta"  # str, contoh nilai dari kolom 'Lokasi'


total_response_time = response_time * 2
is_high_cpu_usage = cpu_usage > 90


jenis_error_list = ["Connection Error", "NullPointerException", "InvalidInputException"]
error_info = {"Jenis Error": "Connection Error", "Response Time": 1500, "CPU Usage": 60.2}

if cpu_usage > 80:
    print("CPU usage tinggi!")
else:
    print("CPU usage normal.")

for jenis in jenis_error_list:
    print(jenis)

def hitung_rata_rata_response_time(jenis_error):
  """
  Fungsi ini menghitung rata-rata response time 
  untuk jenis error tertentu.
  """
  data_error = df[df['Jenis Error'] == jenis_error]
  rata_rata = data_error['Response Time (ms)'].mean()
  return rata_rata

# Memanggil fungsi
rata_rata_connection_error = hitung_rata_rata_response_time('Connection Error')
print(rata_rata_connection_error)

# Mengubah kolom 'Severity Level' menjadi numerik (1-6)
severity_level_mapping = {'Debug': 1, 'Info': 2, 'Warning': 3, 'Error': 4, 'Critical': 5, 'Fatal': 6}
df['Severity Level Numeric'] = df['Severity Level'].apply(lambda x: severity_level_mapping[x])
print(df[['Severity Level', 'Severity Level Numeric']].head())


class ErrorLog:
  def __init__(self, timestamp, jenis_error, response_time):
    self.timestamp = timestamp
    self.jenis_error = jenis_error
    self.response_time = response_time

  def is_critical(self):
    return self.response_time > 3000

# Membuat objek
error1 = ErrorLog("2024-01-01 00:00:00", "Connection Error", 2500)

# Mengakses atribut
print(error1.jenis_error)  # Output: Connection Error

# Memanggil method
print(error1.is_critical())  # Output: False


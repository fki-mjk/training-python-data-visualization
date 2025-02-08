# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


import pandas as pd

# File Path
file_path = '/kaggle/input/home-data-for-ml-course'
train_path = '/train.csv'
test_path = '/test.csv'

df_train = pd.read_csv(file_path+train_path)
df_test = pd.read_csv(file_path+train_path)


# Memeriksa tipe data dan nilai yang hilang
df_train.info()

# Deskripsi statistik dari dataset
df_train.describe()


df_train_impute = df_train.copy()

# Menghapus kolom yang tidak diperlukan
df_train_impute.drop(columns=['Id'], inplace=True)

# Mengisi nilai yang hilang dengan median
num = df_train_impute.select_dtypes('number').columns
cat = df_train_impute.select_dtypes('object').columns
for col in num:
    df_train_impute[col] = df_train_impute[col].fillna(value=df_train[col].median())
    
for col in cat:
    df_train_impute[col] = df_train_impute[col].fillna(value=df_train[col].mode()[0])


df_train_impute = df_train.copy()

# Menghapus kolom yang tidak diperlukan
df_train_impute.drop(columns=['Id'], inplace=True)

num = df_train_impute.select_dtypes('number').columns
cat = df_train_impute.select_dtypes('object').columns

for col in num:
    df_train_impute[col] = df_train_impute[col].fillna(value=df_train[col].median())

for col in cat:
    df_train_impute[col] = df_train_impute[col].fillna(value=df_train[col].mode()[0])

from sklearn.preprocessing import OrdinalEncoder

df_train_impute_encode = df_train_impute.copy()
# Inisialisasi OrdinalEncoder dengan urutan kategori
encoder = OrdinalEncoder()

# Terapkan encoding
encoded_data = encoder.fit_transform(df_train_impute_encode.select_dtypes('object'))

df_train_impute_encode[df_train_impute_encode.select_dtypes('object').columns] = encoded_data 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Memisahkan data menjadi fitur dan target
X = df_train_impute_encode.drop(columns=['SalePrice'])
y = df_train_impute_encode ['SalePrice']

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

import matplotlib.pyplot as plt

# Visualisasi hasil prediksi vs nilai aktual
plt.scatter(y_test, y_pred)
plt.xlabel('Aktual Prices')
plt.ylabel('Predicted Prices')
plt.title('Predicted vs Actual House Prices')
plt.show()

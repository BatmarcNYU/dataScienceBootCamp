import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered = df.iloc[::20, :].loc[:, ['Manufacturer', 'Model', 'Type']]


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
df[df.sum(axis=1) > 100]

arr = np.random.randint(1, 100, (4, 4))
rows_array = arr.reshape(2, -1)
cols_array = arr.T.reshape(2, -1)
sum_row = lambda x: np.sum(x, axis=1)
sum_col = lambda x: np.sum(x, axis=0)
sum_rows_result = sum_row(rows_array)
sum_cols_result = sum_col(cols_array)
print("Question 4 Result:")
print("Rows sum:")
print(sum_rows_result)
print("Columns sum:")
print(sum_cols_result)

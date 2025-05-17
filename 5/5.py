import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = {'Колір': ['Червоний', 'Зелений', 'Синій', 'Зелений', 'Червоний'],
        'Розмір': ['S', 'M', 'L', 'M', 'XL']}
df = pd.DataFrame(data)

print("Оригінальні дані:")
print(df)

le = LabelEncoder()
df['Колір_label'] = le.fit_transform(df['Колір'])
df['Розмір_label'] = le.fit_transform(df['Розмір'])

print("\nДані після Label Encoding:")
print(df)

ohe = OneHotEncoder(sparse_output=False)
one_hot_encoded = ohe.fit_transform(df[['Колір', 'Розмір']])
columns = ohe.get_feature_names_out(['Колір', 'Розмір'])

df_ohe = pd.DataFrame(one_hot_encoded, columns=columns)
print("\nДані після One-Hot Encoding:")
print(df_ohe)

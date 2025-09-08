import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David','baran'],
    'Age': [24, 27, 22, 32,18],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston','tehran']
})
print(df['Age'])
print(df.loc[1])
print(df.iloc[2:4])
print(df.head()) 
print(df.tail())
print(df['Age'])
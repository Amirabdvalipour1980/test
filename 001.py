import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
print('kids:')
print(df[df['Age'] > 50][['Name', 'Age']])
print('tedad: ', df[df['Age'] > 50].count())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
print(df[df['variety'] == "Setosa"][['petal.length']].mean())
print(df[df['variety'] == "Versicolor"][['petal.length']].mean())
print(df[df['variety'] == "Virginica"][['petal.length']].mean())
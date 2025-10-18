from sklearn.model_selection import train_test_split
import pandas as pd

titanic = pd.read_csv('Olympic_Swimming_Results_1912to2020.csv')
x = titanic['Year']
y = titanic['Rank']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(X_train)
print(X_test)
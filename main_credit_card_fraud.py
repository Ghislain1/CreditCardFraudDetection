import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import (
    train_test_split,
)  # hir wollte training und testdaten
from sklearn.metrics import accuracy_score

## Daten aufbereiten
df = pd.read_csv("creditcard.csv")
# df1 = sns.load_dataset("creditcard.csv")
# print(df)

# sns.pairplot(data=df, hue="Class") # df visualisieren
df1 = df.isnull().sum()  # fehl date aufsummen
# print(df1)
df = df.drop(["Time", "Amount"], axis=1)
# print(df)


# Trainingsdaten und testdaten

X = df.drop(["Class"], axis=1)
y = df["Class"]
# z = df["Time"]

X_train, X_test, y_train, y_test, Allo_x, Allo_y = train_test_split(
    X, y, df, test_size=0.2, random_state=42
)

for _ in range(1, 1):
    #
    clf = KNeighborsClassifier(n_neighbors=3)  # claissifier initialisiert
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)  # vorhersage aus dem testdate

    accuracy = accuracy_score(y_test, predictions)

    #
    print(accuracy)

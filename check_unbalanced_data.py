import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from check_data import CheckData


class Check_Unbalanced_Data:
    '''überprüfen die unausgewogenen Daten oder unbalanced Data mit Betrachtung der unveränderten Daten wie Time, Class(1-> fraud, 0-> no_fraud), Amount'''

    def __init__(self, data_df):
        self.data_df = data_df

    def plot_class_distribution(self):
        Labels = ["No Fraud", "Fraud"]
        # zählen die Häufigkeit der Klassen
        zeahlen_classes = pd.value_counts(self.data_df['Class'], sort=True)
        # Erstellen ein Balkendiagramm
        zeahlen_classes.plot(kind='bar', rot=0)
        plt.title("Transaction Class Distribution")
        plt.xticks(range(2), Labels)
        plt.xlabel("Class")
        plt.ylabel("Frequency")
        plt.show()

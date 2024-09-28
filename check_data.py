import pandas as pd


class CheckData:
    def __init__(self, data_df=None):
        if data_df is None:
            self.data_df = pd.read_csv("creditcard.csv")
        else:
            self.data_df = data_df

    def see_first_5_row(self):
        '''Erste 5 Zeile des DataFrame oder Dataset anzeigen'''
        return self.data_df.head()

    def see_last_5_row(self):
        '''letzte 5 Zeile des DataFrame oder Dataset anzeigen'''
        return self.data_df.tail()

    def look_inside(self):
        '''Beschreibung des DataFrames enzeigen durch Anzahl,AVG,prozent'''
        return self.data_df.describe()

    def check_missing_data(self):
        '''überprüfen die fehlende Daten'''
        summ = self.data_df.isnull().sum()
        zeahlen = self.data_df.isnull().count()  # or len(self.data_df)
        percent = summ / zeahlen * 100
        assembly = pd.concat(
            objs=[
                summ, percent], axis=1, keys=[
                'summ', 'percent'])
        return assembly.transpose()

    def show_class_column(self):
        '''Darstellung der Spalte Klasse'''
        return self.data_df["Class"].value_counts()

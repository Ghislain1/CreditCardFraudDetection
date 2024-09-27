import pandas as pd
class CheckData:
    def __init__(self, data_df = None):
        if data_df is None:
            self.data_df = pd.read_csv("/home/marco/VSCode/creditcard.csv")
        else:
            self.data_df = data_df
        
    '''Erste 5 Zeile des DataFrame oder Dataset anzeigen'''
    def see_first_5_row(self):
        return self.data_df.head()
    
    '''letzte 5 Zeile des DataFrame oder Dataset anzeigen'''
    def see_last_5_row(self):
        return self.data_df.tail()
    
    '''Beschreibung des DataFrames enzeigen durch Anzahl,AVG,prozent'''
    def look_inside(self):
        return self.data_df.describe()
    
    '''überprüfen die fehlende Daten'''
    def check_missing_data(self):
        summ = self.data_df.isnull().sum()
        zeahlen = self.data_df.isnull().count() # or len(self.data_df)
        percent = summ / zeahlen * 100
        assembly = pd.concat(objs=[summ,percent], axis=1, keys=['summ', 'percent'])
        return assembly.transpose()
import pandas as pd
from check_data import CheckData
from check_unbalanced_data import Check_Unbalanced_Data


class App:
    def __init__(self):
        self.check_data = CheckData()  # erstellen ein Objekt der CheckData-Klasse

    '''Auf der CheckData-Methode und Ausgabe der Ergebnisse'''

    def run(self):
        print("erste 5 Zeile:")
        print(self.check_data.see_first_5_row())

        print("letzte 5 Zeile:")
        print(self.check_data.see_last_5_row())

        print("\nBeschreibung der Daten:")
        print(self.check_data.look_inside())

        print("Überprüfung der fehlenden daten:")
        print(self.check_data.check_missing_data())

        '''Erstellen ein Objekt der Check_Unbalanced_Data und Aufruf der methode'''
        unbalanced_checker = Check_Unbalanced_Data(self.check_data.data_df)
        unbalanced_checker.plot_class_distribution()

        print(self.check_data.show_class_column())


'''Ausführung der App-Klasse'''
if __name__ == "__main__":
    app = App()  # Erstellung ein Main-Objekt
    app.run()  # Ausführung der main-Mathode

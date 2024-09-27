import pandas as pd
from check_data import CheckData
class App:
    def __init__(self):
        self.check_data = CheckData() # erstellen ein Objekt der CheckData-Klasse
    
    '''Auf der CheckData-Methode und Ausgabe der Ergebnisse'''
    def main(self):
        print("erste 5 Zeile:")
        print(self.check_data.see_first_5_row())
        
        print("letzte 5 Zeile:")
        print(self.check_data.see_last_5_row())
        
        print("\nBeschreibung der Daten:")
        print(self.check_data.look_inside())
        
        print("Überprüfung der fehlenden daten:")
        print(self.check_data.check_missing_data())
'''Ausführung der App-Klasse'''
if __name__ == "__main__":
    main = App() # Erstellung ein Main-Objekt
    main.main() # Ausführung der main-Mathode
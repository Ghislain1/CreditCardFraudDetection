from check_data import CheckData
from check_unbalanced_data import Check_Unbalanced_Data
from credit_card import CreditCard
from prediction import Prediction


class App:
    def __init__(self):
        self.check_data = CheckData()  # erstellen ein Objekt der CheckData-Klasse

    """Auf der CheckData-Methode und Ausgabe der Ergebnisse"""

    def run(self):
        print("erste 5 Zeile:")
        print(self.check_data.see_first_5_row())

        print("letzte 5 Zeile:")
        print(self.check_data.see_last_5_row())

        print("\nBeschreibung der Daten:")
        print(self.check_data.look_inside())

        print("Überprüfung der fehlenden daten:")
        print(self.check_data.check_missing_data())

        """Erstellen ein Objekt der Check_Unbalanced_Data und Aufruf der methode"""
        unbalanced_checker = Check_Unbalanced_Data(self.check_data.data_df)
        unbalanced_checker.plot_class_distribution()

        print(self.check_data.show_class_column())

    def call_prediction(self):
        prediction = Prediction()
        prediction.run()

    def use_credit_card_class(self):
        credit_card = CreditCard()
        # print(credit_card.see_first_5_row())
        credit_card.clean_data()

        # print(credit_card.split_data_Xy())
        predictions = credit_card.make_predictions()
        print(predictions)

        # Print many scores
        print("\nPrints Scores: ")
        # for _ in range(1, 10):
        # score = credit_card.calculate_score()
        # print(score)

        print("\nMake Predictions by using Persistence model: ")
        credit_card.persistence_model()
        print(credit_card.make_predictions_by_joblib())


"""Ausführung der App-Klasse"""
if __name__ == "__main__":
    app = App()  # Erstellung ein Main-Objekt
    # app.run()  # Ausführung der main-Mathode
    # app.call_prediction()
    app.use_credit_card_class()

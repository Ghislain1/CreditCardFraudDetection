import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class Prediction:
    def run(self):
        creditcard_data = pd.read_csv("creditcard.csv")
        X = creditcard_data.drop(columns=["Class"], axis=1)  # PrdicATORS
        print(X)
        y = creditcard_data["Class"]
        # print(y)

        # Fit the Model
        model = DecisionTreeClassifier()
        model.fit(X, y)

        # Prdiction with example
        result = model.predict(
            [
                [
                    0,
                    1.19185711131486,
                    0.26615071205963,
                    0.16648011335321,
                    0.448154078460911,
                    0.0600176492822243,
                    -0.0823608088155687,
                    -0.0788029833323113,
                    0.0851016549148104,
                    -0.255425128109186,
                    -0.166974414004614,
                    1.61272666105479,
                    1.06523531137287,
                    0.48909501589608,
                    -0.143772296441519,
                    0.635558093258208,
                    0.463917041022171,
                    -0.114804663102346,
                    -0.183361270123994,
                    -0.145783041325259,
                    -0.0690831352230203,
                    -0.225775248033138,
                    -0.638671952771851,
                    0.101288021253234,
                    -0.339846475529127,
                    0.167170404418143,
                    0.125894532368176,
                    -0.00898309914322813,
                    0.0147241691924927,
                    2.69,
                ]
            ]
        )
        print(result)

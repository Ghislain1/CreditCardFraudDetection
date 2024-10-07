from sklearn.tree import DecisionTreeClassifier
from check_data import CheckData
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

# Column name to predict
TARGET_TO_PREDICT = "Class"
X_INPUT = [
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


class CreditCard(CheckData):  # Python Inheritance
    def __init__(self):
        super().__init__()
        self.model = None
        self.file_joblib = "creditcard-checker.joblib"

    def clean_data(self) -> None:
        """Find Duplicate in Data"""
        print(self.check_missing_data())
        has_duplicate = self.data_df.duplicated()
        if has_duplicate is True:
            self.data_df = self.data_df.drop_duplicates()

    def split_data_Xy(self):
        """Creating  X (Capital letter ) inputs array, y output array"""
        X = self.data_df.drop(columns=[TARGET_TO_PREDICT])
        y = self.data_df[TARGET_TO_PREDICT]
        return X, y

    def create_train_model(self):
        X, y = self.split_data_Xy()
        self.model = DecisionTreeClassifier()
        self.model.fit(X, y)

    def make_predictions(self):
        self.create_train_model()
        predictions = self.model.predict(X_INPUT)
        return predictions

    def calculate_score(self):
        X, y = self.split_data_Xy()
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2
        )  # test_size: only 20% of data is used

        self.model = DecisionTreeClassifier()
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        return accuracy_score(y_test, predictions)

    def persistence_model(self):
        """Save to the file"""
        X, y = self.split_data_Xy()
        self.model = DecisionTreeClassifier()
        self.model.fit(X, y)
        joblib.dump(self.model, self.file_joblib)

    def make_predictions_by_joblib(self):
        """Laod  file joblib  and make predictiobs"""
        model = joblib.load(self.file_joblib)
        predictions = model.predict(X_INPUT)
        return predictions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DashBoard:
    def __init__(self, file_path="creditcard.csv"):
        # csv-file load
        self.data_dataFrame = pd.read_csv(file_path)
        self.data_dataFrame = self.data_dataFrame.head(n=10000)

    def show_data_info(self):
        # get info about dataset
        print(self.data_dataFrame.info)

    def seaborn_view(self, x_column: str, y_column=None, hue_column: str = None):
        # show the dataset
        if y_column:
            # Erstelle Subplots: 2 Zeilen, 1 Spalte
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

            # scatterplot if two column are giving
            sns.scatterplot(
                data=self.data_dataFrame,
                x=x_column,
                y=y_column,
                hue=hue_column,
                palette="deep",
                ax=ax1,
            )
            sns.lineplot(
                data=self.data_dataFrame,
                x=x_column,
                y=y_column,
                hue=hue_column,
                palette="pastel",
                ax=ax2,
            )
            # Layout-Anpassung, um Überlappungen zu vermeiden
            plt.tight_layout()
            plt.title(f"{x_column} vs {y_column} (colored by {hue_column})")
            plt.show()
        else:
            # Histogram if only one column ist giving
            # sns.histplot(data=self.data_dataFrame, x=x_column)
            # plt.title(f"distribution of {x_column}")
            pass
        # plt.show(sns)

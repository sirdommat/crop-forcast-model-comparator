import pandas as pd
import numpy as np


class persistence_model():
    """ This is a baseline model that uses the previous year's yields at a CARUID 
    as the prediction for the current year. If prior yields are found, then the
    produced yield is 0.
    """

    def __init__(self):
        self._data = None

    def fit(self, X: pd.DataFrame, y: pd.Series) -> None:
        """Fits the model with the data provided in X and y.

        Args:
            X (pd.DataFrame): A DataFrame containing data features. 
                              It must contain the 'Year' and 'CARUID' column.
            y (pd.Series): A Series containing the target values

            X and y must contain the same number of rows.
        """
        self._data = X.loc[:, ['Year', 'CARUID']]
        self._data['y'] = y

    def generate_one_prediction(self, sers: pd.Series) -> float:
        """Generates a prediction for one row of data. Sers must contain 'Year'
        and 'CARUID' columns.

        Args:
            sers (pd.Series): Must contain 'Year and 'CARUID' columns

        Raises:
            Exception: The model has not been fitted with fit() yet.

        Returns:
            float: The last year's yield for this CARUID.
        """
        if self._data is None:
            raise Exception(
                'The model has not been fitted yet. Fit the model first using .fit(X, y)')

        year = sers['Year']
        CARUID = sers['CARUID']

        try:
            idx = self._data.query(
                f'(Year == {year - 1}) & CARUID == {CARUID}').index[0]
            return self._data.iloc[idx, :]['y']
        except:
            return 0

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Generates an array of predictions for the given DataFrame.
        The DataFrame must contain the columns 'Year' and 'CARUID'.

        Args:
            X (pd.DataFrame): Must contain 'Year' and 'CARUID' columns

        Returns:
            np.ndarray: An array of predictions
        """
        predictions = []

        for _, row in X.iterrows():
            predictions.append(self.generate_one_prediction(row))

        return np.asarray(predictions)

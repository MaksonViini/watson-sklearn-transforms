from sklearn.base import BaseEstimator, TransformerMixin


class EncoderCredit(BaseEstimator, TransformerMixin):
    def __init__(self, col):
        self.col = col

    def fill(self, x):
        return 0 if (x == 'NO_CHECKING') | (x == 'UNKNOWN') else x

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X[self.col[0]] = X[self.col[0]].apply(self.fill).astype(float)
        X[self.col[1]] = X[self.col[1]].apply(self.fill).astype(float)
        return X


class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

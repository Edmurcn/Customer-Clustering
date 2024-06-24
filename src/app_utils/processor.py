import pandas as pd   
import numpy as np  
import pickle
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.base import BaseEstimator, TransformerMixin

def get_processor():

    """
    Função para realizar a adequação dos dados preenchidos pela aplicação web

    Utilizando as técnicas de Ordinal e One Hot encoder

    """

    ordinal_encoder_orders = { "Sex": ["Masculino", "Feminino"],
    
                              "Marital status": ["Solteiro(a)", "Outros"],
                              
                              "Education": ["Nenhuma / Fundamental", "Ensino Médio", 
                                            "Gradução", "Pós-Graduação"],

                              "Occupation": ["Desempregado / Autônomos", "Servidores",
                                             "Oficiais / Autoridades / Administradores"],

                              "Settlement Size": ["< 100.000 habitantes", "entre 100.000 e 500.000 habitantes",
                                            "> 500.000 habitantes"]
    }

    preprocessor = OrdinalEncoder(to_encoder)


class OrdinalFeatureEncoder(BaseEstimator, TransformerMixin):
    '''
    A transformer class for ordinal encoding specified categorical features and retaining feature names.

    Attributes:
        to_encode (dict): A dictionary where keys are column names and values are lists representing the desired category orders.

    Methods:
        fit(X, y=None): Fit the transformer to the data.
        transform(X): Transform the input DataFrame by ordinal encoding specified columns and retaining feature names.
    '''
    def __init__(self, to_encode):
        '''
        Initialize the OrdinalFeatureEncoder transformer.

        Args:
            to_encode (dict): A dictionary where keys are column names and values are lists representing the desired category orders.
        '''
        self.to_encode = to_encode
        self.encoder = OrdinalEncoder(dtype=np.int8, 
                                      categories=[to_encode[col] for col in to_encode])

    def fit(self, X, y=None):
        '''
        Fit the transformer to the data.

        Args:
            X (pandas.DataFrame): Input features.
            y (array-like, default=None): Target labels. Ignored.

        Returns:
            self: Returns an instance of self.
        '''
        self.encoder.fit(X[list(self.to_encode.keys())])
        return self

    def transform(self, X):
        '''
        Transform the input DataFrame by ordinal encoding specified columns and retaining feature names.

        Args:
            X (pandas.DataFrame): Input features.

        Returns:
            pandas.DataFrame: Transformed DataFrame after ordinal encoding specified columns and retaining feature names.
        '''
        # Ordinal encode the columns.
        X_ordinal = self.encoder.transform(X[list(self.to_encode.keys())])
        
        # Create a dataframe for the ordinal encoded data.
        ordinal_encoded_df = pd.DataFrame(X_ordinal,
                                          columns=self.encoder.get_feature_names_out(list(self.to_encode.keys())))
        
        # Reset for mapping and concatenated constructing a final dataframe of features.
        X_reset = X.reset_index(drop=True)
        
        return pd.concat([X_reset.drop(columns=list(self.to_encode.keys())), ordinal_encoded_df], axis=1)
    
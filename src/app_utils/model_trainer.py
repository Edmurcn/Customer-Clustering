import pandas as pd  
import numpy as np 
import pickle
from xgboost import XGBClassifier

def get_model():

    """
    Função utilizada para gerar o objeto .pkl do modelo treinado em artifacts

    Esta função será automatizada para treinar o modelo conforme seja 
    adicionado dados ao conjunto.
    
    """

    df = pd.read_csv("/home/edmurcn/Documentos/MeusProjetos/Customer-Clustering/data/dados_label.csv", header=0)

    X = df.drop(["Label"], axis=1).to_numpy()
    y = df["Label"].to_numpy()

    XGB = XGBClassifier(random_state=0)

    model = XGB.fit(X, y)

    pickle.dump(model, open("/home/edmurcn/Documentos/MeusProjetos/Customer-Clustering/artifacts/model.pkl", "wb"))


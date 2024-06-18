import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 
import seaborn as sns   

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_curve, confusion_matrix, f1_score, auc

import time

# Detalhar erros
from src.details_error import CustomException
import sys

# Ignorar avisos
from warnings import filterwarnings
filterwarnings('ignore')

def evaluation_model_multclass_classifier(models, X_train, y_train, n_fold=5):


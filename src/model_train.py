import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 
import seaborn as sns   
import plotly.express as px

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import roc_curve, confusion_matrix, auc
from sklearn.metrics import RocCurveDisplay, ConfusionMatrixDisplay
from sklearn.preprocessing import label_binarize

import time

# Detalhar erros
# from details_error import CustomException
import sys

# Ignorar avisos
from warnings import filterwarnings
filterwarnings('ignore')

#Função que avalia a performance dos modelos
def evaluation_model_multclass_classifier(models, X, y):

    # try:
    #Criando os arquivos para os resultados
    acc_models = {}
    f1_models = {}
    auc_models = {}
    time_evaluation = {}
    cm_models = {}
    prob = {}

    #Criando os subplots para os resultados
    palette = sns.color_palette("flare")

    models_name = list(models.keys())
    n_row_max = ((len(models_name)-1) // 2) + 1
    fig , axs = plt.subplots(n_row_max, 4, figsize=(18, (4*n_row_max)), facecolor="lightgray")
    fig.subplots_adjust(hspace=0.35)

    #Dividindo os dados de maneira equilibrada entre treino e teste
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    classes = np.unique(y)
    y_test_binarized = label_binarize(y_test, classes=classes )

    count = 0
    #Avaliação de todos os modelos
    for model in models:

        model_function = models[model]
        
        start = time.time()
        
        acc_models[model] = np.mean(cross_val_score(model_function, X, y, scoring="accuracy", cv=5))
        f1_models[model] = np.mean(cross_val_score(model_function, X, y, scoring="f1_micro", cv=5))
        auc_models[model] = np.mean(cross_val_score(model_function, X, y, scoring="roc_auc_ovr", cv=5))
        
        finish = time.time()

        time_evaluation[model] = round(finish-start, 5)

       #Dados para a construção da matriz de confusão e curva ROC 

        y_pred = model_function.fit(x_train, y_train).predict(x_test)
        cm_models[count] = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred))

        #Dados para a construção da curva ROC para cada classe
        prob[count] = model_function.predict_proba(x_test)

        count += 1

    #Construção da tabela das métricas
    df_metrics = {}
    df_metrics["Models"] = list(models.keys())
    df_metrics["Accuracy"] = list(acc_models.values())
    df_metrics["F1_micro"] = list(f1_models.values())
    df_metrics["AUC_OVR"] = list(auc_models.values())
    df_metrics["Training_time"] = list(time_evaluation.values())
    df_metrics = pd.DataFrame(df_metrics)

    # Função para a posição dos axes (colunas=4)
    def position(n, n_row_max=n_row_max):
        if n_row_max == 1:
            n_col = n % 4
            return n_col
        else:
            n_col = n % 4
            n_row = n // 4
            return n_row, n_col
    
    # Loop para a construção dos gráficos de matriz de confusão e curva ROC
    for i in range(0, len(models_name)):
        # Gráfico da matriz de confusão
        cm_models[i].plot(ax=axs[position(2*i)], colorbar=False)
        axs[position(2*i)].set_title(f"Confusion matrix \n {models_name[i]}", fontsize=12)

        # Gráfico da curva ROC
        fpr = {}
        tpr = {}
        prob_class = prob[i]
        for j in range(len(classes)):
            fpr[j], tpr[j], _ = roc_curve(y_test_binarized[:, j], prob_class[:, j])
            sns.lineplot(x=fpr[j], y=tpr[j], linestyle='--', 
                 label='%s vs Rest' % (classes[j]), ax=axs[position((2*i)+1)])
        sns.lineplot(x=[0,1], y=[0,1], linestyle="--", c="k", ax=axs[position((2*i)+1)])
        axs[position((2*i)+1)].set_xlim((0,1))
        axs[position((2*i)+1)].set_ylim((0,1.05))
        axs[position((2*i)+1)].set_xlabel("False Positive Rate", fontsize=10)
        axs[position((2*i)+1)].set_ylabel("True Positive Rate", fontsize=10)
        axs[position((2*i)+1)].legend(loc="lower right", fontsize=10)
        axs[position((2*i)+1)].set_title(f"Multiclass ROC curve \n {models_name[i]}")

    plt.savefig('/home/edmurcn/Documentos/MeusProjetos/Customer-Clustering/imagens/metrics.png', bbox_inches='tight')
    plt.close()

    # Gráfico de barra dos parâmetros 

    fig, ax = plt.subplots(figsize=(16, 6), facecolor="lightgray")
    width = 0.35

    x = np.arange(len(df_metrics['Models']))

    acc_bars = ax.bar(x - 1.5*width/2, df_metrics['Accuracy'], width, label=df_metrics.columns[1], color=palette[0])
    f1_bars = ax.bar(x - 0.5*width/2, df_metrics['F1_micro'], width, label=df_metrics.columns[2], color=palette[1])
    auc_bars = ax.bar(x + 0.5*width/2, df_metrics['AUC_OVR'], width, label=df_metrics.columns[3], color=palette[2])
    time_bars = ax.bar(x + 1.5*width/2, df_metrics['Training_time'], width, label=df_metrics.columns[4], color=palette[3])

    ax.set_xlabel('Models', labelpad=20, fontsize=10.8)
    ax.set_ylabel('Metrics', labelpad=20, fontsize=10.8)
    ax.set_title("Models Performance", fontweight='bold', fontsize=12, pad=30)
    ax.set_xticks(x)
    ax.set_xticklabels(df_metrics['Models'], rotation=0, fontsize=10.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Adicionar anotações no topo de cada barra
    for bars in [acc_bars, f1_bars, auc_bars, time_bars]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(round(height, 2), fontweight="bold"),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

    ax.legend(loc='upper left')

    plt.savefig('/home/edmurcn/Documentos/MeusProjetos/Customer-Clustering/imagens/models_performance.png', bbox_inches='tight')
    plt.close()

    return df_metrics

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.tree import DecisionTreeClassifier
from io import StringIO
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
import Data_Processing

def create_tree(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Primero creamos los datyos de entrenamiento con el archivo file_training.
    #       Posteriormente creamos los datos de testeo con el archivo file_testing.      
    x_train, y_train = Data_Processing.data_processing(file_training)

    #       Creación del arbol de decisión.
    decision_tree = DecisionTreeClassifier()

    #       Entrenamiento del arbol de desición con los datos de entrenamiento
    decision_tree = decision_tree.fit(x_train, y_train)

    return decision_tree

def show_most_important_data(decision_tree):
    caract = decision_tree.n_features_
    plt.barh(range(caract), decision_tree.feature_importances_)
    plt.yticks(np.arange(caract))
    plt.xlabel("Importancia características")
    plt.ylabel("Características")
    plt.show()




def lectura_datos():
    """
    export_graphviz(Arbol, out_file = "dot_data.dot",  
                    filled = True, rounded = True,
                    special_characters = True)


    print(Arbol.score(Predictores_Test, Objetivos_Test) * 100, "%")

    #   Acá se imprime el factor que más influye en los resultados
    caract = Predictores_Train.shape[1]
    plt.barh(range(caract), Arbol.feature_importances_)
    plt.yticks(np.arange(caract), Predictores_Train.head())
    plt.xlabel("Importancia características")
    plt.ylabel("Características")
    plt.show()"""
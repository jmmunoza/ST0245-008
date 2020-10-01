import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import Data_Processing

#       Creamos un árbol de desición que solamente toma datos de los puntajes del estudiante.
def create_tree_score(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Creamos los datos de entrenamiento con el archivo file_training.      
    x_train, y_train = Data_Processing.data_score_processing(file_training)

    #       Creación del arbol de decisión.
    decision_tree = DecisionTreeClassifier()

    #       Entrenamiento del arbol de desición con los datos de entrenamiento
    decision_tree = decision_tree.fit(x_train, y_train)

    #       Retorna el árbol entrenado
    return decision_tree


#       Creamos un árbol de desición que solamente toma datos socioeconómicos del estudiante.
def create_tree_socioeconomic(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Creamos los datos de entrenamiento con el archivo file_training.    
    x_train, y_train = Data_Processing.data_socioeconomic_processing(file_training)

    #       Creación del arbol de decisión.
    decision_tree = DecisionTreeClassifier()

    #       Entrenamiento del arbol de desición con los datos de entrenamiento
    decision_tree = decision_tree.fit(x_train, y_train)

    #       Retorna el árbol entrenado
    return decision_tree


#       Creamos un árbol de desición que toma tanto los datos socioeconómicos y los puntajes del estudiante.
def create_tree_score_socioeconomic(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Creamos los datos de entrenamiento con el archivo file_training.    
    x_train, y_train = Data_Processing.data_score_socioeconomic_processing(file_training)

    #       Creación del arbol de decisión.
    decision_tree = DecisionTreeClassifier()

    #       Entrenamiento del arbol de desición con los datos de entrenamiento
    decision_tree = decision_tree.fit(x_train, y_train)

    #       Retorna el árbol entrenado
    return decision_tree
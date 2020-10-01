import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import Data_Processing

#       Creamos un bosque aleatorio que solamente toma datos de los puntajes del estudiante.
def create_random_forest_score(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Creamos los datos de entrenamiento con el archivo file_training.    
    x_train, y_train = Data_Processing.data_score_processing(file_training)

    #       Creación del bosque aleatorio.
    random_forest = RandomForestClassifier()

    #       Entrenamiento del bosque aleatorio con los datos de entrenamiento
    random_forest = random_forest.fit(x_train, y_train)

    #       Retorna el bosque entrenado
    return random_forest


#       Creamos un bosque aleatorio que solamente toma datos socioeconómicos del estudiante.
def create_random_forest_socioeconomic(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Creamos los datos de entrenamiento con el archivo file_training.    
    x_train, y_train = Data_Processing.data_socioeconomic_processing(file_training)

    #       Creación del bosque aleatorio.
    random_forest = RandomForestClassifier()

    #       Entrenamiento del bosque aleatorio con los datos de entrenamiento
    random_forest = random_forest.fit(x_train, y_train)

    #       Retorna el bosque entrenado
    return random_forest


#       Creamos un bosque aleatorio que toma tanto los datos socioeconómicos y los puntajes del estudiante.
def create_random_forest_score_socioeconomic(file_training):
    #       Acá asignamos los datos de X y Y con la función data_processing.
    #       Creamos los datos de entrenamiento con el archivo file_training.      
    x_train, y_train = Data_Processing.data_score_socioeconomic_processing(file_training)

    #       Creación del bosque aleatorio.
    random_forest = RandomForestClassifier()

    #       Entrenamiento del bosque aleatorio con los datos de entrenamiento
    random_forest = random_forest.fit(x_train, y_train)

    #       Retorna el bosque entrenado
    return random_forest
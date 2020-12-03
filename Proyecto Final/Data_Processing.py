import pandas as pd
import numpy as np

#       Procesa únicamente los datos referentes a los puntajes obtenidos en cada asignatura.
def data_score_processing(file):
    #       Se leen los datos del archivo .csv
    data = pd.read_csv(file + '.csv', sep=';', header=0)

    #       Se reemplazan los valores en la fila de exito por valores booleanos. 
    data["exito"] = data["exito"].replace({1: True, 0: False})

    #       Guardamos todos los datos referentes al puntaje en x_data
    x_data = data[["punt_lenguaje","punt_matematicas","punt_biologia",
                   "punt_quimica","punt_fisica","punt_ciencias_sociales",
                   "punt_filosofia", "punt_ingles"]]
    
    #       Guardamos todos los valores booleanos de éxito en y_data
    y_data = data["exito"]

    return x_data, y_data




#       Procesa únicamente los datos referentes a la inforcacion socioeconómica.
def data_socioeconomic_processing(file):
    #       Se leen los datos del archivo .csv
    data = pd.read_csv(file + '.csv', sep=';', header=0)

    data = data[["fami_trabajolaborpadre", "fami_trabajolabormadre", "fami_numlibros", "estu_genero.1", "fami_educacionpadre.1",
                 "fami_educacionmadre.1", "fami_ocupacionpadre.1", "fami_ocupacionmadre.1", "fami_estratovivienda.1", "fami_nivelsisben",
                 "fami_pisoshogar", "fami_tieneinternet.1", "fami_tienecomputador.1","fami_tienemicroondas", "fami_tienehorno", "fami_tieneautomovil.1",
                 "fami_tienedvd", "fami_tiene_nevera.1", "fami_tiene_celular.1", "fami_telefono.1", "fami_ingresofmiliarmensual",
                 "estu_trabajaactualmente", "exito"]]

    #       Se limpian los datos vacios eliminando las filas que los contengan.
    data = data.dropna()
    data = data.reset_index(drop=True)

    #       Se reemplazan los valores en la fila de exito por valores booleanos. 
    data["exito"] = data["exito"].replace({1: True, 0: False})

    #       Guardamos todos los datos referentes a la información socioeconómica en x_data
    x_data = data[["fami_trabajolaborpadre", "fami_trabajolabormadre", "fami_numlibros", "estu_genero.1", "fami_educacionpadre.1",
                   "fami_educacionmadre.1", "fami_ocupacionpadre.1", "fami_ocupacionmadre.1", "fami_estratovivienda.1", "fami_nivelsisben",
                   "fami_pisoshogar", "fami_tieneinternet.1", "fami_tienecomputador.1","fami_tienemicroondas", "fami_tienehorno", "fami_tieneautomovil.1",
                   "fami_tienedvd", "fami_tiene_nevera.1", "fami_tiene_celular.1", "fami_telefono.1", "fami_ingresofmiliarmensual",
                   "estu_trabajaactualmente"]]

    #       Guardamos todos los valores booleanos de éxito en y_data
    y_data = data["exito"]
    
    return x_data, y_data




#       Procesa únicamente los datos referentes a los puntajes y la informacion socioeconomica.
def data_score_socioeconomic_processing(file):
    #       Se leen los datos del archivo .csv
    data = pd.read_csv(file + '.csv', sep=';', header=0)

    data = data[["fami_trabajolaborpadre", "fami_trabajolabormadre", "fami_numlibros", "estu_genero.1", "fami_educacionpadre.1",
                 "fami_educacionmadre.1", "fami_ocupacionpadre.1", "fami_ocupacionmadre.1", "fami_estratovivienda.1", "fami_nivelsisben",
                 "fami_pisoshogar", "fami_tieneinternet.1", "fami_tienecomputador.1","fami_tienemicroondas", "fami_tienehorno", "fami_tieneautomovil.1",
                 "fami_tienedvd", "fami_tiene_nevera.1", "fami_tiene_celular.1", "fami_telefono.1", "fami_ingresofmiliarmensual",
                 "estu_trabajaactualmente", "punt_lenguaje","punt_matematicas","punt_biologia", "punt_quimica","punt_fisica","punt_ciencias_sociales",
                 "punt_ingles", "punt_filosofia", "exito"]]

    #       Se limpian los datos vacios eliminando las filas que los contengan.
    data = data.dropna()
    data = data.reset_index(drop=True)

    #       Se reemplazan los valores en la fila de exito por valores booleanos. 
    data["exito"] = data["exito"].replace({1: True, 0: False})

    #       Guardamos todos los datos referentes al puntaje e información socioeconómica en x_data
    x_data = data[["fami_trabajolaborpadre", "fami_trabajolabormadre", "fami_numlibros", "estu_genero.1", "fami_educacionpadre.1",
                   "fami_educacionmadre.1", "fami_ocupacionpadre.1", "fami_ocupacionmadre.1", "fami_estratovivienda.1", "fami_nivelsisben",
                   "fami_pisoshogar", "fami_tieneinternet.1", "fami_tienecomputador.1","fami_tienemicroondas", "fami_tienehorno", "fami_tieneautomovil.1",
                   "fami_tienedvd", "fami_tiene_nevera.1", "fami_tiene_celular.1", "fami_telefono.1", "fami_ingresofmiliarmensual",
                   "estu_trabajaactualmente", "punt_lenguaje","punt_matematicas","punt_biologia", "punt_quimica","punt_fisica","punt_ciencias_sociales",
                   "punt_ingles", "punt_filosofia"]]

    #       Guardamos todos los valores booleanos de éxito en y_data
    y_data = data["exito"]

    return x_data, y_data
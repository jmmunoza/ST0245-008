import pandas as pd
import numpy as np

#       Procesa únicamente los datos referentes a los puntajes obtenidos en cada asignatura.
def data_score_processing(file):
    #       Reading data from the .csv file
    data = pd.read_csv(file + '.csv', sep=';', header=0)

    #       For convenience, we will replace the success 0 and 1 values ​​with Boolean values.
    data["exito"] = data["exito"].replace({1: True, 0: False})

    #       Guardamos todos los datos referentes al puntaje en x_data
    x_data = data[["punt_lenguaje","punt_matematicas","punt_biologia",
                   "punt_quimica","punt_fisica","punt_ciencias_sociales",
                   "punt_filosofia", "punt_ingles"]]
    
    #       Guardamos todos los valores booleanos de éxito en y_data
    y_data = data["exito"]

    return x_data, y_data

#       Procesa únicamente los datos referentes a los puntajes obtenidos en cada asignatura.
def data_socioeconomic_processing(file):
    #       Reading data from the .csv file
    data = pd.read_csv(file + '.csv', sep=';', header=0)

    #       So as not to have inconveniences when executing the algorithm.
    #       We will replace the values ​​of YES by True, NO and NaN by False.
    data = data.replace({"No": False, "Si" : True})
    data = data.fillna(False)

    #       For convenience, we will replace the success 0 and 1 values ​​with Boolean values.
    data["exito"] = data["exito"].replace({1: True, 0: False})

    #       Debido a que las pregutas socio-economicas son respuestas en texto
    #       que el algoritmo de desición no comprende, debemos convertir cada
    #       respuesta en valores numéricos. No podemos usar valores booleanos
    #       debido a que en la mayoría de los casos hay más de dos respuestas.
    #
    #       Dependiendo del número de distintas repuestas, se usarán n números.

    #       Modificando cada respuesta de fami_trabajolaborpadre por valores numéricos
    data["fami_trabajolaborpadre"] = data["fami_trabajolaborpadre"].replace({False: 0,
                                                                             "Es agricultor, pesquero o jornalero": 1,
                                                                             "Es dueño de un negocio grande, tiene un cargo de nivel directivo o gerencial": 2,
                                                                             "Es dueño de un negocio pequeño (tiene pocos empleados o no tiene, por ejemplo tienda, papelería, etc": 3,
                                                                             "Es operario de máquinas o conduce vehículos (taxita, chofer)": 4,
                                                                             "Es vendedor o trabaja en atención al público": 5,
                                                                             "No aplica": 6,
                                                                             "No sabe": 7,
                                                                             "Pensionado": 8,
                                                                             "Tiene un trabajo de tipo auxiliar administrativo (por ejemplo, secretario o asistente)": 9,
                                                                             "Trabaja como personal de limpieza, mantenimiento, seguridad o construcción": 10,
                                                                             "Trabaja como profesional (por ejemplo médico, abogado, ingeniero)": 11,
                                                                             "Trabaja en el hogar, no trabaja o estudia": 12,
                                                                             "Trabaja por cuenta propia (por ejemplo plomero, electricista)":13})

    #       Modificando cada respuesta de fami_trabajolabormadre por valores numéricos
    data["fami_trabajolabormadre"] = data["fami_trabajolabormadre"].replace({False: 0,
                                                                             "Es agricultor, pesquero o jornalero": 1,
                                                                             "Es dueño de un negocio grande, tiene un cargo de nivel directivo o gerencial": 2,
                                                                             "Es dueño de un negocio pequeño (tiene pocos empleados o no tiene, por ejemplo tienda, papelería, etc": 3,
                                                                             "Es operario de máquinas o conduce vehículos (taxita, chofer)": 4,
                                                                             "Es vendedor o trabaja en atención al público": 5,
                                                                             "No aplica": 6,
                                                                             "No sabe": 7,
                                                                             "Pensionado": 8,
                                                                             "Tiene un trabajo de tipo auxiliar administrativo (por ejemplo, secretario o asistente)": 9,
                                                                             "Trabaja como personal de limpieza, mantenimiento, seguridad o construcción": 10,
                                                                             "Trabaja como profesional (por ejemplo médico, abogado, ingeniero)": 11,
                                                                             "Trabaja en el hogar, no trabaja o estudia": 12,
                                                                             "Trabaja por cuenta propia (por ejemplo plomero, electricista)":13})

    #       Modificando cada respuesta de fami_numlibros por valores numéricos
    data["fami_numlibros"] = data["fami_numlibros"].replace({False: 0,
                                                             "0 A 10 LIBROS": 1,
                                                             "11 A 25 LIBROS": 2,
                                                             "26 A 100 LIBROS": 3,
                                                             "MÁS DE 100 LIBROS": 4})

    #       Modificando cada respuesta de estu_genero.1 por valores numéricos
    data["estu_genero.1"] = data["estu_genero.1"].replace({"F": 1, "M": 0})

    #       Modificando cada respuesta de fami_educacionpadre.1 por valores numéricos
    data["fami_educacionpadre.1"] = data["fami_educacionpadre.1"].replace({False: 0,
                                                                           "Educación profesional completa": 1,
                                                                           "Educación profesional incompleta": 2,
                                                                           "Ninguno": 3,
                                                                           "No sabe": 4,
                                                                           "Postgrado": 5,
                                                                           "Primaria completa": 6,
                                                                           "Primaria incompleta": 7,
                                                                           "Secundaria (Bachillerato) completa": 8,
                                                                           "Secundaria (Bachillerato) incompleta": 9,
                                                                           "Técnica o tecnológica completa": 10,
                                                                           "Técnica o tecnológica incompleta": 11})

    #       Modificando cada respuesta de fami_educacionmadre.1 por valores numéricos
    data["fami_educacionmadre.1"] = data["fami_educacionmadre.1"].replace({False: 0,
                                                                           "Educación profesional completa": 1,
                                                                           "Educación profesional incompleta": 2,
                                                                           "Ninguno": 3,
                                                                           "No sabe": 4,
                                                                           "Postgrado": 5,
                                                                           "Primaria completa": 6,
                                                                           "Primaria incompleta": 7,
                                                                           "Secundaria (Bachillerato) completa": 8,
                                                                           "Secundaria (Bachillerato) incompleta": 9,
                                                                           "Técnica o tecnológica completa": 10,
                                                                           "Técnica o tecnológica incompleta": 11})
    #       Modificando cada respuesta de fami_ocupacionpadre.1 por valores numéricos
    data["fami_ocupacionpadre.1"] = data["fami_ocupacionpadre.1"].replace({False: 0,
                                                                           "Empleado con cargo como director o gerente general": 1,
                                                                           "Empleado de nivel auxiliar o administrativo": 2,
                                                                           "Empleado de nivel directivo": 3,
                                                                           "Empleado de nivel técnico o profesional": 4,
                                                                           "Empleado obrero u operario": 5,
                                                                           "Empresario": 6,
                                                                           "Hogar": 7,
                                                                           "Otra actividad u ocupación": 8,
                                                                           "Pensionado": 9,
                                                                           "Pequeño empresario": 10,
                                                                           "Profesional independiente": 11,
                                                                           "Profesional Independiente": 11,
                                                                           "Trabajador por cuenta propia": 12})
                                        
    #       Modificando cada respuesta de fami_ocupacionmadre.1 por valores numéricos
    data["fami_ocupacionmadre.1"] = data["fami_ocupacionmadre.1"].replace({False: 0,
                                                                           "Empleado con cargo como director o gerente general": 1,
                                                                           "Empleado de nivel auxiliar o administrativo": 2,
                                                                           "Empleado de nivel directivo": 3,
                                                                           "Empleado de nivel técnico o profesional": 4,
                                                                           "Empleado obrero u operario": 5,
                                                                           "Empresario": 6,
                                                                           "Hogar": 7,
                                                                           "Otra actividad u ocupación": 8,
                                                                           "Pensionado": 9,
                                                                           "Pequeño empresario": 10,
                                                                           "Profesional independiente": 11,
                                                                           "Profesional Independiente": 11,
                                                                           "Trabajador por cuenta propia": 12})

    #       Modificando cada respuesta de fami_estratovivienda.1 por valores numéricos
    data["fami_estratovivienda.1"] = data["fami_estratovivienda.1"].replace({False: 0,
                                                                             "Estrato 1": 1,
                                                                             "Estrato 2": 2,
                                                                             "Estrato 3": 3,
                                                                             "Estrato 4": 4,
                                                                             "Estrato 5": 5,
                                                                             "Estrato 6": 6})

    #       Modificando cada respuesta de fami_nivelsisben por valores numéricos
    data["fami_nivelsisben"] = data["fami_nivelsisben"].replace({False: 0,
                                                                 "Nivel 1": 1,
                                                                 "Nivel 2": 2,
                                                                 "Nivel 3": 3,
                                                                 "Esta clasificada en otro nivel del SISBEN": 4,
                                                                 "No está clasificada por el SISBEN": 5})

    #       Modificando cada respuesta de fami_pisohogar por valores numéricos
    data["fami_pisoshogar"] = data["fami_pisoshogar"].replace({False: 0,
                                                               "Cemento, gravilla, ladrillo": 1,
                                                               "Madera burda, tabla, tablón": 2,
                                                               "Madera pulida, baldosa, tableta, mármol, alfombra": 3,
                                                               "Tierra, arena": 4})

    #       Modificando cada respuesta de fami_ingresofmiliarmensual por valores numéricos
    data["fami_ingresofmiliarmensual"] = data["fami_ingresofmiliarmensual"].replace({False: 0,
                                                                                     "10 o más SMLV": 1,
                                                                                     "Entre 1 y menos de 2 SMLV": 2,
                                                                                     "Entre 2 y menos de 3 SMLV": 3,
                                                                                     "Entre 3 y menos de 5 SMLV": 4,
                                                                                     "Entre 5 y menos de 7 SMLV": 5,
                                                                                     "Entre 7 y menos de 10 SMLV": 6,
                                                                                     "Menos de 1 SMLV": 7})

    #       Modificando cada respuesta de estu_trabajaactualmente por valores numéricos
    data["estu_trabajaactualmente"] = data["estu_trabajaactualmente"].replace({False: 0,
                                                                               "Si, 20 horas o más a la semana": 1,
                                                                               "Si, menos de 20 horas a la semana": 2})

    #       Guardamos todos los datos referentes a la información socioeconómica en x_data
    x_data = data[["fami_trabajolaborpadre", "fami_trabajolabormadre", "fami_numlibros", "estu_genero.1", "fami_educacionpadre.1",
                   "fami_educacionmadre.1", "fami_ocupacionpadre.1", "fami_ocupacionmadre.1", "fami_estratovivienda.1", "fami_nivelsisben",
                   "fami_pisoshogar", "fami_tieneinternet.1", "fami_tienecomputador.1","fami_tienemicroondas", "fami_tienehorno", "fami_tieneautomovil.1",
                   "fami_tienedvd", "fami_tiene_nevera.1", "fami_tiene_celular.1", "fami_telefono.1", "fami_ingresofmiliarmensual",
                   "estu_trabajaactualmente"]]

    #       Guardamos todos los valores booleanos de éxito en y_data
    y_data = data["exito"]

    return x_data, y_data

#       Procesa únicamente los datos referentes a los puntajes obtenidos en cada asignatura.
def data_score_socioeconomic_processing(file):
    #       Reading data from the .csv file
    data = pd.read_csv(file + '.csv', sep=';', header=0)

    #       So as not to have inconveniences when executing the algorithm.
    #       We will replace the values ​​of YES by True, NO and NaN by False.
    data = data.replace({"No": False, "Si" : True})
    data = data.fillna(False)

    #       For convenience, we will replace the success 0 and 1 values ​​with Boolean values.
    data["exito"] = data["exito"].replace({1: True, 0: False})

    #       Debido a que las pregutas socio-economicas son respuestas en texto
    #       que el algoritmo de desición no comprende, debemos convertir cada
    #       respuesta en valores numéricos. No podemos usar valores booleanos
    #       debido a que en la mayoría de los casos hay más de dos respuestas.
    #
    #       Dependiendo del número de distintas repuestas, se usarán n números.

    #       Modificando cada respuesta de fami_trabajolaborpadre por valores numéricos
    data["fami_trabajolaborpadre"] = data["fami_trabajolaborpadre"].replace({False: 0,
                                                                             "Es agricultor, pesquero o jornalero": 1,
                                                                             "Es dueño de un negocio grande, tiene un cargo de nivel directivo o gerencial": 2,
                                                                             "Es dueño de un negocio pequeño (tiene pocos empleados o no tiene, por ejemplo tienda, papelería, etc": 3,
                                                                             "Es operario de máquinas o conduce vehículos (taxita, chofer)": 4,
                                                                             "Es vendedor o trabaja en atención al público": 5,
                                                                             "No aplica": 6,
                                                                             "No sabe": 7,
                                                                             "Pensionado": 8,
                                                                             "Tiene un trabajo de tipo auxiliar administrativo (por ejemplo, secretario o asistente)": 9,
                                                                             "Trabaja como personal de limpieza, mantenimiento, seguridad o construcción": 10,
                                                                             "Trabaja como profesional (por ejemplo médico, abogado, ingeniero)": 11,
                                                                             "Trabaja en el hogar, no trabaja o estudia": 12,
                                                                             "Trabaja por cuenta propia (por ejemplo plomero, electricista)":13})

    #       Modificando cada respuesta de fami_trabajolabormadre por valores numéricos
    data["fami_trabajolabormadre"] = data["fami_trabajolabormadre"].replace({False: 0,
                                                                             "Es agricultor, pesquero o jornalero": 1,
                                                                             "Es dueño de un negocio grande, tiene un cargo de nivel directivo o gerencial": 2,
                                                                             "Es dueño de un negocio pequeño (tiene pocos empleados o no tiene, por ejemplo tienda, papelería, etc": 3,
                                                                             "Es operario de máquinas o conduce vehículos (taxita, chofer)": 4,
                                                                             "Es vendedor o trabaja en atención al público": 5,
                                                                             "No aplica": 6,
                                                                             "No sabe": 7,
                                                                             "Pensionado": 8,
                                                                             "Tiene un trabajo de tipo auxiliar administrativo (por ejemplo, secretario o asistente)": 9,
                                                                             "Trabaja como personal de limpieza, mantenimiento, seguridad o construcción": 10,
                                                                             "Trabaja como profesional (por ejemplo médico, abogado, ingeniero)": 11,
                                                                             "Trabaja en el hogar, no trabaja o estudia": 12,
                                                                             "Trabaja por cuenta propia (por ejemplo plomero, electricista)":13})

    #       Modificando cada respuesta de fami_numlibros por valores numéricos
    data["fami_numlibros"] = data["fami_numlibros"].replace({False: 0,
                                                             "0 A 10 LIBROS": 1,
                                                             "11 A 25 LIBROS": 2,
                                                             "26 A 100 LIBROS": 3,
                                                             "MÁS DE 100 LIBROS": 4})

    #       Modificando cada respuesta de estu_genero.1 por valores numéricos
    data["estu_genero.1"] = data["estu_genero.1"].replace({"F": 1, "M": 0})

    #       Modificando cada respuesta de fami_educacionpadre.1 por valores numéricos
    data["fami_educacionpadre.1"] = data["fami_educacionpadre.1"].replace({False: 0,
                                                                           "Educación profesional completa": 1,
                                                                           "Educación profesional incompleta": 2,
                                                                           "Ninguno": 3,
                                                                           "No sabe": 4,
                                                                           "Postgrado": 5,
                                                                           "Primaria completa": 6,
                                                                           "Primaria incompleta": 7,
                                                                           "Secundaria (Bachillerato) completa": 8,
                                                                           "Secundaria (Bachillerato) incompleta": 9,
                                                                           "Técnica o tecnológica completa": 10,
                                                                           "Técnica o tecnológica incompleta": 11})

    #       Modificando cada respuesta de fami_educacionmadre.1 por valores numéricos
    data["fami_educacionmadre.1"] = data["fami_educacionmadre.1"].replace({False: 0,
                                                                           "Educación profesional completa": 1,
                                                                           "Educación profesional incompleta": 2,
                                                                           "Ninguno": 3,
                                                                           "No sabe": 4,
                                                                           "Postgrado": 5,
                                                                           "Primaria completa": 6,
                                                                           "Primaria incompleta": 7,
                                                                           "Secundaria (Bachillerato) completa": 8,
                                                                           "Secundaria (Bachillerato) incompleta": 9,
                                                                           "Técnica o tecnológica completa": 10,
                                                                           "Técnica o tecnológica incompleta": 11})
    #       Modificando cada respuesta de fami_ocupacionpadre.1 por valores numéricos
    data["fami_ocupacionpadre.1"] = data["fami_ocupacionpadre.1"].replace({False: 0,
                                                                           "Empleado con cargo como director o gerente general": 1,
                                                                           "Empleado de nivel auxiliar o administrativo": 2,
                                                                           "Empleado de nivel directivo": 3,
                                                                           "Empleado de nivel técnico o profesional": 4,
                                                                           "Empleado obrero u operario": 5,
                                                                           "Empresario": 6,
                                                                           "Hogar": 7,
                                                                           "Otra actividad u ocupación": 8,
                                                                           "Pensionado": 9,
                                                                           "Pequeño empresario": 10,
                                                                           "Profesional independiente": 11,
                                                                           "Profesional Independiente": 11,
                                                                           "Trabajador por cuenta propia": 12})
                                        
    #       Modificando cada respuesta de fami_ocupacionmadre.1 por valores numéricos
    data["fami_ocupacionmadre.1"] = data["fami_ocupacionmadre.1"].replace({False: 0,
                                                                           "Empleado con cargo como director o gerente general": 1,
                                                                           "Empleado de nivel auxiliar o administrativo": 2,
                                                                           "Empleado de nivel directivo": 3,
                                                                           "Empleado de nivel técnico o profesional": 4,
                                                                           "Empleado obrero u operario": 5,
                                                                           "Empresario": 6,
                                                                           "Hogar": 7,
                                                                           "Otra actividad u ocupación": 8,
                                                                           "Pensionado": 9,
                                                                           "Pequeño empresario": 10,
                                                                           "Profesional independiente": 11,
                                                                           "Profesional Independiente": 11,
                                                                           "Trabajador por cuenta propia": 12})

    #       Modificando cada respuesta de fami_estratovivienda.1 por valores numéricos
    data["fami_estratovivienda.1"] = data["fami_estratovivienda.1"].replace({False: 0,
                                                                             "Estrato 1": 1,
                                                                             "Estrato 2": 2,
                                                                             "Estrato 3": 3,
                                                                             "Estrato 4": 4,
                                                                             "Estrato 5": 5,
                                                                             "Estrato 6": 6})

    #       Modificando cada respuesta de fami_nivelsisben por valores numéricos
    data["fami_nivelsisben"] = data["fami_nivelsisben"].replace({False: 0,
                                                                 "Nivel 1": 1,
                                                                 "Nivel 2": 2,
                                                                 "Nivel 3": 3,
                                                                 "Esta clasificada en otro nivel del SISBEN": 4,
                                                                 "No está clasificada por el SISBEN": 5})

    #       Modificando cada respuesta de fami_pisohogar por valores numéricos
    data["fami_pisoshogar"] = data["fami_pisoshogar"].replace({False: 0,
                                                               "Cemento, gravilla, ladrillo": 1,
                                                               "Madera burda, tabla, tablón": 2,
                                                               "Madera pulida, baldosa, tableta, mármol, alfombra": 3,
                                                               "Tierra, arena": 4})

    #       Modificando cada respuesta de fami_ingresofmiliarmensual por valores numéricos
    data["fami_ingresofmiliarmensual"] = data["fami_ingresofmiliarmensual"].replace({False: 0,
                                                                                     "10 o más SMLV": 1,
                                                                                     "Entre 1 y menos de 2 SMLV": 2,
                                                                                     "Entre 2 y menos de 3 SMLV": 3,
                                                                                     "Entre 3 y menos de 5 SMLV": 4,
                                                                                     "Entre 5 y menos de 7 SMLV": 5,
                                                                                     "Entre 7 y menos de 10 SMLV": 6,
                                                                                     "Menos de 1 SMLV": 7})

    #       Modificando cada respuesta de estu_trabajaactualmente por valores numéricos
    data["estu_trabajaactualmente"] = data["estu_trabajaactualmente"].replace({False: 0,
                                                                               "Si, 20 horas o más a la semana": 1,
                                                                               "Si, menos de 20 horas a la semana": 2})


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

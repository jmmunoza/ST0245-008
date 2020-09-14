import csv
# Acá se realizará la lectura de datos. Se crearon siete listas para guardar los datos de cada estudiante.
# 1. En la lista "personal_information" se guardarán datos del estudiante como su fecha de nacimiento, lugar de nacimiento, etc.
# 2. En la lista "socio_economic_information" se guardarán los datos socio-económicos del  estudiante y su familia.
# 3. En la lista "school_information" se guardarán los datos del colegio del estudiante, como su nombre, código del colegio, jornada, etc.
# 4. En la lista "score" se guardarán los puntajes del estudiante obtenidos en los ICFES.
# 5. En la lista "success" se guardarán la información de éxito del estudiante, si este superó o fracasó en el ICFES.
# 6. En la lista "student" se apilarán las cinco listas previas en el mismo orden en que fueron presentadas.
# 7. En la lista "students" se apilará la lista "student".

students, student, personal_information, socio_economic_information, school_information, score, success = [], [], [], [], [], [], [] 

with open("Nombre del archivo .csv", encoding="utf8") as f:
    reader = csv.reader(f, delimiter=";")
    first_pass = True
    for row in reader:
        if first_pass:
            first_pass = False
            continue
        #personal_ information:       0  = estu_consecutivo.1,      1  = estu_exterior,                2  = periodo,                        3  = estu_tieneetnia,
        #                             4  = estu_tomo_preparacion,   5  = estu_cursodocentesies,        6  = estu_iesapoyoexterno ,          7  = estu_cursoiesexterna,
        #                             8  = estu_simulacrotipoicfes, 9  = estu_actividadrefuerzoareas,  10 = estu_actividadrefuerzogeneric,  14 = estu_inst_cod_departamento,
        #                             15 = estu_tipodocumento.1,    16 = estu_nacionalidad.1,          17 = estu_genero.1,                  18 = estu_fechanacimiento.1,
        #                             19 = periodo.1,               20 = estu_estudiante.1,            21 = estu_pais_reside.1,             22 = estu_depto_reside.1,
        #                             23 = estu_cod_reside_depto.1, 24 = estu_mcpio_reside.1,          25 =  estu_cod_reside_mcpio.1,       26 = estu_areareside
        personal_information = [row[0],  row[1],  row[2],  row[3],  row[4],  row[5],  row[6],  row[7],  row[8],  row[9],  row[10],
                                row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24],
                                row[25], row[26]]
        #socio_economic_information:  11 = fami_trabajolaborpadre,  12 = fami_trabajolabormadre,     13 = fami_numlibros,         27 = estu_valorpensioncolegio,
        #                             28 = fami_educacionpadre.1,   29 = fami_educacionmadre.1,      30 = fami_ocupacionpadre.1,  31 = fami_ocupacionmadre.1,
        #                             32 = fami_estratovivienda.1,  33 = fami_nivelsisben,           34 = fami_pisoshogar,        35 = fami_tieneinternet.1,
        #                             36 = fami_tienecomputador.1,  37 = fami_tienemicroondas,       38 = fami_tienehorno,        39 = fami_tieneautomovil.1,
        #                             40 = fami_tienedvd,           41 = fami_tiene_nevera.1,        42 = fami_tiene_celular.1,   43 = fami_telefono.1,
        #                             44 = fami_ingresofmiarmensl,  45 = estu_trabajaactualmente,    46 = estu_antecedentes,      47 = estu_expectativas   
        socio_economic_information = [row[11], row[12], row[13], row[27], row[28], row[29], row[30], row[31], row[32],
                                      row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41],
                                      row[42], row[43], row[44], row[45], row[46], row[47]]
        #school_information:          48 = cole_codigo_icfes,       49 = cole_codigo_dane,           50 = cole_nombre,            51 = cole_genero,
        #                             52 = cole_naturaleza,         53 = cole_calendario             54 = cole_biligue,           55 = cole_caracter,
        #                             56 = cole_cod_dane_ sede,     57 = cole_nombre_sede,           58 = cole_sede_principal     59 = cole_area_ubicacion
        #                             60 = cole_jornada,            61 = cole_cod_mcipio_ubicacion   62 = cole_mcipio_ubicacion   63 = cole_cod_depto_ubicacion
        #                             64 = cole_depto_ubicacion
        school_information = [row[48], row[49], row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57],
                              row[58], row[59], row[60], row[61], row[62], row[63], row[64]]
        #score:                       65 = lenguaje,       66 = matematicas,    67 = biologia,       68 = quimica,        69 = fisica,
        #                             70 = sociales,       71 = filosofia,      72 = ingles,         73 = desemp_ingles,  74 = profundiza, 
        #                             75 = puntaje_prof,   76 = desemp_prof
        score = [int(float(row[65])), int(float(row[66])), int(float(row[67])), int(float(row[68])), int(float(row[69])),
                 int(float(row[70])), int(float(row[71])), int(float(row[72])), row[73], row[74], int(float(row[75])), row[76]]
        #success:                     77 = éxito (si es 0, no aprobó el ICFES, si es 1, aprobó el ICFES)
        success = [int(row[77])]
        student = [personal_information, socio_economic_information, school_information, score, success]
        students.append(student)

for i in range(len(students)):  
    print(students[i][3])
input()



        


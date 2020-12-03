#   Se importan las librerias de lectura de datos, pandas y la librería random, necesaria para los bosques aleatorios.

from Data_Processing import data_score_processing, data_socioeconomic_processing, data_score_socioeconomic_processing
import pandas as pd
import random

#   Se ingresa una columna variable y la columna objetivo. Se mira si las respuestas de la columna son
#   numericas o no numericas. Si son numericas, se promedian todos los datos de la columna y con este promedio
#   se creará la pregunta. Si no son numericas, se debe de separar el set de datos (variable como objetivos) en donde aparece la determinada
#   respuesta.
#   Se evalua cada dato de la columna en funcíon de la pregunta, si la pregunta arroja positivo, el contador de información postiva aumenta,
#   de lo contrario la información negativa aumenta. Luego se mira si la variable objetivo realmente coincide con el resultado, si es así
#   la informacion real positiva aumenta, de lo contrario la informacion real negativa aumenta.
#   Esto se hace para medir el porcentaje de fracaso y exito en los nodos hijos.
def proof_partition(column, target, answer_data=None, answer_num = None):
    true_data, false_data, true_real, false_real, question = 0, 0, 0, 0, None

    #   Se mira si son datos numericos o no
    if isinstance(column[0], (int,float)):

        #   Se promedian los datos
        sum_value = 0
        for n in range(len(column)):
            sum_value += column[n]
        prom_value = sum_value/len(column)

        #   Se crea la pregunta.
        question = Question(column.name, round(prom_value,2))

        #   Se evaluan los datos en funciion de la pregunta.
        for row in range(len(column)):
            if question.match(column[row]):
                true_data += 1

                #   Se mira si realmente el resultado es verdadero.
                if target[row] == True:
                    true_real += 1
            else:
                false_data += 1

                #   Se mira si realmente el resultado es falso.
                if target[row] == False:
                    false_real += 1
    else:

        #   Se crea la pregunta.
        question = Question(column.name, answer_data)

        #   Se evaluan los datos en funciion de la pregunta.
        for row in range(len(column)):
            if question.match(column[row]):
                true_data += 1

                #   Se mira si realmente el resultado es verdadero.
                if target[row] == True:
                    true_real += 1
            else:
                false_data += 1

                #   Se mira si realmente el resultado es falso.
                if target[row] == False:
                    false_real += 1

    return true_data, false_data, true_real, false_real, question



#   Este metodo se llama cuando ya se tiene la mejor pregunta del nodo, en base a esa pregunta se separan
#   las datos variables y objetivos al lado izquierdo o derecho y se retornan.
def real_partition(rows, target, question):
    left_data, right_data = pd.DataFrame(columns=rows.columns), pd.DataFrame(columns=rows.columns)
    left_target, right_target = [],[]
    for n in range(len(rows)):
        if question.match(rows[question.feature][n]):
            right_data = right_data.append(rows.loc[[n]],ignore_index=True)
            right_target.append(target[n])
        else:
            left_data = left_data.append(rows.loc[[n]],ignore_index=True)
            left_target.append(target[n])
    left_target = pd.Series(left_target)
    right_target = pd.Series(right_target)

    return left_data, right_data , left_target, right_target



#   Este método analiza el atributo que genera el menor indice de Gini. Cuando lo encuentra,
#   retorna el indice Gini junto a la mejor pregunta y los datos ya separados.
def best_split(rows, target):
    best_gini, best_question = 1, None
    #   Se repite el proceso con todos los atributos del dataset.
    for n_column in range(len(rows.columns)):
        column_name = rows.columns[n_column]
        #   Analiza si hay datos o ya se acabaron.
        if len(rows[column_name]) <= 0:
            #   Si ya no hay datos, se retorna todo en nulo.
            return 0, None, None, None, None, None

        #   Se mira si las respuestas del atributo son valores numericos o texto.
        if not isinstance(rows[column_name][0],(int, float)):

            #   Se busca en el atributo todas las respuestas posibles y cuantas veces se repiten.
            answers = n_values(rows[column_name])

            #   Como se tratan de respuestas no numericas, se debe evaluar el indice Gini con todas las respuestas de
            #   cada atributo.
            for n_answer in range(len(answers)):
                true_data, false_data, true_real, false_real, question = proof_partition(rows[column_name],
                                                                                        target,
                                                                                        answer_data=answers.index[n_answer],
                                                                                        answer_num=answers[n_answer])
                                
                #   Se calcula la impureza Gini de los nodos hijos
                gini_left, gini_right = calculate_Gini(true_data,
                                                       false_data,
                                                       true_real,
                                                       false_real)

                #   Se calcula la impureza Gini del nodo padre
                gini_split = calculate_split_Gini(true_data,
                                                  false_data,
                                                  gini_left,
                                                  gini_right)

                #   Se busca el menor indice Gini y se guarda tanto la mejor pregunta como el mejor Gini
                if best_gini > gini_split:
                    best_gini, best_question = gini_split, question
        else:

            #   Si se trata de valores numericos, no hay que calcular el Gini con cada posible respuesta.
            #   Se obtienen los datos que se dirigen al nodo izquierdo y derecho.
            true_data, false_data, true_real, false_real, question = proof_partition(rows[column_name], target)

            #   Se calcula la impureza Gini de los nodos hijos
            gini_left, gini_right = calculate_Gini(true_data,
                                                   false_data,
                                                   true_real,
                                                   false_real)

            #   Se calcula la impureza Gini del nodo padre
            gini_split = calculate_split_Gini(true_data,
                                              false_data,
                                              gini_left,
                                              gini_right)
            
            #   Se busca el menor indice Gini y se guarda tanto la mejor pregunta como el mejor Gini
            if best_gini > gini_split:
                best_gini, best_question = gini_split, question

    #   Una vez obtenido el mejor Gini y la mejor pregunta, se parten los datos en base a esa pregunta.
    left_data, right_data, left_target, right_target = real_partition(rows, target, best_question)

    #   Se retorna toda la información.
    return best_gini, best_question, left_data, right_data, left_target, right_target



#   Se calcula la impureza Gini de los nodos derechos e izquierdos y se retornan.
def calculate_Gini(true_data, false_data, true_real, false_real):
    if true_data == 0:
        true_percentage = 0
    else:
        true_percentage = true_real/true_data
    if false_data == 0:
        false_percentage = 0
    else:
        false_percentage = false_real/false_data

    gini_left = 1-((false_percentage**2) + ((1-false_percentage)**2))
    gini_right = 1-((true_percentage**2) + ((1-true_percentage)**2))

    return gini_left, gini_right



#    Se calcula la impureza Gini del nodo padre en función de la impureza de los nodos hijos.
def calculate_split_Gini(true_data, false_data, gini_left, gini_right):
    return round((((false_data*gini_left) + (true_data*gini_right))/(true_data+false_data)),2)



#   Si se tratan con datos socioeconomicos, se crea un diccionario que
#   contiene las respuestas de cada atributo y cuantas veces se repite
def n_values(column):
    dictionary_n_values = column.value_counts()
    return dictionary_n_values



#   Metodo de los bosques aleatorios, toma un dataset y lo parte en atributos aleatorios.
def partition_data(data_x, data_y, n_pass, sub_data, n_atributes_for_tree):
    x = data_x.iloc[n_pass*sub_data:(n_pass+1)*sub_data]
    part_y = data_y.iloc[n_pass*sub_data:(n_pass+1)*sub_data]
    part_x = pd.DataFrame()
    i = 0
    while i < n_atributes_for_tree:
        n_random = random.randint(0, len(x.columns)-1)
        if x.columns[n_random] in part_x.columns:
            continue
        part_x.insert(len(part_x.columns), x.columns[n_random], x.iloc[:,n_random], True)
        i += 1

    return part_x, part_y 



#   Clase en donde se contruyen los nodos de decision del arbol.
class Decission_node:
    def __init__(self, question=None, Gini=None, n_elements=None, answer=None, n_node=None):
        self.question = question
        self.Gini = Gini
        self.n_elements = n_elements
        self.n_node = n_node
        self.answer = answer
        self.izq = None
        self.der = None

    def __str__(self):
        print("Gini impurity: ", self.Gini)
        print("Question: ", self.question)
        print("N_elements: ", self.n_elements)
        return ""



#   Clase en donde se construye la pregunta de cada nodo.
class Question:
    def __init__(self, feature, value):
        self.feature = feature
        self.value = value

    def __str__(self):
        if isinstance(self.value, (int, float)):
            return str(self.feature) + " >= " + str(self.value)
        else:
            return str(self.feature) + " == " + str(self.value)

    def match(self, feature_example):
        if isinstance(feature_example, (int, float)):
            return feature_example >= self.value
        else:
            return feature_example == self.value











#   Clase en donde se construyen los arboles de decision.
class Decision_Tree:
    def __init__(self, depth=500, max_terminal_nodes=500):
        self.root = None
        self.depth = depth
        self.max_terminal_nodes = max_terminal_nodes

    #   Se puede crear el arbol con los datos x y datos y ya creados, o ingresando el nombre del archivo .csv
    def create_tree(self, file=None, data_x=None, data_y=None):
        if data_x is None and data_y is None:
            data_x, data_y = data_score_processing(file)
        self.root = self._create_tree(self.root, data_x, data_y)
        #   Una vez creado el arbol, se le asigna a cada nodo un identificador unico.
        cont, self.root = self._set_n_node(self.root, 0)


    #   Se crea el arbol de forma recursiva hasta que el indice Gini sea igual a 0, se alcance la profundidad maxima, o se 
    #   alcance la cantidad maxima de nodos.
    def _create_tree(self, root, data_x, data_y, max_terminal_nodes=0, max_depth=1, way=None):

        #   Se busca el mejor indice de Gini, junto con la mejor pregunta, de paso se retornan los datos
        #   separados en función a la pregunta.
        Gini, question, left_data, right_data, left_target, right_target = best_split(data_x, data_y)
        max_terminal_nodes+=1
        if root is None:
            root = Decission_node(question, Gini, len(data_y), answer=way)    
        
        #   Si la pregunta es nula, significa que ya no hay mas datos.
        if question is None:
            root = None

        elif Gini == 0 or max_depth == self.depth or max_terminal_nodes >= self.max_terminal_nodes:
            return root
            
        else:
            #   Se llama la hijo derecho del nodo con sus respectivos datos separados
            root.der = self._create_tree(root.der, right_data, right_target,
                                         max_terminal_nodes=max_terminal_nodes+1,
                                         max_depth=max_depth+1,
                                         way=True)

            #   Se llama el hijo izquierdo del nodo con sus respectivos datos separados
            root.izq = self._create_tree(root.izq, left_data, left_target,
                                         max_terminal_nodes=max_terminal_nodes+1,
                                         max_depth=max_depth+1,
                                         way=False)
        
        return root


    #   Se recorre el arbol en funcion a las preguntas de cada nodo hasta que llegue a una raiz y retorne la respuesta.
    def walk_tree(self, row):
        return self._walk_tree(row, self.root)

    def _walk_tree(self, row, root):
        if root.der is None and root.izq is None:
            return root.answer

        else:
            if root.question.match(row[root.question.feature]):
                
                return self._walk_tree(row, root.der)
            else:
                return self._walk_tree(row, root.izq)

    #   Retorna una lista en donde están almacenados las predicciones del arbol en base a un conjunto de atributos.
    def predict(self,rows):
        predict_data = []
        for n in range(len(rows)):
            value = self.walk_tree(rows.iloc[n])
            predict_data.append(value)
        return predict_data

    #   Compara los datos de predicción con los datos objetivos e imprime la certeza del arbol.
    def score(self, predict_data, target):
        cont = 0
        for n in range(len(predict_data)):
            if predict_data[n] == target[n]:
                cont += 1
        
        print("Acertó", cont, "veces de", len(predict_data))
        print("Tiene una tasa de acierto del", (cont/len(predict_data))*100, "%")
        return (cont/len(predict_data))*100

    #   Este metodo le asigna a los nodos un identeficador unico, necesario para imprimir el arbol
    def _set_n_node(self, root, cont):
        if root is not None:
            root.n_node = cont
            cont += 1
            cont, root.izq = self._set_n_node(root.izq, cont)
            cont, root.der = self._set_n_node(root.der, cont)
        return cont, root

    #   Imprime por pantalla la matríz de confusión del arbol.
    def confusion_matrix(self, prediction, testing):
        True_positive, True_negative, False_positive, False_negative = 0,0,0,0
        for i in range(len(prediction)):
            if prediction[i] == True and testing[i] == True:
                True_positive += 1
            elif prediction[i] == False and testing[i] == False:
                False_positive += 1
            elif prediction[i] == True and testing[i] == False:
                False_negative += 1
            else:
                True_negative += 1
        print("Confusion Matrix:")
        print()
        print("[",True_positive,",",False_negative,"]")          
        print("[",False_positive,",",True_negative,"]")
        print()


    #   Se crea el archivo .dot y se escribe en él el código que leerá Graphviz
    def export_tree(self, file_name, depth):
        file = open(file_name + ".dot", "w")
        file.write('graph ""{')
        file.write('n' + str(self.root.n_node) + ';')
        file.write('n' + str(self.root.n_node) + '[shape=box, style="rounded,filled", color=blue];')
        file = self._export_tree(self.root, file, depth)
        file.write("}")
        file.close()

    def _export_tree(self, root, file, depth, cont=0):
        if root is not None and cont != depth:
            file = self._export_tree(root.der, file, depth, cont=cont+1)
            file.write('n' + str(root.n_node) + '[label="' +
                       str(root.question) + "\n" + 'Gini: ' +
                       str(root.Gini) + "\n" + 'elements: ' +
                       str(root.n_elements) + '"];')
            file.write('n' + str(root.n_node) + '[shape=box, style="rounded,filled"];')
            if root.der is not None:
                file.write('n' + str(root.n_node) + ' -- n' + str(root.der.n_node) + ';')
            if root.izq is not None:
                file.write('n' + str(root.n_node) + ' -- n' + str(root.izq.n_node) + ';')
            file = self._export_tree(root.izq, file, depth, cont=cont+1) 
        return file














#   Clase en donde se crean los bosques aleatorios.
class Random_Forest:
    def __init__(self, n_trees=5, depth_trees=20, n_atributes_for_tree=5):
        self.trees = []
        self.n_trees = n_trees
        self.depth_trees = depth_trees
        self.n_atributes_for_tree = n_atributes_for_tree

    #   Se crean los arboles con variables aleatorias y se almacenan en el arreglos TREES.
    def create_forest(self, file):
        data_x, data_y = data_score_processing(file)
        sub_data = int(len(data_y)/self.n_trees)
        for n in range(self.n_trees):
            part_x, part_y = partition_data(data_x,
                                            data_y,
                                            n,
                                            sub_data,
                                            self.n_atributes_for_tree)
            part_x.index, part_y.index = range(len(part_x.index)), range(len(part_y.index))
            Arbol = Decision_Tree(depth=self.depth_trees)
            Arbol.create_tree(data_x = part_x, data_y = part_y)
            self.trees.append(Arbol)
            print("Arbol numero", n, "creado con exito")

    #   Se predice cada arbol y se almacena que resultado arroja, el resultado con mas votos será el que se 
    #   agrege a la lista de predicción.
    def predict(self, rows):
        predict_data = []
        for i in range(len(rows)):
            true_votes, false_votes = 0, 0
            for n in range(self.n_trees):
                if self.trees[n].walk_tree(rows.iloc[i]) == True:
                    true_votes += 1
                else:
                    false_votes += 1
            if true_votes >= false_votes:
                predict_data.append(True)
            else:
                predict_data.append(False)
        return predict_data

    #   Compara los datos de predicción con los datos objetivos e imprime la certeza del bosque.
    def score(self, predict_data, target):
        cont = 0
        for n in range(len(predict_data)):
            if predict_data[n] == target[n]:
                cont += 1

        print("Acertó", cont, "veces de", len(predict_data))
        print("Tiene una tasa de acierto del", (cont/len(predict_data))*100, "%")
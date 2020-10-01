from Decision_Tree import create_tree_score, create_tree_score_socioeconomic, create_tree_socioeconomic
from sklearn.tree import DecisionTreeClassifier
from Data_Processing import data_score_processing, data_score_socioeconomic_processing, data_socioeconomic_processing

Arbol = create_tree_score("TRAIN 3")
x, y = data_score_processing("TEST 4")
print("Score:")
print(Arbol.score(x, y)* 100, "%")
print()

Arbol1 = create_tree_score_socioeconomic("TRAIN 3")
x1, y1 = data_score_socioeconomic_processing("TEST 4")
print("Score and socioeconomic:")
print(Arbol1.score(x1, y1)* 100, "%")
print()

Arbol2 = create_tree_socioeconomic("TRAIN 3")
x2, y2 = data_socioeconomic_processing("TEST 4")
print("Socioeconomic:")
print(Arbol2.score(x2, y2)* 100, "%")
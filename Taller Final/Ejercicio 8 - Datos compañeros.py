class Alumno:
    def __init__(self, nombre, edad, gustos):
        self.nombre = nombre
        self.edad = edad
        self.gustos = gustos

    def __str__(self):
        print("Estudiante " + str(self.nombre) + ": ")
        print("Tiene una edad de " + str(self.edad) + " años.")
        print("Sus gustos y pasatiempos son: ")
        for i in self.gustos:
            print("     - " + i)
            print()
        return ""

class Nodo:
    def __init__(self, datos = None, siguiente = None):
        self.datos = datos
        self.siguiente = siguiente

class linked_list: 
    def __init__(self):
        self.primero = None
    
    # Método para agregar elementos a la lista
    def agregar(self, datos):
        self.primero = Nodo(datos=datos, siguiente=self.primero) 

    # Método para imprimir la lista de nodos
    def mostrar( self ):
        nodo = self.primero
        while nodo != None:
            print(nodo.datos)
            nodo = nodo.siguiente

lista = linked_list() # Instancia de la clase

"""
    Se agregan todos lo estudiantes.
"""
lista.agregar(Alumno('Juan Felipe Agudelo Vélez', 17, ["gusta de le música blues y jazz",
                                                       "toca guitarra electrica",
                                                       "le gusta el plato tipico de Antioquia"]))

lista.agregar(Alumno('Simón Gómez Arango', 17, ["gusta de escuchar musica",
                                                "ver peliculas",
                                                "leer libros con fuertes mensajes y de terror cosmico",
                                                "Desea procrastinar menos"]))

lista.agregar(Alumno('Jose Miguel Blanco Velez', 17, ["gusta de Escuchar musica trap",
                                                       "jugar videojuegos RPG",
                                                       "ver streaners cono Tyler1 o Asnonbald",
                                                       "alaba a CRISTO REY"]))

lista.agregar(Alumno('Donovan Castrillon Blanco', 17, ["gusta de el baloncesto",
                                                       "ver anime",
                                                       "dormir tarde",
                                                       "escuchar la bebecita bebe lean",
                                                       "traumado con lógica",
                                                       "roba frijoles"]))

lista.agregar(Alumno('Daniel Garcia Salcedo', 18, ["gusta de hacer y escuchar Freestyle",
                                                   "ademas de ser un amante del genero Shooter de los videojuegos"]))

lista.agregar(Alumno('Daniel Gonzales Bernal', 29, ["gusta de viajar por Colombia",
                                                    "tiene una pasion por las motos",
                                                    "solia estudiar medicina",
                                                    "cambió por algo que le gusta mas: sistemas",
                                                    "es calvo"]))

lista.agregar(Alumno('Harold Steven Gonzales Ossa', 17, ["gusta de leer",
                                                         "jugar videojuegos",
                                                         "ver peliculas",
                                                         "estudia Ing. Matematica porque le entretienen las matematicas",
                                                         "esta en busca de su enfoque",
                                                         "es un crack programando"]))

lista.agregar(Alumno('Daniel Andres Hérnander Oyola', 17, ["gusta de los deportes, como el futbol",
                                                           "la comida",
                                                           "la musica",
                                                           "los videojuegos como lo son Halo",
                                                           "alguien de pocas palabras a la hora de presentarse"]))

lista.agregar(Alumno('Juan Felipe Martinez Bedoya', 22, ["jugar videojuegos MOBA y APG",
                                                         "tiene muchos mas gustos como lo son el futbol",
                                                         "ir al gimasio",
                                                         "Ya casi se gradúa asi que a ponerle ánimo!"]))

lista.agregar(Alumno('Julian Andres Mazo Zapata', 17, ["gusta de tocar guitarra acustica y electrica",
                                                       "leer",
                                                       "jugar videojuegos RPG",
                                                       "pasar tiempo virtual o fisico con sus amigos y hacer nuevos"]))

lista.agregar(Alumno('Mylle Scarleth Mosquera Rivas', 17, ["gusta de la música, especialmente salsa, bachata y pop",
                                                          "le gusta bailar",
                                                          "dibujar",
                                                          "leer",
                                                          "es estudiante de Ing. Matenética"]))

lista.agregar(Alumno('Juan Manuel Muñoz Arias', 17, ["Escuchar Gorillaz, Alcolirykoz y Eri gey",
                                                     "Jugar videojuegos, sobre todo Valorant",
                                                     "alaba a cristo Rey"]))

lista.agregar(Alumno('Jayder Ochoa Carvajal', 17, ["guste de ver anime",
                                                   "peliculas aunque no es su gran pasión",
                                                   "se le da bien dibujar",
                                                   "esta en un proceso de autodescubrimiento y aprender cosas nuevas"]))

lista.agregar(Alumno('Santiago Parra Mejia', 16, ["gusta de tocar piano",
                                                  "es muy apasionado con la musica",
                                                  "es introvertido pero trata de abrirse más",
                                                  "decir que ama a Cristo Rey es decir poco"]))

lista.agregar(Alumno('Jose Manuel Ramirez Gomez', 17, ["gusta de Hacer misica electrónica",
                                                       "ugar videojuegos Shooter es su mayor pasatienpo",
                                                       "la matematica pura",
                                                       "de los pocos ingenieros matematicos del grupo"]))

lista.agregar(Alumno('Diego velésquez Varela', 17, ["gusta de tocar guitarra y armónica",
                                                    "escuchar musica alternativa y acistica",
                                                    "su pelicula favorita es interstellar",
                                                    "estudia Ing. matemátic"]))

lista.agregar(Alumno('Salomon Velez Perez', 17, ["gusta de Escribir",
                                                 "jugar videojuegos como League of Legends u Overwatch",
                                                 "puede hablar de JoJos por horas"]))

lista.agregar(Alumno('Cristian Camilo Zapata Garcia', 18, ["gusta de hacer impresionantes presentaciones no aburridas",
                                                           "jugar videojuegos",
                                                           "ver anime",
                                                           "viajar y probar de todo"]))
                                                           
lista.mostrar() # Imprimimos la lista
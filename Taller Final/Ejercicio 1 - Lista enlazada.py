class Nodo:
    def __init__(self, valor):
         self.valor = valor
         self.siguiente = None
    def __str__(self):
        return str(self.valor)

class linkedList:
    def __init__(self):
        self.primero = None
        self.size = 0
    def Append(self, valor):
        miNodo = Nodo(valor)
        if(self.size==0):
            self.primero = miNodo
        else:
            current = self.primero
            while(current.siguiente!=None):
                current = current.siguiente
            current.siguiente = miNodo
        self.size += 1
        return miNodo
    def remove(self, valor):
        if(self.size==0):
            return False
        else:
            current = self.primero
            while(current.siguiente.valor!=valor):
                if(current.siguiente==None):
                    return False
                else:
                    current = current.siguiente
            nodoBorrado = current.siguiente
            current.siguiente = nodoBorrado.siguiente
            self.size -= 1
            return nodoBorrado
    def __len__(self):
        return self.size
    def __str__(self):
        string = "["
        current = self.primero
        while(current!=None):
            string += str(current)
            string += str(",")
            current = current.siguiente
        string += "]"
        return string

miLista = linkedList()
miLista.Append(1)
miLista.Append(2)
miLista.Append(3)
miLista.Append("hola")
miLista.Append(0.15)
miLista.Append(["mundo",5,2,3,24])
print("Mi lista es: ", miLista)
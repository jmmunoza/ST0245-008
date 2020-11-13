class Pila:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
    
    def verificar(self):
        return len(self.items)==0

    def promedio(self):
      sum = self.items[0]
      for i in range(len(self.items)-1):
        sum = sum+self.items[i+1]
      prom = sum/len(self.items)
      return prom

    def inspeccionar(self):
        assert not self.verificar()
        return self.items[-1]

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        assert not self.verificar()
        return  self.items.pop()

    def peek(self):
        if len(self.items)>0:
            return self.items[-1]
        else:
            return None


miPila = Pila()
miPila.apilar(11)
miPila.apilar(22)
miPila.apilar(33)
miPila.apilar(44)
print(miPila)
print(miPila)
print("El promedio de los elementos de la pila es:", miPila.promedio())
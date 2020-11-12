class Pila:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def no_vacia(self):        
        return len(self.items) == 0

    def promedio(self):
      sum = self.items[0]
      for i in range(len(self.items)-1):
        sum = sum+self.items[i+1]
      prom = sum/len(self.items)
      return prom

    def getTop(self):
        return self.items[len(self.items)-1]

    def inspeccionar(self):
        assert not self.verificar()
        return self.items[-1]

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        assert not self.no_vacia()
        return  self.items.pop()

    def peek(self):
        if len(self.items)>0:
            return self.items[-1]
        else:
            return None

def invertir_pila(pila):
    pila_invertida = Pila()
    while not pila.no_vacia():
        pila_invertida.apilar(pila.getTop())
        pila.desapilar()
    return pila_invertida

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
pila.apilar(6)

print(pila.items)
pila = invertir_pila(pila)
print(pila.items)
    


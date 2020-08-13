# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def Imprimir_cada_letra(str, a = 0):  
    a += 1
    if a > len(str):
        return ""
    print(str[:a])
    Imprimir_cada_letra(str, a)

str = input("Dame una cadena de texto: ")
Imprimir_cada_letra(str)
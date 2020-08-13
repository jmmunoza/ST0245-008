# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def Palabra_invertida(str):
    if len(str) == 0:
        return ""
    print(str[len(str)-1], end="")
    Palabra_invertida(str[:-1])

str = input("Dame una palabra: ")
Palabra_invertida(str)

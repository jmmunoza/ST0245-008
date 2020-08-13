# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def palindromo(str):
    if len(str) <= 1:
        print("Es palindromo o carpicuo")
        return "" 
    if str[0] == str[len(str)-1]:
        return palindromo(str[1:-1])
    print("NO es palindromo o carpicuo")

str = input("Dame un número o una palabra:")
palindromo(str)
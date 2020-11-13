from os import system

def Nuggets2(n_nugget, i):
    if ((n_nugget - i) % 6 == 0 or (n_nugget - i) % 9 == 0 or (n_nugget - i) % 20 == 0) and n_nugget - i >= 0:
        return True
    return False

def Nuggets(n, n_6 = 0, n_9 = 0, n_20 = 0):
    if n == 0:
        print("Si es posible hacer el pedido")
        if n_6 != 0:
            print("con", n_6, "caja(s) de 6")

        if n_9 != 0:
            print("con", n_9, "caja(s) de 9")

        if n_20 !=0:
            print("con", n_20, "caja(s) de 20")
        print()
        return True
    else:    
        for i in range(1,n+1):
            if i < n:
                if Nuggets2(n, i*20):
                    Nuggets(n-(i*20), 
                            n_6=n_6,
                            n_9=n_9,
                            n_20=n_20+i)
                    break

                if Nuggets2(n, i*9):
                    Nuggets(n-(i*9), 
                            n_6=n_6,
                            n_9=n_9+i,
                            n_20=n_20)
                    break

                if Nuggets2(n, i*6):
                    Nuggets(n-(i*6), 
                            n_6=n_6+i,
                            n_9=n_9,
                            n_20=n_20)
                    break

                if Nuggets2(n, i*15):
                    Nuggets(n-(i*15), 
                            n_6=n_6+i,
                            n_9=n_9+1,
                            n_20=n_20)
                    break

                if Nuggets2(n, i*26):
                    Nuggets(n-(i*26), 
                            n_6=n_6+i,
                            n_9=n_9,
                            n_20=n_20+1)
                    break

                if Nuggets2(n, i*29):
                    Nuggets(n-(i*29), 
                            n_6=n_6,
                            n_9=n_9+1,
                            n_20=n_20+1)
                    break

                if Nuggets2(n, i*35):
                    Nuggets(n-(i*35), 
                            n_6=n_6+1,
                            n_9=n_9+1,
                            n_20=n_20+1)
                    break
            else:
                print("No es posible hacer el pedido")
                return False

while True:
    
    print("___________________________________")
    a = int(input("Ingresa el numero de Nuggets: "))
    system("cls")
    print("Numero de Nuggets:", a)
    Nuggets(a)
    
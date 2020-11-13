
#   5.1
for i in range(n):   # <-- El for posee una complejidad de 2n+2
    if i % 2 == 0:   # <-- Se hace dicha comparacion n veces
        print(i)     # <-- Puede o no ejecutarse esta accion

#   Este código en notación big O se denota O(n).
#   En el mejor de los casos, que es cuando no se ejecuta
#   el print, tiene una complejidad de 3n + 2.
#   
#   En el peor de los casos, que es cuando se ejecuta el
#   print, tiene una complejidad de 4n + 2.

#   5.2
for i in range(n):   # <-- El for posee una complejidad de 2n+2
    if i % 2 == 0:   # <-- Se hace dicha comparacion n veces
        print(i)     # <-- Puede o no ejecutarse esta accion

for i in range(n):   # <-- El for posee una complejidad de 2n+2
    if i % 2 != 0:   # <-- Se hace dicha comparacion n veces
        print(i)     # <-- Puede o no ejecutarse esta accion

#   Este código en notación big O se denota O(n).
#   No existe un mejor o peor caso, ya que como se puede ver,
#   la instruccion print que no se ejecute en el primer for,
#   se ejecutará si o si en el segundo for. es por esto que su
#   complejidad siempre sera de 7n + 4.

#   5.3
i = 1               # <-- declaración, complejidad 1
while i < n:        # <-- while, complejidad de n veces
    print(i)        # <-- esta accion se repite n - 1 veces
    i = i * 2       # <-- asignacion, se repite n - 1veces

#   Este codigo en notación big O se denota O(logn).
#   No se posee mejor ni peor caso, pero si trampa. Debido a que
#   El i no aumenta de uno en uno, si no que aumenta de forma
#   exponencial, de 2^n.
#   Con ayuda de excel, la ecuación que más se aproxima a la complejidad
#   real es 5 ln(x) + 2.

#   5.4
for i in range(n):  # <-- declaracion for, complejidad 2n + 2
    j = 1           # <-- declaracion j, complejidad n
    while j < n:    # <-- declaracion while, complejidad n^2
        print (j)   # <-- print, complejidad n^2 - n
        j = j * 2   # <-- asignacion j, n^2 - n

#   Aunque con la presencia del aumento cuadratico de j en el segundo while,
#   se siguen contando con fors y whiles anidados, por lo que la complejidad en big O
#   es de O(n^2)
#   Fue dificil plantear una ecuacion, pero con ayuda de excel. La ecuación más aproximada
#   a la complejidad fue 5.22n ^ (1.46)

#   5.5

n = 1000            # <-- declaracion, complejidad 1
if n % 2 == 0:      # <-- comparacion, complejidad 1
    print("par")    # <-- esta sentencia puede o no ocurrir (si ocurre, su complejidad es 1)
else:               
    print("impar")  # <-- esta sentencia puede o no ocurrir (si ocurre, su complejidad es 1)

#   La complejidad de este codigo es la más baja de todas, ya que es constante. No importa
#   si el if sea true o false, si o si se imprimirá par o impar. Es por esto que su complejidad
#   es de 3. En notación big O, cuando se tratan de complejidades constantes se denota O(1)
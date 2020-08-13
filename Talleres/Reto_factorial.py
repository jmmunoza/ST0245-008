import time

# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez
def get_recursive_factorial(n):
    if n == 0:
        return 1
    return n * get_recursive_factorial(n-1)

def get_iteractive_factorial(n):
    res = 1
    i = 1
    while i <= n:
        res *= i
        i+=1
    return res

n = int(input("Dame un numero: "))

start_time = time.time()
get_iteractive_factorial(n)
print("Iteration--- %s seconds ---" % (time.time() - start_time))
print(get_iteractive_factorial(n))

start_time = time.time()
get_recursive_factorial(n)
print("Recursion--- %s seconds ---" % (time.time() - start_time))
print(get_recursive_factorial(n))


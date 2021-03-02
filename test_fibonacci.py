#Variable que contiene los digitos para la validación pan digital
digitos = "123456789"

# Función recursiva que calcula la secuencia de Fibonacci. 
# No es práctica debido a que Python no maneja muy bien la recursión y la tiene limitada
# a: parámetro que con el valor n-1
# b: parámetro con el valor n-2
# total: parámetro que contiene el total de iteraciones, K
def fibonacci_recursivo(a, b, total):
    secuencia = str(a)
    inicio = secuencia[:9]
    fin = secuencia[-9:]

    if set(inicio) == set(digitos) and set(fin) == set(digitos):
        print("Secuencia Fibonacci: " + secuencia)
        print("")
        print("El valor de K es: {k}, los primeros 9 digitos son: {inicio}, los últimos 9 digitos son: {fin}".format(k = total, inicio = inicio, fin = fin))
    else:
        fibonacci_recursivo(b, (a + b), (total+1))

# Función que implementa un ciclo WHILE para calcular la secuencia Fibonacci.
def fibonacci_ciclo():
    a, b = 0 , 1
    total = 0
    secuencia = str(a)
    inicio = secuencia[:9]
    fin = secuencia[-9:]

    while not (set(inicio) == set(digitos) and set(fin) == set(digitos)):
        a, b = b, a + b
        secuencia = str(a)
        inicio = secuencia[:9]
        fin = secuencia[-9:]
        total += 1
        
    print("Secuencia Fibonacci: " + secuencia)
    print("")
    print("El valor de K es: {k}, los primeros 9 digitos son: {inicio}, los últimos 9 digitos son: {fin}".format(k = total, inicio = inicio, fin = fin))


if __name__ == "__main__":
    #fibonacci_recursivo(0, 1, 0)
    fibonacci_ciclo()
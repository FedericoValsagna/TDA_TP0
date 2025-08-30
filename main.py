import time
# Corrida Inicial: 160 segundos

# Primera optimización (98 segundos):
#   Inicialmente, para cada número se calcula la sumatoria de divisores de su potencial amigo, se decide eliminar ese
#   cálculo, pero guardando en un diccionario el potencial amigo de cada número. Al final se compara el potencial
#   amigo de cada número, si coinciden entonces efectivamente son potenciales amigos. Esta optimización hace que no se
#   puedan ver los amigos al pasar, sino que se muestren todos al final.

# Segunda optimización (49 segundos):
#   Para calcular los divisores de un número N se estaba iterando hasta N - 1, cuando realmente no es necesario. El
#   divisor más alto que va a tener un número no puede ser mayor a la mitad, por lo que solo tiene sentido iterar hasta
#   N / 2.

def es_primo(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    if n < 2:
        return []
    primos = []
    primos.append(2)
    for i in range(3, n, 2):
        if es_primo(i):
            primos.append(i)
    return primos


def factorizacion(n, primos):
    factores = {}
    i = 0
    while n > 1:
        if n % primos[i] != 0:
            i += 1
            continue
        if primos[i] not in factores:
            factores[primos[i]] = 1
        else:
            factores[primos[i]] = factores[primos[i]] + 1
        n = n // primos[i]
    return factores
    
def divisores(n, factores: dict):
    divs = []
    factor, exponente = factores.popitem()
    for i in range(exponente + 1):
        resultado = factor ** i
        if resultado != n:
            divs.append(resultado)

    for factor, exponente in factores.items():
        largo_inicial = len(divs)
        for i in range(1, exponente + 1):
            for j in range(largo_inicial):
                resultado = (factor ** i) * divs[j]
                if resultado != n:
                    divs.append(resultado)

    return divs

def amigos(MAX):
    t_inicial = time.time()
    potencial_amigo = {}
    p = primos_hasta(MAX)
    for n in range(2, MAX):
        potencial_amigo[n] = sum(divisores(n, factorizacion(n, p)))
    print(0,0)
    for numero, potencial in potencial_amigo.items():
        if potencial in potencial_amigo.keys() and potencial_amigo[potencial] == numero:
            print(numero, potencial)

    t_final = time.time()
    print(t_final - t_inicial)

amigos(100000)

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
def amigos(MAX):
    t_inicial = time.time()
    potencial_amigo = {}
    for numero in range(MAX):
        sumatoria_de_divisores = 0
        for j in range(1, numero // 2 + 1):
            if numero % j == 0:
                sumatoria_de_divisores += j
        potencial_amigo[numero] = sumatoria_de_divisores

    for numero, potencial in potencial_amigo.items():
        if potencial in potencial_amigo.keys() and potencial_amigo[potencial] == numero:
            print(numero, potencial)

    t_final = time.time()
    print(t_final - t_inicial)


amigos(100000)

import time
# Corrida Inicial: 160 segundos
# Primera optimización (98 Segundos):
#   Inicialmente, para cada número se calcula la sumatoria de divisores de su potencial amigo, se decide eliminar ese
#   cálculo, pero guardando en un diccionario el potencial amigo de cada número. Al final se compara el potencial
#   amigo de cada número, si coinciden entonces efectivamente son potenciales amigos. Esta optimización hace que no se
#   puedan ver los amigos al pasar, sino que se muestren todos al final.
def amigos(MAX):
    t_inicial = time.time()
    potencial_amigo = {}
    for numero in range(MAX):
        sumatoria_de_divisores = 0
        for j in range(1, numero):
            if numero % j == 0:
                sumatoria_de_divisores += j
        potencial_amigo[numero] = sumatoria_de_divisores

    for numero, potencial in potencial_amigo.items():
        # sumdiv(n) = m
        # sumdiv(m) = n
        if potencial in potencial_amigo.keys() and potencial_amigo[potencial] == numero:
            print(numero, potencial)

    t_final = time.time()
    print(t_final - t_inicial)


amigos(100000)

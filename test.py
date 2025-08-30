resultado_esperado_100000 = [(0, 0),(6, 6),(28, 28),(220, 284),(284, 220),(496, 496),(1184, 1210),(1210, 1184),(2620, 2924),(2924, 2620),(5020, 5564),(5564, 5020),(6232, 6368),(6368, 6232),(8128, 8128),(10744, 10856),(10856, 10744),(12285, 14595),(14595, 12285),(17296, 18416),(18416, 17296),(63020, 76084),(66928, 66992),(66992, 66928),(67095, 71145),(69615, 87633),(71145, 67095),(76084, 63020),(79750, 88730),(87633, 69615),(88730, 79750)]

def es_primo(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def primos(n):
    if n < 2:
        return []
    p = []
    p.append(2)
    for i in range(3, n, 2):
        if es_primo(i):
            p.append(i)
    return p


def factorizacion(n, primos):
    f = {}
    i = 0
    while n > 1:
        if n % primos[i] != 0:
            i += 1
            continue
        if primos[i] not in f:
            f[primos[i]] = 1
        else:
            f[primos[i]] = f[primos[i]] + 1
        n = n // primos[i]
    return f
    
def divisores(n, factores: dict):
    d = []
    factor, exponente = factores.popitem()
    for i in range(exponente + 1):
        r = factor ** i
        if r != n:
            d.append(r)

    for factor, exponente in factores.items():
        largo_inicial = len(d)
        for i in range(1, exponente + 1):
            for j in range(largo_inicial):
                r = (factor ** i) * d[j]
                if r != n:
                    d.append(r)

    return d

def amigos_test(MAX):
    potencial_amigo = {}
    p = primos(MAX)
    for n in range(2, MAX):
        # d = divisores(n, factorizacion(n,p))
        if n == 220:
            pass
        d = divisores(n, factorizacion(n, p))
        if n == 220 or n == 284:
            print(f"N: {n}  | Sum: {sum(d)}  | Div: {d}")
        sumatoria_de_divisores = sum(d)
        potencial_amigo[n] = sumatoria_de_divisores

    r = [(0,0)]
    for numero, potencial in potencial_amigo.items():
        if potencial in potencial_amigo.keys() and potencial_amigo[potencial] == numero:
            r.append((numero, potencial))
    return r

def amigos_original(MAX):
    res = {}
    for i in range(MAX):
        d = []
        s = 0
        for j in range(1, i - 1 + 1):
            if i % j == 0:
                d.append(j)
                s += j
        res[i] = (d, s)
    return res



def testi(MAX):
    r = {}
    p = primos(MAX)
    for n in range(2, MAX):
        d = divisores(n, factorizacion(n, p))
        r[n] = (d, sum(d))
    return r


def a():
    N = 100000
    expected = amigos_original(N)
    obtained = testi(N)
    matches = 0
    for n, r in expected.items():
        if n == 0 or n == 1:
            continue
        d, sumatoria = r
        if obtained[n][1] != sumatoria:
            print(f"N: {n} | Esum: {sumatoria} | Osum: {obtained[n][1]}")
            print(f"Ediv: {d}")
            print(f"ODiv: {obtained[n][0]}")
        else:
            matches += 1
    
    print(f"Matches: {matches} / {len(expected)}")
    


def test_100000():
    # a()
    resultado_obtenido = amigos_test(100000)
    print(resultado_obtenido)
    print(f"Parejas Obtenidas: {len(resultado_obtenido)}")
    print(f"Parejas Esperadas: {len(resultado_esperado_100000)}")
    for par in resultado_esperado_100000:
        if par not in resultado_obtenido:
            print(f"Discrepancy: {par}")
    assert resultado_obtenido == resultado_esperado_100000
    print("OK TEST!")

test_100000()

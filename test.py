resultado_esperado_100000 = [(0, 0),(6, 6),(28, 28),(220, 284),(284, 220),(496, 496),(1184, 1210),(1210, 1184),(2620, 2924),(2924, 2620),(5020, 5564),(5564, 5020),(6232, 6368),(6368, 6232),(8128, 8128),(10744, 10856),(10856, 10744),(12285, 14595),(14595, 12285),(17296, 18416),(18416, 17296),(63020, 76084),(66928, 66992),(66992, 66928),(67095, 71145),(69615, 87633),(71145, 67095),(76084, 63020),(79750, 88730),(87633, 69615),(88730, 79750)]

def amigos_test(MAX):
    potencial_amigo = {}
    for numero in range(MAX):
        sumatoria_de_divisores = 0
        for j in range(1, numero // 2 + 1):
            if numero % j == 0:
                sumatoria_de_divisores += j
        potencial_amigo[numero] = sumatoria_de_divisores

    r = []
    for numero, potencial in potencial_amigo.items():
        if potencial in potencial_amigo.keys() and potencial_amigo[potencial] == numero:
            r.append((numero, potencial))
    return r


def test_100000():
    resultado_obtenido = amigos_test(100000)
    assert resultado_obtenido == resultado_esperado_100000
    print("OK TEST!")

test_100000()




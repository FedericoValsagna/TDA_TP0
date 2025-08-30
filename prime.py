from math import sqrt


def primos(n):
    if n < 2:
        return []
    primes = []
    primes.append(2)
    for i in range(3, n, 2):
        if es_primo(i):
            primes.append(i)
    return primes

def es_primo(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def factorizacion(n, primos):
    last_index_prime = binary_search(n // 2, primos, 0, len(primos) - 1)
    f = []
    i = 0
    while (n > 1):
        if (n % primos[i] != 0):
            i += 1
            continue
        f.append(primos[i])
        n = n // primos[i]
    return f
    


def binary_search(n, array, initial_index, end_index):
    arr_length = end_index - initial_index + 1
    mid_index = initial_index + arr_length // 2
    # Casos Base
    if arr_length < 1:
        return initial_index
    if arr_length == 1:
        return mid_index
    if arr_length <= 2:
        if array[initial_index] >= n:
            return initial_index
        else:
            return end_index

    # Caso General
    if array[mid_index] == n:
        return mid_index
    if array[mid_index] > n:
        return binary_search(n, array, initial_index, mid_index)
    if array[mid_index] < n:
        return binary_search(n, array, mid_index + 1, end_index)
    

# # Main
# n = 1000
# p = primos(n)
# m = 5
# # print(primos(m))
# print(factorizacion(m, p))
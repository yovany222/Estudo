import math

def fatorando(n):
    fatores_primos = []

    while n % 2 == 0:
        fatores_primos.append(2)
        n //= 2

    limite = math.sqrt(n+1)
    i = 3
    while i <= limite:
        if n % i == 0:
            fatores_primos.append(i)
            n //= i
            limite = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        fatores_primos.append(n)
    return fatores_primos

print(max(fatorando(600851475143)))
# Maior fator primo de 600851475143

def fatores_primos(n):

    while n % 2 == 0 and n != 2 :
        n = n/2
    i = 3
    while i < n ** 0.5:
        if n % i == 0:
            n = n / i
        i = i + 2
    return n 

            
print(int(fatores_primos(600851475143)))

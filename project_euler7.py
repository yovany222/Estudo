def primo(n):
     if n < 2:
          return False
     for i in range(2,int((n**0.5)+1)):
          if n % i == 0:
              return False
     return True

def primos_ate_x(x):
    primos = []
    contador = 0
    numero = 2
    
    while contador < x:
        if primo(numero):
            primos.append(numero)
            contador += 1
        numero += 1
    
    return primos

print(primos_ate_x(10001))

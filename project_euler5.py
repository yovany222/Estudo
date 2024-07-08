def verificacao(num, limite):
     for i in range(1, limite + 1):
         if num % i != 0:
             return False
     return True

def encontrar_numero(limite):
    num = limite
    while True:
        if verificacao(num, limite):
            return num
        num += 1

limite = 20
resultado = encontrar_numero(limite)
print(f"O menor número divisível por todos os números de 1 a {limite} é {resultado}")
          

# Maior número palindromo resultado do produto de 2 números de 3 dígitos

def eh_palindromo(n):
    return str(n) == str(n)[::-1]

def maior_palindromo():
    maior_pal = 0
    for i in range(999, 99, -1): 
        for j in range(i, 99, -1): 
            produto = i * j
            if eh_palindromo(produto) and produto > maior_pal:
                maior_pal = produto
    return maior_pal

print(maior_palindromo())

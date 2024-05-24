primeiro_numero = 0
segundo_numero = 1
terceiro_numero = 0
soma = 0

while primeiro_numero < 4000000:

    print(primeiro_numero)
    terceiro_numero = primeiro_numero + segundo_numero
    primeiro_numero = segundo_numero
    segundo_numero = terceiro_numero
    
    if primeiro_numero % 2 == 0:
        soma = soma + primeiro_numero

print(f"A soma dos pares é: {soma}")

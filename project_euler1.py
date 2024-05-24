def multiplos(i):
    if i % 5 == 0 and i % 3 != 0:
        return 'Sou divisível por 5'
    if i % 3 == 0 and i % 5 != 0:
        return 'Sou divisível por 3'
    if i % 3 == 0 and i % 3 == 0:
        return 'Sou divisível por 3 e 5'

soma = 0

for i in range(1,1000):
    if multiplos(i) == 'Sou divisível por 5':
        print(f'Sou divisível por 5: {i}')
        soma = soma + i
    if multiplos(i) == 'Sou divisível por 3':
        print(f'Sou divisível por 3: {i}')
        soma = soma + i
    if multiplos(i) == 'Sou divisível por 3 e 5':
        print(f'Sou divisível por 3 e 5: {i}')
        soma = soma + i

print(f'Soma de todos os números acima: {soma}')
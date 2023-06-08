# Operadores in e not in
# Strings são iteráveis
#  0  1  2  3  4  5
#  A  r  t  h  u  r
# -6 -5 -4 -3 -2 -1

nome = 'Arthur'
print(nome[2])
print(nome[-4])

print('t' in nome)
print('z' in nome)
print('ur' in nome)
print('Art' not in nome)
print('zero' in nome)

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')


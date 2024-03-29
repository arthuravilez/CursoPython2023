"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuáriio não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número: ")

if numero.isdigit():
    numero_int = int((numero))
    if numero_int % 2 == 0:
        print(f'O número digitado foi {numero_int} e ele é par!!!')
    else:
        print(f'O número digitado foi {numero_int} e ele é ímpar!!!')
else:
    print("Favor digiar somente números inteiros")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# digita_hora = int(input("Digite a hora 0 a 23: "))

# dia = list(range(12))
# tarde = list(range(12, 18))
# noite =  list(range(18, 24))

# if digita_hora in dia:
#     print('Bom dia')
# elif digita_hora in tarde:
#     print('Boa tarde')
# elif digita_hora in noite:
#     print('Boa noite')
# else:
#     print('Não encontrado!')

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <=17:
        print('Boa tarde')
    elif hora >= 18 and hora <=23:
        print('Boa noite')
    else:
        print('Não conheço esse hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")

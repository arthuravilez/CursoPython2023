"""
Exercício
Peça ao usuário para digitar seu nome
Peça para o usuário digitar sua idade
Se nome e idade forem digitados:
    Exiba nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem{n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    print(f'Seu nome é: {nome}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaço')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome contém: {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe você deixou os campos nome e idade vazios')
    
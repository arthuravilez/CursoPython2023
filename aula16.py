# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar"ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print('Eba você ganhou um voucher para ir ao cinema!!!')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair')

print('FORA DOS BLOCOS')

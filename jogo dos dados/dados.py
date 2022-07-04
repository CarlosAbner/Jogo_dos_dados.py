#importando biblioteca rando para sortear os números
from random import randint
dado1 = [1, 6]
dado2 = [1, 6]
dado1 = randint(1,6)
dado2 = randint(1,6)

#importanto a biblioteca time
from time import sleep

#soma valor dos dois dados
soma = dado1 + dado2

#pedindo para o jogador digitar o valor que precisa que os dados de para ele 
print('=-'*20)
print('JOGO DOS DADOS SORTEADOS')
usuario = int(input('Quantos número você precisa? '))
print('-='*20)

print('Jogando os dados..')
sleep(1)

#resultado dos dados
print('O primeiro dado saiu {} e o segundo {} somando no total {}'.format(dado1, dado2, soma))
print('O jogador pediu {}'.format(usuario))
print('-='*20)

#validando o resultado dos dados e do valor solicitado pelo jogador
if soma == usuario:
    print('PARABENS!! seu número saiu ')
elif soma < usuario:
    print('SINTO MUITO :(  O resultado foi menor do que o esperado')
#validando o resultado dos dados CASO o valor saido tenha sido maior que o valor do usuario
elif soma > usuario:
        print('O valor dos dados foram superiores!!')
        print('=-'*20)
        user = int(input('''Esse valor te ajuda ou te atrapalha? 
        [1] Sim
        [2] Não 
        '''))
        print('=-'*20)
        if user == 1:
            print('Fico feliz em saber que ajudou')
        elif user == 2:
            print('Sinto Muito') 
print('Fim de Jogo')










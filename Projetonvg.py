from random import randint
print('==='*20)
print('{:^60}'.format(' JOGO DE ADIVINHAÇÃO '))
print('==='*20)
número = int(input('Tente adivinhar o número de 0 a 10. Digite o número:'))
palpites = 0
n=randint(0,10)

while número != n:
    if número > 10:
        print('Opção invalida você só pode escolher entre 0 e 10')
    if número > n:
        print('Menos...')
    else:
        print('Mais...')
    print('O número escolido pela maquina foi {}, e você escolheu  {} !'.format(n, número))
    número = int(input('Você errou! Tente de novo : '))
    palpites = palpites + 1
print('O número escolido pela maquina foi {}, e você escolheu  {} !'.format(n,número))
print('Parabéns você ganhou !!', end=' ')
print('Você precisou de {} chances para acertar !'.format(palpites + 1))
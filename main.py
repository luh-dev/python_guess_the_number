import random

numero_x = random.randint(1,10)
tentativas=1
print('Você deve adivinhar o numero que tenho na memoria!!!')
print('Esse numero esta entre 1 e 10')


while tentativas <= 5:
    numero_digitado = int(input('Digite um numero : '))

    if numero_x ==numero_digitado:
        print('acertou!')
        break
    else:

        print('errou, tentativa numero',tentativas)
        if numero_digitado > numero_x:
            print('dica:o numero digitado e maior do que o numero para adivinhar!')
        else:
            print('dica:o numero digitado e menor do que o numero para adivinhar!')

        tentativas = tentativas +1
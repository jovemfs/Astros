from time import sleep


""" arquivo para realizar a testagem sem ter que
executar o código main com a narração, pq ele é gigante
e ia demorar um século :) """


# variaveis testadas 
escolhaidade = 0
acao01 = 0
acao02 = 0
acao03 = 0

# <---------..__ TESTAGEM __..--------->

# <-- NOME E IDADE COMEÇO -->
nome = str(input('Qual será o seu primeiro nome? ')).strip()
while escolhaidade != 1 and escolhaidade != 2 and escolhaidade != 3:
    print('''Opções de idade: 
  [1] - 15
  [2] - 17
  [3] - 18  ''')
    escolhaidade = int(input('Qual será sua idade? '))
    if escolhaidade == 1:
        idade = 15
    elif escolhaidade == 2:
        idade = 17
    elif escolhaidade == 3:
        idade = 18
    else:
        print('''!! OPÇÃO INVÁLIDA. POR FAVOR, REFAÇA !!''')
print(' ')
print('VERIFICAÇÃO: o jogador escolheu se chamar {} e ter {} anos.'.format(nome, idade))
print(' ')
# <-- NOME E IDADE FIM -->

print('''#
#
# 
# ''')
print(' ')

# <-- ITEM INICIAL COMEÇO -->
while acao02 != 1 and acao02 != 2:
    print('''(ação.02) Opções de item: 
  [1] - Pulseira verde-esmeralda
  [2] - Corrente dourada cravejada de brilhantes  ''')
    print(' ')
    acao02 = int(input('Qual item você quer pegar? '))
    if acao02 == 1:
        iteminicial = 'pulseira'
    elif acao02 == 2:
        iteminicial = 'corrente'
    else:
        print(' ')
        print('''!! OPÇÃO INVÁLIDA. POR FAVOR, REFAÇA !!''')
        print(' ')
print(' ')
sleep(2)
print(' VERIFICACAO: {}'.format(iteminicial))
print(' ')
# <-- ITEM INICIAL FINAL -->

print('''#
#
# 
# ''')
print(' ')

# <-- ITEM INICIAL COMEÇO -->
while acao03 != 1 and acao03 != 2 and acao03 != 3:
    print('''(ação.03) Opções de carta: 
  [1] - Carta pequena. Roxo claro quase lilás, com detalhes dourados nas bordas
  [2] - Carta média. Roxo escuro perto do azul, com muitos detalhes dourados no centro
  [3] - Carta grande. Roxo vibrante, detalhes dourados traçam um desenho de "raízes"''')
    print(' ')
    acao03 = int(input('Qual carta você quer pegar? '))
    if acao03 == 1:
        carta = 'lilás'
        vantagem = ''
    elif acao03 == 2:
        carta = 'quase-azul'
        vantagem = ''
    elif acao03 == 3:
        carta = 'vibrante'
        vantagem = ''
    else:
        print(' ')
        print('''!! OPÇÃO INVÁLIDA. POR FAVOR, REFAÇA !!''')
        print(' ')
print(' VERIFICACAO: {}, {}'.format(carta, vantagem))
print(' ')
# <-- ITEM INICIAL COMEÇO -->

print('''#
#
# 
# ''')
print(' ')

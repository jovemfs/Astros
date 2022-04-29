from time import sleep

escolhaidade = 0

print('***'*21)
print('                  Jovem Filho do Sol PRESENTS')
print('***'*21)
print('''         
                      .---------.         
                  .--'   o   .   `--.         
                .'@  @@@   @    .   . `.
             .'   . @@@@ 
            / @@o    @@
            |@@@                                       *_..
           / @@@@   `.-.                    ASTROS
           |@ @@                        +.!       PERDIDOS
           \     @@                            *
            |        @
            \  .  @@  @\  
             `.  @@@@  _\ /    .      o .'  
                `.     / |      o    .'     
                  `--./   .      .--'       
                      `---------'          
''')
print('***'*21)
sleep(1)
print('Olá, jovem. Seja bem-vindo.')
sleep(1)
print('''Antes de iniciarmos nossa aventura, preciso que responda algumas 
perguntinhas rápidas...''')
print('***'*21)
sleep(2)
print('''Você é um jovem menino nascido em uma família proprietária de 
minas de um precioso material raro no universo. Vocês têm muito
dinheiro e são vistos socialmente como um poder-paralelo-aristocrático do
lugar onde habitam, e, por estarem lá há gerações e gerações, alguns os cultuam
quase como deuses.''')
print('****')
sleep(6)

nome = str(input('Qual será o seu primeiro nome? ')).strip()

while escolhaidade != 1 and escolhaidade != 2 and escolhaidade != 3:
    print('''Qual será sua idade? 
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

print('****')
print('VERIFICAÇÃO: o jogador escolheu se chamar {} e ter {} anos.'.format(nome, idade))
print('****')

sleep(5)
print(''' O sir. Sary costumava repetir que os domingos são dias sagrados
para a família Rama. Talvez as baboseiras por ele proferidas fossem
tamanhas que, após algum tempo, seu avô daria o braço a torcer e transferiria
os compromissos sociais para a sexta-feira.''')
sleep(9)
print('***')
print(''' De fato um bom exemplo sobre como o poder e influência de um
conselheiro podem transcender qualquer cargo político. Homens no poder tendem a
dar ouvidos aos místicos excêntricos que aparecem em seus conturbados auges, o 
que de alguma forma te fez detestar cada vez mais os que não eram céticos.''')
sleep(9)
print('***')
print(''' Era notável que o jovem {} não gostava muito da ideia de compromissos
sociais, sobretudo por estarem em um dia que o deixava exausto, sempre. Obviamente
a presença dos Cultuadores e do Culto em si deixavam tudo ainda pior.'''. format(nome))
sleep(9)
print('***')
print(''' Era uma manhã chuvosa e fria, com ventos cortantes e barulhentos.
Atrás da grande porta de cascalho escuro, ouvia-se apenas o caminhar apressado
de sapatos femininos como quem tentava correr de forma discreta.''')

from time import sleep

acao01 = 0

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

while acao01 != ['1', '2', '3']:
  nome = str(input('Qual será o seu primeiro nome? ')).strip()
  escolhaidade = int(input('''Qual será sua idade? 
  [1] - 15
  [2] - 17
  [3] - 18  '''))
  if escolhaidade == 1:
    idade = 15
  elif escolhaidade == 2:
    idade = 17
  elif escolhaidade == 3:
    idade = 18
  else:
    print('Você não selecionou uma opção válida. Volte e refaça.')
    
print('****')
print('VERIFICAÇÃO: o jogador escolheu se chamar {} e ter {} anos.'.format(nome, idade))
print('****')
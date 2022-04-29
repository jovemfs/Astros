from time import sleep

escolhaidade = 0
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
print(' ')
sleep(2)
print('''Você é um jovem menino nascido em uma família proprietária de 
minas de um precioso material raro no universo. Vocês têm muito
dinheiro e são vistos socialmente como um poder-paralelo-aristocrático do
lugar onde habitam, e, por estarem lá há gerações e gerações, alguns os cultuam
quase como deuses.''')
print(' ')
sleep(6)

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
print('***'*21)

sleep(5)
print(' ')
print(''' O sir. Sary costumava repetir que os domingos são dias sagrados
para a família Rama. Talvez as baboseiras por ele proferidas fossem
tamanhas que, após algum tempo, seu avô daria o braço a torcer e transferiria
os compromissos sociais para a sexta-feira.''')
sleep(10)
print(' ')
print(''' De fato um bom exemplo sobre como o poder e influência de um
conselheiro podem transcender qualquer cargo político. Homens no poder tendem a
dar ouvidos aos místicos excêntricos que aparecem em seus conturbados auges, o 
que de alguma forma te fez detestar cada vez mais os que não eram céticos.''')
sleep(10)
print(' ')
print(''' Era notável que o jovem {} não gostava muito da ideia de compromissos
sociais, sobretudo por estarem em um dia que o deixava exausto, sempre. Obviamente
a presença dos Cultuadores e do Culto em si deixavam tudo ainda pior.'''. format(nome))
sleep(11)
print(' ')
print(''' Era uma manhã chuvosa e fria, com ventos cortantes e barulhentos.
Atrás da grande porta de cedro escuro, ouvia-se apenas o caminhar apressado
de sapatos femininos como quem tentava correr de forma discreta. Após alguns
segundos, o som estrindente dos sapatos foi se aproximando, até que a grande
porta de cedro foi sendo afastada aos poucos.''')
sleep(13)
print(' ')
print(''' Quando aberta, a passagem recebeu uma moça jovem que tropeçava nos
próprios pés enquanto tentava fechar a porta atrás de si. Ela se atrapalhava e
tentava a todo custo disfarçar sua falta de experiência, por mais que fizesse com
boa vontade. Tendo conseguido encostar a pesada porta, a jovem olhou deslumbrada
para o que conhecerá: ela estava lá, os aposentos do Jovem Filho do Sol.''')
sleep(13)
print(' ')
print(''' Ninguém no mundo - ao menos no seu mundo - vira tamanha luxuosidade.
Cada detalhe daquele quarto era rico, literalmente rico. A jovem serviçal já havia
passado no quarto dos pais Rama anteriormente, e ainda assim achava que o do filho
superava todos os outros cômodos da casa.''')
sleep(10)
print(' ')
print(''' As paredes eram feitas de um material claro, duro e que refletia a
luz da lua, mas não a do sol. Se parecia com quartzo, mas, ainda que com seu pouco
conhecimento em minerais, sabia que não se tratava daquele material. Era... era
diferente. Ele parecia vibrar como se tivesse ciência do que fazer e só fizesse
o que quisesse. Ele sabia o que refletir, o que espelhar e o que ocultar. Era diferente...''')
sleep(13)
print(' ')
print(''' Todos os cantos daquele espaço primordial eram cuidadosamente preenchidos
com móveis, pinturas, estatuetas e decorações mais. Eles combinavam entre si,
mas parecia que todo aquele amontoado de coisas estava em sincronia não só estética. 
O que mais chamou a atenção da serviçal foi o quadro pendurado no centro da parede
que ficava em frente a cama, o que seria visto ao dormir e acordar.''')
sleep(11)
print(' ')
print(''' A jovem ficou submergida em pensamentos, teorias e ansiedade. Provavelmente
passou longos 20 minutos lendo o ambiente antes de se dar conta de que estava ali a
trabalho. Não só isso, se deu conta de que também havia arranjado problemas em sua
primeira função especial.''')
sleep(11)
print(' ')
print(''' Tendo caído a ficha, correu até a grande cama onde repousava o Jovem Filho
do Sol. Sem se preocupar com cautela, a moça sacodiu o corpo magro do rapaz na tentativa
de fazê-lo acordar imediatamente. Depois de um tempo, ela conseguiu.''')
sleep(9)
print(' ')
print(' - {}, acorde! Está na hora de se preparar para os compromissos!'.format(nome))
sleep(5)
print(' ')
print(''' A pobre mulher se via desesperada para lhe fazer acordar, como se a vida
dela dependesse disso. Era entendível, afinal estava em um dos mais privilegiados
empregos de todos os reinos e terras.
Quando ela te viu acordar, um sorriso de alívio foi tão presente que quase se esqueceu
de esconder.''')
print(' ')
sleep(10)
print(''' Acordando desorientado devido ao susto, o jovem olha para cima e vê a figura
reconfortante de uma garota que aparentava ter sua idade. Ela, ao contrário das outras
que já passaram por ali, não parecia ter receio de tocá-lo, e ele praticamente estava
deitado em seus braços enquanto processava tudo.''')
print(' ')
sleep(11)
print(''' {} começou os olhos e foi se afastando lentamente de forma discreta para
conseguir analisar melhor aquela que viria a ser sua nova "sombra".'''.format(nome))
print(' ')
sleep(6)
print(''' Aquela era a décima serviçal contratada para lhe ajudar. Esse número seria
aceitável se estivessemos falando de um tempo maior do que dez dias, o que
não era o caso.''')
print(' ')
sleep(4)
print(''' Você claramente não conhecia a mulher e ficara constrangido com isso. Ao
contrário do resto da família, você não se sentia mais especial do que os que trabalhavam
na casa. Para falar a verdade, o Jovem Filho do Sol tinha consideráveis problemas
de autoestima.''')
print(' ')
sleep(9)

while acao01 != 1 and acao01 != 2 and acao01 != 3:
    print('''(ação.01) Opções de ação:
[1] - Saudar ela de forma tímida e contida
[2] - Por receio, ignorar sua presença
[3] - Abrir um sorriso grande e acolhedor, afinal era seu primeiro dia e ela
provavelmente estaria ansiosa e com medo.''')
    print(' ')
    acao01 = int(input('Olhando para a mulher a sua frente, o que você deseja fazer? '))
    print(' ')
    if acao01 == 1:
        print(''' {} pensa que, dada a pressão que a moça estaria sofrendo, esse estaria
sendo um dia horrível para ela. Considerando sua criação, a empatia é até que grande
em sua pessoa. Apesar de sua timidez te forçar a ficar em silêncio, você consegue acenar
com as mãos num claro gesto de simpatia, e somente esse pequeno ato foi o suficiente para
ela soltar involuntariamente um longo suspiro de alívio, esse sendo logo repreendido pela
mesma.'''.format(nome))
        sleep(12)
    elif acao01 == 2:
        print(''' A ansiedade dela era inquietante de fato, coisa que chegava a te incomodar também.
Você pensa em dizer algumas palavras para confortá-la, mas a timidez lhe impede. Depois de alguns
segundos em uma troca de olhares desconfortável, {} simplesmente levanta e se coloca em pé ao
lado da cama, tudo conforme o ritual manda.'''.format(nome))
        sleep(9)
    elif acao01 == 3:
        print(''' Apesar da chuva e dos compromissos, {} tivera uma ótima noite de sono e estava de bom humor.
Contemplou a situação da moça por breves segundos e rapidamente se sensibilizou com sua ansiedade
e desajeito. Não se sabe a razão, mas aquela garota havia lhe despertado um sentimento de pertencimento,
como se vocês enfrentassem os mesmos problemas. Você não demorou muito para calcular tudo isso e
imediatamente abrir um sorriso lindo e tranquilizante, gerando um clima imensamente confortável
dentro daquele quarto.
A moça sorriu lindamente de volta. Vocês ficaram imersos naquela bolha de simpatia durante minutos.'''.format(nome))
        sleep(16)
    else:
        print('''!! OPÇÃO INVÁLIDA. POR FAVOR, REFAÇA !!''')
        print(' ')

print(' ')
print(''' ''')

from time import sleep

escolhaidade = 0
acao01 = 0
acao02 = 0
acao03 = 0
vantagem = 0

# iteminicial
# carta
# relacao

print('***'*21)
print('                  The Fabulous ASTRO bros')
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
print(' ')
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
print(''' Era notável que o jovem {} não gosta muito da ideia de compromissos
sociais, sobretudo por estarem em um dia que o deixava exausto, sempre. Obviamente
a presença dos Cultuadores e do Culto em si deixavam tudo ainda pior.'''. format(nome))
sleep(11)
print(' ')
print(''' É uma manhã chuvosa e fria, com ventos cortantes e barulhentos.
Atrás da grande porta de cedro escuro, ouvia-se apenas o caminhar apressado
de sapatos femininos como quem tentava correr de forma discreta. Após alguns
segundos, o som estrindente dos sapatos foi se aproximando, até que a grande
porta de cedro foi sendo afastada aos poucos.''')
sleep(13)
print(' ')
print(''' Quando aberta, a passagem recebe uma moça jovem que tropeça nos
próprios pés enquanto tenta fechar a porta atrás de si. Ela se atrapalha e
tentav a todo custo disfarçar sua falta de experiência, por mais que fizesse com
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
sleep(10)
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
print(''' Acordando desorientado devido ao susto, o Jovem olha para cima e vê a figura
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
print(''' Você claramente não conhece a mulher e ficara constrangido com isso. Ao
contrário do resto da família, você não se sente mais especial do que os que trabalhavam
na casa. Para falar a verdade, o Jovem Filho do Sol tem consideráveis problemas
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
        relacao = 'boa'
        print(''' {} pensa que, dada a pressão que a moça estaria sofrendo, esse estaria
sendo um dia horrível para ela. Considerando sua criação, a empatia é até que grande
em sua pessoa. Apesar de sua timidez te forçar a ficar em silêncio, você consegue acenar
com as mãos num claro gesto de simpatia, e somente esse pequeno ato foi o suficiente para
ela soltar involuntariamente um longo suspiro de alívio, esse sendo logo repreendido pela
mesma.
 Para não ficar em meio a um silêncio gritante, você se levanta sem precisar ser mandado e
já aguarda pelas instruções do ritual que deverá ser orientado por ela.'''.format(nome))
        sleep(12)
    elif acao01 == 2:
        relacao = 'ruim'
        print(''' A ansiedade dela era inquietante de fato, coisa que chegava a te incomodar também.
Você pensa em dizer algumas palavras para confortá-la, mas a timidez lhe impede. Depois de alguns
segundos em uma troca de olhares desconfortável, {} simplesmente levanta e se coloca em pé ao
lado da cama, tudo conforme o ritual manda.'''.format(nome))
        sleep(9)
    elif acao01 == 3:
        relacao = 'otima'
        print(''' Apesar da chuva e dos compromissos, {} tivera uma ótima noite de sono e estava de bom humor.
Contemplou a situação da moça por breves segundos e rapidamente se sensibilizou com sua ansiedade
e desajeito. Não se sabe a razão, mas aquela garota havia lhe despertado um sentimento de pertencimento,
como se vocês enfrentassem os mesmos problemas. Você não demorou muito para calcular tudo isso e
imediatamente abrir um sorriso lindo e tranquilizante, gerando um clima imensamente confortável
dentro daquele quarto.
 A moça sorriu lindamente de volta. Vocês ficaram imersos naquela bolha de simpatia durante minutos,
até que ela pediu educadamente para se levantar.'''.format(nome))
        sleep(16)
    else:
        print('''!! OPÇÃO INVÁLIDA. POR FAVOR, REFAÇA !!''')
        print(' ')

print(' ')
print(''' Ao contrário dos outros dias, na sexta-feira você não se alimenta pela manhã. Como de
costume, em sua mão direita a serviçal carrega uma adaga cuja lâmina verde-esmeralda parece aprisionar almas.
Na esquerda guarda uma bolsa de couro, e seu conteúdo você só pode especular, já que isso é fora da curva e
não costuma aparecer sempre. ''')
print(' ')
sleep(8)
print(''' Ela parece notar seu olhar curioso frente a bolsa que carrega, e por alguns segundos pensou
em fazer suspense, mas logo desistiu da ideia. "Seria legal abrir o jogo com o Jovem e ganhar pontos",
pensou ela. O plano estava montado...''')
print(' ')
sleep(5)
print(''' A moça se aproximou de você com a adaga verde-esmeralda em mãos, dessa vez empunhando-a da
forma correta. Ela deu dois passos para frente, ficando a centímetros de sua face. Você se sente ameaçado,
mas racionalmente sabe que não há nada a temer. A adaga é colocada sobre seu peito, e então o sentimento
de confiança vai embora e o desconforto começa a dominar.''')
print(' ')
sleep(10)
print(''' - Você certamente não conhece essa bolsa, muito menos o que trago nela... -- uma pausa na frase e então
ela começa a te olhar em completo silêncio. A moça claramente estava te desafiando. -- É uma coisa nova, na
verdade é a razão pela qual estamos aqui, eu e Elas.''')
print(' ')
sleep(7)
print(''' "Elas"? "Elas" quem? Isso nunca acontecera, você não faz ideia da razão pela qual está sendo sutilmente
ameaçado por sua serviçal particular.''')
print(' ')
sleep(5)
print(''' - Quem é você? Qual é seu nome? -- com a voz trêmula {} diz enquanto se afasta lentamente da lâmina esmeralda sobre seu peito.
Você alterna sua visão entre a lâmina e a moça que parecia se divertir com sua situação de angústia.'''.format(nome))
print(' ')
sleep(5)
print(''' - Meu nome? -- ela abre um sorriso como quem esperasse ansiosamente por essa pergunta -- Você já se perguntou
a razão pela qual todas as outras evitavam falar com você? -- a moça aguardou sua resposta, o que não aconteceu -- Sou
diferente delas, seus pais me pediram para que fosse. Se você colaborar, eu posso te dar algumas dicas para o torneio.''')
print(' ')
sleep(9)
print(''' Ok, agora começou a ficar estranho. Uma nova serviçal surge em seu quarto, e sua primeira impressão sobre
ela é boa. Porém em minutos sua personalidade flui e ela passa a lhe ameaçar com uma adaga amedrontadora, além de citar
coisas das quais você desconhece completamente. Isso definitivamente estava estranho.''')
print(' ')
sleep(8)
print(''' Em segundos, sua personalidade muda novamente e a garota se afasta juntamente com a adaga, mas segue te olhando
com satisfação visível. Seja lá o que estava tramando, deu certo.''')
print(' ')
sleep(5)
print(''' - {}, eu tenho novidades para você... -- caminhando até o centro do quarto, ela abre a bolsa de couro e despeja
seu conteúdo sobre a mesa redonda de mármore. Você pode observar alguns itens curiosos, dentre eles um frasco contendo um líquido
rosa vibrante, algo que parecia ser uma bússola ou um relógio, uma pulseira verde-esmeralda da mesma tonalidade da adaga e uma
corrente dourada cravejada de brilhantes. A moça pega apenas os dois últimos itens e caminha até você.'''.format(nome))
print(' ')
sleep(10)

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
print(''' {} olha para ela com medo. Existe uma certa resistência, mas após alguns segundos o Jovem estende sua mão
e pega a {} que ela guardava.'''.format(nome, iteminicial))
print(' ')
sleep(4)
print(''' - Me desculpe pela péssima brincadeira, {}. Mas é que hoje será um dia diferente e eu acho que podemos
fazer um trato bom para ambos os lados. Eu estou tão nervosa quanto você, pode ter certeza quanto a isso.'''.format(nome))
print(' ')
sleep(6)
print(''' O Jovem a olha com uma dúvida latente. Não entende de fato sobre o que "um trato" significava.
Estava com medo da moça, mas também intrigado para saber o que o dia de hoje reservava.''')
print(' ')
sleep(5)
print(''' - Certo, podemos fechar um acordo. Mas antes preciso que me explique o que está acontecendo. Além disso,
exijo saber o seu nome. Não confio em quem não responde por si. -- disse {} com a voz trêmula. Era notável sua falha
tentativa de impor respeito, mas ele não era bom nisso.'''.format(nome))
print(' ')
sleep(8)
print(''' A moça também estava ansiosa, mas agora sentia mais autoconfiança. Sabia que seria fácil obter vantagens
por intermédio de {}, mas não sabia que seria tão fácil. Ela se aproximou do Jovem novamente, dessa vez trazendo
o líquido rosa vibrante consigo.'''.format(nome))
print(' ')
sleep(8)
print(''' - Tome isso, {}. -- disse entregando o frasco em suas mãos -- Os outros Jovens não terão informações privilegiadas
como você teve, então espero que valorize e que se lembre de mim. Quando estiver adentrando a Masmorra, peça licença e
beba todo o líquido, mas cuidado para não lhe verem fazendo isso, você sofreria desgraças.'''.format(nome))
print(' ')
sleep(7)
print(''' Você começa a analisar o frasco com cuidado, dessa vez encarando o líquido e tentando se lembrar se já o
vira em algum outro momento de sua vida.''')
print(' ')
sleep(4)
print(''' {}, assim como a maior parte dos jovens ricos, tivera um excelente ensino de conhecimentos gerais. O Jovem
colecionava aulas da matéria Química Celeste e Poções Terrenas, mas não se lembrou de nada que se comportasse como
o líquido daquele frasco. Ele se movia sozinho e vibrava em diferentes tons de rosa. Começou a nascer um receio de ingerir
aquilo, e talvez de fato o Jovem não fosse beber.'''.format(nome))
print(' ')
sleep(11)
print(''' - Tenho condições. Se quiser que lhe ajude, seja lá como exigir, terá que me detalhar o que acontecerá
no dia de hoje, quem são "Elas", o que faz esse líquido e também qual é o seu nome, pergunta da qual você fugiu algumas
vezes.''')
print(' ')
sleep(8)
print(''' - Tudo bem, eu respondo todas. -- ela caminhou até o centro do cômodo novamente, próximo a mesa. Ali retirou um
monte com cartas roxas com detalhes dourados, mas cada uma com tonalidades e tamanhos diferentes. -- Venha até aqui, {},
pegue uma carta e vamos treinar.'''.format(nome))
print(' ')
sleep(7)

while acao03 != 1 and acao03 != 2 and acao03 != 3:
    print('''(ação.03) Opções de carta: 
  [1] - Carta pequena. Roxo claro quase lilás, com detalhes dourados nas bordas
  [2] - Carta média. Roxo escuro perto do azul, com muitos detalhes dourados no centro
  [3] - Carta grande. Roxo vibrante, detalhes dourados traçam um desenho de "raízes"''')
    print(' ')
    acao03 = int(input('Qual carta você quer pegar? '))
    if acao03 == 1:
        carta = 'lilás'
        vantagem += 8
        cartadesc = 'O domo é resistente e inquebrável, o que me faz pensar que seus rastros fariam uma bela armadura.'
    elif acao03 == 2:
        carta = 'quase-azul'
        vantagem += 6
        cartadesc = 'O centro é o núcleo, mas o arquiteto rejeita obviedade. Obtenha vantagens lá.'
    elif acao03 == 3:
        carta = 'vibrante'
        vantagem += 12
        cartadesc = 'Talvez não na superfície. Vá para baixo e fique por cima.'
    else:
        print(' ')
        print('''!! OPÇÃO INVÁLIDA. POR FAVOR, REFAÇA !!''')
        print(' ')

print(''' ''')
print(' ')
sleep(8)

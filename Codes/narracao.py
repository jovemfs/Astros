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
print(''' É notável que o jovem {} não gosta muito da ideia de compromissos
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
print(''' Ela parece notar seu olhar curioso frente a bolsa que carrega, e por breves segundos arquitetava
um plano de como introduzir aquele bate-papo.''')
print(' ')
sleep(5)
print(''' Então sua mão direita levanta a adaga verde-esmeralda. Ela a leva até a altura de sua face, passando
a proferir baixinho palavras em um idioma desconhecido para você. Depois de algumas frases intraduzíveis,
a mulher acaba seu ritual e então a lâmina começa a brilhar como se houvesse fogo contido nela.''')
print(' ')
sleep(10)
print(''' Você conhece aquela adaga de longa data. Estava na sua linhagem há anos, um presente de um suposto
mago a seu querido avô. Más línguas diziam que trazia A Maldição da Melancolia, essa responsável por levar a
alma de sua irmã, prima e tia, todas da mesma forma e no mesmo dia.''')
print(' ')
sleep(8)
print(''' Era óbvio o receio para com a faca, mas por um momento o sentimento foi substituído por um fascínio
quando a mesma começara a brilhar. Era quase hipnotizante, eu diria. Nenhuma jóia brilhara dessa forma perante
os seus olhos, nem mesmo as mais caras de sua coleção familiar.''')
print(' ')
sleep(8)
print(''' A moça se aproximou de você com a arma em mãos, dessa vez empunhando-a da forma correta.
Ela deu dois passos para frente, ficando a centímetros da própria face. Você se sente levemente ameaçado,
mas racionalmente sabe que não há nada a temer. A adaga é colocada frente a seu peito, e então passa a
brilhar mais e mais conforme se aproximam um do outro.''')
print(' ')
sleep(10)
print(''' - Previ que você não conheceria o que trago na bolsa, Jovem {}. -- a moça dá uma longa pausa arrastada
que consegue deixar ambos nervosos enquanto admiram o brilho da lâmina esmeralda. -- Pensei que poderia lhe ajudar.
Essa arma nasceu para um estilo sutil de matar... é uma arte, entende? E você precisa a dominar antes de ser
levado até a Arena.'''.format(nome))
print(' ')
sleep(10)
print(''' "Arena"? "Matar"? Do que diabos aquela mulher estava falando!?''')
print(' ')
sleep(4)
print(''' - Receio que tenha errado de quarto, senhora. Não conheço tal Arena, muito menos "a arte de matar".
Sou um aluno do filósofo de Sinab, e no momento me encontro atrasado para os compromissos sociais. -- {} falou
enquanto tentava se afastar da moça que agora lhe parecia maliciosa.'''.format(nome))
print(' ')
sleep(9)
print(''' Ela te fitou por breves segundos e suspirou pesadamente. Era nítido em sua expressão que lhe restara pouca
paciência. A garota tinha pouco manejo com as palavras, e no atual momento parecia ansiosa demais. A impressão geral
era de que seria uma conversa complicada...''')
print(' ')
sleep(7)
print(''' - Por favor, {}, sem perguntas. Não existe uma forma sã de lhe passar tais informações neste momento. Só
preciso que confie em mim e siga minhas ordens... -- ela saiu de sua frente antes que você pudesse falar algo, e então
caminhou em direção a mesa novamente -- preciso de sua colaboração. Nossas vidas, as duas, valem ISSO. -- falou apontando
para a bolsa de couro.'''.format(nome))
print(' ')
sleep(11)
print(''' Caminhando até o centro do quarto, ela abre a bolsa e despeja seu conteúdo sobre a mesa redonda de mármore.
Você pode observar alguns itens curiosos, dentre eles um frasco contendo um líquido rosa vibrante, algo que parecia ser
uma bússola ou um relógio, um monte de cartas, uma pulseira verde-esmeralda da mesma tonalidade da adaga e uma
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
print(''' - Me desculpe pelos péssimos modos, {}. Hoje é o dia em que seus pais pagarão por seus pecados. Infelizmente
você tem o mesmo sangue que eles, e precisará de muita sorte para o que virá adiante. Farei o possível para lhe ajudar,
mas não temos muito tempo para nos aperfeiçoarmos. -- ela disse enquanto colocava a {} em seu corpo.'''.format(nome, iteminicial))
print(' ')
sleep(10)
print(''' - Pecados? -- surge uma expressão gritante de dúvida em seu rosto -- Ora, sei que minha família possui
inúmeras falhas, mas não imaginei que O Conselho ficaria enfurecido com suas atitudes. O que houve?''')
print(' ')
sleep(7)
print(''' A moça, que antes estava lhe adornando, passa a te olhar fixamente em reprovação. Você se assusta um pouco
com a ousadia dela, mas admite que é emocionante fugir da rotina de intocável autoridade suprema, ainda que isso
significasse um funcionário estranho lhe constrangendo em seu próprio quarto.''')
print(' ')
sleep(12)
print(''' - Não é sobre o conselho, {}. Se trata de algo maior. Eu sei que vocês costumam pensar que dinheiro é a maior
conquista de um homem, mas não, não é. Existem coisas maiores e mais importantes nesse plano, e receio que você falhe no teste
graças a sua ignorância e inocência.'''.format(nome))
print(' ')
sleep(10)
print(''' - Se não é pelo conselho, senhora, então por quem seria? -- Quando repara o tom de arrogância em sua voz,
se lembra a razão pela qual odeia tanto ouvir os discursos arranjados de seu pai, e logo retorna para um tom
mais compassivo e calmo -- Quer dizer, não que eu concorde com tudo, mas não conheço qualquer um além de três no
Conselho que ouse desafiar o poder de meu pai. Vai por mim, eu sei que ele faria um estrago com eles...''')
print(' ')
sleep(12)
print(''' - Não se trata de poder ou medo. Se trata de respeito, algo que há muito vocês ignoram por aqui.
Desde Sary, seus antepassados não respeitam as tradições, vocês pisaram sobre a memória de Jima, não?
Não pense que gosto de estar aqui, mas cada uma de nós foi encarregada de cuidar de um Jovem. A partir
de agora você é meu fardo e eu sou o seu, então trabalhemos em equipe, certo? ''')
print(' ')
sleep(12)
print(''' - Jima? -- você solta uma risada de deboche -- Convenhamos, eu também destesto essa baboseira
real e todo o teatro para cima dos Cultuadores. Mas Jima é só um charlatão igualmente a Sary, dois tolos
mentirosos e manipuladores das massas. Não tenho respeito algum por Jima.''')
print(' ')
sleep(10)
print(''' - {}, ele não era um mentiroso como Sary, muito menos manipulador. Talvez fosse o último
mago a se prestar a tentar ajudar gananciosos reis e salvar seus povos. Teve um nobre papel, mas 
infelizmente padeceu como todos o avisaram. Não vale a pena se envolver com ricos, todos eles são
falsos reis construídos sobre muita maldade e egoísmo.'''.format(nome))
print(' ')
sleep(13)
print(''' - Se quer respeito por sua fé, não espere isso de mim. Jima, Sary e os demais mentirosos
metidos a mágicos somente me atrasaram. Veio cobrar de minha família por ser cegamente fiel à um idiota
que copiava frases de filósofos menores? Ótimo, mas me mantenha fora disso, eu jamais acreditei nessa
baboseira toda de Sary, Jima, Luther ou qualquer outro.''')
print(' ')
sleep(12)
print(''' - Como pode ter uma visão de mundo tão ampla sem nem mesmo ter permissão para sair
do próprio quarto, senhor Rama? -- ela falou com deboche. Deu certo, a garota tinha lhe atingido --
Você, mais do que todos nessa casa, não faz a mínima ideia de como o universo funciona, muito menos
o real valor de um homem bom disposto a ajudar. -- a moça se aproximava de você conforme falava,
e seu tom de voz e expressão facial faziam parecer que ela iria atacar -- Está na hora de pagarem
pelos prejuízos que causaram às inúmeras almas condenadas por seus pais.''')
print(' ')
sleep(15)
print(''' A moça tinha lágrimas contidas em seus olhos num esforço para não caírem naquele
momento. Você sabia que tinha passado do ponto, sabia que a fé para algumas pessoas é a coisa
mais importante de suas vidas. Não entendia sobre pecados, dívidas ou o mal que sua família
teria feito, mas sabia que aquela garota sentira na pele a dor.''')
print(' ')
sleep(12)
print(''' Enquanto você pensava sobre o diálogo que acabara de acontecer, ela caminhou novamente
ate a mesa de centro e pegou o monte de cartas que havia sido retirado da bolsa, dessa vez
voltando até você e lhe oferecendo as cartas sem dizer uma palavra sequer.''')
print(' ')
sleep(9)


while acao03 != 1 and acao03 != 2 and acao03 != 3:
    print('''(ação.03) Opções de carta: 
[1] - Carta pequena. Roxo claro quase lilás, com detalhes dourados nas bordas
[2] - Carta média. Roxo escuro perto do azul, com muitos fios dourados no centro
[3] - Carta grande. Roxo vibrante, pequenos retalhos dourados traçam um desenho de "raízes"''')
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

print(' ')
sleep(4)
print(''' Você olha atentamente para aquelas cartas e tenta se lembrar de algum jogo que
talvez conheça. Tentativa falha, não consegue se recordar de nada. Depois de alguns poucos
minutos observando o monte, finalmente se decide e pega a carta {} para si.'''.format(carta))
print(' ')
sleep(8)
print(''' Inspecionando o item, o Jovem pode observar melhor a tonalidade {} e seus desenhos.
Nenhuma carta é igual a outra, mas a que você pegou se parecia completamente diferente das
demais. Depois de olhar minuciosamente seu contorno, você pode notar algo grafado em Valis:

 "{}"'''.format(carta, cartadesc))
print(' ')
sleep(11)
print(''' As coisas faziam cada vez menos sentido.''')
print(' ')
sleep(4)
print(''' - Tenho uma dúvida, senhora... Qual é mesmo o seu nome?''')
print(' ')
sleep(4)
print(''' Entendendo que cometeu um deslize, você tenta puxar assunto. Um lado narcisista de
sua personalidade grita para que pare: "uma empregada qualquer não é tão importante", pensa ele.
Mas você sabe que errou e que deve se redimir de alguma forma. Vinha pensando há algum tempo
sobre como, se pudesse, gostaria de fazer a diferença na vida dos desfavorecidos, e agora acaba
de desrespeitar a moça que provavelmente viria a trabalhar com você. Falhou, falhou e sabe disso.''')
print(' ')
sleep(12)

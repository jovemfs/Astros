# Astros Perdidos

<img src="https://cdn.mapgenie.io/images/games/the-outer-worlds/maps/byzantium.jpg">
<!--<img src="https://media.moddb.com/images/games/1/60/59938/Outer_Worlds_City.png">-->

*Astros perdidos* é o teste inicial de texto-jogos, tendo sido inspirado por livro-jogos de RPG e também por alguns games primitivos, como <a href="https://www.youtube.com/watch?v=gLKw4AU4KHU">Star Trek</a> de 1971. A ideia principal desse jogo é explorar as possibilidades de vertentes e caminhos com o Python, além de trazer uma história onde você escolhe suas ações e define o seu próprio destino.

###

O funcionamento de um texto-jogo é simples: a narrativa será apresentada e você pode, com base nas opções, escolher o destino de forma não tão linear, tendo em vista a Teoria do Caos onde pequenos eventos causam uma grande diferença no mundo - isso significa que uma decisão simples no início do jogo pode impactar completamente o andar da aventura. 

###

> É uma das leis mais importantes do Universo, presente na essência de quase tudo o que nos cerca. A idéia central da teoria do caos é que uma pequenina mudança no início de um evento qualquer pode trazer conseqüências enormes e absolutamente desconhecidas no futuro. Por isso, tais eventos seriam praticamente imprevisíveis – caóticos, portanto. Parece assustador, mas é só dar uma olhada nos fenômenos mais casuais da vida para notar que essa idéia faz sentido. Imagine que, no passado, você tenha perdido o vestibular na faculdade de seus sonhos porque um prego furou o pneu do ônibus. Desconsolado, você entra em outra universidade. Então, as pessoas com quem você vai conviver serão outras, seus amigos vão mudar, os amores serão diferentes, seus filhos e netos podem ser outros…

###
É necessária também a reflexão sobre *O Demônio de Laplace*, experimento mental de Pierre Simon Laplace que traz a ideia de prever e determinar o futuro baseado em dados de variáveis do passado. Como não é humanamente possível criar variáveis infinitas - e o programa provavelmente explodiria se eu tentasse -, esse texto-jogo terá apenas 3 opções de ação para cada turno, tornando o universo da aventura muito mais determinista do que eu gostaria, infelizmente.

> O determinismo é uma corrente dentro da filosofia que diz que todos os eventos do futuro são determinados por causas preexistentes, ou seja, por relações de causalidade (A → B). Na maioria das vezes, o determinismo na física é conhecido como efeito causa e consequência. Com  isso, se diz que um episódio no futuro é determinado através de uma relação de eventos no passado. <br> Laplace conjecturou a seguinte proposição: Se uma entidade pudesse conhecer todas as variáveis que determinam o estado de todas as partículas do universo como posição, momento linear, carga elétrica, velocidade, impulso, rotação, etc em um dado instante *t* no tempo e o conhecimento de todas as leis e propriedades físicas necessárias, então seria matematicamente possível determinar o estado daquela partícula no futuro (não seria um “demônio” propriamente, mas um ser onisciente).

###

O jogo aborda temas que nos fazem refletir, como filosofia, espiritualidade, demonologia, sociologia e afins. Logo no começo somos apresentados a uma realidade luxuosa e um tanto mágica, porém em alguns turnos percebemos que nem tudo são flores e que existe um mundo para além de tudo o que julgamos saber. A proposta nunca foi inovar, mas sim trazer uma narrativa questionadora e que cause desconforto e angústia em quem se aventurar nos códigos aqui presentes. *Astros Perdidos* foi inspirado em clássicos como *Alice no País das Maravilhas* (1865), *Duna* (1965), *O Mágico de Oz* (1939), *Capitães da Areia* (1937) e *Metrópolis* (1927).

###

Por ser um estilo de RPG textual e narrativo, o código conta com inúmeras linhas que trazem o enredo do jogo. Utilizei a função *sleep* (importada do *time*) para pausar os textos em conformidade com o tempo de progressão da leitura, e dessa forma ela fica consideravelmente mais fluida. O laço *while* é outra função essencial para o funcionamento do jogo, pondo em prática o sistema de variáveis do fluxograma. Além disso, ele também foi imensamente útil para o jogo não dar erro e reiniciar caso você digite um comando errado - algo bem comum na execução de um código -, forçando o jogador a escolher **somente** dentre as opções oferecidas, e também prevenindo no caso de prováveis cliques acidentais.

###

Os fluxogramas utilizados na construção do jogo foram montados com MS Visio. As concepções de imagens foram extraídas de diversos locais da internet e todos os direitos são reservados aos respectivos autores. Todos os arquivos de construção (fluxogramas, referências, PDFs etc) estão disponíveis open source <a href="https://drive.google.com/drive/folders/1c0HQ8niQJpog8KTRT5oVV2rH2i5xRfxi?usp=sharing">bem aqui</a> e catalogados no item <a href="https://github.com/jovemfs/Astros#fontes-e-refer%C3%AAncias">Fontes e referências</a> ainda no README. 

#

### Fontes e referências
- https://www.folhaum.com/post/liberdade-é-ou-não-real-demônio-de-laplace
- https://universoracionalista.org/demonio-de-laplace/
- https://www.google.com/url?sa=i&url=https%3A%2F%2Fmapgenie.io%2Fthe-outer-worlds&psig=AOvVaw1gGN2WyTDWFfnCAw1CtFYi&ust=1651193295011000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCNiaxb_EtfcCFQAAAAAdAAAAABAi
- https://www.moddb.com/games/final-equinox/images/outer-worlds-concept-artved=0CA0QjhxqFwoTCNiaxb_EtfcCFQAAAAAdAAAAABAn
- https://www.moddb.com/games/final-equinox/images/outer-worlds-concept-art
- https://letterboxd.com/film/metropolis/
- https://digital.bbm.usp.br/bitstream/bbm/6845/1/45000008358_Output.o.pdf
- https://www.adobe.com/be_en/active-use/pdf/Alice_in_Wonderland.pdf
- https://www.amazon.com.br/Duna-Frank-Herbert/dp/857657313X

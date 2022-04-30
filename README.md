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

Os fluxogramas utilizados na construção do jogo foram montados com MS Visio. As concepções de imagens foram extraídas de diversos locais da internet e todos os direitos são reservados aos respectivos autores. Todos os arquivos de construção (fluxogramas, referências, PDFs etc) eventualmente estarão disponíveis open source <a href="https://drive.google.com/drive/folders/1c0HQ8niQJpog8KTRT5oVV2rH2i5xRfxi?usp=sharing">bem aqui</a> e catalogados no item <a href="https://github.com/jovemfs/Astros#fontes-e-refer%C3%AAncias">Fontes e referências</a> ainda no README. 

###

Uma refência essencial para a criação de *Astros Perdidos* foram os RPGs de mesa que joguei com meus amigos ao longo da pandemia, com citação especial para as campanhas de *Call Of Cthulhu*, sistema de RPG inspirado nas obras de HP Lovecraft. Diversos livro-jogos também são referências em narrativa e funcionamento, com menção a *Encontro Marcado com o M.E.D.O.* (Steve Jackson), *A Cidade dos Ladrões* (Ian Livingstone), *O Porto do Perigo* (Ian Livingstone) e *Desafio dos Campeões* (Ian Livingstone).

###

O longa *Black Mirror: Bandersnatch* (2018) foi o ponta pé para me fazer iniciar o projeto. Precisava treinar laços em Python e, após rever o filme, pensei que uma boa forma de praticar seria criar situações de validação de escolhas e variáveis que definem a progressão de uma história. Obviamente a complexidade do projeto não chega nem aos pés de todas as referências e inspirações citadas nesse texto, porém esse é apenas um **estudo** sobre programação, nunca se propondo a ser uma obra prima da literatura ou algo do tipo - afinal eu sequer escrevo profissionalmente. Se quiser jogar algo realmente bom, recomendo os livro-jogos do autor <a href="https://www.amazon.com.br/RPG-Ian-Livingstone-Livros/s?rh=n%3A14486176011%2Cp_lbr_books_authors_browse-bin%3AIan+Livingstone
">Ian Livingstone</a>, alguns tendo sido citados no parágrafo anterior.

<img src="https://user-images.githubusercontent.com/59957939/166114736-572c8e7e-3050-4015-9074-e828ec193a73.png">

#

### Fontes e referências
- https://www.folhaum.com/post/liberdade-é-ou-não-real-demônio-de-laplace
- https://universoracionalista.org/demonio-de-laplace/
- https://mapgenie.io/the-outer-worlds
- https://www.moddb.com/games/final-equinox/images/outer-worlds-concept-art
- https://letterboxd.com/film/metropolis/
- https://digital.bbm.usp.br/bitstream/bbm/6845/1/45000008358_Output.o.pdf
- https://www.adobe.com/be_en/active-use/pdf/Alice_in_Wonderland.pdf
- https://www.amazon.com.br/Duna-Frank-Herbert/dp/857657313X
- https://letterboxd.com/film/the-wizard-of-oz-1939/
- https://i.imgur.com/MI9G4jZ.jpeg
- https://i.pinimg.com/originals/5f/ac/ae/5facae9bba755c432e7e9558951773f3.jpg
- https://www.blogrebellen.de/wp-content/uploads/2018/12/tuckersoft-jobs-t.jpg
- https://www.askpython.com/python/text-based-adventure-game
- https://www.amazon.com.br/Cidade-dos-Ladrões-5/dp/8589134458/ref=asc_df_8589134458/?tag=googleshopp00-20&linkCode=df0&hvadid=379708268622&hvpos=&hvnetw=g&hvrand=9504708419674614702&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001773&hvtargid=pla-1040482818632&psc=1
- https://www.amazon.com.br/Porto-do-Perigo-Ian-Livingstone/dp/8583651078/ref=sr_1_2?qid=1651336666&refinements=p_27%3AIan+Livingstone&s=books&sr=1-2&text=Ian+Livingstone
- https://www.amazon.com.br/Desafio-dos-Campeões-Ian-Livingstone/dp/8589134768
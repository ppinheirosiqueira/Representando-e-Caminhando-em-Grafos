# Representando e Caminhando em Grafos
 
[![Python](https://img.shields.io/badge/Linguagem-Python-blue)](https://www.python.org)
[![requirement](https://img.shields.io/badge/Framework-Django-darkgreen)](https://www.djangoproject.com)
[![requirement](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-informational)](https://code.visualstudio.com/docs/?dv=linux64_deb)

# Sumário

1. <a href=#introdução>Introdução</a>
2. <a href=#jogo>Jogo</a>
   1. <a href=#como-rodar-o-jogo>Como rodar o jogo</a>
   2. <a href=#modificando-os-arquivos-do-jogo>Modificando os arquivos do jogo</a>
   3. <a href=#background-do-jogo>Background do jogo</a>
   4. <a href=#jogando>Jogando</a>
3. <a href=#implementação>Implementação</a>
   1. <a href=#classes-classespy>Classes</a>
   2. <a href=#importação-arquivospy>Importando Arquivos</a>
   3. <a href=#dificuldades-graphpy>Dificuldade</a>
   4. <a href=#funções-do-jogo-gamepy>Funções do Jogo</a>
   5. <a href=#telas>Telas</a>
      1. <a href=#urls-urlspy>URLs</a>
      2. <a href=#html>HTML</a>
      3. <a href=#views-viewspy>Views</a>

# Introdução

Este é um trabalho do aluno de Engenharia de Computação do CEFET-MG Campus V - Divinópolis, Pedro Pinheiro de Siqueira, para a disciplina de Algoritmos e Estruturas de Dados II (AEDSII). Este trabalho foi criado com o objetivo dos alunos aplicarem as estruturas de grafos para solucionar um problema real qualquer. Os alunos podiam escolher o problema e se utilizariam-se de C/C++ ou Python para o solucionar.

O problema escolhido não foi exatamente um real, dado que o aluno preferiu criar seu próprio grafo em um jogo. No entanto, o problema que é trabalhado no grafo criado pelo aluno é o de um grafo com arestas ponderadas para um problema mono objetivo, mas que poderia ser multi objetivo dado que os vértices do Grafo apresentado possuem diversas informações. A solução mono objetivo é o suficiente para atender os critérios deste trabalho.

Este problema foi abordado com a criação de um jogo simples de escolhas, onde o jogador terá que escolher para qual cidade (ou local) cuja distância é suficiente para obter bons resultados.

Por ter se decidipo por fazer um jogo e possuir tempo limitado para realizar o trabalho, a linguagem Python foi escolhida, não só o aluno possui um costume maior com ela, mas conseguiria criar uma GUI miníma em browser utilizando-se do Framework Django presente em Python para que isso fosse possível.

# Jogo

War Graph é um jogo de browser onde o jogador precisa tomar decisões sem um conhecimento futuro próximo, sua próxima jogada poderia ser literalmente a última sem ter o real conhecimento disso. O objetivo do jogador é maximizar a área conquistada pelo seu exército.

## Como rodar o Jogo

Para que este jogo rode é necessária a instalação do Python e do Django, o framework utilizado. O Python pode ser encontrado em seu <a href="https://www.python.org">site oficial</a>, a versão utilizada foi a 3.10 apesar <i>de que deve ser possível utilizar uma versão inferior caso já tenha instalada em sua máquina</i>, no entanto, recomenda-se que instale pelo menos esta versão para se ter certeza. Durante a instalação tenha certeza de instalar o pip e de incluir o python no PATH do seu computador.

As versões mais novas de Ptyhon já possuem o pip instalado automaticamente e por isso só é necessário atualizá-los antes de seguir adiante. Para testar se o seu está atualizado, basta abrir a linha de comando do seu computador e digitar `py -m pip install --upgrade pip`, onde o processo de atualização ocorrerá automaticamente se não estiver. Caso no seu caso não esteja nem mesmo instalado, por favor, siga o passo a passo do <a href="https://pip.pypa.io/en/latest/installation/">site do pip</a> para possuir a versão mais atualizada e não encontrar problemas nos passos posteriores.

Com o python instalado, abra a linha de comando do seu computador e instale o django. Para isso, basta digitar na linha de comando `python -m pip install Django`, caso tenha instalado o python corretamente com o pip. Se este comando não funcionar, por favor, siga o passo a passo pode ser visto no <a href="https://docs.djangoproject.com/en/4.1/topics/install/#installing-official-release">site oficial do Django</a>.

Com o Django instalado, abra a linha de comando (terminal) no caminho `...\Representando-e-Caminhando-em-Grafos\WarGraph`, onde se encontram as pastas Game, WarGraph (que tem o mesmo nome da pasta que a engloba), e dois arquivos, o manage.py e um banco de dados (.sqlite3). Para abrir a linha de comando nesta pasta, basta digitar `cmd` na aba de endereços se estiver no W
indows, ou apertar com o botão direito e abrir o terminal se estiver no Linux. Com a linha de comanda aberta nesta pasta, digite o comando `python manage.py runserver`.

Isso abrirá o servidor no <a href="127.0.0.1:8000">link padrão do Django</a>. Caso deseje rodar em algum IP diferente, digite o comando `python manage.py runserver IP desejado:Porta Desejada`.

## Modificando os arquivos do jogo

Para modificar os arquivos do jogo é necessário alterar os arquivos .csv dentro da pasta `...\Representando-e-Caminhando-em-Grafos\WarGraph\Game\static\arquivos`. Existem dois arquivos, o vertices.csv e o arestas.csv. Como os nomes indicam, eles possuem respectivamente os vértices e as arestas do grafo que será jogado. É possível alterar todos os pontos a própria vontade, seja adicionando arestas ou vértices. Relembrando que não pode se colocar acentos nos nomes das cidades.

<p align=center><img src="imgs/vertices.png" width="400px"/><img src="imgs/arestas.png" width="300px"/><p>

Ao alterar qualquer arquivo é necessário rodar novamente o jogo com comando especificado em <a href=#como-rodar-o-jogo>como rodar o jogo</a>. Ao fazer isso, caso não tenha errado na alteração dos arquivos, não verá mensagens de erro no terminal. Caso erre, poderá aparecer duas mensagens diferentes, ou talvez até ambas em conjunto:

<p align=center><img src="imgs/Erro_vertices.png" width="300px"/><img src="imgs/erro_arestas.png" width="320px"/><p>

Esses erros ocorrem quando acabou colocando algum vértice com acento ou com dados faltantes, enquanto nas arestas ocorre geralmente quando foi adicionada alguma aresta onde o vértice dela não existe.

Recomendo que não crie vértices nas mesmas coordenadas que vértices já existentes. Não que vá quebrar o jogo, este funcionará igualmente, pois não foi implementada alguma forma de barrar vértices no mesmo espaço físico que representariam no jogo, mas ficará ruim de jogar (se eles possuirem um mesmo vizinho) dado que a GUI não foi feita para este tipo de problema e acabará colocando as duas cidades no mesmo ponto, impossibilitando que se escolha uma delas. Além disso, é recomendado que se crie arestas para qualquer vértice adicionado. Novamente, o jogo foi preparado para impossibilitar que se jogue em uma cidade sem vizinhos, não ocorrerá nenhum erro, mas o jogador só perderia automaticamente, pois isso é claramente o jogador tentando roubar criando uma cidade de vitória instantânea.

A única limitação real e que não daria erro é que o vértice não pode ter o mesmo nome que outro vértice, não ocasionará em erro como citado, mas o vértice que vier depois no arquivo simplesmente não será adicionado ao Grafo.

## Background do Jogo

Como todo jogo precisa de um Backgruond, um simples foi criado para este, o background pode ser encontrado na aba About, junto com as Regras para a pessoa jogar. No entanto, para boa prática, colocaremos aqui também, para que se entenda o que está ocorrendo no jogo que foi implementado.

<blockquote>
<p align=justify>Você é um general com grandes chances de perder o seu emprego<strike>, ou sua cabeça</strike>. Invadiram o território de seu país e agora você se vê em um único ponto, uma última cidade, sem chance alguma de reaver o território por inteiro sem a decorrência de grandes sacrifícios. Descrentes de sua inteligência e capacidade, seus últimos aliados contratam um grupo de pessoas, que claramente não sabia o que estava fazendo, para criar um algoritmo que tomasse a melhor decisão de qual local atacar em seguida. Você furioso, partiu com seus homens para mostrar que conseguiria tomar uma rota melhor do que a deste algoritmo maldito antes mesmo de ver seu resultado.<p>

<p align=justify>War Graph é um jogo simples de tomada de decisões criado com o único objetivo de seus criadores utilizarem a estrutura de dados chamada Grafo. Seu objetivo primário neste jogo é conquistar uma área maior ou igual a do algoritmo utilizado (varia de acordo com a dificuldade escolhida).<p>

<p align=justify>Seus soldados possuem ❤️ (vida) e 🍗 (suprimentos) e gastam ambos para conquistar qualquer ponto que você vá no mapa. Suprimentos também são gastos para visitar bases já conquistadas. O gasto de 🍗 depende da 📏 (distância) percorrida, quanto mais longe, mais suprimentos serão gastos. Já a sua vida é gasta em combate, cada local possui sua própria infantaria de resistência e para ser conquistado é necessário que o seus soldados paguem com sua ❤️. Um adendo, também é possível perder vida por fome, caso você vá para um local tão distante que seus suprimentos acabem no meio da viagem, sua ❤️ começará a ser consumida no lugar.<p>

<p align=justify>Cada base a ser conquistada possui seu ⚔️ (poderio militar), 🍗 (suprimentos), 🩹 (medicamentos) e 🗺️ (área). Caso sobreviva a viagem e a batalha, após acabar com o ⚔️ adversário, seu exército recebe todos os outros recursos, que são somados a seus 🍗 (suprimentos), ❤️ (vida) e 🗺️ (área) respectivamente.<p>

<p align=justify>Quando uma cidade nunca foi visitada, seu símbolo no mapa aparecerá com a cor verde, quando já foi visitada, irá aparecer com a cor vermelha, caso essa cidade seja uma base, após visitada ela aparecerá com a cor azul, indicando que pode ser revisitada, porém o jogador não ganhará recursos o fazendo. O ponto que você está aparece com uma cor branca.<p>

<p align=justify>Para vencer basta provar seu valor. Conquiste uma área no mínimo igual ao do algoritmo e mostre que seus aliados não deveriam desistir de você tão facilmente.<p></blockquote>

## Jogando

Após colocar o jogo para rodar, é necessário ir ao <a href="http://127.0.0.1:8000/">link</a> como mencionado anteriormente. Nele, o jogador verá o seguinte menu:

<p align=center><img src="imgs/menu.png" width="400px"/><p>

O primeiro botão começará o jogo. O segundo botão levará o jogador a um menu de opções para que escolha qual cidade (vértice do grafo) deseja iniciar o jogo. O terceiro botão leva o jogador a um menu de escolha das dificuldades possíveis para o jogo, sendo elas fácil, normal e difícil, a diferença entre elas para o jogador é meramente a quantidade de área que o jogador precisa conquistar para vencer o jogo. A diferença para o programador será comentada e explicada na sessão de <a href=#implementação>implementação</a>. O último botão, como mencionado anteriormente, levará a uma tela que explicará o jogo para o jogador.

Ao iniciar o jogo, o jogador será levado para a tela a seguir:

<p align=center><img src="imgs/jogo.png"/><p>

Na área em azul no canto esquerdo inferior está a área que o jogador precisa conquistar para vencer. Idealmente ele não saberia essa área, pelo menos até um certo ponto, pois o general saiu de sua base sem essa informação. Porém, para demonstração dos algoritmos implementados, foi de interesse do criador do código que esse objetivo fosse visível. Na parte superior a esquerda vemos a localização do jogador, no momento, como iniciamos em uma cidade aleatória, acabou que caímos em Passos. No canto superior direito vemos os status atual do jogador, para que este consiga tomar as decisões de acordo com sua situação atual.

No centro vemos o mapa atual. Ribeirão Preto no exemplo é uma base, demonstrado pelo símbolo diferente que é um ponto onde podemos ir e voltar a vontade. Os demais pontos são pontos comuns, que só podem ser visitados uma única vez. Para se ver os dados de cada ponto, basta que se passe o mouse em cima do vértice desejado.

<p align=center><img src="imgs/jogo2.png"/><p>

Esses dados não ficam sempre visíveis junto com o nome pois existem regiões com tantas cidades que a informação ficava muito poluída, sendo que mesmo sem eles ela já está bem poluída para algumas cidades.

A partir deste ponto basta o jogador ir clicando nas cidades que deseja ir, tomando sempre a rota que desejar.

Ao finalizar, o jogador será levado para uma tela que o informa se venceu ou perdeu o jogo, além das rotas que ele e o algoritmo tomou. Novamente, esta não seria a opção ideal para um jogo, pois estamos deliberadamente contando ao jogador qual caminho ele precisa fazer para vencer, porém, para o propósito do trabalho e do grafo, acaba sendo necessário demonstrar tais caminhos.

<p align=center><img src="imgs/game_over.png" width="400px"/><p>

# Implementação

Toda a implementação do jogo foi feita no aplicativo Game e por isso seus códigos estão armazenados na pasta `...\Representando-e-Caminhando-em-Grafos\WarGraph\Game`. Vários `.py` desta pasta não foram utilizados e são mantidos por serem parte da base do Django, sendo melhor não apagá-los. Alguns não foram utilizados por não serem necessários, outros pelo pedido do professor de ser capaz de modificar os dados de entrada, o que não seria possível (de maneira simples) ao utilizar por exemplo o `models.py` ou o `admin.py`.

## Classes (classes.py)

O programa trabalha com três classes principais. O Personagem, o Grafo e o Vértice. Existiu uma quarta classe para auxiliar o BFS, mas como o BFS foi descartado durante a implementação, sua classe não está sendo utilizada no momento. Ela está presente no código final pelo menos motivo que qualquer outro código que não foi apagado, o autor acha que vai continuar programando o jogo no futuro e não sabe o que poderá reutilizar.

### Personagem

A classe personagem é utilizada tanto pelo jogador constantemente, onde os status que são vistos por ele sempre são os de seu personagem, como pelos algoritmos que determinam a dificuldade. Esta classe possui as seguintes variáveis (apesar de seus tipos serem definidos aqui, lembre-se que Python que é uma linguagem fracamente tipada, cabe ao programador lembrar de não alterar seus tipos durante as funções que as utilizar/chamar):

* Localização - Uma String que possui a localização atual do personagem
* Suprimentos - Um inteiro positivo que determina a quantidade de suprimentos que o personagem carrega no momento
* Vida - Um inteiro que determina a vida do personagem no momento
* Área - Um inteiro positivo que determina a quantidade de Área que o personagem já conquistou no momento
* Opções - Um inteiro positivo que determina quantas opções existem para o personagem se mover no momento atual - É utilizada de auxiliar para determinar se o jogo já pode acabar ou não
* Caminho - Uma lista de Strings que mostrará o caminho que este personagem já traçou até o momento

Esta classe possui 8 métodos.

#### \_\_init\_\_

O método construtor do Python. Ao se criar um personagem é necessário enviar o local inicial dele e o grafo. Com isso, tanto a localização quanto o Caminho já podem ser atualizados inicialmente. Opções sempre será igual a 0 no começo. A área inicial do personagem será igual a área do vértice que começou. Já seus Suprimentos e Vida são iguais a 100 mais o que existe no vértice que começou.

#### att_local

O método atualizar local, como o nome indica, atualizará a Localização do personagem no momento atual. Junto desta atualização, também é adicionada uma posição a mais na lista Caminho com essa nova Localização.

#### gastar_sup

O método gastar suprimentos, como o nome indica, gastará os suprimentos do personagem no momento atual de acordo com a distância andada. Lembrando que é necessário checar se o personagem possui suprimentos o suficiente para andar aquela distância, e se não possuir, o restante da distância será consumida de sua vida.

#### apos_luta

O método após lutar atualiza a vida do personagem após lutar pela dominância de algum vértice.

#### check_vida

O método checar vida simplesmente retorna True se o personagem estiver vivo (com vida superior a 0), ou False se o personagem estiver morto.

#### conquistando

O método conquitando atualizará a vida, a área e os suprimentos do personagem com base no vértice que acabou de conquistar. Este método foi implementado de forma separada do método att_local pois graças a existência de bases, existem vezes onde o local do personagem será atualizado e não existe a necessidade de se atualizar os outros valores.

#### print_personagem

O método consiste num print com os dados atuais do personagem no momento.

#### copy

O método retornará uma cópia do personagem no momento atual.

### Vértice

A classe vértice possui a maior parte das informações necessárias para que o jogo ocorra. Essas informações são destrinchadas nas seguintes variáveis:

* Nome - Uma String com o nome da cidade/local do vértice (Strings que não contenham pontuação ou acentos)
* X - Um inteiro com a coordenada X do vértice
* Y - Um inteiro com a coordenada Y do vértice
* Suprimentos - Um inteiro positivo com quantos suprimentos se encontram neste vértice
* Medicamentos - Um inteiro positivo com quantos medicamentos se encontram neste vértice 
* Força - Um inteiro positivo que determina a força do exército que se encontra neste vértice
* Base - Uma booleana que determina se este Vértice é uma base ou não
* Área - Um inteiro positivo que determina a área que este vértice contém
* Visitado - Uma booleana que determina se este Vértice já foi visitado ou não
* Vizinhos - Uma lista de Strings que contém os nomes dos Vizinhos deste vértice

Esta classe possui 5 métodos.

#### \_\_init\_\_

Método principal do Vértice, onde Nome, X, Y, Suprimentos, Medicamentos, Força, Base e Área são recebidos como parâmetro da leitura de arquivos. Visitado é setado como False, pois é impossível um Vértice ter sido visitado em sua criação. E é criada uma lista vazia de Vizinhos.

#### add_vizinho

Método onde o Vértice recebe o nome de um novo vizinho, checa se este já não se apresenta em sua lista de Vizinhos e o adiciona se não estiver.

#### att_sup

Atualiza suprimentos do vértice para 0.

#### att_med

Atualiza medicamentos do vértice para 0.

#### att_vis

Atualiza a variável visitado para True.

### Grafo

O Grafo em si, por ser um grafo com lista de adjacentes, acaba se tornando um grafo onde sua única variável é um dicionário de Vértices, onde o nome do Vértice é a chave para acessar o Vértice.

Esta classe possui 9 métodos

#### \_\_init\_\_

Ao ser iniciado, o grafo só possui um dicionário vazio de nome Vértices.

#### add_vertice

Neste método um vértice é enviado ao grafo para ser adicionado, caso este vértice não esteja presente, ele é adicionado ao dicionário.

#### add_edge

Neste método o Grafo recebe o nome dos dois vértices que possuem uma aresta entre eles e simplesmente chama o método add_vizinho de cada um deles.

#### copy

Neste método é retornado um grafo identico ao atual.

#### print_graph

Neste método são mostrados os nomes de todos os vértices, juntos da informação de se eles foram visitados e quais são seus vizinhos.

#### randomVertice

Neste método é retornado um vértice aleatório entre os Vértices presentes no grafo no momento.

#### visitados

Neste método é retornada uma lista de vértices que já foram visitados no Grafo.

#### cidades

Neste método é retornada uma lista em ordem alfabética de todos os vértices que existem no Grafo.

#### reset

Neste método o Grafo é resetado, para isso todos seus vértices são excluídos e o processo de colheita dos vértices ocorre novamente dos arquivos.

## Importação (arquivos.py)

O arquivos.py possui uma única função que é a de colher dados dos arquivos .csv e retorná-los para o usuário como um Grafo.

Para fazer isso, a primeira etapa é a criação de um objeto da classe Grafo, após isso, é realizada uma leitura linha a linha do arquivo de vértices, onde ao fazer isso é chamada a função de adicionar Vértice ao grafo. Após a leitura completa dos vértices, é feita a leitura das arestas. 

A validação de leitura de vértices e de leitura de arestas são feitas de forma separada para que fique mais fácil de visualizar qual arquivo está ocasionando em algum erro indesejado.

## Dificuldades (graph.py)

O jogo funciona com três dificuldades, sendo elas as dificuldades Fácil, Normal e Difícil. O objetivo dessas dificuldades é que um algoritmo um pouco mais complexo fosse executado para que a área final obtida fosse maior. Abaixo falarei qual foi a lógica usada para cada uma delas e o que poderia ser feito para melhorar ainda mais a dificuldade.

Como dito na <a href="#introdução">introdução</a> o problema poderia ser tratado como multi objetivo dado que existem diversas variáveis que poderiam ser maximizadas no grafo, no entanto neste trabalho foram utilizados algoritmos que se importam meramente com um objetivo, o de maximizar a área. Além disso, para tentar tornar o jogo o mais justo possível para o jogador, como este não consegue ver quantos vizinhos o ponto futuro tem (por decisão do programador), os algoritmos implementados também caminham sem olhar se o ponto futuro possui vizinhos que podem ser visitados.

Idealmente o jogador poderia visualizar todos os vértices do mapa para ter alguma noção de quais estão próximos de quais antes de tomar uma decisão, por mais que não soubesse o que tais pontos ofereceriam de recursos. Por exemplo, como estava no exército e as cidades foram tomadas, ele ainda deveria saber quais cidades Ribeirão Preto no exemplo da imagem em <a href=#jogando>jogando</a> pode visitar, por mais que ele não soubesse quantos recursos elas dão, pois sua rede de informações está limitada as cidades a seu entorno. No entanto, o aluno não conseguiu pensar em uma boa forma de fazer esse mapa maior como desejado, dado que mesmo o mapa pequeno para as poucas cidades consegue ter alguns problemas de cidades muito próximas.

Caso houvesse conseguido pensar em uma forma de fazer isso, as funções apresentadas a seguir poderiam ser programadas de outra forma.

### Fácil

No modo Fácil o jogador jogará com o algoritmo Guloso mais simples possível, onde será checado qual o vizinho (possível de ser visitado) que possui a maior área de todas e tentará ir para este ponto, independente da quantidade de vida, suprimentos, exército inimigo, ou qualquer outra coisa. Retornando assim a área final obtida pelo guloso e qual foi a rota que esse guloso fez.

### Normal

No modo Normal o jogador continuará jogando contra um algoritmo guloso bem simples, porém este não checará meramente qual o de maior área entre os vizinhos. Ele checará também se o jogador possui uma quantidade de vida maior do que o exército inimigo que será combatido, indo para a maior área que esta condição é atendida. Retornando assim a área final obtida pelo guloso e qual foi a rota que esse guloso fez. Com essa condição, é impossível que o modo Normal tenha alguma área final menor do que a do modo Fácil, sendo possível no máximo uma área igual onde os pontos andados sem medo de morte acabem levando o guloso a um beco sem saída.

### Difícil

No modo Difícil é realizada uma heurística bem simples. Ela começa pegando o resultado da dificuldade Normal e tentará trabalhar em cima dela para melhorá-la. Para isso são adicionados a rota todos os vértices do Grafo que não foram visitados no modo Normal.

A partir deste ponto, uma repetição começa a ser realizada, onde se troca o item visitado i pelo item visitado j. Sendo que i começa do segundo ponto da rota (pois o primeiro é imutável dado que é a localização inicial do jogador) indo até o penúltimo ponto, e j começa do terceiro ponto da rota indo até o último. Durante esta repetição é realizado o cálculo de se a rota nova obtida é melhor que a que voltou do modo Normal ou não.

Para essa avaliação é realizada a lógica simples de se começar na posição inicial do vetor e tentar visitar a posição seguinte, se não puder, tentar visitar a próxima, pois como foram realizadas trocas, não temos a certeza de que o ponto trocado é vizinho dos seus adjacentes no vetor, sendo sempre necessário checar se é ou não vizinho então do ponto atual que se está. O personagem vai andando neste vetor até morrer e quando isso ocorrer é verificada se a área que ele conseguiu é maior ou não do que a área que o modo Normal conseguiu.

Caso a área da troca seja maior, esta nova rota é salva, e o loop das trocas recomeça do começo do vetor. Ao realizar todo o loop de troca sem executar alguma troca melhor, o programa finaliza.

### Funções Auxiliares

Algumas funções auxiliares foram criadas para trabalhar de forma mais fácil com as três dificuldades. Todas são simples e por isso passarei um breve resumo do que cada uma faz:

* funcao_medio: A mais simples de todas, é a avaliação do guloso no nível Normal, que realiza a comparação citada no <a href=#normal>normal</a>, caso o jogador vá morrer, retorna que o valor de área do local é -1, se não, retorna o valor de área real;
* troca: Realiza as trocas no vetor de rota comentadas <a href=#difícil>difícil</a>;
* testarRota: Após realizada a troca, o nível difícil precisa testar se aquela nova rota criada é melhor ou pior que a melhor rota atual. Para checar a área dessa nova rota é utilizada essa função, que meramente percorre o vetor de rota sempre tentando mover o personagem para a próxima posição, realizando sempre que possível e contabilizando as cidades visitadas e qual foi a área final;
* apos_escolha: Sempre que algum nó foi escolhido como destino do personagem, é necessário que diversas funções do personagem rodem na ordem estabelecida no <a href=#background-do-jogo>background do jogo</a> para atualizar todos os seus valores, essa função juntou todas elas na sequência correta citada;
* zerarNo: Sempre que um vértice é visitado, ele precisa ser "limpo", ou seja, ele não pode fornecer mais área, suprimentos e medicamentos para o jogador, isso foi criado para que bases não abasteçam infinitamente o jogador dado que podem ser revisitadas;
* testarDificuldades: Por último, era necessário verificar se o modo difícil realmente estava performando melhor do que o médio e o fácil. Essa função foi criada para rodar os três modos em todos os vértices e contabilizar em quantos cada um ganhava. Por isso é possível afirmar que com os 41 vértices e 97 arestas, que estão no github, o modo Difícil apresentou um resultado melhor do que o modo Normal em 26 deles. Claro que com possíveis adições de vértices/arestas ou possíveis mudanças nos valores que existem atualmente poderão alterar o desempenho do Difícil.

### Outras formas de modificar a dificuldade

Além do citado anteriormente, com a mudança do mapa, que poderia modificar a forma de pensar como um todo do programa, existem outras formas de alterar o resultado do modo Difícil, já que este não foi perfeito, por isso, novas formas de como realizar as dificuldades começaram a ser imaginadas com a restrição do mapa existente.

Seria possível realizar métodos gulosos diferentes no Fácil e no Normal, que ao invés de só olharem a área ganha, olhassem para o ponto vizinho onde o jogador "sofreria" menos, indo para o ponto onde o balanço de exército inimigo e medicamentos fosse o mais vantajoso possível, outra alternativa seria o quanto o jogador perderá com a distância é compensado pelos suprimentos do local. Talvez, pensando em sobreviver o máximo possível, acabe sem querer, maximizando a área conquistada no processo.

Outra ideia possível seria visitar o vizinho que possui a maior razão área ganha/vida perdida ao visitar o ponto, ao invés de só ir para o ponto com a maior área. Esta solução é tão direta quanto a já implementada, sem grandes comentários.

Para o modo Difícil, imaginando que não foram alterados os anteriores, os pontos que são Bases poderiam ser adicionados mais de uma vez (até mesmo os já visitados), pois é possível que durante as trocas tenha alguma situação onde voltando uma vez para uma base acabasse indo para outro vértice que ela consegue ver e assim a rota melhorasse, mas não é possível somente adicionando todos os pontos não visitados uma vez. 

Outra forma é de executar uma troca dupla, onde poderia ocorrer com algum ponto talvez até mesmo aleatório, ao invés de só testar se uma troca é o suficiente para melhorar o resultado final do algoritmo.

O problema nas alterações do modo Difícil sugeridas é que o jogo poderia ficar muito lento a depender de quantos pontos a mais fossem adicionados para serem comparados, sendo que o modo Difícil atual já é bem mais lento do que os outros dois.

### Função não utilizada mais

O método de caminhamento pensado anteriormente para o Grafo e que seria apresentado neste trabalho seria um BFS modificado. No começo a ideia era de que os gulosos determinariam a área para as três dificuldades e o jogador ao escolher andar veria qual era a % de chance dele vencer a cada movimento. No entanto, para esse cálculo o BFS normal não é o suficiente, pois neste jogo não importa meramente se o ponto A ou B foi visitado como num BFS normal. Além disso, o jogador estando no ponto A, indo para o ponto B e depois para o C é diferente de estar no ponto A, ir para o C e depois para o B, então seria necessário que cada caminhada a um vizinho criasse uma rota diferente e essa fosse sendo atualizada com um próprio personagem atual. Assim ao contrário do BFS padrão que meramente tenta percorrer todo o grafo sem se importar necessariamente com a rota prevista, querendo achar algum vértice específico, no nosso caso não existe um vértice objetivo, o BFS teria que rodar até que não fosse mais possível andar, seja porque o ponto em que chegou não possui vizinhos possíveis de se ir, seja porque o personagem morreu. Com todos os finais diferentes que o BFS achasse, seria calculada a % pela fórmula básica:

$$ chance = {100 * \text{finais com área maior que o objetivo} \over \text{finais totais}} $$

## Funções do Jogo (game.py)

Apesar de ser dito que o problema possuia arestas ponderadas, não existe nenhuma amostra disso na implementação das classes ou nos arquivos. Isso se deve pois o peso de cada aresta é calculado sempre que algum vizinho é olhado do ponto atual para ele, sendo a distância que as cidades possuem de uma para a outra. Isso é feito pela única função do `game.py` que ainda é utilizada. Essa distância é calculada pela fórmula de distância de Manhattan, que determina o peso das arestas de acordo com o Nome do vértice que o jogador está, o Nome do vértice que o jogador vai e o grafo em si. Essa distância utiliza a seguinte fórmula:

$$ dis = |x_{i} - x_{j}| + |y_{i} - y_{j}| $$

Sendo assim uma fórmula impossível de possuir resultados em ponto flutuante dado que as coordenadas utilizadas no jogo são inteiros. Isso foi desejado para não existir uma complicação desnecessária para os jogadores.

Além desta função, anteriormente existiam duas outras funções, uma para determinar a localização do Jogador, pois este possuiria só as coordenadas e não o nome do local em que estivesse, pois o modo de jogo havia sido imaginado de uma forma um pouco diferente, onde não necessariamente começaria em um ponto especifico.

Outra função que se tornou obsoleta, foi mais pela necessidade de se fazer as dificuldades. Anteriormente o combate ocorreria ou não dependendo da distância que o jogador percorresse até o outro vértice. Como se havendo um exército inimigo que defende uma cidade vindo do ponto que você está, você gastando mais tempo para chegar lá indica que houvesse mais tempo para que este exército circundasse na cidade e visse o seu exército chegando. No entanto, sendo probabilidade de chance de ocorrer, ficaria difícil de fazer uma dificuldade, dado que o algoritmo poderia acabar combatendo em vértices que o jogador não e vice versa, tornando-se um problema complicado de se pensar em como setar e que começaria a fugir muito do escopo do trabalho.

## Telas

Em Django existe um processo para as urls que se pode visitar e o que são vistas nelas.

Antes de continuar, é necessário citar que Django permite criar páginas dinamicamente, colocando variáveis ou até if's e for no HTML que se encontra em `...\Representando-e-Caminhando-em-Grafos\WarGraph\Game\templates`, por isso é possível que diferentes urls utilizem o mesmo template e mesmo assim apresentem coisas ao jogador completamente diferentes.

### URLS (urls.py)

Para que se possa visitar uma URL em Django, é necessário que esta seja adicionada em `urls.py`. Neste arquivo se encontra uma lista de urls, onde cada item dela é um path. O path é feito por 3 partes, a primeira é o endereço que ela possui, o segundo é qual função no `views.py` ela chama, e a terceira é o nome deste path para caso seja chamado por outras funções. No `urls.py` do Game pode-se ver todos os endereços criado para o jogo, porém, caso se pesquise, é possível ver que existe um `urls.py` na pasta vizinha a pasta Game, a WarGraph. Como WarGraph é o projeto como um todo, ao ir ao link puro, acabaríamos caindo no index do projeto. No entanto, como só existe um aplicativo instalado neste projeto Django, foi colocado intencionalmente que o link puro aponte para o index do aplicativo em questão.

### HTML

Só foram necessários 4 templates HTML para o funcionamento do jogo. São eles:

* about.html
* fim.html
* jogo.html
* menu.html

O primeiro é o único estático, ele contém as informações citadas no <a href=#background-do-jogo>background do jogo</a>, para que o jogador saiba como jogar ou o que aconteceu.

O segundo possui uma série de if's que vão verificar qual foi o motivo do final do jogo e assim apresentar a tela correta ao jogador a depender de qual foi o final, as únicas variáveis que recebe são as que precisa para entender qual final foi, como vida do personagem, área do personagem, área que era o objetivo, número de vizinhos que o ponto atual possuía.

O terceiro é a tela principal do jogo, este é um dos que possui sua maior costumização, a cada vez que é carregada é feito um novo html com python a depender do ponto atual do jogador. Este html é inserido na parte preta, que é o mapa. Tudo que está envolta é "fixo", ou seja, sempre estão ali, mas seus valores mudam pois dependem das variáveis no momento.

O quarto é o template que possui a maior customização de todos. Ele aceita um grande bloco de html no meio. A única coisa que é constante entre os diferentes menus do jogo são os `.css` que são aplicados a eles. Pois cada menu apresenta opções completamente diferentes ao usuário.

### Views (views.py)

Como citado anteriormente, cada url chama uma função no views. São 11 urls, então são 11 funções no views. Aqui citarei cada uma.

#### index

A página inicial, como mostrada na figura na parte de <a href=#jogando>jogando</a>, possui 4 botões que levam para outras páginas. O index cria uma string que vai colocando o html como string passo a passo e envia essa string para o template menu, que transforma esta string em HTML. Esses botões direcionam para as views: `start`, `cidade`, `dificuldade` e `about` respectivamente.

#### dificuldade

A página de dificuldade é basicamente igual a página de index, só que ao invés de 4 botões são 3, um para cada dificuldade programada, e elas direcionam para a view `esc_dificuldade`, colocando as palavras facil, media e dificil como o argumento `escolha` que podia ser visto no `urls.py` da view esc_dificuldade, dado que a sua url era: `dificuldade/<str:escolha>`.

#### esc_dificuldade

Escolhendo dificuldade seta o valor da variável global `mode` para 1, 2 ou 3 a depender de qual escolha o usuário fez no menu Dificuldade. Após isso, manda renderizar o resultado da função `index`.

#### cidade

A página de cidade também é muito parecido com as outras duas que são menus, a sua única exceção é que foi criada de forma a ter três colunas de botões dado que existem muitas cidades. Caso ainda mais sejam inseridas, é possível começar a pensar em um formulário para escolher qual cidade se deseja começar. Neste menu também é adicionada uma opção inicial, sendo a Aleatória.

Todos os botões possuem o nome da cidade em seu link, pois igual a view dificuldade e esc_dificuldade, a view esc_cidade possui o parâmetro `escolha` em sua url.

#### esc_cidade

Escolhendo cidade seta o valor da variável global `inicial` para o nome da cidade escolhida pelo usuário. Após isso, manda renderizar o resultado da função `index`.

#### start

A função que inicia o jogo. Não possui um render próprio.

Ela começa inicializando o personagem na localização que estiver na variável global `inicial` no momento. Após a criação do personagem, o vértice inicial é zerado.

É checado se o ponto inicial do jogador possui algum vizinho. Se não possuir, é mandado renderizar o resultado da função `fim`. Como é necessário para o fim que exista a variável global `area_obj` e `rota`, ambas são setadas como a área do personagem e o caminho do personagem antes de ser mandado renderizar o resultado da função.

Caso o ponto inicial possua vizinhos, as variáveis globais `area_obj` e `rota` são criadas com a chamada da função de dificuldade que é especificada pela variável global `mode`.

Então é chamado o render da função `jogo`.

#### jogo

Jogo é basicamente a criação do html do mapa central. Onde é criado o HTML como uma string, iguais aos procedimentos do menu, mas preenchendo cada vértice vizinho e o próprio atual com suas próprias informações. Cálculos são feitos para tentar posicionar cada ponto em uma coordenada adequada utilizando o `position:fixed`. Além disso, a variável Opções da classe jogador começa a ser somada 1 para cada vértice que é possível de se visitar. Esses vértices que podem ser visitados possuem um link para a url `escolha/<str:nome>`, onde nome é o nome do Vértice em questão.

Ao final da criação do HTML, caso Opções continue igual a zero, é chamada a função `fim`, pois o jogador não possui opções para andar.

Caso opções não seja 0, zere após passar do teste, para na próxima vez que for utilizar esteja tudo ok ou não.

Com isso tudo feito, é realizado o render da página jogo, passando não só a string que contém o HTML, como o personagem, para seus dados serem colhidos, a área objetivo, a porcentagem de área já completada e a cor da barrinha de área.

#### escolha

Ao clicar em uma das cidades possíveis de se visitar, a função escolha é chamada.

Nesta função é realizado basicamente o mesmo passo a passo que existe na função auxiliar após escolha do `graph.py`:

* É checada a distância do ponto atual do personagem para a escolha;
* O personagem é movido até lá, ou seja, é chamado o método `att_sup` do personagem;
* Caso o ponto não tenha sido visitado, o personagem luta para dominar o ponto, ou seja, é chamado o método `apos_luta` do personagem;
* É checada a vida do personagem e caso seja menor ou igual a zero, a função `fim` é chamada;
* Novamente, se o vértice não tiver sido visitado, o personagem o conquista, ou seja, o método `conquistando` do personagem é chamado;
* O vértice escolhido é zerado;
* A variável visitado dele é marcada como True, sendo que só escrevendo o readme agora lembrei que havia criado uma função só para isso;
* É atualizada a localização do personagem;
* Checada se a área do personagem atingiu o objetivo, e caso tenha, a função `fim` é chamada;
* Se não tiver sido atingida, a função `jogo` é chamada novamente, para que o jogador possa continuar jogando.

#### fim

Como citado na parte de HTML, a página fim precisa de algumas variáveis para determinar qual foi o fim que a chamou. Por isso esta função meramente renderiza a página passando as variáveis para ela.

Uma forma de modificar isso seria modificando a view, como fim/\<int:tipo\>, onde cada final enviaria um inteiro diferente para essa nova view para simbolizar o fim específico que o jogador teve. Não seria necessário enviar as variáveis (apesar de que seria de bom gosto, dado que é legal o jogador ver como o jogo acabou), sendo só necessário que o template tivesse um if para ver qual número é e mostrasse o final correto, sem ter que ficar verificando.

#### reset

O reset reseta o grafo atual, para retornar todos os vértices ao que eram no começo, antes de serem visitados e terem suas variáveis zeradas, além de apagar o personagem. Em seguida, manda renderizar o resultado da função `index, que foi a primeira citada aqui.

#### about

A chamada de função mais fácil, simplesmente é um render da página html `about.html`, pois como citado, esta é a única página realmente estática do programa.

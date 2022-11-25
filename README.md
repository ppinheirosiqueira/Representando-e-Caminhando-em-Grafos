# Representando e Caminhando em Grafos
 
[![Python](https://img.shields.io/badge/Linguagem-Python-blue)](https://www.python.org)
[![requirement](https://img.shields.io/badge/Framework-Django-darkgreen)](https://www.djangoproject.com)
[![requirement](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-informational)](https://code.visualstudio.com/docs/?dv=linux64_deb)

# Objetivo

Neste trabalho o objetivo é aplicar as estruturas em grafos para solucionar um problema real qualquer.

# Problema Abordado

Meu problema é um grafo com arestas ponderadas para um problema mono objetivo, cuja distância é suficiente para obter bons resultados. Existe a possibilidade de ser multi objetivo porém esse não é o foco do seu esforço para esse trabalho. - <span style="color:red;">REESCREVE PEDRO</span>

Este problema foi abordado com a criação de um jogo simples de escolhas.

## Dados do Jogo

O jogo funciona com base em um Grafo não orientado com arestas ponderadas. O Vértice deste grafo possui as seguintes informações iniciais necessárias:

* Nome - Nome da cidade do vértice (Strings que não contenham pontuação ou acentos)
* X - Coordenada X do vértice (Valores inteiros positivos ou negativos)
* Y - Coordenada Y do vértice (Valores inteiros positivos ou negativos)
* Suprimentos - Quantos suprimentos se encontram neste vértice (Valores inteiros positivos)
* Medicamentos - Quantos medicamentos se encontram neste vértice (Valores inteiros positivos)
* Força - A força do exército que se encontra neste vértice (Valores inteiros positivos)
* Base - Se este Vértice é uma base ou não (1 ou 0 para determinar se é uma Base ou Não)
* Área - A área que este vértice contém (Valores inteiros positivos)

Além dessas o vértice possui a booleana Visitado, variável que é setada como False na criação do Vértice. E a lista de adjacências.

O peso das arestas é determinado pela distância entre os dois vértices, sendo esta a distância de Manhattan, que pode ser vista pela fórmula:

$$ dis = |x_{i} - x_{j}| + |y_{i} - y_{j}| $$

Pela forma que o problema foi proposto, foi decidido que cada Vértice teria sua lista de Adjacentes, visto que o Grafo criado não é denso o suficiente para justificar a matriz de adjacência.

Sendo um jogo, existe o Personagem, este Personagem possui as seguintes informações:

* Localização - Localização atual do personagem
* Suprimentos - Quantos suprimentos o personagem carrega no momento
* Vida - Qual a vida do personagem no momento
* Área - Quanta Área o personagem já conquistou no momento
* Opções - Quantas opções existem para o personagem se mover no momento atual
* Caminho - Qual o caminho que este personagem já traçou até o momento

## Background do Jogo

Como todo jogo precisa de um Backgruond, um simples foi criado para este, o background pode ser encontrado na aba About, junto com as Regras para a pessoa jogar. No entanto, para boa prática, colocaremos aqui também:

<p style="width:70%;text-align:justify;margin:auto;">Você é um general com grandes chances de perder o seu emprego<strike>, ou sua cabeça</strike>. Invadiram o território de seu país e agora você se vê em um único ponto, uma última cidade, sem chance alguma de reaver o território por inteiro sem a decorrência de grandes sacrifícios. Descrentes de sua inteligência e capacidade, seus últimos aliados contratam um grupo de pessoas, que claramente não sabia o que estava fazendo, para criar um algoritmo que tomasse a melhor decisão de qual local atacar em seguida. Você furioso, partiu com seus homens para mostrar que conseguiria tomar uma rota melhor do que a deste algoritmo maldito antes mesmo de ver seu resultado.</p><br>

<p style="width:70%;text-align:justify;margin:auto;">War Graph é um jogo simples de tomada de decisões criado com o único objetivo de seus criadores utilizarem a estrutura de dados chamada Grafo. Seu objetivo primário neste jogo é conquistar uma área maior ou igual a do algoritmo utilizado (varia de acordo com a dificuldade escolhida).</p><br>

<p style="width:70%;text-align:justify;margin:auto;">Seus soldados possuem ❤️ (vida) e 🍗 (suprimentos) e gastam ambos para conquistar qualquer ponto que você vá no mapa. Suprimentos também são gastos para visitar bases já conquistadas. O gasto de 🍗 depende da 📏 (distância) percorrida, quanto mais longe, mais suprimentos serão gastos. Já a sua vida é gasta em combate, cada local possui sua própria infantaria de resistência e para ser conquistado é necessário que o seus soldados paguem com sua ❤️. Um adendo, também é possível perder vida por fome, caso você vá para um local tão distante que seus suprimentos acabem no meio da viagem, sua ❤️ começará a ser consumida no lugar.</p><br>

<p style="width:70%;text-align:justify;margin:auto;">Cada base a ser conquistada possui seu ⚔️ (poderio militar), 🍗 (suprimentos), 🩹 (medicamentos) e 🗺️ (área). Caso sobreviva a viagem e a batalha, após acabar com o ⚔️ adversário, seu exército recebe todos os outros recursos, que são somados a seus 🍗 (suprimentos), ❤️ (vida) e 🗺️ (área) respectivamente.</p><br>

<p style="width:70%;text-align:justify;margin:auto;">Quando uma cidade nunca foi visitada, seu símbolo no mapa aparecerá com a <span style="color:#90EE90;">cor verde</span>, quando já foi visitada, irá aparecer com a <span style="color: lightcoral;">cor vermelha</span>, caso essa cidade seja uma base, após visitada ela aparecerá com a cor <span style="color: lightblue;">cor azul</span>, indicando que pode ser revisitada, porém o jogador não ganhará recursos o fazendo. O ponto que você está aparece com uma <span style="color:white">cor branca</span>.</p><br>

<p style="width:70%;text-align:justify;margin:auto;">Para vencer basta provar seu valor. Conquiste uma área no mínimo igual ao do algoritmo e mostre que seus aliados não deveriam desistir de você tão facilmente.</p><br>

## Como rodar o Jogo

Para que este jogo rode é necessária a instalação do Python e do Django, o framework utilizado. O Python pode ser encontrado em seu <a href="https://www.python.org">site oficial</a>, a versão utilizada foi a 3.10 apesar de acreditarmos que seja possível utilizar uma versão inferior caso já tenha instalada em sua máquina. Durante a instalação tenha certeza de instalar o pip e de incluir o python no PATH do seu computador.

As versões mais novas de Ptyhon já possuem o pip instalado automaticamente e por isso só é necessário atualizá-los antes de seguir adiante. Para testar se o seu está atualizado, basta abrir a linha de comando do seu computador e digitar `py -m pip install --upgrade pip`, onde o processo de atualização ocorrerá automaticamente se não estiver. Caso no seu caso não esteja nem mesmo instalado, por favor, siga o passo a passo do <a href="https://pip.pypa.io/en/latest/installation/">site do pip</a> para possuir a versão mais atualizada e não encontrar problemas nos passos posteriores.

Com o python instalado, abra a linha de comando do seu computador e instale o django. Para isso, basta digitar na linha de comando `$ python -m pip install Django`, caso tenha instalado o python corretamente com o pip. Se este comando não funcionar, por favor, siga o passo a passo pode ser visto no <a href="https://docs.djangoproject.com/en/4.1/topics/install/#installing-official-release">site oficial do Django</a>.

Com o Django instalado, abra a linha de comando no caminho `...\Representando-e-Caminhando-em-Grafos\WarGraph`, onde se encontram as pastas Game, WarGraph (que tem o mesmo nome da pasta que a engloba), e dois arquivos, o manage.py e um banco de dados (.sqlite3). Para abrir a linha de comando nesta pasta, basta digitar `cmd` na aba de endereços se estiver no windows, ou apertar com o botão direito e abrir o terminal se estiver no Linux. Com a linha de comanda aberta nesta pasta, digite o comando `python manage.py runserver`.

Isso abrirá o servidor no <a href="127.0.0.1:8000">link padrão do Django</a>. Caso deseje rodar em algum IP diferente, digite o comando `python manage.py runserver IP desejado:Porta Desejada`.

## Modificando os arquivos do jogo

Para modificar os arquivos do jogo é necessário alterar os arquivos .csv dentro da pasta `...\Representando-e-Caminhando-em-Grafos\WarGraph\Game\static\arquivos`. Existem dois arquivos, o vertices.csv e o arestas.csv. Como os nomes indicam, eles possuem respectivamente os vértices e as arestas do grafo que será jogado. É possível alterar todos os pontos a própria vontade, seja adicionando arestas ou vértices. Relembrando que não pode se colocar acentos nos nomes das cidades.

<center><img src="imgs/vertices.png" width="500px"/><img src="imgs/arestas.png" width="400px"/></center>

Ao alterar qualquer arquivo é necessário rodar novamente o jogo com comando especificado em <a href="#-Como-rodar-o-Jogo">Como rodar o jogo</a>. Ao fazer isso, caso não tenha errado na alteração dos arquivos, não verá mensagens de erro no terminal. Caso erre, poderá aparecer duas mensagens diferentes, ou talvez até ambas em conjunto:

<center><img src="imgs/Erro_vertices.png" width="400px"/><img src="imgs/erro_arestas.png" width="400px"/></center>

Esses erros ocorrem quando acabou colocando algum vértice com acento ou com dados faltantes, enquanto nas arestas ocorre geralmente quando você quis adicionar alguma aresta onde o vértice dela não existe.

Recomendo que não crie vértices nas mesmas coordenadas que vértices já existentes. Não que vá quebrar o jogo, este funcionará igualmente, pois não foi implementada alguma forma de barrar vértices no mesmo espaço físico que representariam no jogo, mas ficará ruim de jogar dado que a GUI não foi feita para este tipo de problema e acabará colocando as duas cidades no mesmo ponto, impossibilitando que se escolha uma delas. Além disso, é recomendado que se crie arestas para qualquer vértice adicionado. Novamente, o jogo foi preparado para impossibilitar que se jogue em uma cidade sem vizinhos, não chega a ser impossível, mas você só perderia automaticamente, pois isso é claramente o jogador tentando roubar criando uma cidade de vitória instantânea.

## Jogando

Após colocar o jogo para rodar, é necessário ir ao <a href="http://127.0.0.1:8000/">link</a> como mencionado anteriormente. Nele, o jogador verá o seguinte menu:

<center><img src="imgs/menu.png" width="400px"/></center>

O primeiro botão começará o jogo. O segundo botão levará o jogador a um menu de opções para que escolha qual cidade deseja iniciar o jogo. O terceiro botão leva o jogador a um menu de escolha das dificuldades possíveis para o jogo, sendo elas fácil, normal e difícil, a diferença entre elas para o jogador é meramente a quantidade de área que o jogador precisa conquistar para vencer o jogo. A diferença para o programador será comentada e explicada na sessão de <a href="#-Implementação">implementação</a>. O último botão, como mencionado anteriormente, levará a uma tela que explicará o jogo para o jogador.

Ao iniciar o jogo, o jogador será levado para a tela a seguir:

<center><img src="imgs/jogo.png"/></center>

Na área em azul no canto esquerdo inferior está a área que o jogador precisa conquistar para vencer. Idealmente ele não saberia essa área, pelo menos até um certo ponto, pois o general saiu de sua base sem essa informação. Porém, para demonstração dos algoritmos implementados, foi de interesse do criador do código que esse objetivo fosse visível. Na parte superior a esquerda vemos a localização do jogador, no momento, como iniciamos em uma cidade aleatória, acabou que caímos em Passos. No canto superior direito vemos os status atual do jogador, para que este consiga tomar as decisões de acordo com sua situação atual.

No centro vemos o mapa atual. Ribeirão Preto no exemplo é uma base, demonstrado pelo símbolo diferente que é um ponto onde podemos ir e voltar a vontade. Os demais pontos são pontos comuns, que só podem ser visitados uma única vez. Para se ver os dados de cada ponto, basta que se passe o mouse em cima do vértice desejado.

<center><img src="imgs/jogo2.png"/></center>

Esses dados não ficam sempre visíveis junto com o nome pois existem regiões com tantas cidades que a informação ficava muito poluída, sendo que mesmo sem eles ela já está bem poluída.

A partir deste ponto basta o jogador ir clicando nas cidades que deseja ir, tomando sempre a rota que desejar.

Ao finalizar, o jogador será levado para uma tela que o informa se venceu ou perdeu o jogo, além das rotas que ele e o algoritmo tomou. Novamente, esta não seria a opção ideal para um jogo, pois estamos deliberadamente contando ao jogador qual caminho ele precisa fazer para vencer, porém, para o propósito do trabalho e do grafo, acaba sendo necessário demonstrar tais caminhos.

<center><img src="imgs/game_over.png"/></center>

# Implementação


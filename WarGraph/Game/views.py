from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import arquivos, classes, game, graph

"""
Ao iniciar o aplicativo o jogo é setado para escolher a dificuldade média, com uma cidade aleatória e criar o grafo de acordo com os arquivos
"""
mode = 2
inicial = "aleatoria"
g  = arquivos.colher_dados() # Inicia o Grafo

# Create your views here.

def index(request): # Tela Inicial
    global mode
    body = '<div class="title"><h1>WAR GRAPH</h1></div>'
    body = body + '<div class="middle">'
    body = body + '<div class="show">'
    body = body + 'Dificuldade: ' 
    if mode == 1:
        body = body + 'Fácil'
    elif mode == 2:
        body = body + 'Normal'
    else:
        body = body + 'Difícil'
    body = body + '<br>Cidade Inicial: '
    if inicial == "aleatoria":
        body = body + 'Aleatória'
    else:
        body = body + inicial
    body = body + '</div>'
    body = body + '<a href="start" class="btn btn1">Start game</a>'
    body = body + '<a href="cidade" class="btn btn2">City</a>'
    body = body + '<a href="dificuldade" class="btn btn3">Mode</a>'
    body = body + '<a href="about" class="btn btn4">About</a>'
    body = body + '</div>'

    return render(request, "menu.html", {
        "body": body,
        "title": "WAR GRAPH",
    })

def dificuldade(request):
    body = '<div class="title"><h1>DIFICULDADE</h1></div>'
    body = body + '<div class="middle">'
    body = body + '<a href="dificuldade/facil" class="btn btn3">Easy</a>'
    body = body + '<a href="dificuldade/media" class="btn btn3">Normal</a>'
    body = body + '<a href="dificuldade/dificil" class="btn btn3">Hard</a>'
    body = body + '</div>'

    return render(request, "menu.html", {
        "body": body,
        "title": "Dificuldade",
    })

def esc_dificuldade(request, escolha):
    global mode
    if escolha == "facil":
        mode = 1
    elif escolha == "media":
        mode = 2
    else:
        mode = 3
    return HttpResponseRedirect(reverse('index',None))

def cidade(request):
    cidades = g.cidades()
    body = '<div class="title"><h1>CIDADES</h1></div>'
    body = body + '<div class="cidade_menu">'
    body = body + '<a href="cidade/aleatoria" class="btn btn2">Aleatória</a>'
    for cidade in cidades:
        body = body + '<a href="cidade/' + cidade + '" class="btn btn2">' + cidade + '</a>'
    body = body + '</div>'

    return render(request, "menu.html", {
        "body": body,
        "title": "Cidades",
    })

def esc_cidade(request,escolha):
    global inicial
    inicial = escolha
    return HttpResponseRedirect(reverse('index',None))

def start(request):
    global area_obj
    global p
    global rota
    global mode

    #graph.testarDificuldades(g)

    if inicial != "aleatoria":
        p = classes.Personagem(inicial, g) # Inicia o Personagem com a cidade escolhida inicialmente
    else:
        p = classes.Personagem(g.randomVertice(),g) # Inicia o Personagem com uma cidade randômica

    # p.print_personagem()

    graph.zerarNo(g,p.Localizacao)    
    g2 = g.copy()
    if mode == 1:
        area_obj, rota = graph.guloso_facil(g2,p)
    elif mode == 2:
        area_obj, rota = graph.guloso_medio(g2,p)
    else:
        area_obj, rota = graph.guloso_dificil(g2,p)

    if len(g.vertices[p.Localizacao].Vizinhos) == 0:
        return HttpResponseRedirect(reverse('fim',None))

    return HttpResponseRedirect(reverse('jogo',None))

def jogo(request):  
    global area_obj

    bigX = g.vertices[p.Localizacao].X
    bigY = g.vertices[p.Localizacao].Y
    smallX = g.vertices[p.Localizacao].X
    smallY = g.vertices[p.Localizacao].Y

    for vizinho in g.vertices[p.Localizacao].Vizinhos:
        if g.vertices[vizinho].X > bigX:
            bigX = g.vertices[vizinho].X
        if g.vertices[vizinho].Y > bigY:
            bigY = g.vertices[vizinho].Y
        if g.vertices[vizinho].X < smallX:
            smallX = g.vertices[vizinho].X
        if g.vertices[vizinho].Y < smallY:
            smallY = g.vertices[vizinho].Y

    rangeX = 10 +  abs(bigX-smallX)
    rangeY = 10 + abs(bigY-smallY)

    if g.vertices[p.Localizacao].Base:
        auxP = "base"
    else:
        auxP = "cidade"

    mapa = ""
    # Adicionando onde você está
    mapa += '<a style="bottom:' + str(100*(abs(5 + g.vertices[p.Localizacao].Y - smallY))/rangeY) + '%;left:' +  str(100*(abs(5 + g.vertices[p.Localizacao].X - smallX))/rangeX) + '%;">'
    mapa += '<img src="static/imagens/' + auxP + '.svg" alt="' + p.Localizacao + '" class="filter-white icones"><br>' + p.Localizacao
    mapa += '<span class="tooltiptext">Estou Aqui</span></a>'
    
    for vizinho in g.vertices[p.Localizacao].Vizinhos:
        if g.vertices[vizinho].Base:
            auxP = "base"
            if g.vertices[vizinho].Visitado:
                auxC = "filter-blue"
            else:
                auxC = "filter-green"
        else:
            auxP = "cidade"
            if g.vertices[vizinho].Visitado:
                auxC = "filter-red"
            else:
                auxC = "filter-green"

        if not g.vertices[vizinho].Visitado or g.vertices[vizinho].Base: # Adicionando pontos que você pode ir
            mapa += '<a href="escolha/' +  vizinho + '" style="bottom:' +  str(100*(5 + abs(g.vertices[vizinho].Y - smallY))/rangeY) + '%;left:' +  str(100*(abs(5 + g.vertices[vizinho].X - smallX))/rangeX) + '%;">'
            mapa += '<img src="static/imagens/' + auxP + '.svg" alt="' + vizinho + '" class="' + auxC + ' icones"><br>' + vizinho
            mapa += '<span class="tooltiptext">'
            mapa += '📏: ' + str(game.distancia(p.Localizacao,vizinho,g))
            if g.vertices[vizinho].Base and g.vertices[vizinho].Visitado:
                mapa += "<br>Já visitado"
            else:
                mapa += ' ⚔️: ' + str(g.vertices[vizinho].Strength) + '<br>'
                mapa += '🗺️: ' + str(g.vertices[vizinho].Area)  
                mapa += ' 🩹: ' + str(g.vertices[vizinho].Medicamentos) + '<br>'
                mapa += '🍗: ' + str(g.vertices[vizinho].Suprimentos)
            mapa += '</span></a>'
            p.Opcoes += 1
        else: # Adicionando pontos que você não pode ir
            mapa += '<a style="bottom:' + str(100*(abs(g.vertices[vizinho].Y - smallY))/rangeY) + '%;left:' + str(100*(abs(g.vertices[vizinho].X - smallX))/rangeX) + '%;">'
            mapa += '<img src="static/imagens/' + auxP + '.svg" alt="' + vizinho + '" class="' + auxC + ' icones"><br>' + vizinho
            mapa += '<span class="tooltiptext">Já visitado</span></a>'

    if p.Opcoes == 0:
        return HttpResponseRedirect(reverse('fim',None))

    p.Opcoes = 0

    porcentagem = round(100*p.Area/area_obj,2)

    if porcentagem < 40:
        cor = "vermelho"
    elif porcentagem < 80:
        cor = "marrom"
    else:
        cor = "verde"

    return render(request, "jogo.html", {
        "localizacao": p.Localizacao,
        "vida": p.Vida,
        "area": p.Area,
        "suprimentos": p.Suprimentos,
        "mapa": mapa,
        "area_obj": area_obj,
        "porcentagem": porcentagem,
        "cor": cor,
    })

def escolha(request,nome):
    global area_obj
    # Já tendo a posição do jogador e o nome do Vértice que ele quer ir, é possível andar

    distancia = game.distancia(p.Localizacao,nome,g) # Calcula a distância

    p.gastar_sup(distancia) # Personagem anda até lá

    if not g.vertices[nome].Visitado:
        p.apos_luta(g.vertices[nome].Strength) # Caso nunca tenha ido, tem que batalhar para tomar o ponto
        #game.combate(distancia,p,g.vertices[nome]) # Caso queira um combate com chance de ocorrer

    if p.Vida <= 0 :
        return HttpResponseRedirect(reverse('fim',None)) # Se morreu andando ou batalhando, o jogo acaba

    if not g.vertices[nome].Visitado:
        p.conquistando(g.vertices[nome].Area,g.vertices[nome].Medicamentos,g.vertices[nome].Suprimentos) # Se nunca visitou, conquistar os suprimentos do local

    graph.zerarNo(g,nome)

    g.vertices[nome].Visitado = True # Mudar para True o visitado

    p.att_local(nome) # Atualizar o Local

    if p.Area >= area_obj: # Se a área for igual ou maior, vitória
        return HttpResponseRedirect(reverse('fim',None))

    return HttpResponseRedirect(reverse('jogo',None))

def fim(request):
    global area_obj
    global rota
    # Tela auxiliar de fim do jogo
    return render(request, "fim.html", {
        "p": p,
        "area_obj": area_obj,
        "vizinhos": len(g.vertices[p.Localizacao].Vizinhos),
        "rota": rota,
    })

def reset(request):
    global p
    g.reset() # Reinicia o Grafo
    del p # Apaga o Personagem

    return HttpResponseRedirect(reverse('index',None))

def about(request):
    return render(request, "about.html")
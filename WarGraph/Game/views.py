from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import arquivos, classes, game, graph

dificuldade = 2
inicial = "aleatoria"
g  = arquivos.colher_dados() # Inicia o Grafo

# Create your views here.

def index(request): # Tela Inicial
    global dificuldade

    body = '<div class="title"><h1>WAR GRAPH</h1></div>'
    body = body + '<div class="middle">'
    body = body + '<div class="show">'
    body = body + 'Dificuldade: ' 
    if dificuldade == 1:
        body = body + 'Fácil'
    elif dificuldade == 2:
        body = body + 'Normal'
    else:
        body = body + 'Difícil'
    body = body + '<br>Cidade Inicial: '
    if inicial == " ":
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
    global dificuldade
    if escolha == "facil":
        dificuldade = 1
    elif escolha == "media":
        dificuldade = 2
    else:
        dificuldade = 3
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

    if inicial != "aleatoria":
        p = classes.Personagem(inicial, g) # Inicia o Personagem com a cidade escolhida inicialmente
    else:
        p = classes.Personagem(g.randomVertice(),g) # Inicia o Personagem com uma cidade randômica

    if len(g.vertices[p.Localizacao].Vizinhos) == 0:
        return HttpResponseRedirect(reverse('fim',None))

    # p.print_personagem()

    graph.zerarNo(g,p.Localizacao)    
    g2 = g.copy()
    if dificuldade == 1:
        area_obj, rota = graph.guloso_facil(g2,p)
    elif dificuldade == 2:
        area_obj, rota = graph.guloso_medio(g2,p)
    else:
        area_obj, rota = graph.guloso_dificil(g2,p)
    return HttpResponseRedirect(reverse('jogo',None))

def jogo(request):  
    global area_obj

    chance =  40 #graph.BFS(g,p,area_obj)

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

    rangeX = 1.1*(abs(bigX) + abs(smallX))
    rangeY = 1.1*(abs(bigY) + abs(smallY))

    mapa = ""
    # Adicionando onde você está
    mapa = mapa + '<a style="top:' + str(100*(g.vertices[p.Localizacao].Y + abs(smallY))/rangeY) + '%;left:' +  str(100*(g.vertices[p.Localizacao].X + abs(smallX))/rangeX) + '%;">'
    mapa = mapa + '<img src="static/imagens/cidade.svg" alt="' + p.Localizacao + '" class="filter-blue icones">'
    mapa = mapa + '<span class="tooltiptext">' + p.Localizacao + '<br>Estou Aqui</span></a>'
    
    for vizinho in g.vertices[p.Localizacao].Vizinhos:
        if g.vertices[vizinho].Visitado:
            auxC = "filter-red"
        else:
            auxC = "filter-green"

        if not g.vertices[vizinho].Visitado: # Adicionando pontos que você pode ir
            mapa = mapa + '<a href="escolha/' +  vizinho + '" style="top:' + str(100*(g.vertices[vizinho].Y + abs(smallY))/rangeY) + '%;left:' +  str(100*(g.vertices[vizinho].X + abs(smallX))/rangeX) + '%;">'
            mapa = mapa + '<img src="static/imagens/cidade.svg" alt="' + vizinho + '" class="' + auxC + ' icones">'
            mapa = mapa + '<span class="tooltiptext">' + vizinho + '<br>'
            mapa = mapa + '📏: ' + str(game.distancia(p.Localizacao,vizinho,g))
            mapa = mapa + ' 🗺️: ' + str(g.vertices[vizinho].Area)  + '<br>'
            mapa = mapa + '⚔️: ' + str(g.vertices[vizinho].Strength)
            mapa = mapa + ' 🩹: ' + str(g.vertices[vizinho].Medicamentos) + '<br>'
            mapa = mapa + '🍗: ' + str(g.vertices[vizinho].Suprimentos) + '</span></a>'
            p.Opcoes += 1
        else: # Adicionando pontos que você não pode ir
            mapa = mapa + '<a style="top:' + str(100*(g.vertices[vizinho].Y + abs(smallY))/rangeY) + '%;left:' + str(100*(g.vertices[vizinho].X + abs(smallX))/rangeX) + '%;">'
            mapa = mapa + '<img src="static/imagens/cidade.svg" alt="' + vizinho + '" class="' + auxC + ' icones">'
            mapa = mapa + '<span class="tooltiptext">' + vizinho + '<br>Já visitado</span></a>'

    if p.Opcoes == 0:
        return HttpResponseRedirect(reverse('fim',None))

    p.Opcoes = 0

    porcentagem = round(100*p.Area/area_obj,2)

    if porcentagem < 50:
        cor = "vermelho"
    else:
        cor = "verde"

    return render(request, "jogo.html", {
        "localizacao": p.Localizacao,
        "vida": p.Vida,
        "area": p.Area,
        "suprimentos": p.Suprimentos,
        "mapa": mapa,
        "area_obj": area_obj,
        "chance": round(chance,2),
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
        "vida": p.Vida,
        "area": p.Area,
        "area_obj": area_obj,
        "vizinhos": len(g.vertices[p.Localizacao].Vizinhos),
        "rota": rota,
        "rota_jog": p.Caminho,
    })

def reset(request):
    global p
    g.reset() # Reinicia o Grafo
    del p # Apaga o Personagem

    return HttpResponseRedirect(reverse('index',None))

def about(request):
    return render(request, "about.html")
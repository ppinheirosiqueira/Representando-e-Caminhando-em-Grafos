from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import graph
from . import game
from . import arquivos
from . import classes

dificuldade = 2
inicial = " "
g  = arquivos.colher_dados() # Inicia o Grafo

# Create your views here.

def index(request): # Tela Inicial

    body = '<h1 class="title">WAR GRAPH</h1>'
    body = body + '<div class="middle">'
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
    body = '<h1 class="title">DIFICULDADE</h1>'
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
    print(cidades)
    body = '<h1 class="title">CIDADES</h1>'
    body = body + '<div class="middle">'
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
    
    if inicial != " ":
        p = classes.Personagem(inicial, g, dificuldade) # Inicia o Personagem com a cidade escolhida inicialmente
    else:
        p = classes.Personagem(g.randomVertice(),g, dificuldade) # Inicia o Personagem com uma cidade randômica

    p.print_personagem()

    g.vertices[p.Localizacao].Visitado = True
    g2 = g.copy()
    if dificuldade == 1:
        area_obj = graph.guloso_facil(g2,p)
    elif dificuldade == 2:
        area_obj = graph.guloso_medio(g2,p)
    else:
        area_obj = graph.guloso_dificil(g2,p)
    return HttpResponseRedirect(reverse('jogo',None))

def jogo(request):  
    global area_obj
    chance = graph.BFS(g,p,area_obj)

    mapa = "Estou em " + p.Localizacao + "<br>"
    mapa = mapa + "O meu objetivo é ter " + str(area_obj) + " de area<br>"
    mapa = mapa + "Possuo " + str(round(chance,2)) + "% de chance de vitória<br>"
    for vizinho in g.vertices[p.Localizacao].Vizinhos:
        if(g.vertices[vizinho].Base or not g.vertices[vizinho].Visitado):
            mapa = mapa + '<a href="escolha/' +  vizinho + '">' + '<button type="button" href="escolha/' + vizinho + '">' +  vizinho + '</button></a><br>'

    return render(request, "jogo.html", {
        "vida": p.Vida,
        "area": p.Area,
        "suprimentos": p.Suprimentos,
        "mapa": mapa,
    })

def escolha(request,nome):
    global area_obj
    # Já tendo a posição do jogador e o nome do Vértice que ele quer ir, é possível andar

    distancia = game.distancia(p.Localizacao,nome,g)

    p.gastar_sup(distancia) # Personagem anda até lá

    if not g.vertices[nome].Visitado:
        game.combate(distancia,p,g.vertices[nome])

    if p.Vida < 0 :
        return HttpResponseRedirect(reverse('fim',None))

    if not g.vertices[nome].Visitado:
        p.conquistando(g.vertices[nome].Area,g.vertices[nome].Medicamentos,g.vertices[nome].Suprimentos)

    g.vertices[nome].Visitado = True

    p.att_local(nome)

    if p.Area >= area_obj:
        return HttpResponseRedirect(reverse('fim',None))

    return HttpResponseRedirect(reverse('jogo',None))

def fim(request):
    # Tela auxiliar de fim do jogo
    return render(request, "fim.html", {
        "vida": p.Vida,
        "area": p.Area,
        "suprimentos": p.Suprimentos,
    })

def reset(request):
    global inicial
    global p
    global dificuldade
    g.reset() # Reinicia o Grafo
    inicial = " " # Coloca a cidade inicial como randomica novamente
    dificuldade = 2 # Reseta a dificuldade para normal
    del p # Apaga o Personagem

    return HttpResponseRedirect(reverse('index',None))

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import graph
from . import game

dificuldade = 2
g  = graph.colher_dados() # Inicia o Grafo
p = game.Personagem(g.randomVertice(),dificuldade) # Inicia o Personagem

# Create your views here.

def index(request): # Tela Inicial

    return HttpResponse("Oi")

    return HttpResponseRedirect(reverse('jogo',None))

def jogo(request):  
    
    """
    print()
    g.print_graph()
    print()
    p.print_personagem()
    print()

    #loc = game.descobrir_localizacao(g,p)

    print("O personagem está em: " + p.Localizacao)

    g2 = g.copy()

    g.add_vertice(graph.Vertice("Teste",10,12,24,52,12,False,25))
    g2.add_vertice(graph.Vertice("Pedras",3,2,10,10,20,False,10))

    print()
    g.print_graph()
    print() 
    g2.print_graph()
    print()"""

    mapa = "Estou em " + p.Localizacao + "<br>"
    for vizinho in g.vertices[p.Localizacao].Vizinhos:
        if(g.vertices[vizinho].Base or not g.vertices[vizinho].Visitado):
            mapa = mapa + '<a href="escolha/' +  vizinho + '">' + vizinho + '</a><br>'


    return render(request, "index.html", {
        "vida": p.Vida,
        "area": p.Area,
        "suprimentos": p.Suprimentos,
        "mapa": mapa,
    })

def escolha(request,nome):
    # Já tendo a posição do jogador e o nome do Vértice que ele quer ir, é possível andar

    distancia = game.distancia(p,nome,g)

    p.att_sup(distancia) # Personagem anda até lá

    if not g.vertices[nome].Visitado:
        p.att_area(g.vertices[nome].Area)

    g.vertices[nome].Visitado = True

    game.combate(distancia,p,g.vertices[nome])

    if p.Vida < 0 :
        return HttpResponseRedirect(reverse('fim',None))

    p.att_local(nome)

    return HttpResponseRedirect(reverse('jogo',None))

def fim(request):
    # Tela auxiliar de fim do jogo
    return render(request, "fim.html", {
        "vida": p.Vida,
        "area": p.Area,
        "suprimentos": p.Suprimentos,
    })

def reset(request):
    g.reset() # Inicia o Grafo
    p.__init__(g.randomVertice(),dificuldade) # Inicia o Personagem

    return HttpResponseRedirect(reverse('jogo',None))

from django.shortcuts import render
from django.http import HttpResponse

from . import graph
from . import game

# Create your views here.

def index(request):
    p = game.Personagem() # Inicia o Personagem
    g = graph.colher_dados() # Inicia o grafo

    print()
    g.print_graph()
    print()
    p.print_personagem()
    print()

    print("O personagem está em: " + str(game.descobrir_localizacao(g,p)))

    return HttpResponse("Hello, world. You're at the polls index.")
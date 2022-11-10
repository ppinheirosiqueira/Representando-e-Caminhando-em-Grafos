from . import game

def guloso_facil(g,nome):
    pAux = game.Personagem(g.vertices[nome].name)

    while pAux.Vida >= 0:
        print("Localização Atual: " + pAux.Localizacao)
        print("Vida Atual: " + str(pAux.Vida))
        print("Suprimentos Atual: " + str(pAux.Suprimentos))
        nomeVizinho = ""
        areaVizinho = -10
        for vizinho in g.vertices[pAux.Localizacao].Vizinhos:
            if g.vertices[vizinho].Area > areaVizinho and (not g.vertices[vizinho].Visitado or g.vertices[vizinho].Base):
                areaVizinho = g.vertices[vizinho].Area
                nomeVizinho = g.vertices[vizinho].name
        distancia = game.distancia(pAux,nomeVizinho,g)
        pAux.att_sup(distancia) # Personagem anda até lá
        if not g.vertices[nomeVizinho].Visitado:
            pAux.att_vida(g.vertices[nomeVizinho].Strength)
        if pAux.Vida < 0 :
            break
        if not g.vertices[nomeVizinho].Visitado:
            pAux.att_tudo(g.vertices[nomeVizinho].Area,g.vertices[nomeVizinho].Medicamentos,g.vertices[nomeVizinho].Suprimentos)
        g.vertices[nomeVizinho].Visitado = True
        pAux.att_local(nomeVizinho)
        g.vertices[nomeVizinho].Area = 0
    
    print("Área do guloso foi igual a: " + str(pAux.Area))

def guloso_medio(g,nome):
    pAux = game.Personagem(g.vertices[nome].name)
    print("Área do guloso foi igual a: " + str(pAux.Area))

def guloso_dificil(g, nome):
    pAux = game.Personagem(g.vertices[nome].name)
    print("Área do guloso foi igual a: " + str(pAux.Area))

def BFS(g, nome):
    pAux = game.Personagem(g.vertices[nome].name)
    print("Área do guloso foi igual a: " + str(pAux.Area))
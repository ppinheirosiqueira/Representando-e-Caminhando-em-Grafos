from . import game
from . import classes
import copy

def guloso_facil(g,nome):
    pAux = classes.Personagem(g.vertices[nome].name)

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
        distancia = game.distancia(pAux.Localizacao,nomeVizinho,g)
        pAux.gastar_sup(distancia) # Personagem anda até lá
        if not g.vertices[nomeVizinho].Visitado:
            pAux.apos_luta(g.vertices[nomeVizinho].Strength)
        if pAux.Vida < 0 :
            break
        if not g.vertices[nomeVizinho].Visitado:
            pAux.conquistando(g.vertices[nomeVizinho].Area,g.vertices[nomeVizinho].Medicamentos,g.vertices[nomeVizinho].Suprimentos)
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

def BFS(g, personagem):
    auxPonto = [0,0] # Vetor Auxiliar que conterá o personagem e os nós que já foram caminhados
    andando = [] # Vetor que conterá todas as opções de andado e que continuará andando
    final = [] # Sempre que o personagem morrer, será levado para este vetor

    auxPonto[0] = copy.deepcopy(personagem) # Informações do personagem
    auxPonto[1] = [personagem.Localizacao] # Nomes dos locais visitados - Preciso rodar no grafo depois e ver todos os pontos já visitados

    andando.append(auxPonto) # Andando começa no ponto que o personagem está

    print("\n\n")
    print(andando[0][1])
    while len(andando) > 0: # Enquanto houver formas de andar
        auxLocais = g.vertices[andando[0][0].Localizacao].Vizinhos # Pego os vizinhos do primeiro ponto do vetor de andar
        print("Andando: " + str(len(andando)))
        print(auxLocais)
        print("\n")
        while len(auxLocais) > 0: # Enquanto houver vizinhos a visitar
            if auxLocais[0] not in andando[0][1] or g.vertices[auxLocais[0]].Base: # Vai para lá se for base
                auxPonto[0] = copy.deepcopy(andando[0][0]) # Copio o personagem como ele está
                auxPonto[1] = copy.deepcopy(andando[0][1]) # Copio onde já andou
                distancia = game.distancia(auxPonto[0].Localizacao,auxLocais[0],g) # Calculo a distância de onde o personagem está até onde ele vai
                auxPonto[0].gastar_sup(distancia) # Personagem anda até lá
                if auxLocais[0] not in auxPonto[1]: # Se o local a ser visitado ainda não foi visitado
                    auxPonto[0].apos_luta(g.vertices[auxLocais[0]].Strength) # Desconto a vida do ataque
                if auxPonto[0].Vida < 0 : # Caso a vida do personagem seja menor do que zero
                    auxPonto[1].append(auxLocais[0])
                    final.append(auxPonto) # Adiciono o personagem e onde ele foi para o vetor final
                    continue
                if auxLocais[0] not in auxPonto[1]: # Caso o personagem não tenha visitado o ponto ainda, adiciono o que o ponto me da
                    auxPonto[0].conquistando(g.vertices[auxLocais[0]].Area,g.vertices[auxLocais[0]].Medicamentos,g.vertices[auxLocais[0]].Suprimentos)
                    auxPonto[1].append(auxLocais[0]) # Adiciono este ponto aos pontos visitados
                auxPonto[0].att_local(auxLocais[0]) # Atualizo onde o personagem está
                andando.append(auxPonto) # Adiciono o ponto para ser visitado em seguida
                print("Ponto adicionado para andar: " + auxPonto[0].Localizacao)
            auxLocais.pop(0) # Retiro o primeiro ponto dos q precisam ser visitados
        andando.pop(0) # Retiro o primeiro da fila do andando pois já visitei todos os pontos que podia dele
    i = 1
    print("Tivemos " + str(len(final)) + " finais")
    for item in final:
        print(str(i) + "º final:")
        print("Área: " + str(final[i-1][0].Area))
        print("Vida: " + str(final[i-1][0].Vida))
        print("Locais Visitados: ") 
        print(final[i-1][1])



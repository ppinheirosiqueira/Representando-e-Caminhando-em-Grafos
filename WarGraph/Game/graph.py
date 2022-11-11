from . import game
from . import classes
import copy

def guloso_facil(g,personagem):
    pAux = personagem.copy(g,1)

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
    
    return pAux.Area

def guloso_medio(g,personagem):
    pAux = personagem.copy(g,2)

    return pAux.Area

def guloso_dificil(g, personagem):
    pAux = personagem.copy(g,3)

    return pAux.Area

def BFS(g, personagem,area_obj,dificuldade):
    andando = [] # Vetor que conterá todas as opções de andado e que continuará andando
    final = [] # Sempre que o personagem morrer, será levado para este vetor

    # Precisa atualizar para pegar o grafo todo por onde já foi andado
    # Estrutura auxiliar criada para o BFS, conterá o personagem e por onde andou
    andando.append(classes.BFS_point(personagem,g,dificuldade,g.visitados())) # Andando começa no ponto que o personagem está

    while len(andando) > 0: # Enquanto houver formas de andar
        print("\n")
        print("A lista andando tem tamanho atual de: " + str(len(andando)))
        print("Olhando: " + andando[0].personagem.Localizacao)
        print("Que já andou por: " )
        print(andando[0].lista)
        auxLocais = copy.deepcopy(g.vertices[andando[0].personagem.Localizacao].Vizinhos) # Pego os vizinhos do primeiro ponto do vetor de andar
        print("Falta andar por: ")
        print(auxLocais)
        while len(auxLocais) > 0: # Enquanto houver vizinhos a visitar
            print("Testando: " + auxLocais[0])
            if auxLocais[0] not in andando[0].lista or g.vertices[auxLocais[0]].Base: # Vai para lá se for base ou se não tiver visitado ainda
                auxBFS = classes.BFS_point(andando[0].personagem,g,dificuldade,andando[0].lista)
                distancia = game.distancia(auxBFS.personagem.Localizacao,auxLocais[0],g) # Calcula a distância de onde o personagem está até onde ele vai
                auxBFS.personagem.gastar_sup(distancia) # Personagem anda até lá
                if auxLocais[0] not in auxBFS.lista: # Se o local a ser visitado ainda não foi visitado
                    auxBFS.personagem.apos_luta(g.vertices[auxLocais[0]].Strength) # Desconto a vida do ataque
                if auxBFS.personagem.Vida < 0 : # Caso a vida do personagem seja menor do que zero
                    print("Morreu indo para o destino")
                    auxBFS.lista.append(auxLocais[0])
                    final.append(auxBFS) # Adiciono o personagem e onde ele foi para o vetor final
                    auxLocais.pop(0)
                    continue
                if auxLocais[0] not in auxBFS.lista: # Caso o personagem não tenha visitado o ponto ainda, adiciono o que o ponto me da
                    auxBFS.personagem.conquistando(g.vertices[auxLocais[0]].Area,g.vertices[auxLocais[0]].Medicamentos,g.vertices[auxLocais[0]].Suprimentos)
                auxBFS.lista.append(auxLocais[0]) # Adiciono este ponto aos pontos visitados
                auxBFS.personagem.att_local(auxLocais[0]) # Atualizo onde o personagem está
                andando.append(auxBFS) # Adiciono o ponto para ser visitado em seguida
                print("Ponto adicionado para andar: " + auxBFS.personagem.Localizacao)
            else:
                print("Ponto não adicionado porque já foi visitado")
            auxLocais.pop(0) # Retiro o primeiro ponto dos q precisam ser visitados
        andando.pop(0) # Retiro o primeiro da fila do andando pois já visitei todos os pontos que podia dele
    
    i = 1
    print("\n\nTivemos " + str(len(final)) + " finais")
    
    chance = 0

    for item in final:
        print(str(i) + "º final:")
        print("Área: " + str(item.personagem.Area))
        print("Vida: " + str(item.personagem.Vida))
        print("Locais Visitados: ") 
        print(item.lista)
        print("")
        i+=1
        if item.personagem.Area >= area_obj:
            chance+=1
    
    return 100*chance/len(final)



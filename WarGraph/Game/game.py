import random

def distancia(estou,vou,g):
    return abs(g.vertices[estou].X - g.vertices[vou].X) + abs(g.vertices[estou].Y - g.vertices[vou].Y) # Utilizando distância de Manhattan para não lidar com números quebrados

def descobrir_localizacao(g,p):
    for key in list(g.vertices.keys()):
        if (p.X == g.vertices[key].X and p.Y == g.vertices[key].Y):
            return key
    return "perdido no meio do nada"

def combate(dis,p,v):
    if (dis/100 < random.random()): # Se a distância for pequena demais, a chance de combate é baixa
        return 
    p.apos_luta(v.Strength)

def retornarDificuldade(dificuldade):
    if dificuldade == 1:
        return [150,150]
    elif dificuldade == 2:
        return [100,100]
    else:
        return [50,50]
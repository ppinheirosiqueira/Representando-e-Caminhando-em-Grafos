import random

class Personagem:
    def __init__(self, key, dificuldade):
        self.Localizacao = key
        aux = retornarDificuldade(dificuldade)
        self.Suprimentos = aux[0]
        self.Vida = aux[1]
        self.Area = 0
    
    def att_local(self, key):
        self.Localizacao = key
    
    def att_sup(self,distancia):
        if distancia > self.Suprimentos:
            distancia = distancia - self.Suprimentos
            self.Suprimentos = 0
            self.Vida = self.Vida - distancia
        else:
            self.Suprimentos = self.Suprimentos - distancia

    def att_vida(self,ataque):
        self.Vida = self.Vida - ataque

    def check_vida(self):
        if self.Vida > 0:
            return True
        else:
            return False

    def att_area(self,valor):
        self.Area = self.Area + valor

    def print_personagem(self):
        print("O personagem atualmente está em " + self.Localizacao + ", tem " + str(self.Vida) + " de vida, com suprimentos para andar mais " + str(self.Suprimentos) + " e já conquistou " + str(self.Area))

def distancia(p,nome,g):
    return abs(g.vertices[p.Localizacao].X - g.vertices[nome].X) + abs(g.vertices[p.Localizacao].Y - g.vertices[nome].Y) # Utilizando distância de Manhattan para não lidar com números quebrados

def descobrir_localizacao(g,p):
    for key in list(g.vertices.keys()):
        if (p.X == g.vertices[key].X and p.Y == g.vertices[key].Y):
            return key
    return "perdido no meio do nada"

def combate(dis,p,v):
    if (dis/100 < random.random()): # Se a distância for pequena demais, a chance de combate é baixa
        return 
    p.att_vida(v.Strength)

def retornarDificuldade(dificuldade):
    if dificuldade == 1:
        return [150,150]
    elif dificuldade == 2:
        return [100,100]
    else:
        return [50,50]
from . import graph

class Personagem:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Suprimentos = 100
        self.Vida = 100
        self.area = 0
    
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
    
    def print_personagem(self):
        print("O personagem atualmente está nas coordenadas (" + str(self.X) + "," + str(self.Y) + "), tem " + str(self.Vida) + " de vida, com suprimentos para andar mais " + str(self.Suprimentos) + " e já conquistou " + str(self.area))


def caminhar(xi,xf,yi,yf):
    return abs(xf-xi) + abs(yf-yi) # Utilizando distância de Manhattan para não lidar com números quebrados

def descobrir_localizacao(g,p):
    for key in list(g.vertices.keys()):
        if (p.X == g.vertices[key].X and p.Y == g.vertices[key].Y):
            return key
    return "perdido no meio do nada"
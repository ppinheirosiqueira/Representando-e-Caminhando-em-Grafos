import copy
import random
from . import arquivos

# Como estou imaginando um cenário com bases principais que possuem pontos em volta, apesar das bases serem bem conectadas com esses pontos e entre si, o grafo não será absurdamente denso
# Assim, é melhor utilizar uma lista de adjacentes

class Vertice:
    def __init__(self,nome,x,y,sup,med,forca,base,area):
        self.name = nome
        self.X = int(x)
        self.Y = int(y)
        self.Suprimentos = int(sup)
        self.Medicamentos = int(med)
        self.Strength = int(forca)
        self.Area = int(area)
        self.Base = bool(int(base))
        self.Visitado = False
        self.Vizinhos = list()
    
    def add_vizinho(self,v):
        if v not in self.Vizinhos:
            self.Vizinhos.append(v)
            self.Vizinhos.sort()
    
    def att_sup(self):
        self.Suprimentos = 0
    
    def att_med(self):
        self.Medicamentos = 0
    
    def att_vis(self):
        self.Visitado = True

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertice(self,v):
        if isinstance(v,Vertice) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else:
            return False

    def add_edge(self, v, u):
        self.vertices[v].add_vizinho(u)
        self.vertices[u].add_vizinho(v)

    def copy(self):
        gaux = Graph()
        gaux.vertices = copy.deepcopy(self.vertices)
        return gaux
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print("Cidade: " + key + ", visitado: " + str(self.vertices[key].Visitado))
            print("Vizinhos: ")
            print(self.vertices[key].Vizinhos)

    def randomVertice(self):
        key = random.choice(list(self.vertices))
        return key

    def visitados(self):
        visitados = []
        for key in sorted(list(self.vertices.keys())):
            if self.vertices[key].Visitado:
                visitados.append(key)
        return visitados

    def cidades(self):
        return sorted(list(self.vertices.keys()))
    
    def reset(self):
        for key in sorted(list(self.vertices.keys())):
            del self.vertices[key]
    
        self.vertices = arquivos.colher_dados().vertices

class Personagem:
    def __init__(self, key, g):
        self.Localizacao = key
        self.Suprimentos = 100  + g.vertices[key].Suprimentos
        self.Vida = 100 + g.vertices[key].Medicamentos
        self.Area = 0 + g.vertices[key].Area
        self.Opcoes = 0
        self.Caminho = []
        self.Caminho.append(self.Localizacao)
    
    def att_local(self, key):
        self.Localizacao = key
        self.Caminho.append(self.Localizacao)

    def gastar_sup(self,distancia):
        if distancia > self.Suprimentos:
            distancia = distancia - self.Suprimentos
            self.Suprimentos = 0
            self.Vida = self.Vida - distancia
        else:
            self.Suprimentos = self.Suprimentos - distancia

    def apos_luta(self,ataque):
        self.Vida = self.Vida - ataque

    def check_vida(self):
        if self.Vida > 0:
            return True
        else:
            return False

    def conquistando(self, valorArea, valorMed, valorSup):
        self.Area = self.Area + valorArea
        self.Vida = self.Vida + valorMed
        self.Suprimentos = self.Suprimentos + valorSup

    def print_personagem(self):
        print("O personagem atualmente está em " + self.Localizacao + ", tem " + str(self.Vida) + " de vida, com suprimentos para andar mais " + str(self.Suprimentos) + " e já conquistou " + str(self.Area))

    def copy(self,g):
        p = Personagem(self.Localizacao,g)
        p.Area = self.Area
        p.Vida = self.Vida
        p.Suprimentos = self.Suprimentos
        p.Localizacao = self.Localizacao
        p.Caminho = copy.deepcopy(self.Caminho)

        return p

class BFS_point:
    def __init__(self, personagem, g, lista):
        self.personagem = personagem.copy(g)
        self.lista = copy.deepcopy(lista)
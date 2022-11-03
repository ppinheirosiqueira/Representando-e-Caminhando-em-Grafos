import csv
import copy
import random
from . import game

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
        self.Base = bool(int(base))
        self.Area = int(area)
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
            print(key + ", visitado: " + str(self.vertices[key].Visitado) + ", base: " + str(self.vertices[key].Base))

    def randomVertice(self):
        key = random.choice(list(self.vertices))
        return key
    
    def reset(self):
        for key in sorted(list(self.vertices.keys())):
            del self.vertices[key]
    
        self.vertices = colher_dados().vertices

def colher_dados():
    g = Graph()
    try:
        # Adicionando vértices aos grafo
        with open("Game\\static\\vertices.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                g.add_vertice(Vertice(row["Nome"],row["X"],row["Y"],row["Suprimentos"],row["Medicamentos"],row["Forca"],row["Base"],row["Area"]))
        # Adicionando as areastas em seus vértices
        
        with open("Game\\static\\arestas.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                g.add_edge(row["V"],row["U"])
    except:
        print("\nAlgum arquivo seu deu erro aqui mermão\n")

    return g

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


import csv

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
        self.base = base
        self.area = int(area)
        self.visitado = False
        self.vizinhos = list()
    
    def add_vizinho(self,v):
        if v not in self.vizinhos:
            self.vizinhos.append(v)
            self.vizinhos.sort()
    
    def att_sup(self):
        self.Suprimentos = 0
    
    def att_med(self):
        self.Medicamentos = 0
    
    def att_vis(self):
        self.visitado = True

class Graph:
    vertices = {}

    def add_vertice(self,v):
        if isinstance(v,Vertice) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else:
            return False

    def add_edge(self, v, u):
        self.vertices[v].add_vizinho(u)
        self.vertices[u].add_vizinho(v)

        # Por que não funciona?

        # if u in self.vertices and v in self.vertices:
        #     for key, value in self.vertices.items():
        #         if key == u:
        #             value.add_viziho(v)
        #         if key == v:
        #             value.add_vizinho(u)
        #     #return True
        #else:
        #    return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + " " + str(self.vertices[key].vizinhos))

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
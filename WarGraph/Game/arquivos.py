import csv
from . import classes

def colher_dados():
    g = classes.Graph()
    try:
        # Adicionando vértices aos grafo
        with open("Game\\static\\arquivos\\vertices.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                g.add_vertice(classes.Vertice(row["Nome"],row["X"],row["Y"],row["Suprimentos"],row["Medicamentos"],row["Forca"],row["Area"]))
    except:
        print("\nErro ao Adicionar Vértices\n")
    
    try:
        # Adicionando as areastas em seus vértices
        with open("Game\\static\\arquivos\\arestas.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                g.add_edge(row["V"],row["U"])
    except:        
        print("\nErro ao Adicionar Arestas\n")

    return g
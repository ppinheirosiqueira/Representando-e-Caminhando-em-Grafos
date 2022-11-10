import csv
from . import classes

def colher_dados():
    g = classes.Graph()
    try:
        # Adicionando vértices aos grafo
        with open("Game\\static\\vertices.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                g.add_vertice(classes.Vertice(row["Nome"],row["X"],row["Y"],row["Suprimentos"],row["Medicamentos"],row["Forca"],row["Base"],row["Area"]))
        # Adicionando as areastas em seus vértices
        
        with open("Game\\static\\arestas.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                g.add_edge(row["V"],row["U"])
    except:
        print("\nAlgum arquivo seu deu erro aqui mermão\n")

    return g
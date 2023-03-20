import graph
import util
import math

# Input Vertices
n_vertex = int(input())
vertices = []

G = graph.Graph(n_vertex)

for i in range(n_vertex):
  vertices.append([int(x) for x in input().split(",")])

# Input and form edges
n_edges = int(input())

for i in range(n_edges):
    p, q = input().split(":")
    p = [int(x) for x in p.split(",")]
    q = [int(x) for x in q.split(",")]

    G.add_edge(vertices.index(p),vertices.index(q),math.dist(p,q))

# Determines Center of the Graph
grafo = G.get_matrix()

distance_matrix = graph.floydWarshall(grafo, n_vertex)

ecct = graph.eccentricity(distance_matrix)

center = vertices[ecct.index(min(ecct))]


# Determines the most peripheral vertex
peripheral = vertices[ecct.index(max(ecct))]

# Determines the farthest vertex from the most peripheral vertex
aux_list = []
for i in range(n_vertex):
    aux_list.append(distance_matrix[i][vertices.index(peripheral)])

farthest = vertices[aux_list.index(max(aux_list))]

# Outputs:
util.coord(center)
util.coord(peripheral)
util.coord(farthest)

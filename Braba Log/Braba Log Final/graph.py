import util

INF = util.infinite()

class Graph:

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([INF for i in range(size)])
            self.adjMatrix[i][i] = 0
        self.size = size

    # Add edges
    def add_edge(self, v1, v2,weight):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = weight

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print()

    def get_matrix(self):
      return self.adjMatrix

      
# Solves all pair shortest path
# via Floyd Warshall Algorithm
def floydWarshall(graph,vertices):
  dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
  
  for k in range(vertices):
    # Pick all vertices as source one by one
    for i in range(vertices):
      # Pick all vertices as destination for the above picked source
      for j in range(vertices):
        # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
        dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
  
  return dist


# Calculates each eccentricity and creates a list with them
def eccentricity(distance_matrix):
  n_vertex = len(distance_matrix)
  ecct = [INF for i in range(n_vertex)]

  for i in range(n_vertex):
      aux_list= []
      for j in range(n_vertex):
          aux_list.append(distance_matrix[j][i])
      ecct[i] = max(aux_list)

  return ecct


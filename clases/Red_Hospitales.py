import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Red_Hospitales:
  def __init__(self):
    self.hospitales = []
    self.distancias = {}
    self.grafo = nx.Graph()

  def agregar_hospital(self, hospital):
    self.hospitales.append(hospital)

  def agregar_distancia(self, Hospital_origen, Hospital_destino, distancia):
    if Hospital_origen in self.hospitales and Hospital_destino in self.hospitales:
      tupla = (Hospital_origen, Hospital_destino)
      self.distancias[tupla] = distancia
      self.creargrafo()
    else:
      print("Uno o ambos hospitales no existen en la red.")

  def creargrafo(self):
    self.grafo.add_nodes_from(self.hospitales)
    for (h1, h2), distancia in self.distancias.items():
      self.grafo.add_edge(h1, h2, weight=distancia)
    

  def imprimirgrafo(self):
    pos = nx.spring_layout(self.grafo, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(self.grafo, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
    # Dibujar las etiquetas de peso (distancia)
    labels = nx.get_edge_attributes(self.grafo, 'weight')
    nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels, font_size=10)
    plt.title("Red de Hospitales Representada como Grafo Ponderado", fontsize=14)
    plt.show()

  def dfs(self, inicio):
        visitados = set()  # Conjunto para almacenar los nodos visitados
        pila = [inicio]    # Pila para el recorrido DFS
        recorrido = []     # Lista para almacenar el orden de los nodos visitados
        while pila:
            nodo = pila.pop()  # Extraer el nodo del tope de la pila
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                # Agregar vecinos no visitados a la pila en orden inverso para simular profundidad
                vecinos = sorted(self.grafo.neighbors(nodo), reverse=False)
                pila.extend(vecino for vecino in vecinos if vecino not in visitados)
        return recorrido

  def bfs(self, inicio):
      visitados = set([inicio])
      cola = [inicio]
      recorrido = []
      while cola:
          nodo = cola.pop(0)
          recorrido.append(nodo)
          for vecino in sorted(self.grafo.neighbors(nodo)):
              if vecino not in visitados:
                  visitados.add(vecino)
                  cola.append(vecino)
      return recorrido

  def dijkstra(self, inicio, destino):
      cola_prioridad = [(0, inicio)]  # (distancia acumulada, nodo)
      distancias = {nodo: float('inf') for nodo in self.grafo.nodes}
      distancias[inicio] = 0
      while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == destino:
                print(f"Distancia mínima desde {inicio} hasta {destino}: {distancia_actual}")
                return distancia_actual  # Retorna la distancia si llega al destino

            for vecino in self.grafo.neighbors(nodo_actual):
                peso = self.grafo[nodo_actual][vecino]['weight']
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        # Si no se puede llegar al destino, retornar None
      return None
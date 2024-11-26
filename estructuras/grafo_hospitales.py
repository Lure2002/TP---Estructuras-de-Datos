# estructuras/grafo_hospitales.py
class GrafoHospitales:
    def __init__(self):
        self.grafo = {}

    def agregar_hospital(self, hospital):
        if hospital not in self.grafo:
            self.grafo[hospital] = {}

    def agregar_conexion(self, hospital1, hospital2, distancia):
        if hospital1 in self.grafo and hospital2 in self.grafo:
            self.grafo[hospital1][hospital2] = distancia
            self.grafo[hospital2][hospital1] = distancia

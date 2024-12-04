class Heap:
    def __init__(self):
        self.vector = []  # Lista vacía que crecerá dinámicamente

    def insertar(self, palabra):
        """Inserta una nueva palabra en el heap."""
        self.vector.append(palabra)  # Añade la palabra al final
        self.heapify_up(len(self.vector)-1)  # Reorganiza el heap desde el nuevo elemento

    def eliminarpaciente(self,id):
        for i in range(len(self.vector)):
          if self.vector[i][1].retornarid() == id:
            self.vector.pop(i)
            return None

    def extraer_min(self):
        """Extrae la palabra mínima del heap (raíz) y reorganiza el heap."""
        if len(self.vector) == 0:
            raise Exception("El heap está vacío.")

        minimo = self.vector[0]  # El mínimo está en la raíz (índice 0)
        ultimo = self.vector.pop()  # Elimina el último elemento
        return minimo

    def heapify_up(self, indice):
        """Reorganiza el heap desde el nodo actual hacia arriba para mantener la propiedad del heap."""
        while indice > 0:
            indice_padre = (indice-1 )  # Índice del padre
            if self.vector[indice][0] < self.vector[indice_padre][0]:  # Comparación alfabética
                # Intercambia el elemento actual con su padre
                self.vector[indice], self.vector[indice_padre] = (
                    self.vector[indice_padre],
                    self.vector[indice],
                )
                indice = indice_padre  # Actualiza el índice al del padre
            else:
                break

    def mostrar_heap(self):
        for gravedad, paciente in self.vector:
            print(f"Gravedad: {gravedad}, Paciente: {paciente.retornarid()}")
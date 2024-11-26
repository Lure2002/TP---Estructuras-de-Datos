# estructuras/arbol_pacientes.py
class NodoPaciente:
    def __init__(self, paciente):
        self.paciente = paciente
        self.izquierda = None
        self.derecha = None

class ArbolPacientes:
    def __init__(self):
        self.raiz = None

    def insertar(self, paciente):
        if self.raiz is None:
            self.raiz = NodoPaciente(paciente)
        else:
            self._insertar_recursivo(self.raiz, paciente)

    def _insertar_recursivo(self, nodo, paciente):
        if paciente.id_paciente < nodo.paciente.id_paciente:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPaciente(paciente)
            else:
                self._insertar_recursivo(nodo.izquierda, paciente)
        elif paciente.id_paciente > nodo.paciente.id_paciente:
            if nodo.derecha is None:
                nodo.derecha = NodoPaciente(paciente)
            else:
                self._insertar_recursivo(nodo.derecha, paciente)

    def buscar(self, id_paciente):
        return self._buscar_recursivo(self.raiz, id_paciente)

    def _buscar_recursivo(self, nodo, id_paciente):
        if nodo is None:
            return None
        if id_paciente == nodo.paciente.id_paciente:
            return nodo.paciente
        elif id_paciente < nodo.paciente.id_paciente:
            return self._buscar_recursivo(nodo.izquierda, id_paciente)
        else:
            return self._buscar_recursivo(nodo.derecha, id_paciente)

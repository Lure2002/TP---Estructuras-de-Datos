import paciente
import NodoArbolBinario

class Hospital:
    def __init__(self):
        self.pacientes = {}
        self.arbolbi = None

    def agregarpaciente(self, id_paciente, nombre, edad, sexo,historial_enfermedades=None, medicamentos=None):
        num = paciente(id_paciente, nombre, edad, sexo,historial_enfermedades, medicamentos)
        self.pacientes[id_paciente] = num
        self.arbol(id_paciente)
        return None

    def arbol(self,id_paciente):
        if self.arbolbi is None:
              self.arbolbi = NodoArbolBinario(self.pacientes[id_paciente] )
        else:
            lista = list(self.pacientes.keys())
            lista.sort()
            if len(lista) < 4:
              med = len(lista)//2
              self.arbolbi = NodoArbolBinario(self.pacientes[lista[med]] )
              self.recursionarbol(lista)
            else:
              med = len(lista)//2
              self.arbolbi = NodoArbolBinario(self.pacientes[lista[med]] )
              listder = lista[med+1: ]
              listizq = lista[:(med)]
              if len(listder) > 1:
                medder = len(listder)//2
                self.arbolbi.anadir(self.pacientes[listder[medder]] )
                self.recursionarbol(listder)
              else:
                self.recursionarbol(listder)
              if len(listizq) > 1:
                medizq = len(listizq)//2
                self.arbolbi.anadir(self.pacientes[listizq[medizq]] )
                self.recursionarbol(listizq)
              else:
                  self.recursionarbol(listizq)

    def recursionarbol(self,lista):
        if len(lista) == 0:
          return None
        elif len(lista) == 1:
          self.arbolbi.anadir(self.pacientes[lista[0]] )
          return None
        elif len(lista) == 2:
          self.arbolbi.anadir(self.pacientes[lista[0]] )
          return None
        elif len(lista) == 3:
          self.arbolbi.anadir(self.pacientes[lista[2]] )
          self.arbolbi.anadir(self.pacientes[lista[0]] )
        else:
          medio = len(lista)//2
          listder = lista[medio+1: ]
          listizq = lista[:(medio)]
          medizq = len(listizq)//2
          medder = len(listder)//2
          self.arbolbi.anadir(self.pacientes[listder[medder]] )
          self.recursionarbol(listder)
          self.arbolbi.anadir(self.pacientes[listizq[medizq]] )
          self.recursionarbol(listizq)
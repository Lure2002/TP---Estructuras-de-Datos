from clases.paciente  import Paciente
from clases.NodoArbolBinario import NodoArbolBinario
from clases.Heap import Heap
from datetime import date
class Hospital:
    def __init__(self):
        self.pacientes = {}
        self.arbolbi = None
        self.pacienteguardia = Heap()

    def agregarpaciente(self, id_paciente, nombre, fechanac, sexo,historial_enfermedades=None, medicamentos=None):
        if self.buscarpaciente(id_paciente) is not None:
            return "El paciente ya existe."
        else:
          num = Paciente(id_paciente, nombre, fechanac, sexo,historial_enfermedades, medicamentos)
          self.pacientes[id_paciente] = num
          self.arbol()
          return "El paciente se agrego con exito"

    def removerpaciente(self,id_paciente):
          if self.buscarpaciente(id_paciente) is not None:
              del self.pacientes[id_paciente]
              self.arbol()
              return None
          else:
              return "El paciente no existe."

    def buscarpaciente(self,id_paciente):
      if self.arbolbi is None:
        return None
      else:
        return self.arbolbi.busqueda(id_paciente)

    def agregarpacienteguardia(self,id_paciente, nombre, fechanac , sexo,historial_enfermedades=None, medicamentos=None,gravedad = None):
      #gravedad esta condicionada por grave = 2,moderado= 1,no_urgente = 0
        if gravedad  == "grave":
          gravedad =2
        elif gravedad == "moderado":
          gravedad = 1
        else:
          gravedad = 0
        existe = self.buscarpaciente(id_paciente)
        if existe is  None:
          num = Paciente(id_paciente, nombre, fechanac , sexo,historial_enfermedades, medicamentos)
          self.pacientes[id_paciente] = num
          self.arbol()
          tupla = (gravedad,num)
          self.pacienteguardia.insertar(tupla)
        else:
          pac = existe
          tupla = (gravedad,pac)
          self.pacienteguardia.insertar(tupla)

    def eliminarpacienteguardiaatendido(self):
          self.pacienteguardia.extraer_min()
          return "El paciente se fue atendido"

    def eliminarpacienteguardia(self,id_paciente):
          self.pacienteguardia.eliminarpaciente(id_paciente)
          return "El paciente se fue"

    def modificardatos(self,id_paciente,opcion,valor):
        if self.buscarpaciente(id_paciente) is not None:
            if opcion == "nombre":
                self.pacientes[id_paciente].modificar_nombre(valor)
            elif opcion == "sexo":
                self.pacientes[id_paciente].modificar_sexo(valor)
            else:
                return "Opcion no valida"
        else:
            return "El paciente no existe."

    def agregardatos(self,id_paciente,opcion,valor):
        if self.buscarpaciente(id_paciente) is not None:
            if opcion == "enfermedad":
                self.pacientes[id_paciente].agregar_enfermedad(valor)
            elif opcion == "medicamento":
                self.pacientes[id_paciente].agregar_medicamento(valor)
            else:
                return "Opcion no valida"
        else:
            return "El paciente no existe."

    def eliminar_enfermedad(self,id_paciente,enfermedad):
        if self.buscarpaciente(id_paciente) is not None:
            self.pacientes[id_paciente].eliminar_enfermedad(enfermedad)
        else:
            return "El paciente no existe."

    def eliminar_medicamento(self,id_paciente,medicamento):
        if self.buscarpaciente(id_paciente) is not None:
            self.pacientes[id_paciente].eliminar_medicamento(medicamento)
        else:
            return "El paciente no existe."
    def agregar_consulta(self,id_paciente,consulta,diagnostico,tratamiento,medicamentos=None):
        if self.buscarpaciente(id_paciente) is not None:
            self.pacientes[id_paciente].agregarcosulta(consulta, diagnostico, tratamiento,medicamentos)
        else:
            return "El paciente no existe."

    def mostrarpaciente(self,id_paciente):
      pac = self.buscarpaciente(id_paciente)
      if pac is not None:
        return print(pac)
      else:
        return "El paciente no existe."
      
    def mostrarguardia(self):
      return self.pacienteguardia.mostrar_heap()

    def imprimirarbolbi(self):
        return self.arbolbi.imprimir_arbol_con_señalamiento()

    def mostrar_historial_paciente(self,id_paciente):
        if self.buscarpaciente(id_paciente) is not None:
            self.pacientes[id_paciente].imprimir_historial_paciente()
        else:
            return "El paciente no existe."

    def arbol(self):
        if self.arbolbi is None:
            lista = list(self.pacientes.keys())
            self.arbolbi = NodoArbolBinario(self.pacientes[lista[0]] )
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
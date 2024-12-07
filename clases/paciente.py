from datetime import date
from clases.ArbolGeneral import Arbol_General, agregar_hijo_nodo, arbol_vacio, agregar_nodo, imprimir_consultas_recursivo
class Paciente:
    def __init__(self, id_paciente, nombre, fechadenacimiento, sexo,historial_enfermedades=None, medicamentos=None):
        self.id_paciente = int(id_paciente)
        self.nombre = str(nombre)
        self.edad =  (date.today() - fechadenacimiento).days
        self.sexo = str(sexo)
        self.historial_enfermedades = historial_enfermedades or []
        self.medicamentos = medicamentos or []
        self.consultas = Arbol_General(id_paciente)

    def agregarcosulta (self,consulta,diagnostico,tratamiento,medicamentos=None):#medicamento es lista el resto str
              trar = {}
              trar["consulta"] = consulta
              trar["diagnostico"]= diagnostico
              trar["tratamiento"]= tratamiento
              trar["medicamento"] = medicamentos or []
              if self.buscardiagnostico(diagnostico) is True:
                tupla = (date.today(),trar)
                agregar_hijo_nodo(self.consultas,diagnostico,tupla)
              else:
                agregar_nodo(self.consultas,diagnostico)
                tupla = (date.today(),trar)
                agregar_hijo_nodo(self.consultas,diagnostico,tupla)
    def hijoarbol(self):
        return self.consultas.retornarhijos()
    def retornarid(self):
        return self.id_paciente
    def retornadedad(self):
        if self.edad < 365:
          dias = self.edad % 365
          return print("el paciente tiene: ",dias,"dias")
        else:
          anos = self.edad//365
          return print("el paciente tiene: ",anos,"años de edad")

    def modificar_sexo(self, sexo):
        self.sexo =sexo

    def modificar_nombre(self, nombre):
        self.nombre = nombre

    def agregar_enfermedad(self, enfermedad):
        if enfermedad in self.historial_enfermedades:
            return "la enfermedad ya se encuentra"
        else:
          self.historial_enfermedades.append(enfermedad)
          return "se añadio con exito"

    def agregar_medicamento(self, medicamento):
        if medicamento in self.medicamentos:
            return "el medicamento ya se encuentra"
        else:
            self.medicamentos.append(medicamento)
            return "se añadio con exito"

    def eliminar_enfermedad(self, enfermedad):
        if enfermedad in self.historial_enfermedades:
            self.historial_enfermedades.remove(enfermedad)
            return "se añadio con exito"
        else:
          return "la enfermedad no se encuentra"

    def eliminar_medicamento(self, medicamento):
        if medicamento in self.medicamentos:
            self.historial_enfermedades.remove(medicamento)
            return "se añadio con exito"
        else:
          return "el medicamento no se encuentra"

    def imprimir_historial_paciente(self):
        print(f"Historial del paciente {self.nombre}:")
        print(f"antecedentes de enfermedades", self.historial_enfermedades)
        print(f"medicamentos que toma el paciente", self.medicamentos)
        print(f"historial de consultas")
        imprimir_consultas_recursivo(self.consultas)

      
    def buscardiagnostico(self,diagnostico,nodo = None,rep = None ):
        if diagnostico in self.historial_enfermedades:
          return True
        else:
          #print(rep)
          if rep is None:
                nodo = self.hijoarbol()
                if nodo is None:
                  return False
                else:
                  if nodo.info == diagnostico:
                    return True
                  else:
                    #print("primer iteracion",nodo.info)
                    rep = 1
                    nodo = nodo.sig
                    return self.buscardiagnostico(diagnostico, nodo,rep)
          else:
            if nodo is None:
                return False
            else:
              if nodo.info == diagnostico:
                return True
              else:
                #print("segunda iteracion",nodo.info)
                nodo = nodo.sig
                rep += 1
                return self.buscardiagnostico(diagnostico, nodo,rep)

    def buscartratamiento(self,medicamento,nodo = None,rep = None):
        if medicamento in self.medicamentos:
          return True
        else: 
          if rep is None:
                nodo = self.hijoarbol()
                if nodo is None:
                  return False
                else:
                  consulta = nodo.hijos
                  while consulta is not None:
                      if medicamento in consulta.info[1]["medicamento"]:
                          return True
                      consulta = consulta.sig
                  rep = 1
                  nodo = nodo.sig
                  return self.buscartratamiento(medicamento, nodo,rep)
          else:
                if nodo is None:
                    return False
                else:
                  consulta = nodo.hijos
                  while consulta is not None:
                      if medicamento in consulta.info[1]["medicamento"]:
                          return True
                      consulta = consulta.sig
                  nodo = nodo.sig
                  rep += 1
                  return self.buscartratamiento(medicamento, nodo)


    def __str__(self):
        return print(f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.edad}, Enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}")
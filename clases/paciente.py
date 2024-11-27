from enum import Enum
from datetime import date
from estructuras.busqueda_recursiva import buscar_en_historial
from medicamentos import Medicamento

class Sexo(Enum):
    Masculino:0
    Femenino:1

class Paciente:
    def __init__(self, id_paciente:int, nombre:str, fecha_de_nacimiento:date, sexo:Sexo, dni:int, historial=None, medicamentos=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.dni = dni
        self.historial = historial or []
        self.medicamentos = medicamentos or []

        def agregar_consulta(self,fecha,consulta,diagnostico,tratamiento):
            for element in self.historial_enfermedades:
                if element == diagnostico:
                    diagnosticostr = str(diagnostico) 
                    diagnosticostr ={}
                    diagnosticostr["fecha"] = str(fecha)
                    diagnosticostr["consulta"] = consulta
                    diagnosticostr["diagnostico"]= diagnostico
                    diagnosticostr["tratamiento"]= tratamiento
                    diagnosticostr["historial"] = True
                    self.consultas[str(diagnostico)] = diagnosticostr
                    return
                
            if self.buscardiagnostico(diagnostico):
                antf = [self.consultas[str(diagnostico)]["fecha"]] + [str(fecha)]
                antc = [self.consultas[str(diagnostico)]["consulta"]] + [str(consulta)]
                antt = [self.consultas[str(diagnostico)]["tratamiento"]] + [str(tratamiento)]
                self.consultas[str(diagnostico)]["historial"] = True
                self.consultas[str(diagnostico)]["fecha"] = antf
                self.consultas[str(diagnostico)]["consulta"] = antc
                self.consultas[str(diagnostico)]["tratamiento"] = antt
            
            else:
                diagnosticostr = str(diagnostico) 
                diagnosticostr ={}
                diagnosticostr["fecha"]= fecha
                diagnosticostr["consulta"]= consulta
                diagnosticostr["diagnostico"]= diagnostico
                diagnosticostr["tratamiento"]= tratamiento
                diagnosticostr["historial"] = False
                self.consultas[str(diagnostico)] = diagnosticostr

    def retornarid(self):
        return self.id_paciente

    def agregar_enfermedad(self, enfermedad):
        self.historial_enfermedades.append(enfermedad)

    def modificar_sexo(self, sexo):
        self.sexo =sexo

    def modificar_nombre(self, nombre):
        self.nombre = nombre
    
    def modificar_edad(self, edad):
        self.edad = edad

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def eliminar_enfermedad(self, enfermedad):
        if enfermedad in self.historial_enfermedades:
            self.historial_enfermedades.remove(enfermedad)

    def buscardiagnostico(self,diagonostico,index = 0):
        listakeys = []
        listakeys += self.historial_enfermedades
        listakeys += list(self.consultas.keys())
        if index >= len(listakeys):
            return False
        elif listakeys[index] == diagonostico:
            return True
        else:
            return self.buscardiagnostico(diagonostico,index + 1)

    def buscartratamiento(self,tratamiento,index = 0):
        listavalues = []
        listavalues += self.medicamentos
        stop = len(listavalues)
        listavalues += list(self.consultas.values())
        if index >= len(listavalues):
            return False
        else:
            if index < stop:
                if listavalues[index] == tratamiento:
                    return True
                else:
                    return self.buscartratamiento(tratamiento,index + 1)
            else:
                if listavalues[index]["historial"]:
                    listratam = listavalues[index]["tratamiento"]
                    for element in listratam:
                        if element == tratamiento:
                            return True
                    return self.buscartratamiento(tratamiento,index + 1)
                else:
                    if listavalues[index]["tratamiento"] == tratamiento:
                        return True
                    else:
                        return self.buscartratamiento(tratamiento,index + 1) 
                
    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.edad}, Enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}"
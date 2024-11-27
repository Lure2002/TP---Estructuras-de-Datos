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

    def modificar_sexo(self, sexo: Sexo):
        self.sexo =sexo

    def modificar_nombre(self, nombre: str):
        self.nombre = nombre

    def agregar_medicamento(self, medicamento:str):
        self.medicamentos.append(medicamento)
    
    def agregar_enfermedad(self, enfermedad:str):
        self.historial_enfermedades.append(enfermedad)
    
    def agregar_consulta(self,fecha:date,tema:str,diagnostico:str,tratamiento:str, medicamentos:list[Medicamento]):
        diagnosticostr = str(diagnostico) 
        diagnosticostr ={}
        diagnosticostr["fecha"]= fecha
        diagnosticostr["tema"]= tema
        diagnosticostr["diagnostico"]= diagnostico
        diagnosticostr["tratamiento"]= tratamiento
        self.consultas[str(diagnostico)] = diagnosticostr
    
    def buscar(self, keyword):
        buscar_en_historial(self,keyword)
    
    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.edad}, Enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}"
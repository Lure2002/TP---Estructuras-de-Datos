from enum import Enum
from datetime import date
from estructuras import busqueda_recursiva

class Sexo(Enum):
    Masculino:0
    Femenino:1

class Medicamento:
    def __init__(self, nombre:str, laboratorio:str, comprimidos:int):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.comprimidos = comprimidos
        
    def __str__(self):
        return f"{self.nombre} ({self.laboratorio}, {self.comprimidos} comprimidos)"

class Historia:
    def __init__(self, fecha:date=date.ctime(), tema:str="", diagnostico:str="", tratamiento:str="", medicamentos:list[Medicamento] = []):
        self.fecha = fecha
        self.tema = tema
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.medicamentos = medicamentos
        
    def __str__(self):
        return f"[{self.fecha}] Tema: {self.tema}, Diagnóstico: {self.diagnostico}, Tratamiento: {self.tratamiento}"

class Paciente:
    def __init__(self, id_paciente:int, nombre:str, edad:int, sexo:Sexo,historial=None, medicamentos=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.historial = historial or []
        self.medicamentos = medicamentos or []

    def agregar_consulta(self,fecha:date,consulta:str,diagnostico:str,tratamiento:str):
        diagnosticostr = str(diagnostico) 
        diagnosticostr ={}
        diagnosticostr["fecha"]= fecha
        diagnosticostr["consulta"]= consulta
        diagnosticostr["diagnostico"]= diagnostico
        diagnosticostr["tratamiento"]= tratamiento
        self.consultas[str(diagnostico)] = diagnosticostr

    def agregar_enfermedad(self, enfermedad:str):
        self.historial_enfermedades.append(enfermedad)

    def modificar_sexo(self, sexo: Sexo):
        self.sexo =sexo

    def modificar_nombre(self, nombre: str):
        self.nombre = nombre
    
    def modificar_edad(self, edad:int):
        self.edad = edad

    def agregar_medicamento(self, medicamento:str):
        self.medicamentos.append(medicamento)
    
    def buscar(self, keyword):
        busqueda_recursiva.buscar_en_historial(self,keyword)
    
    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.edad}, Enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}"
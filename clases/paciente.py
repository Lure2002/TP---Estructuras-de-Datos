from enum import Enum
from datetime import date
from estructuras.busqueda_recursiva import buscar_en_historial
from medicamentos import Medicamento
from historia import Historia

class Sexo(Enum):
    Masculino = 0
    Femenino = 1

class Paciente:
    def __init__(self, id_paciente: int, nombre: str, fecha_de_nacimiento: date, sexo: Sexo, dni: int, historial: list[Historia] = None, medicamentos: list[Medicamento] = None, prioridad: int = 0):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.dni = dni
        self.historial = historial if historial else []
        self.medicamentos = medicamentos if medicamentos else []

    def id(self):
        return self.id_paciente

    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_de_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_de_nacimiento.month, self.fecha_de_nacimiento.day))

    def modificar_nombre(self, nombre: str):
        self.nombre = nombre

    def modificar_fecha_de_nacimiento(self, nueva_fecha: date):
        self.fecha_de_nacimiento = nueva_fecha

    def modificar_sexo(self, sexo: Sexo):
        self.sexo = sexo

    def agregar_historia(self, historia: Historia):
        self.historial.append(historia)

    def buscar(self, keyword: str):
        return buscar_en_historial(self, keyword)

    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.calcular_edad()}, Medicamentos: {self.medicamentos}, Historias: {len(self.historial)}"

from datetime import date

class Doctor:
    def __init__(self, nombres:str, apellido:str, fecha_de_nacimiento:date, dni:int, area:str, matricula:int, residente:bool):
        self.nombres = nombres
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.area = area
        self.matricula = matricula
        self.residente = residente
        
    def __str__(self):
        return f"{self.nombres} {self.apellido} - {self.area} - Matricula: {self.matricula}"
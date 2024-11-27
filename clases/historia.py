from datetime import date
from medicamentos import Medicamento
from doctor import Doctor

class Historia:
    def __init__(self, doctor:Doctor, tema:str, diagnostico:str, tratamiento:str, fecha:date=date.ctime(), medicamentos:list[Medicamento] = []):
        self.doctor = doctor
        self.tema = tema
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.fecha = fecha
        self.medicamentos = medicamentos
        
    def __str__(self):
        medicamentos_str = "\n".join(str(medicamento) for medicamento in self.medicamentos)
        return f"""[{self.fecha}]
    Doctor: {self.doctor} 
    Tema: {self.tema} 
    Diagnóstico: {self.diagnostico} 
    Tratamiento: {self.tratamiento}
    Medicamentos: {medicamentos_str}"""
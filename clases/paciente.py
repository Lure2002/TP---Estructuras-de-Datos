class Paciente:
    def __init__(self, id_paciente, nombre, edad, historial_enfermedades=None, medicamentos=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.historial_enfermedades = historial_enfermedades or []
        self.medicamentos = medicamentos or []

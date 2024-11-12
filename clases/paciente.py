class Paciente:
    def __init__(self, id_paciente, nombre, edad, historial_enfermedades=None, medicamentos=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.historial_enfermedades = historial_enfermedades or []
        self.medicamentos = medicamentos or []

    def agregar_enfermedad(self, enfermedad):
        self.historial_enfermedades.append(enfermedad)

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def eliminar_enfermedad(self, enfermedad):
        if enfermedad in self.historial_enfermedades:
            self.historial_enfermedades.remove(enfermedad)

    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.edad}, Enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}"
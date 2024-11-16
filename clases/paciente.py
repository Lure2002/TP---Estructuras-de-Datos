class Paciente:
    def __init__(self, id_paciente, nombre, edad, sexo,historial_enfermedades=None, medicamentos=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.historial_enfermedades = historial_enfermedades or []
        self.medicamentos = medicamentos or []
        self.consultas = {}

    def agregar_consulta(self,fecha,consulta,diagnostico,tratamiento):
        diagnosticostr = str(diagnostico) 
        diagnosticostr ={}
        diagnosticostr["fecha"]= fecha
        diagnosticostr["consulta"]= consulta
        diagnosticostr["diagnostico"]= diagnostico
        diagnosticostr["tratamiento"]= tratamiento
        self.consultas[str(diagnostico)] = diagnosticostr

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

    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre}, Edad: {self.edad}, Enfermedades: {self.historial_enfermedades}, Medicamentos: {self.medicamentos}"
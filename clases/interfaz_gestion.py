from clases.paciente import Paciente

class GestionPacientes:
    def __init__(self):
        self.pacientes:list[Paciente] = {}

    def agregar_paciente(self, paciente:Paciente):
        if paciente.id_paciente in self.pacientes:
            raise ValueError("El paciente ya existe.")
        self.pacientes[paciente.id_paciente] = paciente

    def eliminar_paciente(self, id_paciente:int):
        if id_paciente in self.pacientes:
            del self.pacientes[id_paciente]
        else:
            raise ValueError("El paciente no existe.")

    def modificar_paciente(self, id_paciente:int, **kwargs):
        paciente:Paciente = self.pacientes.get(id_paciente)
        if not paciente:
            raise ValueError("El paciente no existe.")
        for key, value in kwargs.items():
            if hasattr(paciente, key):
                setattr(paciente, key, value)

    def buscar_paciente(self, id_paciente:int):
        return self.pacientes.get(id_paciente, None)

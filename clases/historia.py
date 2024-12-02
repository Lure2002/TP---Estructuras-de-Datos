from datetime import date
from medicamentos import Medicamento
from doctor import Doctor
from hospital import Hospital
from enum import Enum

class TipoEvento(Enum):
    Consulta=0
    diagnóstico=1
    Tratamiento=2

class Historia:
    def __init__(self, doctor:Doctor, establecimiento:Hospital, tema:str, tipo_historia:TipoEvento, diagnostico:str, tratamiento:str, fecha:date=date.ctime(), medicamentos:list[Medicamento] = []):
        self.doctor = doctor
        self.establecimiento = establecimiento
        self.tema = tema
        self.tipo_historia = tipo_historia
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.fecha = fecha
        self.medicamentos = medicamentos
        
    def __str__(self):
        medicamentos_str = "\n".join(str(medicamento) for medicamento in self.medicamentos)
        return f"""[{self.fecha}]
    Doctor: {self.doctor} 
    Establecimiento: {self.establecimiento}
    Tema: {self.tema} 
    Diagnóstico: {self.diagnostico} 
    Tratamiento: {self.tratamiento}
    Medicamentos: {medicamentos_str}"""
    
    
# from enum import Enum
# from datetime import date
# from estructuras.busqueda_recursiva import buscar_en_historial
# from medicamentos import Medicamento
# from doctor import Doctor
# from hospital import Hospital

# class TipoEvento(Enum):
#     Consulta = 0
#     Diagnóstico = 1
#     Tratamiento = 2

# class NodoHistoria:
#     def __init__(self, evento: TipoEvento, descripcion: str, fecha: date, doctor: Doctor, hospital: Hospital):
#         self.evento = evento
#         self.descripcion = descripcion
#         self.fecha = fecha
#         self.doctor = doctor
#         self.establecimiento = hospital
#         self.hijos = []  # Lista de nodos hijos (eventos subsecuentes)

#     def agregar_hijo(self, nodo_hijo):
#         """Agrega un evento relacionado como hijo del nodo actual."""
#         self.hijos.append(nodo_hijo)

#     def __str__(self):
#         return f"{self.evento.name}: {self.descripcion} ({self.fecha}) - Dr. {self.doctor.apellido} {self.doctor.nombres}"

# class ArbolHistorial:
#     def __init__(self):
#         self.raiz:NodoHistoria = None 

#     def agregar_evento(self, nodo_padre: NodoHistoria, nodo_hijo: NodoHistoria):
#         if nodo_padre is None:
#             if self.raiz is None:
#                 self.raiz = nodo_hijo  # Si no hay raíz, el nuevo evento se convierte en la raíz
#             else:
#                 raise ValueError("Debe especificar un nodo padre para agregar un hijo.")
#         else:
#             nodo_padre.agregar_hijo(nodo_hijo)

#     def buscar_evento(self, keyword: str):
#         """Busca eventos en el árbol por palabras clave."""
#         return self._buscar_recursivo(self.raiz, keyword)

#     def _buscar_recursivo(self, nodo: NodoHistoria, keyword: str):
#         """Búsqueda recursiva de un evento en el árbol."""
#         if nodo is None:
#             return None
#         resultados = []
#         if keyword.lower() in nodo.descripcion.lower():
#             resultados.append(nodo)
#         for hijo in nodo.hijos:
#             resultados.extend(self._buscar_recursivo(hijo, keyword))
#         return resultados
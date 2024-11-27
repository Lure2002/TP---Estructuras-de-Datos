class Medicamento:
    def __init__(self, nombre:str, laboratorio:str, comprimidos:int):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.comprimidos = comprimidos
        
    def __str__(self):
        return f"{self.nombre} ({self.laboratorio}, {self.comprimidos} comprimidos)"
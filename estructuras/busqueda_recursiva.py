from clases.paciente import Historia

def buscar_en_historial(historial:list[Historia], keyword:str, index:int=0):
    if index >= len(historial):  # Caso base: fin de la lista
        return False

    historia = historial[index]

    # Buscar en el tema
    if keyword.lower() in historia.tema.lower():
        return historial[index]

    # Buscar en el tema
    if keyword.lower() in historia.tratamiento.lower():
        return historial[index]
    
    # Buscar en medicamentos
    for medicamento in historia.medicamentos:
        if keyword.lower() in medicamento.nombre.lower():
            return historial[index]

    # Llamada recursiva al siguiente elemento del historial
    return buscar_en_historial(historial, keyword, index + 1)
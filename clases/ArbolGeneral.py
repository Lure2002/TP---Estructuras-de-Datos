class Arbol_General:
	#clase nodo arbol
    def __init__(self,info):
        self.info = info
        self.sig = None #lista donde guarda todos los hermanos, en la raiz no hay hermanos
        self.hijos = None#sin hijos
    def retornarhijos(self):
      return self.hijos

def arbol_vacio(raiz):
	#retorna si el arbol esta vacio
	return raiz == None

def agregar_hijo_raiz(raiz,info):
	#inserto el dato en el arbol
	if arbol_vacio(raiz):
		raiz = Arbol_General(info)
		#referencio el comienzo de la lista
	else:
		raiz = agregar_nodo(raiz,info)
	return raiz #una vez actualizado el dato se retorna la raiz

def agregar_nodo(raiz,info):
	nodo = Arbol_General(info)
	if(raiz.hijos is None):
			#no tiene hijos
			raiz.hijos = nodo
	else:
		anterior = raiz.hijos
		actual = raiz.hijos.sig
		while (actual is not None):
			anterior = anterior.sig #anterior = actual
			actual = actual.sig
		anterior.sig = nodo
		nodo.sig = actual
	return raiz

def agregar_hijo_nodo(raiz,nodo,info):
		if not arbol_vacio(raiz):
			anterior = raiz.hijos
			actual = raiz.hijos.sig
			ok = False
			while (actual is not None) and (not ok):
				if anterior.info == nodo:
					ok = True
				else:
					anterior = anterior.sig #anterior = actual
					actual = actual.sig
			if anterior.info == nodo:
				nodo = agregar_nodo(anterior,info)
			anterior.sig = nodo
			nodo.sig = actual
		return raiz

def imprimir_consultas_recursivo(nodo, nivel=0):
    """Función recursiva para imprimir consultas."""
    if nodo is not None:
          # Imprimir información de la consulta actual
          if isinstance(nodo.info, tuple):  # Asegurarse de que sea una consulta
              fecha, consulta_info = nodo.info
              print("  " * nivel + f"Fecha: {fecha}")
              print("  " * nivel + f"Consulta: {consulta_info['consulta']}")
              print("  " * nivel + f"Diagnóstico: {consulta_info['diagnostico']}")
              print("  " * nivel + f"Tratamiento: {consulta_info['tratamiento']}")
              print("  " * nivel + f"Medicamento: {consulta_info['medicamento']}")
              print()  # Imprimir una línea en blanco entre consultas

          # Imprimir consultas de los hijos (recursivamente)
          imprimir_consultas_recursivo(nodo.hijos, nivel + 1)

          # Imprimir consultas de los hermanos
          imprimir_consultas_recursivo(nodo.sig, nivel)
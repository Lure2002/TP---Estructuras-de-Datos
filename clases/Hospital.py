from clases.paciente import Paciente
          
class NodoArbolBinario:
	def __init__(self, paciente:Paciente):
		self.paciente = paciente
		self.hijoizq:NodoArbolBinario = None
		self.hijoder:NodoArbolBinario = None

class Hospital:
	def __init__(self):
		self.pacientes:dict[int, Paciente] = dict()
		self.arbolbi:NodoArbolBinario = None 

	def agregar_paciente(self, nuevo_paciente:Paciente):
		self.pacientes[nuevo_paciente.id()] = nuevo_paciente
		self.arbolbi = self._insertar_nodo(self.arbolbi, nuevo_paciente)

	def _insertar_nodo(self, raiz:NodoArbolBinario, elemento:Paciente):
		if raiz is None:
			return NodoArbolBinario(elemento)
		if elemento.id() < raiz.paciente.id():
			raiz.hijoizq = self._insertar_nodo(raiz.hijoizq, elemento)
		else:
			raiz.hijoder = self._insertar_nodo(raiz.hijoder, elemento)
		return raiz

	def eliminar_paciente(self, id_paciente):
		if id_paciente in self.pacientes:
			self.arbolbi = self._eliminar_nodo(self.arbolbi, id_paciente)
			del self.pacientes[id_paciente]
		else:
			print(f"Paciente con ID {id_paciente} no encontrado.")

	def _eliminar_nodo(self, raiz, clave):
		if raiz is None:
			return None
		if clave < raiz.paciente.id():
			raiz.hijoizq = self._eliminar_nodo(raiz.hijoizq, clave)
		elif clave > raiz.paciente.id():
			raiz.hijoder = self._eliminar_nodo(raiz.hijoder, clave)
		else:
			if raiz.hijoizq is None and raiz.hijoder is None:
				return None
			elif raiz.hijoizq is None:
				return raiz.hijoder
			elif raiz.hijoder is None:
				return raiz.hijoizq
			sucesor = self._reemplazar(raiz.hijoder)
			raiz.paciente = sucesor.paciente
			raiz.hijoder = self._eliminar_nodo(raiz.hijoder, sucesor.paciente.id())
		return raiz

	def _reemplazar(self, raiz):
		while raiz.hijoizq is not None:
			raiz = raiz.hijoizq
		return raiz

	def cola_de_prioridades(self):
		pass

	def buscar_paciente(self, id_paciente):
		return self._buscar(self.arbolbi, id_paciente)

	def _buscar(self, raiz, clave):
		if raiz is None or raiz.paciente.id() == clave:
			return raiz
		if clave < raiz.paciente.id():
			return self._buscar(raiz.hijoizq, clave)
		return self._buscar(raiz.hijoder, clave)

	def inorden(self):
		print("Inorden:", end=" ")
		self._inorden(self.arbolbi)
		print()

	def _inorden(self, raiz):
		if raiz is not None:
			self._inorden(raiz.hijoizq)
			print(raiz.paciente.id(), end=" ")
			self._inorden(raiz.hijoder)

	def preorden(self):
		print("Preorden:", end=" ")
		self._preorden(self.arbolbi)
		print()

	def _preorden(self, raiz):
		if raiz is not None:
			print(raiz.paciente.id(), end=" ")
			self._preorden(raiz.hijoizq)
			self._preorden(raiz.hijoder)

	def postorden(self):
		print("Postorden:", end=" ")
		self._postorden(self.arbolbi)
		print()

	def _postorden(self, raiz):
		if raiz is not None:
			self._postorden(raiz.hijoizq)
			self._postorden(raiz.hijoder)
			print(raiz.paciente.id(), end=" ")

	def por_nivel(self):
		print("Por nivel:", end=" ")
		self._por_nivel(self.arbolbi)
		print()

	def _por_nivel(self, raiz):
		from collections import deque
		if raiz is None:
			return
		cola = deque([raiz])
		while cola:
			nodo = cola.popleft()
			print(nodo.paciente.id(), end=" ")
			if nodo.hijoizq:
				cola.append(nodo.hijoizq)
			if nodo.hijoder:
				cola.append(nodo.hijoder)

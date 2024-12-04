class NodoArbolBinario:
    def __init__(self,id):
        self.raiz = id
        self.hijoder = None
        self.hijoizq = None

    def anadirder(self,element):
        self.hijoder = element

    def anadirizq(self,element):
        self.hijoder = element

    def anadir(self,id):
        if id.retornarid() < self.raiz.retornarid():
            if self.hijoizq is None:
                self.hijoizq = NodoArbolBinario(id)
            else:
                self.hijoizq.anadir(id)
        else:
            if self.hijoder is None:
                self.hijoder = NodoArbolBinario(id)
            else:
                self.hijoder.anadir(id)

    def busqueda(self,id):
        if id == self.raiz.retornarid():
            return self.raiz
        elif id < self.raiz.retornarid():
            if self.hijoizq is None:
                return None
            else:
                return self.hijoizq.busqueda(id)
        else:
            if self.hijoder is None:
                return None
            else:
                return self.hijoder.busqueda(id)

    def imprimir_arbol_con_señalamiento (self,prefijo="", es_izquierdo=True):
      """Imprime el árbol con señalamiento en lugar de indentación."""
      if self.raiz is None:
          return
      if es_izquierdo:
          conector = "/-- "
      else:
          conector = "\-- "

      print(prefijo + conector + str(self.raiz.retornarid()))

      prefijo_hijo = prefijo + ("|   " if es_izquierdo else "    ")

      if self.hijoizq:  # Check if left child exists before printing
        self.hijoizq.imprimir_arbol_con_señalamiento(prefijo_hijo, True)
      if self.hijoder:  # Check if right child exists before printing
        self.hijoder.imprimir_arbol_con_señalamiento(prefijo_hijo, False)

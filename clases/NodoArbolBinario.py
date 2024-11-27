class NodoArbolBinario:
    def __init__(self,id):
        self.raiz = id
        self.hijoder = None
        self.hijoizq = None

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

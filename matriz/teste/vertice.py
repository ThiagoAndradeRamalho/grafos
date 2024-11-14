class Vertice:

    def __init__(self, rotulo):
        self._rotulo = rotulo
        self._visitado = False
        self.posicaoVisitado = 0
        self._pai = None
        self._tempo_descoberta = 0
        self._tempo_termino = 0
        self._nivel = 0
        self._indice = 0

    @property
    def rotulo(self):
        return self._rotulo
    
    @rotulo.setter
    def rotulo(self, value):
        self._rotulo = value
    
    @property
    def visitado(self):
        return self._visitado
    
    @visitado.setter
    def visitado(self, boolean):
        self._visitado = boolean

    def __str__(self):
        return self.rotulo
    
    def __repr__(self):
        return self.__str__()

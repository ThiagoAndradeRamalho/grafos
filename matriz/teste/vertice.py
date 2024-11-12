class Vertice:

    def __init__(self, rotulo):
        self._rotulo = rotulo
        self._visitado = False
        self.posicaoVisitado = 0
        self.pai = None

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

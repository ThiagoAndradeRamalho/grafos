class Aresta:

    def __init__(self, origem, destino, peso):
        self._origem = origem
        self._destino = destino
        self._peso = peso

    @property
    def origem(self):
        return self._origem
    
    @property
    def destino(self):
        return self._destino
    
    @property
    def peso(self):
        return self._peso
    
    def __str__(self):
        return f"({self._origem}, {self._destino}): {self._peso}"
    
    def __repr__(self):
        return self.__str__()
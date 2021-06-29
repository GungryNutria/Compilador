class Token:
    def __init__(self, palabra, tipo):
        self.palabra = palabra
        self.tipo = tipo

    def getPalabra(self):
        return self.palabra
        
    def getTipo(self):
        return  self.tipo
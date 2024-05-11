class ControleRemoto:

    def __init__(self, televisor):
        self.televisor = televisor

    def aumentaVolume(self, valor):
        self.televisor.aumentaVolume(valor)
        print("Volume atual:", self.televisor.volume)

    def diminuiVolume(self, valor):
        self.televisor.diminuiVolume(valor)
        print("Volume atual:", self.televisor.volume)

    def trocaCanal(self, canal):
        self.televisor.trocaCanal(canal)
        print("Canal atual:", self.televisor.canalAtual)


    def sintonizaCanal(self, televisor, canal):
        televisor.sintonizaCanal(canal)
        print("Canal sintonizado:", self.televisor.canalAtual)
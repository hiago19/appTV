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
        if self.televisor.listaCanais:
            if canal in self.televisor.listaCanais:
                self.televisor.canalAtual = canal
                print("Canal atual:", self.televisor.canalAtual)
            else:
                print("Canal não disponível.")
        else:
            print("Não há canais disponíveis. Sintonize um novo canal.")

    def sintonizaCanal(self, canal):
        self.televisor.sintonizaCanal(canal)
        print("Canal sintonizado:", self.televisor.canalAtual)
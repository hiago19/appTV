class televisor:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canalAtual = None
        self.listaCanais = []
        self.volume = 20

    def aumentaVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.televisor.listaCanais:
            self.televisor.trocaCanal(canal)
            print("Canal atual:", self.televisor.canalAtual)
        else:
            print("Canal não disponível.")

    def sintonizaCanal(self, canal):
        if canal not in self.listaCanais:
            self.listaCanais.append(canal)
            self.canalAtual = canal

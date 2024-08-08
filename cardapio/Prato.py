from cardapio.ItemCardapio import ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome:str, preco:float, descricao:str):
        super().__init__(nome, preco)
        self._descricao = descricao

    def aplicar_desconto(self):
        self.preco -= (self._preco * 0.05)
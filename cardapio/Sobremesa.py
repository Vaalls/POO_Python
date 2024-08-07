from cardapio.ItemCardapio import ItemCardapio
class Sobremesa(ItemCardapio):
    def __init__(self, nome:str, preco:float, tipo:str, tamanho:str, descricao:str):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return f'Tipo da sobremesa: {self._tipo}'

    def aplicar_desconto(self):
        pass
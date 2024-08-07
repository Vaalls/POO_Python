class Restaurante:
    restaurantes = []
    def __init__(self, nome:str, categoria:str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

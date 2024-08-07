class Restaurante:
    restaurantes = []
    def __init__(self, nome:str, categoria:str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(self):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | '
              f'{"Avaliação".ljust(20)} | {"Status"}')
        for restaurant in Restaurante.restaurantes:
            print(f'{restaurant._nome.ljust(20)} | {restaurant.categoria.ljust(20)} | '
                  f'{str(restaurant.media_avaliacoes).ljust(20)} | {restaurant.ativo}')
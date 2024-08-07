from cardapio.ItemCardapio import ItemCardapio
from modelos.Avaliacao import Avaliacao
from modelos.Cliente import Cliente


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

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: Cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_nota = len(self._avaliacao)
        media = round(soma_notas / qtd_nota, 1)
        return media

    def adicionar_item(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
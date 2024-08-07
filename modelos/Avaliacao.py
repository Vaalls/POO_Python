from modelos.Cliente import Cliente
class Avaliacao:
    def __init__(self, cliente:Cliente, nota:float):
        self._cliente = cliente
        self._nota = nota

    def __str__(self):
        return f'A avaliação de {self._cliente._nome} é de {self._nota}'

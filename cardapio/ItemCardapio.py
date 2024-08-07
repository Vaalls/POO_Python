from abc import abstractmethod


class ItemCardapio():
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass

# Se torna um metodo obrigatorio para todas as classe que fazem herança

Classe "App" a principal do nosso sistema para podermos rodar e testar o funcionamento do projeto.
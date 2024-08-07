from cardapio.Bebida import Bebida
from cardapio.Prato import Prato
from modelos.Avaliacao import Avaliacao
from modelos.Cliente import Cliente
from modelos.Resturante import Restaurante

cliente = Cliente('Gabriel', 20)
avaliacao = Avaliacao(cliente, 9.2)

restaurante = Restaurante('Vallz', 'Italiano')
print(restaurante)
restaurante.alternar_estado()
print(f'O restaurante {restaurante.nome} {restaurante.ativo}, foi ativado com sucesso!')

bebida_suco = Bebida('Coca-Cola', 9, 'Média')

prato_macarrao = Prato('Macarrão', 30.85, 'Macarrão da casa')

restaurante.adicionar_item(bebida_suco)

restaurante.exibir_cardapio



def main():
    main

if __name__ == '__main__':
    main()
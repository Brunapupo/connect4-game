from random import randrange


class Jogador:

    def __init__(self, peca_jogador, nome_jogador):
        self._peca_jogador = peca_jogador
        self._nome_jogador = nome_jogador

    def decidir_jogada(self):
        jogada_jogador = int(input(f"Agora é sua vez, {self._nome_jogador}! escolha uma das colunas entre 1 a 7: "))
        return jogada_jogador

    def get_peca_jogador(self):
        return self._peca_jogador


class JogadorComputador(Jogador):

    def __init__(self, peca_jogador, nome_jogador):
        super().__init__(peca_jogador, nome_jogador)

    def decidir_jogada(self):
        jogada_computador = randrange(1, 7)
        return jogada_computador

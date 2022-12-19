from tabuleiro import Tabuleiro
from juiz import Juiz
from jogador import Jogador, JogadorComputador


class Jogo:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.juiz = Juiz()
        self.jogador_1 = Jogador('🦒', 'Jogador 1')
        self.jogador_2 = Jogador('🧡', 'Jogador 2')
        self.computador = JogadorComputador('🧡', 'Computador')

    def realizar_jogada(self, jogador):
        jogada = jogador.decidir_jogada()
        jogada_valida = self.tabuleiro.jogar_peca(jogada, jogador.get_peca_jogador())
        if not jogada_valida:
            while not jogada_valida:
                jogada_jogador = int(input("Jogada Invalida! tente denovo!: "))
                jogada_valida = self.tabuleiro.jogar_peca(jogada_jogador, jogador.get_peca_jogador())

    def iniciar_jogo(self):
        humano_computador = -1
        while humano_computador < 0 or humano_computador > 1:
            humano_computador = int(input("Digite [0] para jogar contra um humano, [1] contra o computador: "))
            if humano_computador != 0 and humano_computador != 1:
                print("Tentativa intaválida! escolha entre [0] ou [1]")

        fim_do_jogo = False
        self.tabuleiro.mostra_tabuleiro()
        while not fim_do_jogo:

            #  humano x humano
            if humano_computador == 0:
                #  jogada do jogador 1
                self.realizar_jogada(self.jogador_1)
                self.tabuleiro.mostra_tabuleiro()
                vitoria = self.juiz.verifica_vitoria(self.tabuleiro.get_numeros(), self.tabuleiro.get_tabuleiro())

                if vitoria:
                    print("Parabéns Jogador 1, você ganhou!")
                    fim_do_jogo = True
                    self.tabuleiro.mostra_tabuleiro()
                    continue

                #  jogada do jogador 2
                self.realizar_jogada(self.jogador_2)
                self.tabuleiro.mostra_tabuleiro()
                vitoria = self.juiz.verifica_vitoria(self.tabuleiro.get_numeros(), self.tabuleiro.get_tabuleiro())

                if vitoria:
                    print("Parabéns Jogador 2, você ganhou!")
                    fim_do_jogo = True
                    self.tabuleiro.mostra_tabuleiro()
                    continue

            #  humano x computador
            elif humano_computador == 1:
                #  jogada jogador
                self.realizar_jogada(self.jogador_1)
                self.tabuleiro.mostra_tabuleiro()
                vitoria = self.juiz.verifica_vitoria(self.tabuleiro.get_numeros(), self.tabuleiro.get_tabuleiro())

                if vitoria:
                    print("Parabéns Jogador, você ganhou!")
                    fim_do_jogo = True
                    self.tabuleiro.mostra_tabuleiro()
                    continue

                #  jogada computador
                print("Jogada do computador.")
                self.realizar_jogada(self.computador)
                self.tabuleiro.mostra_tabuleiro()
                vitoria = self.juiz.verifica_vitoria(self.tabuleiro.get_numeros(), self.tabuleiro.get_tabuleiro())

                if vitoria:
                    print("O computador ganhou!")
                    fim_do_jogo = True
                    self.tabuleiro.mostra_tabuleiro()
                    continue

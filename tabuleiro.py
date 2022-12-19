class Tabuleiro:

    def __init__(self):
        self._numeros = ["__1___", "__2___", "__3___", "__4___", "__5___", "__6___", "__7___"]
        self._tabuleiro = [
            ["______", "______", "______", "______", "______", "______", "______"],
            ["______", "______", "______", "______", "______", "______", "______"],
            ["______", "______", "______", "______", "______", "______", "______"],
            ["______", "______", "______", "______", "______", "______", "______"],
            ["______", "______", "______", "______", "______", "______", "______"],
            ["______", "______", "______", "______", "______", "______", "______"],
        ]

    def get_numeros(self):
        return self._numeros

    def get_tabuleiro(self):
        return self._tabuleiro

    def mostra_tabuleiro(self):
        print("   ", end=" |")
        for n in self._numeros:
            print(f"{n}", end="|")
        print()

        for i in range(len(self._tabuleiro)):
            linha = self._tabuleiro[i]
            print(f" {i+1} ", end=" |")

            for c in linha:
                print(f"{c}", end="|")
            print()

    def jogar_peca(self, jogada_jogador, peca_jogador):
        if jogada_jogador < 1 or jogada_jogador > 7:
            return False
        jogada_jogador = jogada_jogador - 1
        i = len(self._tabuleiro) - 1
        while i >= 0:
            posicao_atual = self._tabuleiro[i][jogada_jogador]
            if posicao_atual == '______':
                self._tabuleiro[i][jogada_jogador] = "__" + peca_jogador + "__"
                return True
            i -= 1
        return False

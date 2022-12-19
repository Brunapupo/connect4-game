class Juiz:

    def verifica_vitoria(self, numeros, tabuleiro):
        resultado = False
        #  verificação das colunas
        resultado = self._verifica_colunas(resultado, numeros, tabuleiro)
        #  verificação das linhas
        resultado = self._verifica_linhas(resultado, numeros, tabuleiro)
        #  diagonal principal
        resultado = self._verifica_diagonal_principal(resultado, tabuleiro)
        #  diagonais acima da diagonal principal
        resultado = self._verifica_acima_principal(resultado, tabuleiro)
        #  diagonais abaixo da diagonal principal
        resultado = self._verifica_abaixo_principal(resultado, tabuleiro)
        #  diagonais acima da secundaria
        resultado = self._verifica_acima_secundaria(resultado, tabuleiro)
        #  diagonais abaixo da secundaria
        resultado = self._verifica_abaixo_secundaria(resultado, numeros, tabuleiro)
        #  diagonal secundaria
        resultado = self._verifica_diagonal_secundaria(resultado, numeros, tabuleiro)
        return resultado


    # verifica vitória percorrendo todas linhas, colunas, e todas as diagonais abaixo e acima princial e secundária
    # do tabuleiro.
    def _verifica_colunas(self, resultado, numeros, tabuleiro):
        for coluna in range(len(numeros)):
            cont = 0
            for linha in range(1, len(tabuleiro)):
                posicao_atual = tabuleiro[linha][coluna]
                if posicao_atual == tabuleiro[linha - 1][coluna] and posicao_atual != '______':
                    cont += 1
                    if cont == 3:
                        resultado = True
                else:
                    cont = 0
        return resultado

    def _verifica_linhas(self, resultado, numeros, tabuleiro):
        for linha in range(1, len(tabuleiro)):
            cont = 0
            for coluna in range(0, len(numeros)):
                posicao_atual = tabuleiro[linha][coluna]
                if posicao_atual == tabuleiro[linha][coluna - 1] and posicao_atual != '______':
                    cont += 1
                    if cont == 3:
                        print(cont)
                        resultado = True
                else:
                    cont = 0
        return resultado

    def _verifica_diagonal_principal(self, resultado, tabuleiro):
        diagonal = 1
        cont = 0
        while diagonal <= len(tabuleiro) - 1:
            posicao_atual = tabuleiro[diagonal][diagonal]
            if posicao_atual == tabuleiro[diagonal-1][diagonal-1] and posicao_atual != '______':
                cont += 1
                if cont == 3:
                    resultado = True
            else:
                cont = 0
            diagonal += 1
        return resultado

    def _verifica_acima_principal(self, resultado, tabuleiro):
        elementos_lista = []
        diagonal = 1
        while diagonal <= len(tabuleiro) - 1:
            linha = 0
            coluna = diagonal
            lista = []
            while coluna <= len(tabuleiro) - 1:
                posicao_atual = tabuleiro[linha][coluna]
                lista.append(posicao_atual)
                linha += 1
                coluna += 1
            diagonal += 1
            elementos_lista.append(lista)
        for lista in elementos_lista:
            cont = 0
            for i in range(1, len(lista)):
                posicao_atual = lista[i]
                if posicao_atual == lista[i - 1] and posicao_atual != '______':
                    cont += 1
                    if cont == 3:
                        resultado = True
                else:
                    cont = 0
        return resultado

    def _verifica_abaixo_principal(self, resultado, tabuleiro):
        elementos_lista = []
        diagonal = 1
        while diagonal <= len(tabuleiro) - 1:
            linha = diagonal
            coluna = 0
            lista = []
            while linha <= len(tabuleiro) - 1:
                posicao_atual = tabuleiro[linha][coluna]
                lista.append(posicao_atual)
                linha += 1
                coluna += 1
            diagonal += 1
            elementos_lista.append(lista)
        for lista in elementos_lista:
            cont = 0
            for i in range(1, len(lista)):
                posicao_atual = lista[i]
                if posicao_atual == lista[i - 1] and posicao_atual != '______':
                    cont += 1
                    if cont == 3:
                        resultado = True
                else:
                    cont = 0
        return resultado

    def _verifica_acima_secundaria(self, resultado, tabuleiro):
        elementos_lista = []
        diagonal = 0
        while diagonal <= len(tabuleiro) - 1:
            linha = 0
            coluna = len(tabuleiro) - 1 - diagonal
            lista = []
            while coluna >= 0:
                posicao_atual = tabuleiro[linha][coluna]
                lista.append(posicao_atual)
                coluna -= 1
                linha += 1
            diagonal += 1
            elementos_lista.append(lista)

        for lista in elementos_lista:
            cont = 0
            for i in range(1, len(lista)):
                posicao_atual = lista[i]
                if posicao_atual == lista[i - 1] and posicao_atual != '______':
                    cont += 1
                    if cont == 3:
                        resultado = True
                else:
                    cont = 0
        return resultado

    def _verifica_abaixo_secundaria(self, resultado, numeros, tabuleiro):
        elementos_lista = []
        diagonal = 0
        while diagonal <= len(tabuleiro):
            linha = diagonal
            coluna = len(numeros) - 1
            lista = []
            while coluna > diagonal:
                posicao_atual = tabuleiro[linha][coluna]
                lista.append(posicao_atual)
                coluna -= 1
                linha += 1
            diagonal += 1
            elementos_lista.append(lista)

        for lista in elementos_lista:
            cont = 0
            for i in range(1, len(lista)):
                posicao_atual = lista[i]
                if posicao_atual == lista[i - 1] and posicao_atual != '______':
                    cont += 1
                    if cont == 3:
                        resultado = True
                else:
                    cont = 0
        return resultado

    def _verifica_diagonal_secundaria(self, resultado, numeros, tabuleiro):
        linha = 1
        cont = 0
        tam = len(numeros)
        coluna = tam - 2
        while linha < tam - 1:
            posicao_atual = tabuleiro[linha][coluna]
            if posicao_atual == tabuleiro[linha-1][coluna+1] and posicao_atual != '______':
                cont += 1
                if cont == 3:
                    resultado = True
            else:
                cont = 0
            linha = linha + 1
            coluna = coluna - 1
        return resultado

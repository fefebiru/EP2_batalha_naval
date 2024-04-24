def posicao_suporta(mapa,blocos,linha,coluna,orientacao):

    retorno = True
    
    if blocos > 0:
        if orientacao == 'v':
            for horizontal in range(len(mapa)):
                for vertical in range(len(mapa[horizontal])):
                    for x in range(blocos):
                        if linha + x > len(mapa)-1:
                            retorno = False
                        elif mapa[linha+x][coluna] != ' ':
                            retorno = False
        elif orientacao == 'h':
            for horizontal in range(len(mapa)):
                for vertical in range(len(mapa[horizontal])):
                    for x in range(blocos):
                        if coluna + x > len(mapa[horizontal])-1:
                            retorno = False
                        else: 
                            if mapa[linha][coluna+x] != ' ':
                                retorno = False

    return retorno
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

import random

def aloca_navios(mapa,blocos):

    for navio in blocos:
        x = False

        while not x:
            linha = random.randint(0, len(mapa)-1)
            coluna = random.randint(0, len(mapa[0])-1)         
            orientacao = random.choice(['h', 'v'])   
            posi = posicao_suporta(mapa,navio,linha,coluna,orientacao)

            if posi:
                if orientacao == 'v':
                    for a in range(navio):
                        mapa[linha+a][coluna] = 'N'
                    x = True    
                elif orientacao == 'h':
                    for e in range(navio):
                        mapa[linha][coluna+e] = 'N'
                    x = True

    return mapa
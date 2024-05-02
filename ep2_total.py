import time
import random


jogo = 's'

cor_navio = '\u001b[32m'
cor_agua = '\u001b[34m'
cor_atingido = '\u001b[31m'
reset = '\u001b[0m'

navio_ = '▓'

navio_colorido = cor_navio + navio_ + reset

navio_atingido = cor_atingido + navio_ + reset

agua_final = cor_agua + navio_ + reset

while jogo != 'n':

    #função 1
    def cria_mapa(n):

        lista = []
        conjunto = []

        for j in range(n):
            lista = []
            for i in range(n):
                lista.append(' ')
                if len(lista) == n:
                    conjunto.append(lista)

        return conjunto
    # função 2
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
    # função 3
    def aloca_navios_comp(mapa,blocos):

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
                            mapa[linha+a][coluna] = navio_colorido
                        x = True    
                    elif orientacao == 'h':
                        for e in range(navio):
                            mapa[linha][coluna+e] = navio_colorido
                        x = True
            
        return mapa
    #função aloca navios jogador
    def aloca_navios_jog(mapa,blocos,linha,coluna,orientacao):

        new_map = [row[:] for row in mapa]

        for navio in blocos:
            x = False
        
            while not x:  
                posi = posicao_suporta(mapa,navio,linha,coluna,orientacao)

                if posi:
                    if orientacao == 'v':
                        for a in range(navio):
                            new_map[linha+a][coluna] = navio_colorido
                        x = True    
                    elif orientacao == 'h':
                        for e in range(navio):
                            new_map[linha][coluna+e] = navio_colorido
                        x = True

        return new_map
    # função 4
    def foi_derrotado(mapa):
        
        for linha in mapa:
            for valor in linha:
                if valor == navio_colorido:
                    return False
                
        return True
    #função para colocando os mapas na formatação:
    def mostraMapa(mat1, mat2,comp,jog):
        print(f'     COMPUTADOR - {comp}                 JOGADOR - {jog}     \n')
        print('   A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')
        for linha in range(10):
            print(f'{linha+1:2d}', end='')
            for coluna in range(10):
                print(f' {mat1[linha][coluna]} ', end='')
            print(f'{linha+1:2d}', end='')
            print(f'  {linha+1:2d}', end='')
            for coluna in range(10):
                print(f' {mat2[linha][coluna]} ', end='')
            print(f'{linha+1:2d}', end='')
            print(' ')
        print('   A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')
    # quantidade de blocos por modelo de navio
    CONFIGURACAO = {
        'destroyer': 3,
        'porta-avioes': 5,
        'submarino': 2,
        'torpedeiro': 3,
        'cruzador': 2,
        'couracado': 4
    }

    # frotas de cada pais
    PAISES =  {
        'Brasil': {
            'cruzador': 1,
            'torpedeiro': 2,
            'destroyer': 1,
            'couracado': 1,
            'porta-avioes': 1
        }, 
        'França': {
            'cruzador': 3, 
            'porta-avioes': 1, 
            'destroyer': 1, 
            'submarino': 1, 
            'couracado': 1
        },
        'Austrália': {
            'couracado': 1,
            'cruzador': 3, 
            'submarino': 1,
            'porta-avioes': 1, 
            'torpedeiro': 1
        },
        'Rússia': {
            'cruzador': 1,
            'porta-avioes': 1,
            'couracado': 2,
            'destroyer': 1,
            'submarino': 1
        },
        'Japão': {
            'torpedeiro': 2,
            'cruzador': 1,
            'destroyer': 2,
            'couracado': 1,
            'submarino': 1
        }
    }

    # alfabeto para montar o nome das colunas
    ALFABETO = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

    # cores para o terminal
    CORES = {
        'reset': '\u001b[0m',
        'red': '\u001b[31m',
        'black': '\u001b[30m',
        'green': '\u001b[32m',
        'yellow': '\u001b[33m',
        'blue': '\u001b[34m',
        'magenta': '\u001b[35m',
        'cyan': '\u001b[36m',
        'white': '\u001b[37m'
    }

    paises = ['','Brasil','França','Austrália','Rússia','Japão']
    comp = random.choice(['Brasil','França','Austrália','Rússia','Japão'])
    zan = ' '
    zan +='='*37
    zan += ' '

    print(zan)
    print('|',' '*(len(zan)-4),'|')
    print('| Bem-vindo ao INSPER - Batalha Naval |')
    print('|',' '*(len(zan)-4),'|')
    print(' =======   xxxxxxxxxxxxxxxxx   ======= \n')
    print('Iniciando o Jogo!\n')
    print(f'Computador está alocando os navios de guerra do país {comp}...')
    print('Computador já está em posição de batalha!\n')

    #----------------------------------------------------------------------------------------------------------------- 
    #lsta de países
    print('1: Brasil\n  1 cruzador\n  2 torpedeiro\n  1 destroyer\n  1 couracado\n  1 porta-avioes\n')
    print('2: França\n  3 cruzador\n  1 porta-avioes\n  1 destroyer\n  1 submarino\n  1 couracado\n')
    print('3: Austrália\n  1 couracado\n  3 cruzador\n  1 submarino\n  1 porta-avioes\n  1 torpedeiro\n')
    print('4: Rússia\n  1 cruzador\n  1 porta-avioes\n  2 couracado\n  1 destroyer\n  1 submarino\n')
    print('5: Japão\n  2 torpedeiro\n  1 cruzador\n  2 destroyer\n  1 couracado\n  1 submarino\n')

    #----------------------------------------------------------------------------------------------------------------- 
    #início interação usuário - máquina

    pais = input('Qual o número da nação da sua frota? ')
    while True:
        if pais not in ['1','2','3','4','5'] or paises[int(pais)] == comp:
            print('\nOpção inválida')
            print('Você escolheu o mesmo país que o computador!')
            print('Por favor escolha outro país\n')
            pais = input('Qual o número da nação da sua frota? ')
        if pais in ['1','2','3','4','5']:
            break
    
    pais = int(pais)
    escolhido = paises[pais]
    print(f'\nVocê escolheu a nação {escolhido}! \n')
    maps = cria_mapa(10)
    new_map = cria_mapa(10)
    mapa_comp = cria_mapa(10)

    mostraMapa(maps,maps,comp,escolhido)
    print('\n')

    #----------------------------------------------------------------------------------------------------------------- 
    #alocando os navios do jogador   
    blocos = []
    for navio,qtd in  PAISES[escolhido].items():
        blocos = []
        for i in range(qtd):
            print(f'Alocar: {navio} ({CONFIGURACAO[navio]} blocos)')
            while True:
                col = input('Coluna: ')
                col = col.upper()
                if col in ['A','B','C','D','E','F','G','H','I','J']:
                    break
                else:
                    print("Coluna inválida")

            co = ALFABETO[col]

            while True:
                lin = input('Linha: ')
                if lin in ['1','2','3','4','5','6','7','8','9','10']:
                    lin = int(lin)
                    break
                else: 
                    print("Linha inválida!")

            lin -= 1

            while True:
                ori = input('Orientação: [v][h] ')
                if ori in ['h','v']:
                    break
                else: 
                    print("Orientação inválida!")

            while True:
                if posicao_suporta(new_map,CONFIGURACAO[navio],lin,co,ori) == True:
                    break
                else:
                    print('Posição Inválida!')
                    print(f'Alocar: {navio} ({CONFIGURACAO[navio]} blocos)')
                    while True:
                        col = input('Coluna: ')
                        col = col.upper()
                        if col in ['A','B','C','D','E','F','G','H','I','J']:
                            break
                        else:
                            print("Coluna inválida")
                    
                    co = ALFABETO[col]
                    while True:
                        lin = input('Linha: ')
                        if lin in ['1','2','3','4','5','6','7','8','9','10']:
                            lin = int(lin)
                            break
                        else: 
                            print("Linha inválida!")
                    
                    lin -= 1

                    while True:
                        ori = input('Orientação: [v][h] ')
                        if ori in ['h','v']:
                            break
                        else: 
                            print("Orientação inválida!")

            blocos.append(CONFIGURACAO[navio])

            new_map = aloca_navios_jog(new_map,blocos,lin,co,ori)
            mostraMapa(maps,new_map,comp,escolhido)
            print('\n')
    
    print('Todos os navios foram alocados!\n')

    #-----------------------------------------------------------------------------------------------------------------
    # alocar os navios do computador

    blocos_c = []

    print('O computador está alocando seus blocos...\n')

    for navio,qtd in  PAISES[comp].items():
        for i in range(qtd):
            blocos_c.append(CONFIGURACAO[navio])
            
    mapa_comp = aloca_navios_comp(mapa_comp,blocos_c)
            
    #-----------------------------------------------------------------------------------------------------------------
    # iniciando batalha
    print('Iniciando batalha naval!')
    for na in range(5,0,-1):
        if na == 1:
            print(f'{na}\n')
        else:
            print(na)
        time.sleep(1)

    mostraMapa(maps,new_map,comp,escolhido)
    print('\n')

    #-----------------------------------------------------------------------------------------------------------------
    #disparos jogador

    while True:
        while True:
            coluna = input("Coluna do disparo:  ")
            coluna = coluna.upper()
            if coluna in ['A','B','C','D','E','F','G','H','I','J']:
                break
            else:
                print("Coluna inválida")
        while True:
            linha = input("Linha do disparo:  ")
            if linha in ['1','2','3','4','5','6','7','8','9','10']:
                linha = int(linha)
                break
            elif linha not in ['1','2','3','4','5','6','7','8','9','10']: 
                print("Linha inválida!")

        linha -= 1

        col = ALFABETO[coluna]

        if mapa_comp[linha][col]== " ":
            mapa_comp[linha][col] = agua_final
            maps[linha][col] = agua_final
            print(f'\n Jogador      --->>>> {coluna}{linha+1}    Água!\n')

            jogar_novamente = False
        elif mapa_comp[linha][col]== navio_colorido:
            mapa_comp[linha][col] = navio_atingido
            maps[linha][col] = navio_atingido
            print(f'\n Jogador      --->>>> {coluna}{linha+1}    BOOOOOMMMMMMMM!\n')

            jogar_novamente = False
        else:
            print('Você já atirou nesta posição, atire novamente!')
            jogar_novamente = True

    #-----------------------------------------------------------------------------------------------------------------
    #disparos computador

        if jogar_novamente == False:
            linha = random.randint(0,9)
            coluna = random.choice(['A','B','C','D','E','F','G','H','I','J'])
            col = ALFABETO[coluna]

            while new_map[linha][col] == navio_atingido or new_map[linha][col] == agua_final:
                linha = random.randint(0,9)
                coluna = random.choice(['A','B','C','D','E','F','G','H','I','J'])
                col = ALFABETO[coluna]

            if new_map[linha][col]== " ":
                new_map[linha][col] = agua_final
                print(f' Computador      --->>>> {coluna}{linha+1}    Água!\n')
                mostraMapa(maps,new_map,comp,escolhido)
                print('\n')
            elif new_map[linha][col]== navio_colorido:
                new_map[linha][col] = navio_atingido
                print(f' Computador      --->>>> {coluna}{linha+1}    BOOOOOMMMMMMMM!\n')
                mostraMapa(maps,new_map,comp,escolhido)
                print('\n') 

    #-----------------------------------------------------------------------------------------------------------------
    #verifica se acabou o jogo ou não

        if foi_derrotado(new_map) == True:
            print('O jogo acabou!')
            print('Você perdeu!')
            break
        elif foi_derrotado(mapa_comp) == True:
            print('O jogo acabou!')
            print('Você ganhou!')
            break    

    while True:
        jogo = input('\nJogar novamente? [s][n] ')
        jogo = jogo.lower()
        if jogo == 's' or jogo == 'n':
            print('\n')
            break

print('\nAté a próxima!\n')
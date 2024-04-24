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
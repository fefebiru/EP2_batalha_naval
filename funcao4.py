def foi_derrotado(mapa):
    
    for linha in mapa:
        for valor in linha:
            if valor == 'N':
                return False
            
    return True

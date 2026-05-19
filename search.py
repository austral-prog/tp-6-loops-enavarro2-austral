# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    indice = -1
    if target not in lst:
        return -1
    else:
        for i in lst:
            indice += 1
            if i == target:
                return indice


def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    indice = start - 1
    if target not in lst[start:]: # Del índice start para adelante
        return -1
    else:
        for i in lst[start:]: # Del índice start para adelante
            indice += 1
            if i == target:
                return indice


def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    indice = -1
    if "" not in lst:
        return -1
    else:
        for i in lst:
            indice += 1
            if i == "":
                return indice

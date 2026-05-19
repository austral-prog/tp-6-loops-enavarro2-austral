# Replace the "ANSWER HERE" for your answer

def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    indice = -1
    for i in lst:
            indice += 1
            if i == "":
                del lst[indice]
                lst.insert(indice, value)
                return indice
    return -1


def remove(value, lst):
    """
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """
    indice = -1
    eliminaciones = 0
    for i in lst:
        indice += 1
        if i == value:
            lst[indice] = ""
            eliminaciones += 1
    return eliminaciones
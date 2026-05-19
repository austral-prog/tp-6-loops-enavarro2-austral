# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    unica_lista = []
    for lista in matrix:
        for elemento in lista:
            unica_lista.append(elemento)
    return unica_lista


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    unica_lista = []
    for lista in matrix:
        suma_de_la_fila = 0
        for elemento in lista:
            suma_de_la_fila += elemento
        unica_lista.append(suma_de_la_fila)
    return unica_lista


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    nueva_lista = []
    cantidad_filas = len(matrix)
    cantidad_columnas = len(matrix[0])

    for columna in range(cantidad_columnas):
        suma_columna = 0
        for fila in range(cantidad_filas):
            suma_columna += matrix[fila][columna]
        nueva_lista.append(suma_columna)

    return nueva_lista
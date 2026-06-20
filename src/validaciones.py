def separar_ingredientes(texto):
    """
    Convierte el texto ingresado por el usuario en una lista de ingredientes válida.

    Parámetros:
        texto (str): ingredientes separados por coma.

    Retorna:
        list: lista de ingredientes limpios.
              Si el texto es inválido, devuelve lista vacía.
    """
    if texto.strip() == "":
        return []

    ingredientes = texto.split(",")
    ingredientes_validos = []

    for ingrediente in ingredientes:
        ingrediente = ingrediente.strip().lower()

        if ingrediente != "":
            ingredientes_validos.append(ingrediente)

    return ingredientes_validos


def es_valida_opcion_menu(opcion):
    """
    Verifica si la opción ingresada pertenece al menú.

    Parámetros:
        opcion (str): opción ingresada por el usuario.

    Retorna:
        bool: True si la opción es válida, False si no.
    """

    opciones_validas = ["1", "2", "3", "4"]

    if opcion in opciones_validas:
        return True

    return False


def validar_resultados_api(resultados):
    """
    Verifica si la API devolvió resultados válidos.

    Parámetros:
        resultados (list): lista de recetas obtenidas desde la API.

    Retorna:
        bool: True si hay resultados, False si no.
    """

    if resultados is None:
        return False

    if type(resultados) != list:
        return False

    if len(resultados) == 0:
        return False

    return True

def validar_numero_receta(opcion_elegida, opcion_maxima):
    try:
        n = int(opcion_elegida)
        if 0 <= n <= opcion_maxima:
            return True
        else:
            print('El número de receta no existe')
            return False
    except ValueError :
        print('El número no es válido')

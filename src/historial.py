#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:07:08 2026

@author: juanalolamuruzeta
"""

import os
import pandas as pd
from datetime import datetime


COLUMNAS_HISTORIAL = [
    "fecha",
    "ingredientes",
    "cantidad_resultados",
    "mejor_porcentaje",
    "receta_mejor_coincidencia",
    "categoria",
    "pais"
]


def guardar_busqueda(ingredientes, cantidad_resultados, mejor_porcentaje, receta_mejor_coincidencia, categoria, pais):
    """
    Guarda una búsqueda realizada por el usuario en un archivo CSV.

    Parámetros:
        ingredientes (str): ingredientes ingresados por el usuario.
        cantidad_resultados (int): cantidad de recetas encontradas.
        mejor_porcentaje (float): mejor porcentaje de coincidencia obtenido.
        receta_mejor_coincidencia (str): receta con mayor coincidencia.
        categoria (str): categoría de la receta con mayor coincidencia.
        pais (str): país o región de la receta con mayor coincidencia.

    Retorna:
        bool: True si se guardó correctamente, False si hubo un error.
    """

    if type(ingredientes) != str:
        print("Error: los ingredientes deben ser texto.")
        return False

    if ingredientes.strip() == "":
        print("Error: debe ingresar al menos un ingrediente.")
        return False

    if type(cantidad_resultados) != int:
        print("Error: la cantidad de resultados debe ser un número entero.")
        return False

    if cantidad_resultados < 0:
        print("Error: la cantidad de resultados no puede ser negativa.")
        return False

    if type(mejor_porcentaje) != int and type(mejor_porcentaje) != float:
        print("Error: el mejor porcentaje debe ser un número.")
        return False

    if mejor_porcentaje < 0 or mejor_porcentaje > 100:
        print("Error: el mejor porcentaje debe estar entre 0 y 100.")
        return False

    if receta_mejor_coincidencia is None or receta_mejor_coincidencia == "":
        receta_mejor_coincidencia = "Sin datos"

    if categoria is None or categoria == "":
        categoria = "Sin datos"

    if pais is None or pais == "":
        pais = "Sin datos"

    if not os.path.exists("datos"):
        os.makedirs("datos")

    archivo = "datos/historial_busquedas.csv"

    nuevo_registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ingredientes": ingredientes.strip().lower(),
        "cantidad_resultados": cantidad_resultados,
        "mejor_porcentaje": mejor_porcentaje,
        "receta_mejor_coincidencia": receta_mejor_coincidencia,
        "categoria": categoria,
        "pais": pais
    }

    if os.path.exists(archivo):
        historial = pd.read_csv(archivo)

        for columna in COLUMNAS_HISTORIAL:
            if columna not in historial.columns:
                historial[columna] = "Sin datos"

        historial = historial[COLUMNAS_HISTORIAL]

    else:
        historial = pd.DataFrame(columns=COLUMNAS_HISTORIAL)

    nuevo_df = pd.DataFrame([nuevo_registro])
    historial = pd.concat([historial, nuevo_df], ignore_index=True)

    historial.to_csv(archivo, index=False)

    print("Búsqueda guardada correctamente.")
    return True


def leer_historial():
    """
    Lee el archivo historial_busquedas.csv y devuelve su contenido.

    Retorna:
        DataFrame: historial de búsquedas si existe.
        DataFrame vacío si el archivo no existe, está vacío o hay error.
    """

    archivo = "datos/historial_busquedas.csv"

    if not os.path.exists(archivo):
        print("Todavía no existe un historial de búsquedas.")
        return pd.DataFrame(columns=COLUMNAS_HISTORIAL)

    try:
        historial = pd.read_csv(archivo)

    except:
        print("Error: no se pudo leer el historial.")
        return pd.DataFrame(columns=COLUMNAS_HISTORIAL)

    if historial.empty:
        print("El historial está vacío.")
        return pd.DataFrame(columns=COLUMNAS_HISTORIAL)

    for columna in COLUMNAS_HISTORIAL:
        if columna not in historial.columns:
            historial[columna] = "Sin datos"

    historial = historial[COLUMNAS_HISTORIAL]

    return historial


def mostrar_historial():
    """
    Muestra en consola el historial de búsquedas realizadas.

    Retorna:
        None
    """

    historial = leer_historial()

    if historial is None or historial.empty:
        print("No hay búsquedas registradas.")
        return None

    columnas = [
        "fecha",
        "ingredientes",
        "cantidad_resultados",
        "mejor_porcentaje",
        "receta_mejor_coincidencia",
        "categoria",
        "pais"
    ]

    historial = historial[columnas]

    print("\nHISTORIAL DE BÚSQUEDAS")
    print("----------------------")
    print(historial.to_string(index=False))

    return None


def obtener_ingredientes_mas_buscados():
    """
    Obtiene los ingredientes más buscados a partir del historial.

    Retorna:
        Series: conteo de ingredientes más buscados.
    """

    historial = leer_historial()

    if historial is None or historial.empty:
        print("No hay historial para analizar ingredientes.")
        return pd.Series(dtype=int)

    lista_ingredientes = []

    for texto in historial["ingredientes"]:
        ingredientes = str(texto).split(",")

        for ingrediente in ingredientes:
            ingrediente_limpio = ingrediente.strip().lower()

            if ingrediente_limpio != "":
                lista_ingredientes.append(ingrediente_limpio)

    if len(lista_ingredientes) == 0:
        return pd.Series(dtype=int)

    ingredientes_mas_buscados = pd.Series(lista_ingredientes).value_counts()

    return ingredientes_mas_buscados

# Acá dejamos COLUMNAS_HISTORIAL para no repetir mil veces las columnas
 y para que todo coincida.
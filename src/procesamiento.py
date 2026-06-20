#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:04:38 2026

@author: juanalolamuruzeta
"""

from src.api_recetas import obtener_detalle_receta


def calcular_coincidencias(ingredientes_usuario, ingredientes_receta):
    """
    Devuelve la cantidad de ingredientes coincidentes entre el usuario y una receta.

    Parámetros:
        ingredientes_usuario (list): ingredientes ingresados por el usuario.
        ingredientes_receta (list): ingredientes de la receta.

    Retorna:
        int: cantidad de ingredientes coincidentes.
    """

    if not ingredientes_usuario:
        return 0

    if not ingredientes_receta:
        return 0

    contador = 0

    for ingrediente in ingredientes_usuario:
        ingrediente = ingrediente.strip().lower()

        if ingrediente in ingredientes_receta:
            contador += 1

    return contador


def calcular_porcentaje_coincidencia(coincidencias, cantidad_ingredientes_usuario):
    """
    Calcula el porcentaje de coincidencia entre los ingredientes ingresados
    por el usuario y una receta.

    Parámetros:
        coincidencias (int): cantidad de ingredientes coincidentes.
        cantidad_ingredientes_usuario (int): cantidad total de ingredientes ingresados.

    Retorna:
        float: porcentaje de coincidencia.
    """

    if cantidad_ingredientes_usuario == 0:
        return 0

    porcentaje = (coincidencias / cantidad_ingredientes_usuario) * 100

    return round(porcentaje, 2)


def ordenar_por_coincidencia(recetas):
    """
    Ordena las recetas de mayor a menor porcentaje de coincidencia.

    Parámetros:
        recetas (list): lista de diccionarios con información de las recetas.

    Retorna:
        list: lista ordenada.
    """

    if not recetas:
        return []

    recetas_ordenadas = sorted(
        recetas,
        key=lambda receta: receta["porcentaje"],
        reverse=True
    )

    return recetas_ordenadas


def filtrar_por_porcentaje(recetas, minimo):
    """
    Filtra recetas según un porcentaje mínimo de coincidencia.

    Parámetros:
        recetas (list): lista de recetas.
        minimo (float): porcentaje mínimo.

    Retorna:
        list: recetas filtradas.
    """

    if not recetas:
        return []

    recetas_filtradas = []

    for receta in recetas:
        if receta["porcentaje"] >= minimo:
            recetas_filtradas.append(receta)

    return recetas_filtradas


def filtrar_por_categoria(recetas, categoria):
    """
    Filtra las recetas que pertenecen a la categoría indicada.

    Parámetros:
        recetas (list): lista de recetas.
        categoria (str): categoría a buscar.

    Retorna:
        list: recetas de la categoría seleccionada.
    """

    if not recetas:
        return []

    if type(categoria) != str or categoria.strip() == "":
        return recetas

    lista_filtradas = []

    for receta in recetas:
        categoria_receta = str(receta.get("categoria", "")).lower()

        if categoria_receta == categoria.lower():
            lista_filtradas.append(receta)

    return lista_filtradas


def filtrar_recetas_por_pais(recetas, pais):
    if pais == "":
        return recetas

    recetas_filtradas = []

    for receta in recetas:
        if pais.lower() == receta["pais"].lower():
            recetas_filtradas.append(receta)

    return recetas_filtradas


# Acá dejé una sola variable para el porcentaje:
# receta["porcentaje"]

# No uses a veces "porcentaje" y a veces "porcentaje_coincidencia", porque después se rompe.


def extraer_ingredientes(receta_completa):
    """
    Revisa las 20 posibles claves en las que puede haber un ingrediente
    (por ejemplo: strIngredient1, strIngredient2, ..., etc) y devuelve
    una lista con los valores que no estaban vacíos. Es decir hasta 20 ingredientes.
    """
    ingredientes = []

    for i in range(1, 21):
        if f"strIngredient{i}" in receta_completa and receta_completa[f"strIngredient{i}"] != "":
            ingredientes.append(receta_completa[f"strIngredient{i}"])

    return ingredientes


def procesar_json_recetas_api(recetas, ingredientes):
    """
    Convierte la lista de diccionarios que viene en el json de la api
    a una lista con los datos como los queremos nosotros (diccionario con otras claves y valores)
    """
    recetas_limpiadas = []

    for receta in recetas:

        receta_completa = obtener_detalle_receta(receta["idMeal"])

        ingredientes_receta = extraer_ingredientes(receta_completa)

        coincidencias = 0

        for ingrediente in ingredientes:
            if ingrediente in ingredientes_receta:
                coincidencias += 1

        porcentaje_coincidencias = coincidencias / len(ingredientes)

        detalle = {
            "nombre": receta_completa["strMeal"],
            "id": receta_completa["idMeal"],
            "categoria": receta_completa["strCategory"],
            "pais": receta_completa["strCountry"],
            "ingredientes_receta": ingredientes_receta,
            "coincidencias": coincidencias,
            "porcentaje": porcentaje_coincidencias,
            "instrucciones": receta_completa["strInstructions"]
        }

        recetas_limpiadas.append(detalle)

    return recetas_limpiadas
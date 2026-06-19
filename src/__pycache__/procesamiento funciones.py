#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:04:38 2026

@author: juanalolamuruzeta
"""

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

Acá dejé una sola variable para el porcentaje:
receta["porcentaje"]

No uses a veces "porcentaje" y a veces "porcentaje_coincidencia", porque después se rompe.
# %%

# %%


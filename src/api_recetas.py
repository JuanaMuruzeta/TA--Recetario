#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:44:37 2026

@author: delfinafernandezcovaro
"""

# src/api_recetas.py

import requests


URL_BASE = "https://www.themealdb.com/api/json/v1/1"


def consultar_api(endpoint, parametros):
    """
    Realiza una consulta a la API TheMealDB.

    Parámetros:
        endpoint (str): sección de la API que se quiere consultar.
        parametros (dict): datos necesarios para realizar la búsqueda.

    Retorna:
        dict: información obtenida de la API.
    """

    try:
        respuesta = requests.get(URL_BASE + "/" + endpoint, params=parametros)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos

        else:
            print("Error: la API no respondió correctamente.")
            return None

    except:
        print("Error: no se pudo conectar con la API.")
        return None



def buscar_recetas_por_ingrediente(ingrediente):
    """
    Busca recetas en TheMealDB usando un ingrediente principal.

    Parámetro:
        ingrediente (str): ingrediente ingresado por el usuario.

    Retorna:
        list: lista de recetas encontradas.
    """

    if ingrediente == "":
        print("Error: debe ingresar un ingrediente.")
        return []

    datos = consultar_api("filter.php", {"i": ingrediente})

    if datos == None:
        return []

    if datos["meals"] == None:
        return []

    return datos["meals"]



def obtener_detalle_receta(id_receta):
    """
    Obtiene la información completa de una receta utilizando su ID.

    Parámetro:
        id_receta (str): identificador de la receta seleccionada.

    Retorna:
        dict: detalle completo de la receta.
    """

    if id_receta == "":
        print("Error: debe ingresar un ID de receta.")
        return None

    datos = consultar_api("lookup.php", {"i": id_receta})

    if datos == None:
        return None

    if datos["meals"] == None:
        return None

    return datos["meals"][0]



def buscar_recetas_por_pais(pais):
    """
    Busca recetas en TheMealDB según el país seleccionado.

    Parámetro:
        pais (str): país elegido para filtrar las recetas.

    Retorna:
        list: lista de recetas del país indicado.
    """

    if pais == "":
        print("Error: debe ingresar un país.")
        return []

    datos = consultar_api("filter.php", {"a": pais})

    if datos == None:
        return []

    if datos["meals"] == None:
        return []

    return datos["meals"]



def obtener_ingredientes_receta(detalle_receta):
    """
    Obtiene todos los ingredientes de una receta.

    Parámetro:
        detalle_receta (dict): información completa de una receta.

    Retorna:
        list: lista con los ingredientes de la receta.
    """

    ingredientes = []

    if detalle_receta == None:
        return ingredientes

    for numero in range(1, 21):

        nombre = "strIngredient" + str(numero)

        ingrediente = detalle_receta[nombre]

        if ingrediente != None and ingrediente.strip() != "":
            ingredientes.append(ingrediente.strip().lower())

    return ingredientes
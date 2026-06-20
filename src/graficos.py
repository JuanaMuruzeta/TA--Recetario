#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:13:25 2026

@author: giuliamaniotti
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from src.historial import leer_historial


def crear_carpeta_graficos():
    """
    Crea la carpeta graficos si no existe.

    Retorna:
    None
    """

    if not os.path.exists("graficos"):
        os.makedirs("graficos")


def grafico_ingredientes_por_categoria():
    """
    Genera un gráfico de barras con los ingredientes más buscados,
    agrupados por categoría.

    Retorna:
    None
    """

    crear_carpeta_graficos()
    historial = leer_historial()

    if historial is None or historial.empty:
        print("No hay historial para generar este gráfico.")
        return None

    if "ingredientes" not in historial.columns or "categoria" not in historial.columns:
        print("Faltan columnas necesarias: ingredientes o categoria.")
        return None

    datos = []

    for i in range(len(historial)):
        ingredientes = str(historial.loc[i, "ingredientes"]).split(",")
        categoria = str(historial.loc[i, "categoria"])

        for ingrediente in ingredientes:
            ingrediente_limpio = ingrediente.strip().lower()

            if ingrediente_limpio != "" and categoria != "Sin datos":
                datos.append({
                    "ingrediente": ingrediente_limpio,
                    "categoria": categoria
                })

    if len(datos) == 0:
        print("No hay datos suficientes para graficar ingredientes por categoría.")
        return None

    df = pd.DataFrame(datos)
    resumen = df.groupby(["categoria", "ingrediente"]).size().reset_index(name="cantidad")
    resumen = resumen.sort_values("cantidad", ascending=False).head(10)

    etiquetas = resumen["categoria"] + " - " + resumen["ingrediente"]

    plt.figure(figsize=(10, 6))
    plt.bar(etiquetas, resumen["cantidad"])
    plt.title("Ingredientes más buscados agrupados por categoría")
    plt.xlabel("Categoría e ingrediente")
    plt.ylabel("Cantidad de búsquedas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/grafico_ingredientes_por_categoria.png")
    plt.show()
    plt.close()

    print("Gráfico guardado: graficos/grafico_ingredientes_por_categoria.png")

    return None


def grafico_paises_mas_solicitados():
    """
    Genera un gráfico de barras con los países más solicitados según el historial.

    Retorna:
    None
    """

    crear_carpeta_graficos()
    historial = leer_historial()

    if historial is None or historial.empty:
        print("No hay historial para generar este gráfico.")
        return None

    if "pais" not in historial.columns:
        print("Falta la columna pais en el historial.")
        return None

    paises = historial["pais"]
    paises = paises[paises != "Sin datos"]

    if len(paises) == 0:
        print("No hay países registrados para graficar.")
        return None

    conteo = paises.value_counts().head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(conteo.index, conteo.values)
    plt.title("Países más solicitados")
    plt.xlabel("País o región")
    plt.ylabel("Cantidad de apariciones")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/grafico_paises_mas_solicitados.png")
    plt.show()
    plt.close()

    print("Gráfico guardado: graficos/grafico_paises_mas_solicitados.png")

    return None


def grafico_mejor_porcentaje_por_busqueda():
    """
    Genera un gráfico de barras con el mejor porcentaje de coincidencia
    obtenido en cada búsqueda.

    Retorna:
    None
    """

    crear_carpeta_graficos()
    historial = leer_historial()

    if historial is None or historial.empty:
        print("No hay historial para generar este gráfico.")
        return None

    if "ingredientes" not in historial.columns or "mejor_porcentaje" not in historial.columns:
        print("Faltan columnas necesarias: ingredientes o mejor_porcentaje.")
        return None

    ultimas_busquedas = historial.tail(10)

    plt.figure(figsize=(10, 6))
    plt.bar(ultimas_busquedas["ingredientes"], ultimas_busquedas["mejor_porcentaje"])
    plt.title("Mejor porcentaje de coincidencia por búsqueda")
    plt.xlabel("Ingredientes buscados")
    plt.ylabel("Mejor porcentaje de coincidencia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/grafico_mejor_porcentaje_por_busqueda.png")
    plt.show()
    plt.close()

    print("Gráfico guardado: graficos/grafico_mejor_porcentaje_por_busqueda.png")

    return None


def grafico_top_10_paises_base_datos(recetas):
    """
    Genera un gráfico con los 10 países o regiones con más recetas
    dentro de la lista de recetas procesadas.

    Parámetros:
    recetas : list
        Lista de diccionarios de recetas.

    Retorna:
    None
    """

    crear_carpeta_graficos()

    if recetas is None or len(recetas) == 0:
        print("No hay recetas para generar este gráfico.")
        return None

    paises = []

    for receta in recetas:
        pais = receta.get("pais", "Sin datos")

        if pais != "Sin datos" and pais is not None:
            paises.append(pais)

    if len(paises) == 0:
        print("No hay países disponibles en las recetas.")
        return None

    conteo = pd.Series(paises).value_counts().head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(conteo.index, conteo.values)
    plt.title("Top 10 países o regiones con más recetas")
    plt.xlabel("País o región")
    plt.ylabel("Cantidad de recetas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/grafico_top_10_paises_base_datos.png")
    plt.show()
    plt.close()

    print("Gráfico guardado: graficos/grafico_top_10_paises_base_datos.png")

    return None


def grafico_cantidad_recetas_por_pais(recetas):
    """
    Genera un gráfico de barras con la cantidad de recetas por país
    dentro de una lista de recetas procesadas.

    Parámetros:
    recetas : list
        Lista de diccionarios de recetas.

    Retorna:
    None
    """

    crear_carpeta_graficos()

    if recetas is None or len(recetas) == 0:
        print("No hay recetas para generar este gráfico.")
        return None

    paises = []

    for receta in recetas:
        pais = receta.get("pais", "Sin datos")

        if pais != "Sin datos" and pais is not None:
            paises.append(pais)

    if len(paises) == 0:
        print("No hay países disponibles para graficar.")
        return None

    conteo = pd.Series(paises).value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(conteo.index, conteo.values)
    plt.title("Cantidad de recetas por país")
    plt.xlabel("País o región")
    plt.ylabel("Cantidad de recetas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/grafico_cantidad_recetas_por_pais.png")
    plt.show()
    plt.close()

    print("Gráfico guardado: graficos/grafico_cantidad_recetas_por_pais.png")

    return None


def generar_grafico_historial():
    """
    Genera todos los gráficos que se pueden hacer usando el historial.

    Retorna:
    None
    """

    grafico_ingredientes_por_categoria()
    grafico_paises_mas_solicitados()
    grafico_mejor_porcentaje_por_busqueda()

    print("Gráficos del historial generados correctamente.")

    return None


def menu_graficos():
    """
    Muestra un menú para que el usuario elija qué gráfico quiere ver.

    Retorna:
    None
    """

    salir = False

    while salir == False:
        print()
        print("MENÚ DE GRÁFICOS")
        print("1. Ingredientes más buscados por categoría")
        print("2. Países más solicitados")
        print("3. Mejor porcentaje por búsqueda")
        print("4. Generar todos los gráficos del historial")
        print("0. Volver al menú principal")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            grafico_ingredientes_por_categoria()

        elif opcion == "2":
            grafico_paises_mas_solicitados()

        elif opcion == "3":
            grafico_mejor_porcentaje_por_busqueda()

        elif opcion == "4":
            generar_grafico_historial()

        elif opcion == "0":
            salir = True

        else:
            print("Opción inválida. Ingrese un número válido.")

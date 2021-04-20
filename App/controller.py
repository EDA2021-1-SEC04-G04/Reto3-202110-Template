"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init(tipo: int, factor:float):
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalogo = model.NewCatalog()
    return catalogo

def loadData(catalogo, tipolista):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    list_type = def_type_list(typ)
    loadPistas(catalogo)
    loadEventos(catalogo)
    loadSvalues(catalogo)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    tupla = (delta_time, delta_memory)
    return tupla
    
# Funciones para la carga de datos

def loadPistas(catalogo):
    pistafile = cf.data_dir + 'context_content_features-50pct.csv'
    input_file = csv.DictReader(open(pistafile, encoding='utf-8'),delimiter = ',')
    for category in input_file:
        model.addPista(catalogo, category)
    return catalog

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

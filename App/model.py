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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf
import datetime
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def NewCatalog(tipo:str, factor:float):
    catalog = {'Pistas' :None,
               'Eventos' : None,
                'Artistas' : None,
                'Registros_Eventos' : None,
                'Svalues' : None
                }
    catalog['Pistas'] = mp.newMap(1100000, maptype = tipo, loadfactor= factor)
    catalog['Eventos'] = mp.newMap(maptype= tipo, loadfactor= factor)
    catalog['Artistas'] = lt.newList()
    catalog['Svalues'] = mp.newMap(5500, maptype = tipo, loadfactor= factor)
    catalog['Registros_Eventos'] = lt.newList(datastructure= 'ARRAY_LIST')
    
    
    
    
    
    
    
    
    
    return catalog

# Funciones para agregar informacion al catalogo

def addPista(catalogo, pista):
    key = pista['track_id']
    x = mp.get(catalogo['Pistas'], key)
    if x is None:
        pista['reproducciones'] = 0
        pista['eventos'] = lt.newList()
        mp.put(catalogo['Pistas'], key, pista)
        addArtista(catalogo, key, pista['artist_id'])
        
    else:
        y = me.getValue(x)
        y['reproducciones'] += 1
        lt.addLast(y['eventos'],pista['id'])

def addEvento(catalogo,evento):
    mp.put(catalogo['Eventos'], evento['id'], evento)
    

def addSvalue(catalogo, svalue):
    key = svalue['hashtag']
    mp.put(catalogo['Svalues'], key,svalue
           )
    
def addArtista(catalogo, pista, artista):
    if str(artista) not in catalogo['Artistas']:
        lt.addLast(catalogo['Artistas'], artista)
    
def addRegistro(catalogo, registro):
    lt.addLast(catalogo['Registros_Eventos'], registro)
# Funciones para creacion de datos

def Arbolde(Pistas, criterio):
    arbol = om.newMap(omaptype=RBT)
    for song in Pistas:
        x = om.get(arbol,song[criterio])
        if x is None:
            p = lt.newList()
            lt.addLast(p,song)
            om.put(arbol, song[criterio],p)
        else:
            lt.addLast(om.getValue(x),song)


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compare(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareHashtags(h1, h2):
    hasthgas = me.getKey(h2)
    if (h1 == hasthgas):
        return 0
    elif (h1 > hasthgas):
        return 1
    else:
        return -1
    


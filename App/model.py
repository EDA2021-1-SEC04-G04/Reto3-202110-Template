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
                'Svalues' : None
                }
    catalog['Pistas'] = mp.newMap(1100000, maptype = tipo, loadfactor= factor)
    catalog['Eventos'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    catalog['Artistas'] = lt.newList()
    catalog['Svalues'] = mp.newMap(5500, maptype = tipo, loadfactor= factor)
    
    
    
    
    
    
    
    
    
    
    return catalog

# Funciones para agregar informacion al catalogo

def addPista(catalogo, pista):
    key = pista['track_id']
    if mp.contains(catalogo['Pistas'], key):
        track = mp.get(catalogo['Pistas'], key)
        lt.addLast(track['value'],pista)
    else:
        l = lt.newList('ARRAY_LIST')
        lt.addLast(l,pista)
        mp.put(catalogo['Pistas'], key,l)
        track = mp.get(catalogo['Pistas'], key)

def addEvento(map,evento):
    fecha = evento['created_at']
    fechaevento = datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fechaevento.date())
    if entry is None:
        datentry = newDataEntry(evento)
        om.put(map, fechaevento.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addIndiceFecha(datentry, evento)
    return map

def addIndiceFecha(entrada, evento):
    lst = entrada['lsteventos']
    lt.addLast(lst, evento)
    HashtagIndex = entrada['HashtagIndex']
    offentry = mp.get(HashtagIndex, evento['hashtag'])
    if (offentry is None):
        entry = newOffenseEntry(evento['hashtag'], evento)
        lt.addLast(entry['lsteventos'], evento)
        mp.put(HashtagIndex, evento['hashtag'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lsteventos'], evento)
    return entrada

def newDataEntry(evento):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'HashtagIndex': None, 'lsteventos': None}
    entry['HashtagIndex'] = mp.newMap(numelements=30,
                                     maptype='CHAINING',
                                     comparefunction= compareHashtags
                                     )
    entry['lsteventos'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def newOffenseEntry(hashtag, evento):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'hashtag': None, 'lsteventos': None}
    ofentry['hashtag'] = hashtag
    ofentry['lsteventos'] = lt.newList('SINGLELINKED', compareHashtags)
    return ofentry


def addSvalue(catalogo, svalue):
    key = svalue['hashtag']
    mp.put(catalogo['Svalues'], key,svalue
           )
    
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareDates(date1, date2):
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
    


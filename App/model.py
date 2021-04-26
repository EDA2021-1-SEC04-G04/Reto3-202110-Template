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
                'Registros': None,
                'Svalues' : None,
                'Content' : None
                }
    catalog['Pistas'] = mp.newMap(1100000, maptype = tipo, loadfactor= factor)
    catalog['Eventos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['Artistas'] = lt.newList()
    catalog['Registros_Eventos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['Svalues'] = mp.newMap(5500, maptype = tipo, loadfactor= factor)
    catalog['Content'] = mp.newMap(15,maptype=tipo,loadfactor=factor) 

    return catalog

# Funciones para agregar informacion al catalogo

def addPista(catalogo, pista):
    track_id = pista['track_id']
    track = mp.get(catalogo['Pistas'], track_id)
    if track is None:
        pista['reproducciones'] = 0
        pista['eventos'] = lt.newList()
        mp.put(catalogo['Pistas'], track_id, pista)
        addArtista(catalogo, pista['artist_id'])
        
    else:
        pista = me.getValue(track)
        pista['reproducciones'] += 1
        lt.addLast(pista['eventos'],pista['id'])

def addEvento(catalogo,evento):
    lt.addLast(catalogo['Eventos'],evento)
    

def addSvalue(catalogo, svalue):
    key = svalue['hashtag']
    mp.put(catalogo['Svalues'], key,svalue
           )
    
def addArtista(catalogo, artista):
    if str(artista) not in catalogo['Artistas']:
        lt.addLast(catalogo['Artistas'], artista)
    
def addRegistro(catalogo, registro):
    lt.addLast(catalogo['Registros_Eventos'], registro)

def addContent(catalogo):
    contenido = catalogo['Content']
    mp.put(contenido,'instrumentalness',None)
    mp.put(contenido,'liveness',None)
    mp.put(contenido,'speechiness',None)
    mp.put(contenido,'danceability',None)
    mp.put(contenido,'valence',None)
    mp.put(contenido,'loudness',None)
    mp.put(contenido,'tempo',None)
    mp.put(contenido,'acousticness',None)
    mp.put(contenido,'energy',None)
    mp.put(contenido,'mode',None)
    mp.put(contenido,'key',None)

# Funciones para creacion de datos

def Arbolde(catalog,Pistas,criterio):
    content = catalog['Content']
    characteristic = mp.get(content,criterio)
    arbol = me.getValue(characteristic)
    if arbol is None:
        arbol = om.newMap(omaptype='RBT',comparefunction=compareValue)
        keyset= mp.keySet(Pistas)
        for num in range(0,lt.size(keyset)):
            llave = lt.getElement(keyset,num)
            pair = mp.get(Pistas,llave)
            if pair != None:
                cancion = me.getValue(pair)
                val_crit = float(cancion[criterio])
                entry = om.get(arbol,val_crit)
                if entry is None:
                    songs = lt.newList()
                    lt.addLast(songs,cancion)
                    om.put(arbol, val_crit,songs)
                else:
                    lt.addLast(me.getValue(entry),cancion)
        mp.put(content,criterio,arbol)
    return arbol

'''            
def arbolDeArbol(arbol,criterio, min,max):
    arbol_derivado = om.newMap(omaptype='RBT',comparefunction=compareValue)
    for songs in lt.iterator(arbol):
        for num in range(0,lt.size(songs)):
            song = lt.getElement(arbol,num)
            print(song)
            val_crit = float(song[criterio])
            entry = om.get(arbol_derivado,val_crit)
            if entry is None:
                songs = lt.newList()
                lt.addLast(songs,song)
                om.put(arbol, val_crit,songs)
            else:
                lt.addLast(me.getValue(entry),song)
    return arbol_derivado
'''
def filtradoenlista(lista,criterio,min,max):
    pistas = lt.newList(datastructure='ARRAY_LIST')
    reproducciones = 0
    artistas = mp.newMap(maptype='PROBING', loadfactor=0.5)
    for y in arbol:
        for x in range(0,lt.size(y)):
            pista = lt.getElement(y,x)
            if (float(pista[criterio]) >= min) and (float(pista[criterio]) <= min):
                lt.addLast(pistas,pista)
                reproducciones += pista['reproducciones']
                if mp.contains(artistas,pista['artist_id']) == False:
                    mp.put(artistas,pista['artist_id'])
                    
                
    return pistas, reproducciones, artistas
    

# Funciones de consulta

def songsByValues(arbol,val_min,val_max):
    lst = om.values(arbol, val_min, val_max)
    totplays = 0
    artists = lt.newList()
    totartists = 0
    uni_tracks = lt.newList()
    totsongs = 0
    for songs in lt.iterator(lst):
        for num in range(0,lt.size(songs)):
            song = lt.getElement(songs,num)
            if lt.isPresent(artists,song['artist_id'])!=0:
                totartists +=1
                lt.addLast(artists,song['artist_id'])

            totplays += song['reproducciones']

            if lt.isPresent(uni_tracks,song['track_id'])!=0:
                totsongs +=1
                lt.addLast(uni_tracks,song['track_id'])

    return totplays,totartists,totsongs,lst

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareValue(value1, value2):
    """
    Compara dos fechas
    """
    if (value1 == value2):
        return 0
    elif (value1 > value2):
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
    


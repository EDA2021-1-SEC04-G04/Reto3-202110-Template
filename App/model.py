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
                'Content' : None,
                'Generos' : None
                }
    catalog['Pistas'] = mp.newMap(1100000, maptype = tipo, loadfactor= factor)
    catalog['Eventos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['Artistas'] = lt.newList()
    catalog['Registros_Eventos'] = om.newMap(omaptype='RBT')
    catalog['Svalues'] = mp.newMap(5500, maptype = tipo, loadfactor= factor)
    catalog['Content'] = mp.newMap(15,maptype=tipo,loadfactor=factor)
    catalog['Generos'] = mp.newMap(30, maptype=tipo, loadfactor=factor) 

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
    hora = registro['created_at']
    hora_registro = datetime.datetime.strptime(hora, '%Y-%m-%d %H:%M:%S')
    entrada = om.get(catalogo['Registros_Eventos'], hora_registro.time())
    if entrada is None:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, registro)
        om.put(catalogo['Registros_Eventos'], hora_registro.time(), lista)
    else:
        l = me.getValue(entrada)
        lt.addLast(l,registro)

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
    
def addGenerosniciales(catalogo):
    re,re1,dt,dt1,co,co1,hp,hp1,jf,jf1,pp,pp1,rb,rb1,r,r1,mt,mt1 = ("reggae",(60.0,90.0), "down-tempo", (70.0,100.0), "chill-out", (90.0,120.0), \
        "hip-hop",(85.0,115.0),"jazz and funk",(120.0,125.0),"pop",(100.0,130.0),"r&b",(60.0,80.0),"rock",(110.0,140.0),"metal",(100.0,160.0))
    mp.put(catalogo['Generos'],re,re1)
    mp.put(catalogo['Generos'],dt,dt1)
    mp.put(catalogo['Generos'],co,co1)
    mp.put(catalogo['Generos'],hp,hp1)
    mp.put(catalogo['Generos'],jf,jf1)
    mp.put(catalogo['Generos'],pp,pp1)
    mp.put(catalogo['Generos'],rb,rb1)
    mp.put(catalogo['Generos'],r,r1)
    mp.put(catalogo['Generos'],mt,mt1)

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
def filtradoenlista(lista,criterio,min_,max_):
    pistas = lt.newList(datastructure='ARRAY_LIST')
    reproducciones = 0
    artistas = mp.newMap(maptype='PROBING', loadfactor=0.5)
    for tadlistas in lt.iterator(lista):
        for pos in range(0,lt.size(tadlistas)):
            pista = lt.getElement(tadlistas,pos)
            if (float(pista[criterio]) >= min_) and (float(pista[criterio]) <= max_):
                lt.addLast(pistas,pista)
                reproducciones += pista['reproducciones']
                if mp.contains(artistas,pista['artist_id']) == False:
                    mp.put(artistas,pista['artist_id'], None)
                    
                
    return pistas, reproducciones, artistas
    
    
# Funciones de consulta

def songsByValues(arbol,val_min,val_max):
    lst = om.values(arbol, val_min, val_max)
    totplays = 0
    artists = lt.newList()
    totartists = 0
    totsongs = 0
    lista = lt.newList()
    for songs in lt.iterator(lst):
        for num in range(0,lt.size(songs)):
            song = lt.getElement(songs,num)
            lt.addLast(lista,song)
            totplays += lt.size(song['eventos']) +1
            totsongs += 1
            if lt.isPresent(artists,song['artist_id'])==False:
                totartists +=1
                lt.addLast(artists,song['artist_id'])
    return totplays,totartists,totsongs,lista

# Funciones utilizadas para comparar elementos dentro de una lista

def separarpistas(catalogo,lista):
    canciones = mp.newMap(maptype='PROBING', loadfactor=0.5)
    for recorrido in lt.iterator(lista):
        for num in range(0,lt.size(recorrido)):
            registro = lt.getElement(recorrido, num)
            if mp.contains(canciones, registro['track_id']) == False:
                pista = mp.get(catalog['Pistas'],registro['track_id'])
                pista = me.getValue(pista).copy()
                pista['hashtags'] = lt.newList(datastructure='ARRAY_LIST')
                lt.addLast(pista['hastags'],registro['hashtag'])
                mp.put(canciones,registro['track_id'], pista)
            else:
                pista = mp.get(canciones,registro['track_id'])
                pista = me.getValue(pista)
                lt.addLast(pista['hashtags'],registro['hashtag'])
    return canciones

def recorridogeneros(catalogo, pistas):
    generos = mp.keySet(catalogo['Generos'])
    contadores = mp.newMap(maptype='PROBING', loadfactor=0.5)
    print(mp.keySet(pistas))
    for genero in generos:
        listacanciones = lt.newList(datastructure='ARRAY_LIST')
        mp.put(contadores, genero, [0,listacanciones])
    for llave in mp.keySet(pistas):
        entrada = mp.get(pistas,llave)
        pista = me.getValue(entrada)
        for genero in generos:
            valores = mp.get(catalogo['Generos'], genero)
            valores = me.getValue(valores)
            if pista['tempo'] >= valores[0] and pista['tempo'] <= valores[1]:
                añadir = mp.get(contadores, genero)
                añadir = me.getValue(añadir)
                añadir[0] += pista['reproducciones']
    return contadores

def cancionestop(pistas, catalogo):
    cantidad = 0
    for pista in lt.iterator(pistas):
        pista['VaderProm'] = float
        
        for hashtag in lt.iterator(pista['hashtags']):
            valorvalues = mp.get(catalog['Svalues'], hashtag)
            valorvalues = me.getValue(valorvalues)
            if valoravalues['vader_avg'] is not None:
                pista['VaderProm'] += valoravalues['vader_avg']
            cantidad += 1
    pista['VaderProm'] = pista['VaderProm']/cantidad
    return pistas      

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
    

def comparargeneros(g1,g2):
    gen1 = g1[0]
    gen2 = g2[0]
    if (gen1 == gen2):
        return 0
    elif (gen1 > gen2):
        return 1
    elif (gen1 < gen2):
        return -1
"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import random

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Caracterizar las reproducciones")
    print("3- Encontrar música para festejar")
    print("4- Encontrar música para estudiar")
    print("5- Estudiar géneros musicales")
    print("6- Indicar género musical mas escuchado en un horario")
    print("0- Salir")

catalog = None

#Funciones de requerimiento

def req_1(catalog,criterio,val_min,val_max):
    pistas = catalog['Pistas']
    arbol = controller.ArbolDe(catalog,pistas,criterio)
    rep_art = controller.songsByValues(arbol,val_min,val_max)
    printReq1(rep_art,content,val_min,val_max)

def req_2(catalog,ene_min,ene_max,dan_min,dan_max):
    pistas = catalog['Pistas']
    arbol_ene = controller.ArbolDe(catalog,pistas,'energy')
    filtrado = controller.songsByValues(arbol_ene,ene_min,ene_max)[3]
    arbol_dan = controller.arbolDeArbol(filtrado,'danceability')
    rep = controller.songsByValues(arbol_dan,dan_min,dan_max)
    printReq2(rep[2],req)

#Funciones de impresión

def printReq1(rep_art,content,val_min,val_max):
    print('+'*10,' Resultados Req. #1...', '+'*10)
    linea = content + ' entre ' +str(val_min) +' y ' + str(val_max)
    respuesta = 'Reproducciones totales: ' + str(rep_art[0]) + ' Número de artistas únicos totales: ' + str(rep_art[1])
    print(linea)
    print(respuesta)

def print_events(catalog):
    eventos = catalog['Eventos']
    size = lt.size(eventos)
    if size:
        print('Estos son los primeros 5 eventos cargados')
        i = 0
        while i <5:
            print("-"*237)
            primera_linea = "{0:<2}{1:^20}{2:^20}{3:^20}{4:^20}{5:^20}{6:^20}{7:^20}{8:^20}{9:^20}{10:^20}\
                ".format(str(i+1)+('.'),'ID del evento','Instrumentalness','Liveness','Speechiness','Danceability','Valence','Loudness','Tempo','Acousticness','Energy')
            print(primera_linea)
            evento = lt.getElement(eventos,i)
            event_id = evento['id']
            inst = evento['instrumentalness']
            live = evento['liveness']
            spe = evento['speechiness']
            dance = evento['danceability']
            val = evento['valence']
            loud = evento['loudness']
            temp = evento['tempo']
            aco = evento['acousticness']
            ene = evento['energy']            
            info_video = "{0:<2}{1:^20}{2:^20}{3:^20}{4:^20}{5:^20}{6:^20}{7:^20}{8:^20}{9:^20}{10:^20}".format(' ',event_id,inst,live,spe,dance,val,loud,temp,aco,ene)
            print(info_video)

            segunda_linea = "{0:^20}{1:^20}{2:^10}{3:^25}{4:^40}{5:^40}\
                ".format('Mode','Key','Lenguaje','Lugar de creacion','Zona horaria','ID de la pista')
            print(segunda_linea)
            mode = evento['mode']
            key = evento['key']
            lang = evento['tweet_lang']
            cre_at = evento['created_at']
            time_zone = evento['time_zone']
            track_id = evento['track_id']            
            info2_video = "{0:^20}{1:^20}{2:^10}{3:^25}{4:^40}{5:^40}".format(mode,key,lang,cre_at,time_zone,track_id)
            print(info2_video)
            i+=1
        print('\nY estos son los últimos 5 eventos cargados\n')
        j=lt.size(catalog['Eventos'])
        while j > lt.size(catalog['Eventos'])-5:
            print("-"*237)
            primera_linea = "{0:<8}{1:^20}{2:^20}{3:^20}{4:^20}{5:^20}{6:^20}{7:^20}{8:^20}{9:^20}{10:^20}\
                ".format(str(j)+('.'),'ID del evento','Instrumentalness','Liveness','Speechiness','Danceability','Valence','Loudness','Tempo','Acousticness','Energy')
            print(primera_linea)
            evento = lt.getElement(eventos,j)
            event_id = evento['id']
            inst = evento['instrumentalness']
            live = evento['liveness']
            spe = evento['speechiness']
            dance = evento['danceability']
            val = evento['valence']
            loud = evento['loudness']
            temp = evento['tempo']
            aco = evento['acousticness']
            ene = evento['energy']            
            info_video = "{0:<8}{1:^20}{2:^20}{3:^20}{4:^20}{5:^20}{6:^20}{7:^20}{8:^20}{9:^20}{10:^20}".format(' ',event_id,inst,live,spe,dance,val,loud,temp,aco,ene)
            print(info_video)

            segunda_linea = "{0:^20}{1:^20}{2:^10}{3:^25}{4:^40}{5:^40}\
                ".format('Mode','Key','Lenguaje','Lugar de creacion','Zona horaria','ID de la pista')
            print(segunda_linea)
            mode = evento['mode']
            key = evento['key']
            lang = evento['tweet_lang']
            cre_at = evento['created_at']
            time_zone = evento['time_zone']
            track_id = evento['track_id']            
            info2_video = "{0:^20}{1:^20}{2:^10}{3:^25}{4:^40}{5:^40}".format(mode,key,lang,cre_at,time_zone,track_id)
            print(info2_video)
            j-=1
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        tipo = int(input("Ingrese 1 si desea manejar las colisiones con el método chaining o 2 para linear probing: "))
        load_factor = float(input("Ingrese el factor de carga con el que desea trabajar: "))
        #cambio medida tiempo y memoria
        catalog = controller.init(tipo,load_factor)
        answer = controller.loadData(catalog,tipo)
        print('El total de registros de eventos de escucha cargados es de: ' + str(lt.size(catalog['Eventos'])))
        print('El total de artistas únicos cargados es de: '+ str(lt.size(catalog['Artistas'])))
        print('El total de pistas de audio únicas cargadas es de: ' + str(mp.size(catalog['Pistas'])))
        print_events(catalog)
        print("Cargado correctamente")
    elif int(inputs[0]) == 2:
        content = input('Ingrese la característica sobre la que desea hacer la consulta: ')
        val_min = float(input("Ingrese el valor mínimo de esta característica: "))
        val_max = float(input("Ingrese el valor máximo de esta característica: "))
        req_1(catalog,content,val_min,val_max)
    elif int(inputs[0]) == 3:
        ene_min = float(input("Ingrese el valor mínimo de energía de la canción: "))
        ene_max = float(input("Ingrese el valor máximo de energía de la canción: "))
        dan_min = float(input("Ingrese el valor mínimo de danzabilidad de la canción: "))
        dan_max = float(input("Ingrese el valor máximo de danzabilidad de la canción: "))
        req_2(catalog,ene_min,ene_max,dan_min,dan_max)
    elif int(inputs[0]) == 0:
        sys.exit(0)
sys.exit(0)

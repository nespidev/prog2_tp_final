#TRABAJO INTEGRADOR FINAL
#PROGRAMACIÓN 2 - 2023 – 2do cuatrimestre
#TECNICATURA UNIVERSITARIA EN DESARROLLO WEB
#ALUMNO: Juan Nahuel Espinola Grativol

# librerias
import os
import json

# modelos
from modelos.artista import Artista
from modelos.actor import Actor
from modelos.director import Director
from modelos.genero import Genero
from modelos.pelicula import Pelicula


class Biblioteca:

    __archivoDeDatos = "biblioteca.json"
    __actores = []
    __directores = []
    __generos = []
    __peliculas = []

    #Comandos
    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    #Consultas
    def obtenerActores(orden=None, reverso=False):
        actores = Biblioteca.__actores
        if isinstance(orden, str):
            if orden == 'nombre':
                #Se ordena alfabeticamente por su nombre
                actores = sorted(actores, key=lambda actor: actor.obtenerNombre(), reverse=reverso)
            elif orden == 'colegas':
                #Se ordena por cantidad de colegas
                actores = sorted(actores, key=lambda actor: len(actor.obtenerColegas()), reverse=reverso)
            elif orden == 'peliculas':
                #Se ordena por cantidad de peliculas
                actores = sorted(actores, key=lambda actor: len(actor.obtenerPeliculas()), reverse=reverso)
        return actores

    def obtenerDirectores(orden=None, reverso=False):
        directores = Biblioteca.__directores
        if isinstance(orden, str):
            if orden == 'nombre':
                #Se ordena alfabeticamente por su nombre
                directores = sorted(directores, key=lambda director: director.obtenerNombre(), reverse=reverso)
            elif orden == 'peliculas':
                #Se ordena por cantidad de peliculas
                directores = sorted(directores, key=lambda director: director.obtenerPeliculas(), reverse=reverso)
        return directores

    def obtenerPeliculas(orden=None, reverso=False):
        peliculas = Biblioteca.__peliculas
        if isinstance(orden, str):
            if orden == 'nombre':
                #Se ordena alfabeticamente por su nombre
                peliculas = sorted(peliculas, key=lambda pelicula: pelicula.obtenerNombre(), reverse=reverso)
            elif orden == 'director':
                #Se ordena alfabeticamente por nombre de director
                peliculas = sorted(peliculas, key=lambda pelicula: pelicula.obtenerDirector(), reverse=reverso)
            elif orden == 'actores':
                #Se ordena alfabeticamente por cantidad de actores
                peliculas = sorted(peliculas, key=lambda pelicula: len(pelicula.obtenerActores()), reverse=reverso)
            elif orden == 'anio':
                #Se ordena por año de salida
                peliculas = sorted(peliculas, key=lambda pelicula: pelicula.obtenerAnio(), reverse=reverso)
        return peliculas

    def obtenerGeneros(orden=None, reverso=False):
        generos = Biblioteca.__generos
        if isinstance(orden, str):
            if orden == 'nombre':
                #Se ordena alfabeticamente por su nombre
                generos = sorted(generos, key=lambda genero: genero.obtenerNombre(), reverse=reverso)
        return generos

    def buscarActor(id):
        actores = Biblioteca.__actores
        for actor in actores:
            if actor.obtenerId() == id:
                return actor
        return None

    def buscarDirector(id):
        directores = Biblioteca.__directores
        for director in directores:
            if director.obtenerId() == id:
                return director
        return None

    def buscarGenero(id):
        generos = Biblioteca.__generos
        for genero in generos:
            if genero.obtenerId() == id:
                return genero
        return None

    def buscarPelicula(id):
        peliculas = Biblioteca.__peliculas
        for pelicula in peliculas:
            if pelicula.obtenerId() == id:
                return pelicula
        return None

    def __parsearArchivoDeDatos():
        archivo = open(Biblioteca.__archivoDeDatos, "r")
        datos = json.load(archivo)
        archivo.close()
        return datos

    def __convertirJsonAListas(lista):
        Biblioteca.__peliculas = []
        for pelicula in lista["peliculas"]:
            Biblioteca.__peliculas.append(Pelicula(**pelicula))

        Biblioteca.__generos = []
        for genero in lista["generos"]:
            Biblioteca.__generos.append(Genero(**genero))

        Biblioteca.__directores = []
        for director in lista["directores"]:
            Biblioteca.__directores.append(Director(**director))

        Biblioteca.__actores = []
        for actor in lista["actores"]:
            Biblioteca.__actores.append(Actor(**actor))

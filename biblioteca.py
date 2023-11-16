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

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    def obtenerActores(orden=None, reverso=False):
        actores = Biblioteca.__actores
        if isinstance(orden, str):
            if orden == 'nombre':
                actores = sorted(actores, key=lambda actor: actor.obtenerPeliculas(), reverse=reverso)
            elif orden == 'colegas':
                pass # completar
            elif orden == 'peliculas':
                pass # completar
        return actores

    def obtenerDirectores(orden=None, reverso=False):
        directores = Biblioteca.__directores
        # directores_ordenado = []
        if isinstance(orden, str):
            if orden == 'nombre':
                # nombres = []
                # for director in directores:
                #     nombres.append(director.obtenerNombre())
                # nombres.sort(reverse=reverso)
                # for nombre in nombres:
                #     for director in directores:
                #         if nombre == director.obtenerNombre():
                #             directores_ordenado.append(director)
                directores = sorted(directores, key=lambda director: director.obtenerNombre(), reverse=reverso)

            elif orden == 'peliculas':
                directores = sorted(directores, key=lambda director: director.obtenerPeliculas(), reverse=reverso)
        return directores

    def obtenerPeliculas(orden=None, reverso=False):
        peliculas = Biblioteca.__peliculas
        if isinstance(orden, str):
            if orden == 'nombre':
                peliculas = sorted(peliculas, key=lambda pelicula: pelicula.obtenerNombre(), reverse=reverso)
            elif orden == 'director':
                pass # completar
            elif orden == 'actores':
                pass # completar
            elif orden == 'anio':
                pass # completar
        return peliculas

    def obtenerGeneros(orden=None, reverso=False):
        generos = Biblioteca.__generos
        if isinstance(orden, str):
            if orden == 'nombre':
                pass # completar
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

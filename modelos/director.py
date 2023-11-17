#TRABAJO INTEGRADOR FINAL
#PROGRAMACIÓN 2 - 2023 – 2do cuatrimestre
#TECNICATURA UNIVERSITARIA EN DESARROLLO WEB
#ALUMNO: Juan Nahuel Espinola Grativol

import json
import biblioteca
from modelos.artista import Artista

class Director(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    #Consultas
    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            if self is pelicula.obtenerDirector():
                peliculas.append(pelicula)
        return peliculas
    
    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": len(self.obtenerGeneros()),
            "peliculas": len(self.obtenerPeliculas()),
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
        }
    
    def __eq__(self, otro):
        return self.obtenerId() == otro.obtenerId()

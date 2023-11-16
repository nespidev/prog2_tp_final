import json
import biblioteca
from modelos.artista import Artista

class Director(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

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
    
    def __eq__(self, director):
        # if isinstance(otro, Director):
            return self.obtenerId() == director.obtenerId()
        # else:
        #     print ('director equals',otro)
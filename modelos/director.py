import json
import biblioteca
from modelos.artista import Artista

class Director(Artista):

    def __init__(self, id, nom):
        super().__init__(id,nom)

    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            if self in pelicula.obtenerDirectores():
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
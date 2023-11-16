import json
import biblioteca
from modelos.artista import Artista

class Actor(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)
    
    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            for actor in pelicula.obtenerActores():
                if self is actor:
                    peliculas.append(pelicula)
        return peliculas
        
    def obtenerColegas(self):
        colegas = []
        peliculas = biblioteca.Biblioteca.obtenerPeliculas()  
        for pelicula in peliculas:
            actores = pelicula.obtenerActores()
            for actor in actores:
                if actor not in colegas and actor is not self:
                    colegas.append(actor)
        return colegas

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": len(self.obtenerPeliculas()),
            "colegas": len(self.obtenerColegas())
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
            "colegas": self.__mapearColegas()
        }
    
    def __mapearColegas(self):
        colegas = self.obtenerColegas()
        colegasMapa = map(lambda a: a.obtenerNombre(), colegas)
        return list(colegasMapa)
    
    def __eq__(self, otro):
        return self.obtenerId() == otro.obtenerId()

import json
import biblioteca
from modelos.artista import Artista

class Actor(Artista):

    def __init__(self, id, nom):
        super().__init__(id, nom)
    
    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            if self in pelicula.obtenerActores():
                peliculas.append(pelicula)
            return peliculas
        
    def obtenerColegas(self):
        colegas = set()

        for pelicula in self.obtenerPeliculas():
            colegas.update(pelicula.obtenerActores())
        colegas.remove(self)  # Eliminar actual actor de la lista de colegas
        return list(colegas)

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

import json
import biblioteca

class Pelicula:
    def __init__(self, id, nom, gen, dir, actrs, anio):
        self.__id = id
        self.__nombre = nom
        self.__genero = gen
        self.__director = dir
        self.__actores = actrs
        self.__anio = anio

    def establecerNombre(self, nom):
        self.__nombre = nom

    def establecerGenero(self, gen):
        self.__genero = gen

    def establecerDirector(self, dir):
        self.__director = dir
    
    def establecerActores(self, actrs):
        self.__actores = actrs

    def establecerAnio(self, anio):
        self.__anio = anio

    def obtenerId(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerGenero(self):
        return biblioteca.Biblioteca.buscarGenero(self.__genero)
    
    def obtenerDirector(self):
        return biblioteca.Biblioteca.buscarDirector(self.__director)
    
    def obtenerActores(self):
        
        return [biblioteca.Biblioteca.buscarActores(actor) for actor in self.__actores]
    
    def obtenerAnio(self):
        return self.anio
    
        
    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "director": self.obtenerDirector().obtenerNombre(),
            "actores": len(self.obtenerActores()),
            "anio": self.__anio
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "director": self.obtenerDirector().obtenerNombre(),
            "actores": self.__mapearActores(),
            "anio": self.__anio
        }
    
    def __mapearActores(self):
        actores = self.obtenerActores()
        actoresMapa = map(lambda a: a.obtenerNombre(), actores)
        return list(actoresMapa)
    
    def __eq__(self, otro):
        self.__id == otro.obtenerId()
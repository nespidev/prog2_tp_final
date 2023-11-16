import json
import biblioteca

class Pelicula:
    def __init__(self, id, nombre, genero, director, actores, anio):
        self.__id = id
        self.__nombre = nombre
        self.__genero = genero
        self.__director = director
        self.__actores = actores
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
        # actores = []
        # for actor in biblioteca.Biblioteca.obtenerActores():
        #     for elemento in self.__actores:
        #         if elemento['id'] == actor.obtenerId():
        #             actores.append(actor)
        # return actores
        devolverActores = []
        todosLosActores = biblioteca.Biblioteca.obtenerActores()

        for actorEnTodos in todosLosActores:
            for actorEnPeli in self.__actores:
                if actorEnPeli['id'] == actorEnTodos.obtenerId():
                    devolverActores.append(actorEnTodos)
        return devolverActores
    
    def obtenerAnio(self):
        return self.__anio
    
        
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
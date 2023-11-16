import json


class Genero:

    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    def establecerNombre(self, nombre):
        self.__nombre = nombre
    
    def obtenerId(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre()
        }

    def __eq__(self, otro):
        return self.__id == otro.obtenerId()
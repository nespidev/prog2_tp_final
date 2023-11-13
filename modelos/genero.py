import json


class Genero:

    def __init__(self, id, nom):
        self.__id = id
        self.__nombre = nom

    def establecerNombre(self, nom):
        self.__nombre = nom

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
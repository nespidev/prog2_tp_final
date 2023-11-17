#TRABAJO INTEGRADOR FINAL
#PROGRAMACIÓN 2 - 2023 – 2do cuatrimestre
#TECNICATURA UNIVERSITARIA EN DESARROLLO WEB
#ALUMNO: Juan Nahuel Espinola Grativol

import json

class Genero:

    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    #Comandos
    def establecerNombre(self, nombre):
        self.__nombre = nombre
    
    #Consultas
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
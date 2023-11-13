class Artista:
    
    def __init__(self, id, nom):
        self.__id = id
        self.__nombre = nom

    #Comandos
    def establecerNombre(self, nom):
        self.__nombre = nom

    #Consultas
    def obtenerId(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre

    def obtenerGeneros(self):
        generos = set()
        for pelicula in self.obtenerPeliculas():
            if self in pelicula:
                generos.update(pelicula.obtenerGenero())
        return generos

    def _mapearGeneros(self):
        generos = self.obtenerGeneros()
        generosMapa = map(lambda g: g.obtenerNombre(), generos)
        return list(generosMapa)

    def _mapearPeliculas(self):
        peliculas = self.obtenerPeliculas()
        peliculasMapa = map(lambda p: {"nombre": p.obtenerNombre(), "anio": p.obtenerAnio()}, peliculas)
        return list(peliculasMapa)

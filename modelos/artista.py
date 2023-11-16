class Artista:
    
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    #Comandos
    def establecerNombre(self, nom):
        self.__nombre = nom

    #Consultas
    def obtenerId(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre

    def obtenerGeneros(self):
        generos = []
        peliculas = self.obtenerPeliculas()
        for pelicula in peliculas:
            director = pelicula.obtenerDirector()
            if self == director or self in pelicula.obtenerActores():
                genero = pelicula.obtenerGenero()
                if genero not in generos:
                    generos.append(genero)
        return generos

    def _mapearGeneros(self):
        generos = self.obtenerGeneros()
        generosMapa = map(lambda g: g.obtenerNombre(), generos)
        return list(generosMapa)

    def _mapearPeliculas(self):
        peliculas = self.obtenerPeliculas()
        peliculasMapa = map(lambda p: {"nombre": p.obtenerNombre(), "anio": p.obtenerAnio()}, peliculas)
        return list(peliculasMapa)

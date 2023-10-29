class Artista:
    
    def __init__(self, id, nom):
        self.id = id
        self.nombre = nom

    #Comandos
    def establecerNombre(self, nom):
        self.nombre = nom

    #Consultas
    def obtenerId(self):
        return self.id
    
    def obtenerNombre(self):
        return self.nombre

    def obtenerGeneros(self):
        generos = []
        for pelicula in self.obtenerPeliculas():
            generos.append(pelicula.obtenerGenero())
        generos = [generos[i] for i in range(len(generos)) if i == generos.index(generos[i]) ] # remueve generos duplicados
        return generos

    def _mapearGeneros(self):
        generos = self.obtenerGeneros()
        generosMapa = map(lambda g: g.obtenerNombre(), generos)
        return list(generosMapa)

    def _mapearPeliculas(self):
        peliculas = self.obtenerPeliculas()
        peliculasMapa = map(lambda p: {"nombre": p.obtenerNombre(), "anio": p.obtenerAnio()}, peliculas)
        return list(peliculasMapa)

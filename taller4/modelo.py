class Libro:
    def __init__(self, nombre: str, autor: str, anioPubl:str, editorial:str, cantPaginas:int):
        self.nombre = nombre
        self.autor = autor
        self.anioPubl = anioPubl
        self.editorial = editorial
        self.cantPaginas = cantPaginas
    
    def setNombre(self, nombre:str) -> None:
        self.nombre = nombre
    
    def setAutor(self, autor:str) -> None:
        self.autor = autor
    
    def setAnioPublicacion(self, anioPubl:str) -> None:
        self.anioPubl = anioPubl

    def setEditorial(self, editorial:str) -> None:
        self.editorial = editorial

    def setCantPaginas(self, cantPaginas: int) -> None:
        self.cantPaginas = cantPaginas

    def getNombre(self) -> str:
        return self.nombre

    def getAutor(self) -> str:
        return self.autor

    def getAnioPublicacion(self) -> str:
        return self.anioPubl

    def getEditorial(self) -> str:
        return self.editorial

    def getCantPaginas(self) -> int:
        return self.cantPaginas

class Casa:
    def __init__(self, direccion: str, estrato: int, color: str, cantPisos:int, cantHabitaciones: int):
        self.direccion = direccion
        self.estrato = estrato
        self.color = color
        self.cantPisos = cantPisos
        self.cantHabitaciones = cantHabitaciones
    
    def getDireccion(self) -> str:
        return self.direccion;

    def getEstrato(self):
        return self.estrato;
    
    def getColor(self):
        return self.color;

class Pelicula:
    def __init__(self, titulo: str, genero: str, sinopsis: str, duracion: int, cantActores: int):
        self.titulo = titulo
        self.genero = genero
        self.sinopsis = sinopsis
        self.duracion = duracion
        self.cantActores = cantActores
        
    def getTitulo(self):
        return self.titulo

    def getGenero(self):
        return self.genero

    def getDuracion(self):
        return self.duracion

libros = []
casas = []
peliculas = []
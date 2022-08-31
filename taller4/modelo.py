from datetime import date, datetime
import math

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

class Bodega:
    def __init__(self, nombre: str, direccion: str, espacio: int, tipoVenta:str, cantTrabajadores: int):
        self.nombre = nombre
        self.direccion = direccion
        self.espacio = espacio
        self.tipoVenta = tipoVenta
        self.cantTrabajadores = cantTrabajadores
    
    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion
    
    def getEspacio(self):
        return self.espacio
    
    def getTipoVenta(self):
        return self.tipoVenta

    def getCantTrabajadores(self):
        return self.cantTrabajadores

class Lampara:
    def __init__(self, marca: str, precio: int, ubicacion: str, colgante: str, moderna:str):
        self.marca = marca
        self.precio = precio
        self.ubicacion = ubicacion
        self.colgante = colgante
        self.moderna = moderna
    
    def getMarca(self):
        return self.marca

    def getPrecio(self):
        return self.precio
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getColgante(self):
        return self.colgante
    
    def getModerna(self):
        return self.moderna

#Ejercicio 2
class Rectangulo():
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    
    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura
    
    def getArea(self):
        return self.base * self.altura

    def getPerimetro(self):
        return 2 * (self.base * self.altura)

class Empleado():
    def __init__(self, nombre: str, genero: str, edad: int, fechaInicio: str, numHorasMes: int, valorHora: int):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.fechaInicio = fechaInicio
        self.numHorasMes = numHorasMes
        self.valorHora = valorHora
        
    def getNombre(self):
        return self.nombre
    
    def getGenero(self):
        return self.genero
    
    def getEdad(self):
        return self.edad
    
    def getFechaInicio(self):
        return self.fechaInicio
    
    def getNumHorasMes(self):
        return self.numHorasMes
    
    def getValorHora(self):
        return self.valorHora
    
    def getSalarioMensual(self):
        return self.numHorasMes * self.valorHora
    
    def getDiasAntiguedad(self):
        arrFecha = self.fechaInicio.split("/")
        
        fInicio = date(int(arrFecha[0]), int(arrFecha[1]), int(arrFecha[2]))
        fHoy = date(2022, 8, 31)
        return (fHoy - fInicio).days
    
    def getSemanasAntiguedad(self):
        return self.getDiasAntiguedad() // 7
    
    def getAniosAntiguedad(self):
        return int(self.getSemanasAntiguedad() * 0.0191781)
    
    def getAniosParaPensionPorEdad(self):
        if self.genero == "M":
            return 62 - self.edad
        else:
            return 57 - self.edad
    
    def getAniosParaPensionPorCotizacion(self):
        if self.getSemanasAntiguedad() < 1300:
            return int((1300 - self.getSemanasAntiguedad()) * 0.0191781)
        else:
            return 0
    
    def cantPagoSalud(self):
        return self.getSalarioMensual() * (4 / 100)

    def cantPagoPension(self):
        return self.getSalarioMensual() * (4 / 100)

class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
      
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 // self.num2
    
    def cuadrado(self):
        return math.pow(self.num1, 2)
    
    def exponente(self):
        return math.pow(self.num1, self.num2)
    
    def logaritmo(self):
        return math.log10(self.num1)
    
    def seno(self):
        return math.sin(self.num1)
    
    def coseno(self):
        return math.cos(self.num1)
    
    def tangente(self):
        return math.tan(self.num1)    
    
    def arc_tan(self):
        return math.atan(self.num1)
    
    def arc_coseno(self):
        return math.acos(self.num1)

class Asignatura:
    def __init__(self, nombre: str, nota1 :int, nota2 :int, nota3 :int, nota4:int):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def getNombre(self):
        return self.nombre
    
    def getNota1(self):
        return self.nota1
    
    def getNota2(self):
        return self.nota2
    
    def getNota3(self):
        return self.nota3
    
    def getNota4(self):
        return self.nota4
    
    def getPromedio(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
    
libros = []
casas = []
peliculas = []
bodegas = []
lamparas = []
asignaturas = []
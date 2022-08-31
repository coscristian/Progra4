from modelo import *

def mostrarPromedoGeneral(asignaturas: Asignatura) -> None:
    sumaPromedios = 0
    for asignatura in asignaturas:
        sumaPromedios += asignatura.getPromedio()

    promedioGeneral = sumaPromedios / 2
    print(f"Promedio general {promedioGeneral}")
    if promedioGeneral < 3:
        print("\tSemestre Pérdido")
    elif 3 <= promedioGeneral <= 4:
        print("\tBuen trabajo")
    elif 4 < promedioGeneral <= 5:
        print("\tFelicidades serás becado")
        
def mostrarAsignaturas(asignaturas: Asignatura) -> None:
    for asignatura in asignaturas:
        print(f"Asignatura {asignatura.getNombre()}")
        print(f"\tNota 1:  {asignatura.getNota1()}")
        print(f"\tNota 2:  {asignatura.getNota2()}")
        print(f"\tNota 3:  {asignatura.getNota3()}")
        print(f"\tNota 4:  {asignatura.getNota4()}")
        print(f"\t\tPromedio:  {asignatura.getPromedio()}")
        if (asignatura.getPromedio() < 3):
            print("\t\tAsignatura perdida")
        else:
            print("\t\tAsignatura ganada")

def mostrarMenuOperaciones() -> None:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. División")
    print("5. Cuadrado")
    print("6. Exponente")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tagente")
    print("11. ArcoTangente")
    print("12. ArcoCoseno")
    print("¿Qué opcion dese seleccionar?")
    
def mostrarEmpleado(empleado: Empleado) -> None:
    print(f"\tNombre:\t {empleado.getNombre()}")
    print(f"\tGénero:\t {empleado.getGenero()}")
    print(f"\tEdad:\t {empleado.getEdad()}")
    print(f"\tFechaIn:\t {empleado.getFechaInicio()}")
    print(f"\tNumHorasMes:\t {empleado.getNumHorasMes()}")
    print(f"\tValorHora:\t {empleado.getValorHora()}")
    print(f"\tAntiguedad:")
    print(f"\t\tAños:\t {empleado.getAniosAntiguedad()} años")
    print(f"\t\tDías:\t {empleado.getDiasAntiguedad()} días")
    print(f"\tTiempo para pensionarse por edad:\t {empleado.getAniosParaPensionPorEdad()} años")
    print(f"\tTiempo para pensionarse por cotización:\t {empleado.getAniosParaPensionPorCotizacion()} años")
    print(f"\tPago Salud al año:\t ${empleado.cantPagoSalud()}")
    print(f"\tPago pensión al año:\t ${empleado.cantPagoPension()}")

def mostrarRectangulo(rectangulo: Rectangulo) -> None:
    print(f"\tBas:\t {rectangulo.getBase()}")
    print(f"\tAlt:\t {rectangulo.getAltura()}")
    print(f"\tAr:\t\t {rectangulo.getArea()}")
    print(f"\tPerim:\t\t {rectangulo.getPerimetro()}")

def mostrarLamparas(lamparas: Lampara) -> None:
    cont = 1
    for lampara in lamparas:
        print(f"Lampara {cont}")
        print(f"\tMarca:\t {lampara.getMarca()}")
        print(f"\tPrecio:\t {lampara.getPrecio()}")
        print(f"\tUbicacion:\t {lampara.getUbicacion()}")
        print(f"\tColgante:\t {lampara.getColgante()}")
        print(f"\tModerna:\t {lampara.getModerna()}")
        cont += 1      

def mostrarBodegas(bodegas: Bodega) -> None:
    cont = 1
    for bodega in bodegas:
        print(f"Bodega {cont}")
        print(f"\tNombre:\t {bodega.getNombre()}")
        print(f"\tDirección:\t {bodega.getDireccion()}")
        print(f"\tEspacio:\t {bodega.getEspacio()}")
        print(f"\tTipo producto:\t {bodega.getTipoVenta()}")
        print(f"\tCant Trabjadores:\t {bodega.getCantTrabajadores()}")
        cont += 1             

def mostrarPeliculas(peliculas: Pelicula) -> None:
    cont = 1
    for pelicula in peliculas:
        print(f"Pelicula {cont}")
        print(f"\tTitulo:\t {pelicula.getTitulo()}")
        print(f"\tGénero:\t {pelicula.getGenero()}")
        print(f"\tDuración:\t {pelicula.getDuracion()}")
        cont += 1      

def mostrarCasas(casas: Casa) -> None:
    cont = 1
    for casa in casas:
        print(f"Casa {cont}")
        print(f"\tDirección:\t {casa.getDireccion()}")
        print(f"\tEstrato:\t {casa.getEstrato()}")
        print(f"\tColor:\t {casa.getColor()}")
        cont += 1    

def mostrarLibros(libros: Libro) -> None:
    cont = 1
    for libro in libros:
        print(f"Libro {cont}")
        print(f"\tNombre:\t {libro.getNombre()}")
        print(f"\tAutor:\t {libro.getAutor()}")
        print(f"\tAño P:\t {libro.getAnioPublicacion()}")
        print(f"\tEditorial:\t {libro.getEditorial()}")
        print(f"\tCant Pag:\t {libro.getCantPaginas()}")
        cont += 1

def mostrarSubMenuEntidad(entidad: str) -> None:
    print(f"1. Crear {entidad}")
    print(f"2. Mostrar {entidad} cread@s")

def mostrarSubMenu() -> None:
    print(".: Ejercicio 1 :.")
    print("0. Salir")
    print("1. Libro")
    print("2. Casa")
    print("3. Película")
    print("4. Bodega")
    print("5. Lámpara")

def mostrarMensaje(mensaje = "") -> None:
    print("MENSAJE: ", mensaje) 

def leerEntero(mensaje = "") -> int:
    return int(input(mensaje))

def leerReal(mensaje = "") -> int:
    return float(input(mensaje))

def leerCadena(mensaje = "") -> int:
    return input(mensaje)

def mostrarMenuPrincipal():
    print(".: MENU PRINCIPAL :.")
    print("0. Salir")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("6. Ejercicio 6")
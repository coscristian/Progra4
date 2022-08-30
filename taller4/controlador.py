import vista as v
import modelo as mdl

def guardarLampara(lampara: mdl.Lampara) -> None:
    mdl.lamparas.append(lampara)
    
def guardarBodega(bodega: mdl.Bodega) -> None:
    mdl.bodegas.append(bodega)

def guardarPelicula(pelicula: mdl.Pelicula) -> None:
    mdl.peliculas.append(pelicula)

def guardarCasa(casa: mdl.Casa) -> None:
    mdl.casas.append(casa)

def guardarLibro(libro:mdl.Libro) -> None:
    mdl.libros.append(libro)

def crearLibro() -> mdl.Libro:
    nombre = v.leerCadena("Ingrese el nombre del libro: ")
    autor = v.leerCadena("Ingrese el autor del libro: ")
    anioPubl = v.leerCadena("Ingrese el año de publiación del libro: ")
    editorial = v.leerCadena("Ingrese la editorial del libro: ")
    cantPaginas = v.leerCadena("Ingrese la cantidad de páginas del libro: ")
    return mdl.Libro(nombre, autor, anioPubl, editorial, cantPaginas)
    
def seleccionarOpcionLibros(opcion: int) -> None:
    if opcion == 1:
        libro = crearLibro()
        guardarLibro(libro)
        v.mostrarMensaje("Libro creado correctamente")
    elif opcion == 2:
        if len(mdl.libros) > 0:
            v.mostrarLibros(mdl.libros)
        else:
            v.mostrarMensaje("No hay casas creadas!!")

def crearCasa() -> mdl.Casa:
    direccion = v.leerCadena("Ingrese la dirección: ")
    estrato = v.leerEntero("Ingrese el estrato: ")
    color = v.leerCadena("Ingrese el color: ")
    cantPisos = v.leerEntero("Ingrese la cantidad de pisos: ")
    cantHabitaciones = v.leerEntero("Ingrese la cantidad de habitaciones: ")
    return mdl.Casa(direccion, estrato, color, cantPisos, cantHabitaciones)

def seleccionarOpcionCasas(opcion: int) -> None:
    if opcion == 1:
        casa = crearCasa()
        v.mostrarMensaje("Casa creada correctamente")
        guardarCasa(casa)
    elif opcion == 2:
        if len(mdl.casas) > 0:
            v.mostrarCasas(mdl.casas)
        else:
            v.mostrarMensaje("No hay casas creadas!!")

def crearPelicula() -> mdl.Pelicula:
    titulo = v.leerCadena("Ingrese el titulo: ")
    genero = v.leerCadena("Ingrese el género: ")
    sinopsis = v.leerCadena("Ingrese la sinopsis: ")
    duracion = v.leerEntero("Ingrese la duración (minutos): ")
    cantActores = v.leerEntero("Ingrese la cantidad de actores: ")
    return mdl.Pelicula(titulo, genero, sinopsis, duracion, cantActores)
    
def seleccionarOpcionPeliculas(opcion: int) -> None:
    if opcion == 1:
        pelicula = crearPelicula()
        v.mostrarMensaje("Pelicula creada correctamente")
        guardarPelicula(pelicula)
    elif opcion == 2:
        if len(mdl.peliculas) > 0:
            v.mostrarPeliculas(mdl.peliculas)
        else:
            v.mostrarMensaje("No hay peliculas creadas!!")        

def crearBodega() -> mdl.Bodega:
    nombre = v.leerCadena("Ingrese el nombre: ")
    direccion = v.leerCadena("Ingrese la dirección: ")
    espacio = v.leerEntero("Ingrese el espacio en metros: ")
    tipoVenta = v.leerCadena("Ingrese el producto que se vende: ")
    cantEmpleados = v.leerEntero("Ingrese la cantidad de empleados: ")
    return mdl.Bodega(nombre, direccion, espacio, tipoVenta, cantEmpleados)

def seleccionarOpcionBodegas(opcion: int) -> None:
    if opcion == 1:
        bodega = crearBodega()
        v.mostrarMensaje("Bodega creada correctamente")
        guardarBodega(bodega)
    elif opcion == 2:
        if len(mdl.bodegas) > 0:
            v.mostrarBodegas(mdl.bodegas)
        else:
            v.mostrarMensaje("No hay bodegas creadas!!")          

def crearLampara() -> mdl.Lampara:
    marca = v.leerCadena("Ingrese la marca: ")
    precio = v.leerEntero("Ingrese el precio: ")
    ubicacion = v.leerCadena("Ingrese la ubicacion: ")
    colgante = v.leerCadena("Es colgante?: ")
    moderna = v.leerCadena("Es moderna?: ")
    return mdl.Lampara(marca, precio, ubicacion, colgante, moderna)

def seleccionarOpcionLamparas(opcion: int) -> None:
    if opcion == 1:
        lampara = crearLampara()
        v.mostrarMensaje("Lampara creada correctamente")
        guardarLampara(lampara)
    elif opcion == 2:
        if len(mdl.lamparas) > 0:
            v.mostrarLamparas(mdl.lamparas)
        else:
            v.mostrarMensaje("No hay lamparas creadas!!")       

def seleccionarEntidad(opcionEntidad: int) -> None:
    if opcionEntidad == 1:
        v.mostrarSubMenuEntidad("Libros")
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionLibros(opcionSubMenuEntidad)
    elif opcionEntidad == 2:
        v.mostrarSubMenuEntidad("Casas")
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionCasas(opcionSubMenuEntidad)
    elif opcionEntidad == 3:
        v.mostrarSubMenuEntidad("Peliculas")
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionPeliculas(opcionSubMenuEntidad)      
    elif opcionEntidad == 4:
        v.mostrarSubMenuEntidad("Bodegas")  
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionBodegas(opcionSubMenuEntidad)
    elif opcionEntidad == 5:
        v.mostrarSubMenuEntidad("Lámparas")  
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionLamparas(opcionSubMenuEntidad)        
        
def ejercicio1() -> None:
    v.mostrarSubMenu()
    opcionEntidad = v.leerEntero("¿Qué entidad desea seleccionar?: ")
    seleccionarEntidad(opcionEntidad)

def crearRectangulo() -> mdl.Rectangulo:
    base = v.leerEntero("Ingrese la base: ")
    altura = v.leerEntero("Ingrese la altura: ")
    return mdl.Rectangulo(base, altura)

def ejercicio2() -> None:
    v.mostrarMensaje(".: Rectangulo :.")
    rectangulo = crearRectangulo()
    v.mostrarRectangulo(rectangulo)

def crearEmpleado() -> mdl.Empleado:
    nombre = v.leerCadena("Ingrese el nombre: ")
    genero = v.leerCadena("Ingrese el género: ")
    edad = v.leerEntero("Ingrese la edad:")
    fechaInicio = v.leerCadena("Ingrese la fecha de inicio (Y/M/D): ")
    numHorasMes = v.leerEntero("Ingrese las horas por mes: ")
    valorHora = v.leerEntero("Ingrese el valor de la hora: ")
    return mdl.Empleado(nombre, genero, edad, fechaInicio, numHorasMes, valorHora)
    
def ejercicio3() -> None:
    v.mostrarMensaje(".: Empleado :.")
    empleado = crearEmpleado()
    v.mostrarEmpleado(empleado)

def seleccionarEjercicio(opcion: int) -> None:
    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
        pass
    elif opcion == 4:
        #ejercicio4()
        pass
    elif opcion == 5:
        #ejercicio5()
        pass
    elif opcion == 6:
        #ejercicio6()
        pass

def menuPrincipal():
    opcion = 1
    while opcion != 0:
        try:
            v.mostrarMenuPrincipal()
            opcion = v.leerEntero("¿Qué opción desea seleccionar?: ")
            seleccionarEjercicio(opcion)
        except Exception as e:
            v.mostrarMensaje(e)
    v.mostrarMensaje("Saliendo del Sistema...")

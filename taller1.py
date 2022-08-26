import math

def elegirOpcion(opcion: int):
  if opcion == 1:
    areaCuadrado()
  elif opcion == 2:
    areaRectangulo()
  elif opcion == 3:
    areaTriangulo()    
  elif opcion == 4:
    areaRombo()
  elif opcion == 5:
    areaPentagono()    
  elif opcion == 6:
    areaHexagono()    
  elif opcion == 7:
    areaCirculo()    
  elif opcion == 8:
    areaTrapecio()  
  elif opcion == 9:
    areaParalelogramo()   

def menuPrincipal():
  opcion = 1
  while(opcion != 0):
    print(".: MENU PRINCIPAL :.")
    print("0. Salir")
    print("1. Area Cuadrado")
    print("2. Area Rectangulo")
    print("3. Area Triangulo")
    print("4. Area Rombo")
    print("5. Area Pentagono")
    print("6. Area Hexagono")
    print("7. Area Circulo")
    print("8. Area Trapecio")
    print("9. Area Paralelogramo")
    opcion = int(input("¿Qué opción desea ejecutar?: "))
    elegirOpcion(opcion)
    
  print("MENSAJE: SALIENDO...")


def areaCuadrado():
    print(".: CUADRADO :.")
    lado = float(input("Ingrese el valor del lado: "))
    print("El área del cuadrado es: ", lado*2)

def areaRectangulo():
    print(".: RECTANGULO :.")
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    print("El área de el rectangulo es: ", base*altura)

def areaTriangulo():
    print(".: TRIANGULO :.")
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    print("El área de el triangulo es: ", base*altura / 2)

def areaRombo():
    print(".: ROMBO :.")
    dMayor = float(input("Ingrese el valor de la diagonal mayor: "))
    dMenor = float(input("Ingrese el valor de la diagonal menor: "))
    print("El área de el rombo es: ", dMayor * dMenor / 2)

def areaPentagono():
    print(".: PENTAGONO :.")
    perimetro = float(input("Ingrese el valor de el perimetro: "))
    apotema = float(input("Ingrese el valor de el apotema: "))
    print("El área de el pentagono es: ", perimetro * apotema / 2)

def areaHexagono():
    print(".: HEXAGONO :.")
    perimetro = float(input("Ingrese el valor de el perimetro: "))
    apotema = float(input("Ingrese el valor de el apotema: "))
    print("El área de el hexagono es: ", perimetro * apotema / 2)

def areaCirculo():
    print(".: CIRCULO :.")
    radio = float(input("Ingrese el valor de el radio: "))
    print("El área de el circulo es: ", math.pi * math.pow(radio, 2))

def areaTrapecio():
    print(".: TRAPECIO :.")
    base1 = float(input("Ingrese el valor de la base 1: "))
    base2 = float(input("Ingrese el valor de la base 2: "))
    altura = float(input("Ingrese el valor de la altura: "))
    print("El área de el trapecio es: ", (base1 + base2)*altura/2)

def areaParalelogramo():
    print(".: PARALELOGRAMO :.")
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    print("El área de el paralelogramo es: ", base*altura)

# Principal
def main():
  while(True):
    try:
      menuPrincipal()
      break
    except Exception as err:
      print("MENSAJE: ERROR: ", err)

if __name__ == '__main__':
    main()
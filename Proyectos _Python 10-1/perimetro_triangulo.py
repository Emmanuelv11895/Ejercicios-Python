# Función principal
def main():
    # Solicitar al usuario que ingrese la longitud de los lados del triángulo
    lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
    lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
    lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

    # Calcular el perímetro
    perimetro = lado1 + lado2 + lado3

    # Mostrar el resultado
    print("El perímetro del triángulo es:", perimetro)

# Llamar a la función principal
if __name__ == "__main__":
    main()
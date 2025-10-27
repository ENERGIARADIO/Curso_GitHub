def main():
    print("¡Hola Mundo desde GitHub!")
    print("Este es mi primer repositorio")
    
    # Ejemplo de cálculo
    numero = 5
    resultado = numero * 2
    print(f"El doble de {numero} es {resultado}")
    
    # Nueva funcionalidad - suma
    a = 10
    b = 20
    suma = a + b
    print(f"La suma de {a} + {b} = {suma}")
    
    # Usar la calculadora
    calculadora()

def calcular_factorial(n):
    """Calcula el factorial de un número"""
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n-1)

def calculadora():
    """Calculadora simple"""
    print("\n--- Calculadora ---")
    num1 = float(input("Ingresa primer número: "))
    num2 = float(input("Ingresa segundo número: "))
    
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("División: No se puede dividir por cero")

if __name__ == "__main__":
    main()
    print(f"Factorial de 5: {calcular_factorial(5)}")
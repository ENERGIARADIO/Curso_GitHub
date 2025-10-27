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

def calcular_factorial(n):
    """Calcula el factorial de un número"""
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n-1)

if __name__ == "__main__":
    main()
    print(f"Factorial de 5: {calcular_factorial(5)}")
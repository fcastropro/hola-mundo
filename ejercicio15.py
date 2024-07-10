print("Ejercicio 15")
print("Factorial de un número: Escribe un programa que calcule el factorial de un número introducido por el usuario.")
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input("Ingrese un número: "))))
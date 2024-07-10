print("Ejercicio 10")
print("Números primos: Escribe un programa que determine si un número introducido por el usuario es primo")
num=int(input("Ingrese un número: "))
lam = lambda num : all(num % i for i in range(2, num))
primo = lam(num)
if primo:
  print(f"El número {num} es primo")
else:
  print(f"El número {num} no es primo")
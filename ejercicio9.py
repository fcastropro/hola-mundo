print("Ejercicio 9")
print("Tabla de multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número introducido por el usuario.")
multiplo=int(input("Ingrese un número para generar la tabla de multiplicar: "))
import time
for i in range(0,13):
  print(f"{i} x {multiplo} = "+str(i*multiplo))
  time.sleep(1)
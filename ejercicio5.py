print("Ejercicio 5")
print("Número mayor: Escribe un programa que pida tres números al usuario y determine cuál es el mayor.")
numeros=[]
for i in range(0,3):
  numeros.append(int(input("Ingrese un número ")))
print("Número mayor es: " + str(max(numeros)))
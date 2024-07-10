print("Ejercicio 16")
print("Generar números aleatorios: Escribe un programa que genere y muestre 5 números aleatorios entre 1 y 100.")
import random
for i in range(1,6):
  print(f"{i}.- "+str(random.randint(1,100)))
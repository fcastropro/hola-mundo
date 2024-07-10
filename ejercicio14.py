print("Ejercicio 14")
print("Palíndromo: Escribe un programa que determine si una cadena introducida por el usuario es un palíndromo.")
cadena=list(input("Ingrese la cadena ").upper())
rev=list(reversed(cadena))
if cadena==rev:
  print("La cadena es un palindromo")
else:
  print("La cadena no es un palindromo")
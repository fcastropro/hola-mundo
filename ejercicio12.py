print("Ejercicio 12")
print("Invertir una cadena: Escribe un programa que invierta una cadena introducida por el usuario.")
cadena=list(input("Ingrese la cadena "))
cadena.reverse()
cadenainvertida=""
for i in cadena:
  cadenainvertida+=i
print("La cadena invertida es= "+str(cadenainvertida))
print("Ejercicio 13")
print("Contar vocales: Escribe un programa que cuente el número de vocales en una cadena introducida por el usuario.")
cadena=list(input("Ingrese la cadena "))
print("El número de vocales de la cadena ingresada es: "+str(len(list(filter(lambda x: x[0].lower() in 'aeiou', cadena)))))
notas = input("ingrese sus notas: ")
notas = [float(notas)for notas in notas.split()]
promedio = sum(notas)/len(notas)
print("Su promedio es: ", promedio)
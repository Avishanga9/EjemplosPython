#Sumar los elementos de un arreglo
arreglo = []
cant = int(input("Dime cuantos numeros#: "))
cont = 0 
while (cont < cant):
    num =int(input("Dime un numero#: "))
    arreglo.append(num)
    cont +=1
suma = 0
for num in arreglo:
    suma += suma

print("La suma es", suma)        
listaEst = []
resp = "Si"
while(resp.upper() != "No"):
    tam = len(listaEst)
    print("Elementos guardados: ", tam)
    nombres = input("escriba el nombre del esstudiante: ")
    listaEst.append(nombres)
    resp = input("Desea agregar mas? Si - No: ")

for est in listaEst:
    print(est)    
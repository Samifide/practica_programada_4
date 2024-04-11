#ejercicio2
pasajeros = []
def ingresar_pasajeros(pasajeros):
    for i in range(5):
        pasajeros_dia = [] 
        print("Ingrese la cantidad de pasajeros para el día", i + 1, ":")
        for s in range(4):  
            while True:
                suma_pas = input(f"Cantidad de pasajeros para el servicio {s + 1}: ")
                suma_pas = int(suma_pas)
                if suma_pas <= 60:
                    pasajeros_dia.append(suma_pas)
                    break  
                else:
                    print("Demasiados pasajeros")
        pasajeros.append(pasajeros_dia)
    return pasajeros

def prom_pasajerostotal(pasajeros):
    total_pas = len(pasajeros)
    total_pas = total_pas * 4
    suma_pasajeros = 0
    for dia in pasajeros:
        for cantidad_pasajeros in dia:
            suma_pasajeros += cantidad_pasajeros
    return suma_pasajeros / total_pas

def prom_pasajeros(pasajeros_dia):
    suma_pasaj = sum(pasajeros_dia)
    total_pas = len(pasajeros_dia)
    return suma_pasaj / total_pas

def mejor_servicio(pasajeros_dia):
    servicio1 = pasajeros_dia[0]
    servicio2 = pasajeros_dia[1]
    servicio3 = pasajeros_dia[2]
    servicio4 = pasajeros_dia[3]

    if servicio1 >= servicio2 and servicio1 >= servicio3 and servicio1 >= servicio4:
        return 1
    elif servicio2 >= servicio3 and servicio2 >= servicio4:
        return 2
    elif servicio3 >= servicio4:
        return 3
    else:
        return 4

def menor_servicio_dia(pasajeros):
    minimos = []
    for dia in pasajeros:
        minimo_servicio_dia = min(dia)
        minimos.append(minimo_servicio_dia)
    return minimos

ingresar_pasajeros(pasajeros)

num = 1
for dia in pasajeros:
    promedio = prom_pasajeros(dia)
    print("El promedio de pasajeros para el día", num, "es:", promedio)
    mejor = mejor_servicio(dia)
    print("El mejor servicio para el día", num, "es el servicio", mejor)
    
    num += 1

promedio_total = prom_pasajerostotal(pasajeros)
print("El promedio total de pasajeros es:", promedio_total)
minimos = menor_servicio_dia(pasajeros)
elmenor = min(minimos)
dia_menor = minimos.index(elmenor) + 1
print("El menor servicio es de ", elmenor, "y el día es:", dia_menor)

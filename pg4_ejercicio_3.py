#Ejercicio # 03
##El equipo de fútbol nacional Las Tuercas F.C. cuenta con
##25 jugadores en su planilla, cada uno de ellos recibe un
##salario mensual diferente y el equipo paga los salarios
##en efectivo. Por lo que le ha solicitado desarrollar un
##programa que reciba el salario de cada uno de los
##futbolistas, posterior, debe informar cuál es el monto de
##dinero que se debe retirar del banco y la denominación de
##billetes y monedas necesaria para poder realizar el pago
##exacto en efectivo.
##Considere las denominaciones de billetes y monedas
##disponibles en nuestro país.


def retiro(lista_Futbolistas):
    monto=int(input("Porfavor escriba la cantidad de dinero que desea retirar \n **!!recuerde¡¡ se le devolvera en el dollar de su pais**"))
    nombre=input("Porfavor escriba su nombre con el que se registro previamente")
    
    for i in range(len(lista_Futbolistas)):
        e=lista_Futbolistas[i]
        Verificar=e[0]
        if nombre == Verificar:
            almacenado=lista_Futbolistas[i][1]
            Sobrante=almacenado-monto
            if Sobrante<0:
                print("no tiene dinero suficiente para realizar el retiro")
            else:
                lista_Futbolistas[i][1]=Sobrante
                montoEnColon=monto*507.63
                billetes=int(montoEnColon/(500*2))
                centabos=int(montoEnColon%(500*2))
                print("Se le estan devolviendo",int(montoEnColon),"colones o ",billetes, "billetes y ", ("%.2f" % centabos), "centavos \n en su cuenta quedan",lista_Futbolistas[i][1])
                

def registro(lista_Futbolistas):
    print("Esto es un registro")
    nombre_futbolista=input("Porfavor escriba su nombre como futbolista: ")
    salaraio=int(input("Porfavor escriba su salario esxacto en dolares:"))
    lista_Futbolistas.append([nombre_futbolista,salaraio])

def agregar(lista_Futbolistas):
    monto=int(input("Porfavor escriba la cantidad de dinero que desea Agregar en dolares"))
    nombre=input("Porfavor escriba su nombre con el que se registro previamente")
    
    for i in range(len(lista_Futbolistas)):
        e=lista_Futbolistas[i]
        Verificar=e[0]
        if nombre == Verificar:
            almacenado=lista_Futbolistas[i][1]
            Sobrante=almacenado+monto
            lista_Futbolistas[i][1]=Sobrante
            print("Se le estan agregando",monto, "\n en su cuenta quedan",lista_Futbolistas[i][1])
    

    
lista_Futbolistas=[]
while True:
    print("Antes de cualquier accion debe registrar futbolistas")
    registro(lista_Futbolistas)
    print(lista_Futbolistas)
    while True:
        Decicion=int(input("que accion desea realizar \n 1-Realizar un registro nuevo \n 2-Retirar dinero \n 3-Agregar dinero"))
        if Decicion==1:
            registro(lista_Futbolistas)
            print(lista_Futbolistas)
        elif Decicion==2:
            retiro(lista_Futbolistas)
        elif Decicion==3:
            agregar(lista_Futbolistas)
        else:
            print("Accion no opcional")
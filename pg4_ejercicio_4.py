##Ejercicio # 04
##En el abastecedor La Deportiva se ha detectado la necesidad de
##controlar el aforo de personas que se mantienen dentro del negocio
##para cumplir con la normativa del Ministerio de Salud. El propietario del
##abastecedor requiere desarrollar dos aplicaciones, una para registrar
##el ingreso de cada persona (uno a uno) y otra para registrar el egreso
##(uno a uno).
##Son dos aplicaciones independientes porque existe una puerta para el
##ingreso y otra para el egreso.
##La capacidad del abastecedor es de 10 personas como máximo.
##Considere almacenar la cantidad de personas actuales en un
##archivo de texto para que esta información se comparta entre las
##aplicaciones.


import time
import os

RegistrosCompletos=open("RegistrosCompletos.txt","a")
RegistrosCompletos.close()

def negocio(Nombre,Personas,Eliminados):
    print("Ahora estas en el sistema del negocio \n")
    for i in range(len(Personas)):
        Persona=Personas[i]
        if Nombre==Persona[1]:
            print(Persona)
            print("\n")

            desicion=int(input("Que accion desea realiza \n 1-Volver al programa de registro \n 2- salir permanenetemente del sistema"))

            if desicion==2:
                print("\n Se esta registrando sus datos a eliminados")
                Hora=time.strftime("%H:%M:%S")
                fecha=time.strftime("%d/%m/%y")
                eliminado=Persona
                eliminado+=("\n Hora de eliminado",Hora,"\n Fecha de eliminacion de registro",fecha)
                Eliminados.append(eliminado)
                Personas.remove(Persona)
                print("\n ****Lista de Registrados actuales****")
                print(Personas)
                print("\n ****Lista de eliminados****")
                print(Eliminados)
                print("\n")
            

def registro(Personas):
    print("esta es el area de registro")
    new=input("Escriba su nombre ")
    Hora=time.strftime("%H:%M:%S")
    fecha=time.strftime("%d/%m/%y")
    Personas.append(["nombre de persona",new, "\n Hora de ingreso en sistema: ",Hora, "\n fecha de ingreso en sistema", fecha])
    print("\n")


Personas=[]
Eliminados=[]

registro(Personas)

while True:
    print(Personas)
    RegistrosCompletos=open("RegistrosCompletos.txt","w")
    RegistrosCompletos.write(str(Personas))
    RegistrosCompletos.write(str(Eliminados))
    RegistrosCompletos.close()
    
    print("\n")
    desicion=int(input("¿Desea Ingresar mas personas o quiero dirigisrse al negocio? \n |Deseo ingresar mas personas=1 | Deseo ingresar al area del negocio=2| Visualisar Registros y elimanaciones"))
    if desicion== 1:
        if len(Personas)<10 :
            print("\n")
            registro(Personas)
        elif len(Personas)>=10:
            print("\n")
            print("No puede ingresar a mas personas a saturado el limite de personas, se va a dirigir al negocio por Default")
            Nombre=input("Escriba su nombre porfavor")
            negocio(Nombre,Personas,Eliminados)
         
    elif desicion== 2:
        Nombre=input("Escriba su nombre porfavor")
        negocio(Nombre,Personas,Eliminados)

    elif desicion== 3:
        print("\n ****Lista de Registrados actuales****")
        print(Personas)
        print("\n ****Lista de eliminados****")
        print(Eliminados)
        
    else:
        print("no opcional")
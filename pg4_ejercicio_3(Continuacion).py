##Ejercicio # 03 (continuación)
##Para ejemplificar los cálculos a realizar se presenta la
##siguiente información.
##El jugador “Luis” gana ₡1,845,725 lo que implica que para
##hacer su pago se requiere el siguiente desglose.
##Denominación Cantidad Monto
##50,000 36 1,800,000
##20,000 2 40,000
##5,000 1 5,000
##500 1 500
##100 2 200
##25 1 25
##1,845,725
##Una vez calculado el desglose de un
##jugador, debe acumular la cantidad de
##cada denominación por todos los
##jugadores. Eso significa que debe indicar
##la sumatoria de todos los billetes de 50
##mil, todos los de 20 mil, etc.

def desglose(lista_Futbolistas):
    for i in lista_Futbolistas:
        print("nombre",i[0])
        print("Desglose de salario")
        salario_en_dolares=i[1]
        salario=int(salario_en_dolares*507.63)
        print("salario en dolares: ",salario_en_dolares)
        print("salario en colones: ",salario)

        print("Billetes disponibles: \n 50000 \n 20000 \n 10000 \n 5000 \n 2000 \n 1000 \n 500 \n 100 \n 50 \n 25 \n 10 \n 5 \n 1")

        if salario>= 50000 :
            billetesCanticuenta=int(salario/50000)
            cincuentaMil=billetesCanticuenta*50000
            salario=salario-cincuentaMil
            print(billetesCanticuenta,"billetes de 50000",cincuentaMil )

        if salario>= 20000 :
            billetesCantiVeinte=int(salario/20000)
            VeinteMil=billetesCantiVeinte*20000
            salario=salario-VeinteMil
            print(billetesCantiVeinte,"billetes de 20000",VeinteMil)

        if salario>= 10000 :
            billetesCantidiez=int(salario/10000)
            diesmill=billetesCantidiez*10000
            salario=salario-diesmill
            print( billetesCantidiez,"billetes de 10000",diesmill)

        if salario>= 5000 :
            billetesCanticincomil=int(salario/5000)
            cincoMil=billetesCanticincomil*5000
            salario=salario-cincoMil
            print( billetesCanticincomil,"billetes de 5000",cincoMil)

        if salario>= 2000 :
            billetesCantiDosmil=int(salario/2000)
            DosMil=billetesCantiDosmil*2000
            salario=salario-DosMil
            print( billetesCantiDosmil,"billetes de 2000",DosMil)

        if salario>= 1000 :
            billetesCantimil=int(salario/1000)
            mil=billetesCantimil*1000
            salario=salario-mil
            print( billetesCantimil,"billetes de 1000",mil)

        if salario>= 500 :
            colonesquinientos=int(salario/500)
            quinientos=colonesquinientos*500
            salario=salario-quinientos
            print( colonesquinientos,"monedas de 500",quinientos)
            
        if salario>= 100 :
            colonescien=int(salario/100)
            cien=colonescien*100
            salario=salario-cien
            print( colonescien,"monedas de 100",cien)

        if salario>= 50 :
            colonescincuenta=int(salario/50)
            cincuenta=colonescincuenta*50
            salario=salario-cincuenta
            print( colonescincuenta,"monedas de 50",cincuenta)

        if salario>= 25 :
            colonesveintisinco=int(salario/25)
            veinticinco=colonesveintisinco*25
            salario=salario-veinticinco
            print( colonesveintisinco,"monedas de 25",veinticinco)

        if salario>= 10 :
            colonesdies=int(salario/10)
            dies=colonesdies*100
            salario=salario-dies
            print( colonesdies,"monedas de 10",dies)

        if salario>= 5 :
            colonescinco=int(salario/5)
            cinco=colonescinco*5
            salario=salario-cinco
            print( colonescinco,"monedas de 5",cinco)

        if salario>= 1 :
            colonesuno=int(salario/1)
            uno=colonesuno*1
            salario=salario-uno
            print( colonesuno,"monedas de 1",uno)


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
        Decicion=int(input("que accion desea realizar \n 1-Realizar un registro nuevo \n 2-Retirar dinero \n 3-Agregar dinero \n 4-Ver desglose de pago de cada jugador"))
        if Decicion==1:
            registro(lista_Futbolistas)
            print(lista_Futbolistas)
        elif Decicion==2:
            retiro(lista_Futbolistas)
        elif Decicion==3:
            agregar(lista_Futbolistas)
        elif Decicion==4:
            desglose(lista_Futbolistas)
        else:
            print("Accion no opcional")

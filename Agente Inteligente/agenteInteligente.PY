"""
Utilizando el PEAS programar las reglas para programar el agente inteligente.

Autor: Luis Fernando Cueva Flores
Versión: 1.0
"""
def validar_numeros_enteros():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        numero : int
    '''
    #mientras sea verdadero se ingresara un dato en la variable numero, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el usuario debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=int(input())
            #rempemos ciclo repetitivo
            break
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero

def vias_cerradas_abiertas():
    '''
    Funcion que hace el ingreso de informacion de las vias

    Parametros:
        Esta funcion no tiene parametros
    Retorna: 
        Esta funcion no retorna nada
    '''
    #Declara variable objetivo 
    estado_meta = {'Quito': '0', 'Chone': '0','Lorena': '0','Pilaton': '0'}
    #Defino el costo como contador
    costo=0
    #Ingreso a que carretera desea ir el usuario
    print("¿A que carretera desea ir?")
    #imprimo un menu
    print("1. Quito\n2. Chone\n3. Lorena\n4. Pilaton")
    print("Elija una opcion: ",end="")
    #Elijo una de las vias ingresando un numero entero
    opcion1=validar_numeros_enteros()
    #valido que solo ingrese numeros dentro del rango del menu
    while(opcion1<1 or opcion1>4):
        print("Elija un numero dentro del rango del menu!, Intente de nuevo: ",end="")
        opcion1=validar_numeros_enteros()

    #Ingreso desde que carretera esta saliendo el usuario
    print("¿Desde cual carretera esta saliendo?")
    #si desea ir a Quito
    if(opcion1==1):
        #imprimo las vias de donde esta saliendo el usuario
        print("1. Chone\n2. Lorena\n3. Pilaton")
        print("Elija una opcion: ",end="")
        #Elijo una de las vias ingresando un numero entero
        opcion2=validar_numeros_enteros()
        #valido que solo ingrese numeros dentro del rango del menu
        while(opcion2<1 or opcion2>3):
            print("Elija un numero dentro del rango del menu!, Intente de nuevo: ",end="")
            opcion2=validar_numeros_enteros()
    #si desea ir a Chone
    if(opcion1==2):
        #imprimo las vias de donde esta saliendo el usuario
        print("1. Quito\n2. Lorena\n3. Pilaton")
        print("Elija una opcion: ",end="")
        #Elijo una de las vias ingresando un numero entero
        opcion2=validar_numeros_enteros()
        #valido que solo ingrese numeros dentro del rango del menu
        while(opcion2<1 or opcion2>3):
            print("Elija un numero dentro del rango del menu!, Intente de nuevo: ",end="")
            opcion2=validar_numeros_enteros()
    #si desea ir a Lorena
    if(opcion1==3):
        #imprimo las vias de donde esta saliendo el usuario
        print("1. Quito\n2. Chone\n3. Pilaton")
        print("Elija una opcion: ",end="")
        #Elijo una de las vias ingresando un numero entero
        opcion2=validar_numeros_enteros()
        #valido que solo ingrese numeros dentro del rango del menu
        while(opcion2<1 or opcion2>3):
            print("Elija un numero dentro del rango del menu!, Intente de nuevo: ",end="")
            opcion2=validar_numeros_enteros()
    #si desea ir a Pilaton
    if(opcion1==4):
        #imprimo las vias de donde esta saliendo el usuario
        print("1. Quito\n2. Chone\n3. Lorena")
        print("Elija una opcion: ",end="")
        #Elijo una de las vias ingresando un numero entero
        opcion2=validar_numeros_enteros()
        #valido que solo ingrese numeros dentro del rango del menu
        while(opcion2<1 or opcion2>3):
            print("Elija un numero dentro del rango del menu!, Intente de nuevo: ",end="")
            opcion2=validar_numeros_enteros()
    #ingreso el estado de las vias
    print("Ingrese el estdado de la via a la que desea ir (0:Via cerrada , 1:Abierta):")
    #ingreso un numero que define el estado de la via
    estado_via=validar_numeros_enteros()
    #valido que solo ingrese 1 o 0
    while(estado_via<0 or estado_via>1):
        print("Ingrese un estado de via valido!!",end="")
        estado_via=validar_numeros_enteros()
    #si desea ir a Quito
    if(opcion1==1):
        #cambiamos el estados de la via segun lo ingresado por el usuario
        estado_meta['Quito']=estado_via
        #si la via esta abierta
        if(estado_via==0):
            print("La via se encuentra abierta puede ir a Quito sin problema")
        #si la via esta cerrada 
        else:
            #imprimir el estado de la via
            print("La via Quito esta cerrada")
            #abrimos la via
            print("Abriendo la via...")
            #aumentamos el costo en 25
            costo=costo+30
            #imprimimos desde donde sale a donde quiere ir
            if(opcion2==1):
                print("La via ya se encuentra abierta, saliendo de Chone a Quito")
            if(opcion2==2):
                print("La via ya se encuentra abierta, saliendo de Lorena a Quito")
            if(opcion2==3):
                print("La via ya se encuentra abierta, saliendo de Pilaton a Quito")
    #si desea ir a Chone
    if(opcion1==2):
        #cambiamos el estados de la via segun lo ingresado por el usuario
        estado_meta['Chone']=estado_via
        #si la via esta abierta
        if(estado_via==0):
            print("La via se encuentra abierta puede ir a Chone sin problema")
        #si la via esta cerrada 
        else:
            #imprimir el estado de la via
            print("La via Chone esta cerrada")
            #abrimos la via
            print("Abriendo la via...")
            #aumentamos el costo en 25
            costo=costo+25
            #imprimimos desde donde sale a donde quiere ir
            if(opcion2==1):
                print("La via ya se encuentra abierta, saliendo de Quito a Chone")
            if(opcion2==2):
                print("La via ya se encuentra abierta, saliendo de Lorena a Chone")
            if(opcion2==3):
                print("La via ya se encuentra abierta, saliendo de Pilaton a Chone")
    #si desea ir a lorena
    if(opcion1==3):
        #cambiamos el estados de la via segun lo ingresado por el usuario
        estado_meta['Lorena']=estado_via
        #si la via esta abierta
        if(estado_via==0):
            print("La via se encuentra abierta puede ir a Lorena sin problema")
        #si la via esta cerrada 
        else:
            #imprimir el estado de la via
            print("La via Chone esta cerrada")
            #abrimos la via
            print("Abriendo la via...")
            #aumentamos el costo en 25
            costo=costo+15
            #imprimimos desde donde sale a donde quiere ir
            if(opcion2==1):
                print("La via ya se encuentra abierta, saliendo de Quito a Lorena")
            if(opcion2==2):
                print("La via ya se encuentra abierta, saliendo de Chone a Lorena")
            if(opcion2==3):
                print("La via ya se encuentra abierta, saliendo de Pilaton a Lorena")
    #si desea ir a Pilaton
    if(opcion1==4):
        #cambiamos el estados de la via segun lo ingresado por el usuario
        estado_meta['Lorena']=estado_via
        #si la via esta abierta
        if(estado_via==0):
            print("La via se encuentra abierta puede ir a Pilaton sin problema")
        #si la via esta cerrada    
        else:
            #imprimir el estado de la via
            print("La via Pilaton esta cerrada")
            #abrimos la via
            print("Abriendo la via...")
            #aumentamos el costo en 25
            costo=costo+20
            #imprimimos desde donde sale a donde quiere ir
            if(opcion2==1):
                print("La via ya se encuentra abierta, saliendo de Quito a Pilaton")
            if(opcion2==2):
                print("La via ya se encuentra abierta, saliendo de Chone a Pilaton")
            if(opcion2==3):
                print("La via ya se encuentra abierta, saliendo de Lorena a Pilaton")
    #imprimo el costo
    print("El costo por abrir la via es $",costo)
if __name__ == '__main__':
    vias_cerradas_abiertas()
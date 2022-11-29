import random #imporatmos random para usar la funcion de generar numeros aleatorios
import os     #importamos os para hacer uso de la funcion que limpia la pantalla y pausa en el codigo
"""
Bingo, consiste en ir marcando en nuestro cartón los números que aleatoriamente van surgiendo en cada momento por el tombo 
y el primero que haga línea en cruz, vertical u horizontal sera el ganador

Autores:
Luis Fernando Cueva Flores
Lisbeth Adali Carvajal Escobar
Erick Patricio Ramirez Ortiz

Verisión:
VER.1.2
"""
def imprimir_logo_del_juego():
    '''
    Funcion que imprime en letras gigantes "BINGO" en color azul

    Parametros:
    ------------
        Esta funcion no tiene parametros.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    
    #imprime en color azul
    print(chr(27)+"[1;34m")
    print("████████    ██████████    ██      ██    ██████████    ██████████")
    print("██     ██       ██        ████    ██    ██            ██      ██")
    print("██     ██       ██        ██ ██   ██    ██            ██      ██")
    print("███████         ██        ██  ██  ██    ██  ██████    ██      ██")
    print("██     ██       ██        ██   ██ ██    ██      ██    ██      ██")
    print("██     ██       ██        ██    ████    ██      ██    ██      ██")
    print("████████    ██████████    ██     ███    ██████████    ██████████")

def ingreso_numero_de_jugadores():
    '''
    Funcion donde se valida si el numero ingresado por el jugador es entero, si lo que se ingresó no es un numero
    entero entonces el jugador tendra que volver a ingresar un dato hasta que sea entero

    Parametros:
    ------------
            Esta funcion no tiene parametros.
    Retorna:
    ------------
        Retorna la variable numJugadores como int.
    '''
    
    #para validar usamos un ciclo for donde mientras sea verdad:
    while True:
        try:
            #se ingresa un entero en la variable numJugadores
            numJugadores=int(input("Ingrese el numero de jugadores: "))
            break
        except ValueError:
            #si ve que lo que se ha ingresado no es un numero entero entonces imprimira un mensaje de error
            print("No ha ingresado un numero entero.")
    return numJugadores

def ingreso_nombre_de_jugadores(nombresJugadores,nJugadores):
    '''
    Funcion donde el jugador podra ingresar su nombre dentro del juego

    Parametros:
    ------------
        nombresJugadores : lista
            Variable donde se guardara los nombres de los participantes segun nJugadores
        nJugadores       : int
            Variable entera que indica cuantos jugadores estan participando

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    for i in range(nJugadores):
        #En este print("") hacemos uso del de formatos ascii en donde le pondra color a las letras
        print(chr(27)+"[1;37m"+"JUGADOR ",i+1)
        #imprimir en color cian
        print(chr(27)+"[;36m")
        #ingresamosnombre jugador
        nombres=input("Ingrese nombre del jugador:")
        #agregamos lo que se agrego en variable nombres a la lista nombreJugadores
        nombresJugadores.append(nombres)
    #limpiar la pantalla
    os.system("cls")

def generacion_de_cartones(carton1,carton2,carton3,carton4,nJugadores):
    '''
    En esta funcion segun el numero de jugadores se va generando un carton con 25 numeros aleatorios para cada uno de los participantes

    Parametros:
    ------------
        carton1    : Lista
        carton2    : Lista
        carton3    : Lista
        carton4    : Lista
            variables donde se generaran los 25 numeros para jugar al bingo
        nJugadores : int
            Variable entera que indica cuantos jugadores estan participando
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    #si solo hay un jugador entonces solo se generara un carton para él
    if(nJugadores==1): 
        #Mientras el tamaño de la lista carton2 sea menor a 26 hacer:
        while len(carton1) < 26:       
            #generamos un numero entre 1 y 99 y la agregamos a la variable numero
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton1" entonces 
            if numero not in carton1:    
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton1.append(numero)     
        #como en todo carton del juego del bingo se iguala a cero la posicio 13 del carton ya que no hay numero 
        #central en los cartones(0 significa que no hay numero en este caso)
        carton1[13]=0   
                        
    #si hay dos jugadores entonces solo se generara dos cartones para los dos participantes
    if(nJugadores==2):

        #Mientras el tamaño de la lista carton1 sea menor a 26 hacer:
        while len(carton1) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99) 
            #Si el numero que se ha generado no existe dentro de la lista "carton1" entonces 
            if numero not in carton1:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton1.append(numero)
        #Mientras el tamaño de la lista carton2 sea menor a 26 hacer:
        while len(carton2) < 26:
            #hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton2" entonces 
            if numero not in carton2:
                 #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton2.append(numero)
        #carton1 y carton2 en la posicion 13 seran igual a cero
        carton1[13]=0
        carton2[13]=0  
    #si hay tres jugadores entonces se generara tres cartones para los tres participantes
    if(nJugadores==3):
        #Mientras el tamaño de la lista carton1 sea menor a 26 hacer: 
        while len(carton1) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton1" entonces
            if numero not in carton1:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton1.append(numero)
        #Mientras el tamaño de la lista carton2 sea menor a 26 hacer:
        while len(carton2) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton2" entonces
            if numero not in carton2:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton2.append(numero)
         #Mientras el tamaño de la lista carton3 sea menor a 26 hacer:        
        while len(carton3) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton3" entonces
            if numero not in carton3:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton3.append(numero)
        #carton1, carton2 y carton3 en la posicion 13 seran igual a cero
        carton1[13]=0
        carton2[13]=0
        carton3[13]=0 
    #si hay cuatrp jugadores entonces se generara cuatro cartones para los cuatro participantes      
    if(nJugadores==4):
         #Mientras el tamaño de la lista carton1 sea menor a 26 hacer:
        while len(carton1) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton1" entonces
            if numero not in carton1:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton1.append(numero)
        #Mientras el tamaño de la lista carton2 sea menor a 26 hacer:
        while len(carton2) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton2" entonces
            if numero not in carton2:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton2.append(numero)
        #Mientras el tamaño de la lista carton3 sea menor a 26 hacer:         
        while len(carton3) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton3" entonces
            if numero not in carton3:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton3.append(numero)
         #Mientras el tamaño de la lista carton4 sea menor a 26 hacer:
        while len(carton4) < 26:
            #En este ciclo while hacemos que genere un numero aleatorio entre el 1 y 99 en la variable "numero"
            numero = random.randint(1, 99)
            #Si el numero que se ha generado no existe dentro de la lista "carton3" entonces
            if numero not in carton4:
                #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
                carton4.append(numero)
        #carton1, carton2, carton3 y carto4 en la posicion 13 seran igual a cero        
        carton1[13]=0
        carton2[13]=0
        carton3[13]=0
        carton4[13]=0 

def imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores):
    '''
    Funcion que imprime el carto de los participantes segun el numero de jugadores

    Parametros:
    ------------
        carton1    : Lista
        carton2    : Lista
        carton3    : Lista
        carton4    : Lista
            variables donde se generaran los 25 numeros para jugar al bingo
        nJugadores : int
            Variable entera que indica cuantos jugadores estan participando
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    #En este if si solo hay un jugador solo se imprimira 1 carton para jugar
    if (nJugadores==1):
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            #se imprime los numeros generados para el carton
            print(carton1[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0): 
                print("")   
        print("")
    
    #En este if si hay dos jugadores solo se imprimira 2 cartones para jugar
    if (nJugadores==2):
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            #se imprime los numeros generados para el carton
            print(carton1[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton2)):
            #se imprime los numeros generados para el carton
            print(carton2[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        
    #En este if si hay 3 jugadores solo se imprimira 3 cartones para jugar
    if (nJugadores==3):
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            #se imprime los numeros generados para el carton
            print(carton1[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")#Aqui se imprime el nombre del jugador
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton2)):
            #se imprime los numeros generados para el carton
            print(carton2[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[2],":")#Aqui se imprime el nombre del jugador
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton3)):
            #se imprime los numeros generados para el carton
            print(carton3[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
    #En este if si hay 4 jugadores se imprimira 4 cartones para jugar
    if (nJugadores==4):
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            #se imprime los numeros generados para el carton
            print(carton1[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton2)):
            #se imprime los numeros generados para el carton
            print(carton2[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[2],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton3)):
            #se imprime los numeros generados para el carton
            print(carton3[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")
        #Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[3],":")
        #hacemos que las letras se impriman de color cian
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton4)):
            #se imprime los numeros generados para el carton
            print(carton4[i]," ",end="")
            #con este if hacemos que se impriman los numeros de manera que parezca una matriz
            if(i%5==0):
                print("")
        print("")

def bombo_generando_numeros(bombo):
    '''
    Funcion que genera un los numeros que van del 1 al 99 con los que se jugara el bingo

    Parametros:
    ------------
        bombo : Lista
            variables donde se guardaran los numeros que genere el bombo

    Retorna:
    ------------
        Retorna la variable numero la cual es un numero aleatorio entre 1 y 99 como int.
    '''
    #En este while mientras el tamaño del bombo sea menor a 100 entonces
    while len(bombo) < 100:      
            #generamos numeros aleatorios del 1 al 99
            numero = random.randint(1, 99)
            #en donde si el numero generado no se encuentra en la lista entonces
            if numero not in bombo:
                #se lo agregara a la lista y retornara el numero generado para ser comparado con los cartones de los jugadores
                bombo.append(numero)      
                return numero            

def mensaje_ganador():
    '''
    Funcion que imprime en letras gigantes la palabra "BINGO" en color verde

    Parametros:
    ------------
        Esta funcion no tiene parametros.

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    print(chr(27)+"[1;32m") 
    print("████████      ██████████   ██       ██    ██████████   ██████████")
    print("██     ██         ██       ████     ██    ██           ██      ██")
    print("██      ██        ██       ██ ██    ██    ██           ██      ██")
    print("████████          ██       ██  ██   ██    ██    ████   ██      ██")
    print("██      ██        ██       ██   ██  ██    ██      ██   ██      ██")
    print("██     ██         ██       ██    ██ ██    ██      ██   ██      ██")
    print("████████      ██████████   ██     ████    ██████████   ██████████")

if __name__ == '__main__':
    #En carton1,carton2,carton3 y carton 4 se declaran como listas en las cuales se generaran numeros aleatorios en los cartones de los jugadores
    carton1=[]
    carton2=[]
    carton3=[]
    carton4=[] 
    #se declara la lista bombo en donde se generaran los numeros del 1 al 99 para poder jugar el bingo
    bombo=[]
    #En esta lista es en donde se guardaran el numero de nombres ingresados por el o los usuarios(donde el maximo de nombres sera 4)
    nombresJugadores=[]
    #Esta linea imprime la bienvenida al juego en color amarillo haciendo uso de formato ascii
    print(chr(27)+"[1;33m"+"BIENVENIDO(S) AL JUEGO DEL BINGO!") 
    #Esta funcion imprime la palabra bingo la cual aparecera en la presentacion del juego
    imprimir_logo_del_juego()
    #Esta linea imprime la maxima cantidad de jugadores que podran participar en color rojo 
    print(chr(27)+"[1;31m"+"(MAXIMO 4 JUGADORES))")
    #En este print hacemos que de ahora en adelante las letras se impriman de color cian
    print(chr(27)+"[;36m") 
    #en la variable "nJugadoresla vamos a igualar a una funcion en donde se ingresara un numero y en caso de que lo que se haya ingresado no sea un numero
    #entero entonces tendra que volver a ingresar un valor hasta que sea un numero entero
    nJugadores=ingreso_numero_de_jugadores() 
    #En el ciclo repetitivo while esta la condicion que dice que si "nJugadores" sera menor a 1 o mayor a 4 entonces:
    while nJugadores<1 or nJugadores>4:         
        #habra que volver a ingresar un numero ya que el juego te especifica el maximo de jugadores
        nJugadores=ingreso_numero_de_jugadores()   
    
    #en esta funcion mandaremos como argumento el valor entero de nJugadores y la lista "nombresJugadores" ya que segun el valor de nJugadores 
    #se ingresara un numero de nombres en la lista
    ingreso_nombre_de_jugadores(nombresJugadores,nJugadores)
    #se generan cartones para el numero de jugares que vayan a participar
    generacion_de_cartones(carton1,carton2,carton3,carton4,nJugadores)
    #funcion que limpia la pantalla
    os.system("cls")
    #imprimimos el numero de cartones segun el numero de participantes
    imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
    
    #pausamos el codigo hasta que se presione una tecla
    os.system("Pause")
    #imprimimos el mensaje de empezar el juego en color verde
    print(chr(27)+"[1;32m"+"EMPEZANDO EL JUEGO...") 
    #pausamos el codigo hasta que se presione una tecla
    os.system("Pause")
    #igualamos a la variable numeroDeBolas a cero para mas despues sumar 1 cada vez que se genera una bola hasta que sean 99
    numeroDeBolas=0 
    #mientras la variable numeroDeBolas sea menor o igual a 99 entonces
    while (numeroDeBolas<=99): 
        #generamos una bola y guardamos el numero de esa bola en la variable "bolaGenerada"
        bolaGenerada=bombo_generando_numeros(bombo)
        #se imprime el numero de la bola generada en color rojo
        print(chr(27)+"[1;31m"+"EL BOMBO HA ARROJADO EL NUMERO: ",bolaGenerada) 
        #Si el numero de jugadores es 1 entonces 
        if(nJugadores==1):
            #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
            if(bolaGenerada in carton1):         
                #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la variable bolaGenerada en la lista
                # vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                carton1[carton1.index(bolaGenerada)]=0 
                                            
            #ahora se imprimiran las letras en color amarillo
            print("\x1b[1;33m"+"-------------------------")
            #si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
            if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break 
            #si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)    
            elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
            elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0): 
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
            elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
            elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)    
            elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)    
            elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)   
            elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)    
            elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)    
            elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,7,19,25 son igual a cero(una equis)    
            elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,9,17,21 son igual a cero(una equis)    
            elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #se imprime los cartones segun el numero de jugadores
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        #Si el numero de jugadores es 2 entonces 
        if(nJugadores==2):
            #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
            if(bolaGenerada in carton1):             
                #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la variable bolaGenerada en la lista
                # vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                carton1[carton1.index(bolaGenerada)]=0  
                                            
            #ahora se imprimiran las letras en color amarillo
            print("\x1b[1;33m"+"-------------------------")
            #si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
            if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break 
            #si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)    
            elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 3,8,18,23 son igual a cero(una linea vertical)     
            elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0): 
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)    
            elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)    
            elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)    
            elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)    
            elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)    
            elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)    
            elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)    
            elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,7,19,25 son igual a cero(una equis)    
            elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,9,17,21 son igual a cero(una equis)    
            elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si el numero de la variable generada se encuentra dentro de la lista carton2 entonces
            if(bolaGenerada in carton2): 
                #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la variable bolaGenerada en la lista 
                #vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                carton2[carton2.index(bolaGenerada)]=0 
                                            
            #si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
            if(carton2[1]==0 and carton2[6]==0 and carton2[11]==0 and carton2[16]==0 and carton2[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
            elif(carton2[2]==0 and carton2[7]==0 and carton2[12]==0 and carton2[17]==0 and carton2[22]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 3,8,18,23 son igual a cero(una linea vertical)    
            elif(carton2[3]==0 and carton2[8]==0 and carton2[18]==0 and carton2[23]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)    
            elif(carton2[4]==0 and carton2[9]==0 and carton2[14]==0 and carton2[19]==0 and carton2[24]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)    
            elif(carton2[5]==0 and carton2[10]==0 and carton2[15]==0 and carton2[20]==0 and carton2[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
            elif(carton2[1]==0 and carton2[2]==0 and carton2[3]==0 and carton2[4]==0 and carton2[5]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)    
            elif(carton2[6]==0 and carton2[7]==0 and carton2[8]==0 and carton2[9]==0 and carton2[10]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 11,12,14,15son igual a cero(una linea horizontal)    
            elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)    
            elif(carton2[16]==0 and carton2[17]==0 and carton2[18]==0 and carton2[19]==0 and carton2[20]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
            elif(carton2[21]==0 and carton2[22]==0 and carton2[23]==0 and carton2[24]==0 and carton2[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,7,19,25 son igual a cero(una cruz)
            elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,9,17,21 son igual a cero(una cruz)
            elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #se imprime los cartones segun el numero de jugadores
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)   
        #Si el numero de jugadores es 3 entonces     
        if(nJugadores==3):
            #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
            if(bolaGenerada in carton1):     
                #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la variable bolaGenerada en la lista 
                #vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                carton1[carton1.index(bolaGenerada)]=0 
                                            
            #ahora se imprimiran las letras en color amarillo
            print("\x1b[1;33m"+"-------------------------")

            if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):#si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break #con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):#si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0): #si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):#si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):#si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):#si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):#si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):#si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):#si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            if(bolaGenerada in carton2):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton2[carton2.index(bolaGenerada)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la
                                            #variable bolaGenerada en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            
            if(carton2[1]==0 and carton2[6]==0 and carton2[11]==0 and carton2[16]==0 and carton2[21]==0):#si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[2]==0 and carton2[7]==0 and carton2[12]==0 and carton2[17]==0 and carton2[22]==0):#si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[3]==0 and carton2[8]==0 and carton2[18]==0 and carton2[23]==0):#si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[4]==0 and carton2[9]==0 and carton2[14]==0 and carton2[19]==0 and carton2[24]==0):#si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[5]==0 and carton2[10]==0 and carton2[15]==0 and carton2[20]==0 and carton2[25]==0):#si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[1]==0 and carton2[2]==0 and carton2[3]==0 and carton2[4]==0 and carton2[5]==0):#si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[6]==0 and carton2[7]==0 and carton2[8]==0 and carton2[9]==0 and carton2[10]==0):#si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[16]==0 and carton2[17]==0 and carton2[18]==0 and carton2[19]==0 and carton2[20]==0):#si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[21]==0 and carton2[22]==0 and carton2[23]==0 and carton2[24]==0 and carton2[25]==0):#si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            if(bolaGenerada in carton3):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton3[carton3.index(bolaGenerada)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                        #variable bolaGenerada en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            
            if(carton3[1]==0 and carton3[6]==0 and carton3[11]==0 and carton3[16]==0 and carton3[21]==0): #si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado           
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[2]==0 and carton3[7]==0 and carton3[12]==0 and carton3[17]==0 and carton3[22]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[3]==0 and carton3[8]==0 and carton3[18]==0 and carton3[23]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[4]==0 and carton3[9]==0 and carton3[14]==0 and carton3[19]==0 and carton3[24]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[5]==0 and carton3[10]==0 and carton3[15]==0 and carton3[20]==0 and carton3[25]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[1]==0 and carton3[2]==0 and carton3[3]==0 and carton3[4]==0 and carton3[5]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[6]==0 and carton3[7]==0 and carton3[8]==0 and carton3[9]==0 and carton3[10]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[11]==0 and carton3[12]==0  and carton3[14]==0 and carton3[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[16]==0 and carton3[17]==0 and carton3[18]==0 and carton3[19]==0 and carton3[20]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[21]==0 and carton3[22]==0 and carton3[23]==0 and carton3[24]==0 and carton3[25]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[1]==0 and carton3[7]==0  and carton3[19]==0 and carton3[25]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[5]==0 and carton3[9]==0  and carton3[17]==0 and carton3[21]==0):
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
        if(nJugadores==4):
            if(bolaGenerada in carton1):               #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton1[carton1.index(bolaGenerada)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                            #variable bolaGenerada en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                                            
            print("\x1b[1;33m"+"-------------------------")#ahora se imprimiran las letras en color amarillo

            if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):#si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break #con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):#si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0): #si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):#si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):#si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):#si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):#si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0])#se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):#si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):#si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 1 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            if(bolaGenerada in carton2):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton2[carton2.index(bolaGenerada)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la
                                        #variable bolaGenerada en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada 
            
            if(carton2[1]==0 and carton2[6]==0 and carton2[11]==0 and carton2[16]==0 and carton2[21]==0):#si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[2]==0 and carton2[7]==0 and carton2[12]==0 and carton2[17]==0 and carton2[22]==0):#si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[3]==0 and carton2[8]==0 and carton2[18]==0 and carton2[23]==0):#si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[4]==0 and carton2[9]==0 and carton2[14]==0 and carton2[19]==0 and carton2[24]==0):#si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[5]==0 and carton2[10]==0 and carton2[15]==0 and carton2[20]==0 and carton2[25]==0):#si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[1]==0 and carton2[2]==0 and carton2[3]==0 and carton2[4]==0 and carton2[5]==0):#si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[6]==0 and carton2[7]==0 and carton2[8]==0 and carton2[9]==0 and carton2[10]==0):#si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[16]==0 and carton2[17]==0 and carton2[18]==0 and carton2[19]==0 and carton2[20]==0):#si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[21]==0 and carton2[22]==0 and carton2[23]==0 and carton2[24]==0 and carton2[25]==0):#si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            if(bolaGenerada in carton3):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton3[carton3.index(bolaGenerada)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                        #variable bolaGenerada en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            
            if(carton3[1]==0 and carton3[6]==0 and carton3[11]==0 and carton3[16]==0 and carton3[21]==0): #si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado           
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[2]==0 and carton3[7]==0 and carton3[12]==0 and carton3[17]==0 and carton3[22]==0):#si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[3]==0 and carton3[8]==0 and carton3[18]==0 and carton3[23]==0):#si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[4]==0 and carton3[9]==0 and carton3[14]==0 and carton3[19]==0 and carton3[24]==0):#si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
            elif(carton3[5]==0 and carton3[10]==0 and carton3[15]==0 and carton3[20]==0 and carton3[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
            elif(carton3[1]==0 and carton3[2]==0 and carton3[3]==0 and carton3[4]==0 and carton3[5]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
            elif(carton3[6]==0 and carton3[7]==0 and carton3[8]==0 and carton3[9]==0 and carton3[10]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
            elif(carton3[11]==0 and carton3[12]==0  and carton3[14]==0 and carton3[15]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
            elif(carton3[16]==0 and carton3[17]==0 and carton3[18]==0 and carton3[19]==0 and carton3[20]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
            elif(carton3[21]==0 and carton3[22]==0 and carton3[23]==0 and carton3[24]==0 and carton3[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
                #si las posiciones 1,7,19,25 son igual a cero(una equis)
            elif(carton3[1]==0 and carton3[7]==0  and carton3[19]==0 and carton3[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
                #si las posiciones 5,9,17,21 son igual a cero(una equis)
            elif(carton3[5]==0 and carton3[9]==0  and carton3[17]==0 and carton3[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2])
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            if(bolaGenerada in carton4):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la variable bolaGenerada en la lista
                # vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                carton4[carton4.index(bolaGenerada)]=0
                                        
            #si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
            if(carton4[1]==0 and carton4[6]==0 and carton4[11]==0 and carton4[16]==0 and carton4[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
            elif(carton4[2]==0 and carton4[7]==0 and carton4[12]==0 and carton4[17]==0 and carton4[22]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
            elif(carton4[3]==0 and carton4[8]==0 and carton4[18]==0 and carton4[23]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
            elif(carton4[4]==0 and carton4[9]==0 and carton4[14]==0 and carton4[19]==0 and carton4[24]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
            elif(carton4[5]==0 and carton4[10]==0 and carton4[15]==0 and carton4[20]==0 and carton4[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
            elif(carton4[1]==0 and carton4[2]==0 and carton4[3]==0 and carton4[4]==0 and carton4[5]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
            elif(carton4[6]==0 and carton4[7]==0 and carton4[8]==0 and carton4[9]==0 and carton4[10]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
            elif(carton4[11]==0 and carton4[12]==0  and carton4[14]==0 and carton4[15]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
            elif(carton4[16]==0 and carton4[17]==0 and carton4[18]==0 and carton4[19]==0 and carton4[20]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
            elif(carton4[21]==0 and carton4[22]==0 and carton4[23]==0 and carton4[24]==0 and carton4[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 1,7,19,25 son igual a cero(una equis)
            elif(carton4[1]==0 and carton4[7]==0  and carton4[19]==0 and carton4[25]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
            #si las posiciones 5,9,17,21 son igual a cero(una equis)
            elif(carton4[5]==0 and carton4[9]==0  and carton4[17]==0 and carton4[21]==0):
                #entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                mensaje_ganador()
                #se imprime el nombre del jugador ganador en color amarillo
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
                #con este break rompemos el ciclo repetitivo finalizando el programa
                break
                #se imprime los cartones segun el numero de jugadores    
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        #pausamos el codigo hasta aplastar una tecla
        os.system("Pause")
    print()

import random #imporatmos random para usar la funcion de generar numeros aleatorios
import os     #importamos os para hacer uso de la funcion que limpia la pantalla y pausa en el codigo
os.system("cls")#esta funcion limpia la pantalla

"""
Bingoconsiste en ir marcando en nuestro cartón los números que, aleatoriamente, van surgiendo en cada momento. 
El primero que haga línea gana un premio
Autores:
Luis Cueva
Lisbeth Carvajal
Erick Ramirez
Verisión:
VER.2
"""

def imprimir_logo_del_juego():
    '''
    Funcion que imprime en letras gigantes "BINGO" en color azul
    '''
    print(chr(27)+"[1;34m")#azul
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

    Retorna
    -------
    Retorna la variable numJugadores como int
    '''
    while True:#para validar usamos un ciclo for donde mientras sea verdad:
        try:
            numJugadores=int(input("Ingrese el numero de jugadores: "))#ingresamos un numero
            break
        except ValueError:
            print("No ha ingresado un numero entero.")#si ve que lo que se ha ingresado no es un numero entero entonces imprimira un mensaje de error
    return numJugadores

def ingreso_nombre_de_jugadores(nombresJugadores,nJugadores):
    '''
    Funcion donde el jugador podra ingresar su nombre dentro del juego

    Parametros
    ----------
    nombresJugadores : lista
        Variable donde se guardara los nombres de los participantes segun nJugadores
    nJugadores       : int
        Variable entera que indica cuantos jugadores estan participando
    '''
    for i in range(nJugadores):
        print(chr(27)+"[1;37m"+"JUGADOR ",i+1)#En este print("") hacemos uso del de formatos ascii en donde le pondra color a las letras
        print(chr(27)+"[;36m") 
        nombres=input("Ingrese nombre del jugador:")#ingresamosnombre jugador
        nombresJugadores.append(nombres)
    os.system("cls")#el os.system("cls") permite limpiar la pantalla

def generacion_de_cartones(carton1,carton2,carton3,carton4,nJugadores):
    '''
    En esta funcion segun el numero de jugadores se va generando un carton con 25 numeros aleatorios para cada uno de los participantes

    Parametros
    ----------
    carton1    : Lista
    carton2    : Lista
    carton3    : Lista
    carton4    : Lista
        variables donde se generaran los 25 numeros para jugar al bingo
    nJugadores : int
        Variable entera que indica cuantos jugadores estan participando
    '''
    if(nJugadores==1): #si solo hay un jugador entonces solo se generara un carton para él
        while len(carton1) < 26:        #En este ciclo while hacemos que genere un numero aleatorio entre el 1y y 99en la variable "numero"
            numero = random.randint(1, 99)
            if numero not in carton1:      #Si el numero que se ha generado no existe dentro de la lista "carton1" entonces 
                carton1.append(numero)     #se lo agregara a la lista, asi validamos de que no se agreguen numeros repetidos en la lista
        carton1[13]=0   #como en todo carton del juego del bingo se iguala a cero la posicio 13 del carton ya que no hay numero 
                        #central en los cartones(0 significa que no hay numero en este caso)
        
    if(nJugadores==2):#si hay dos jugadores entonces solo se generara dos cartones para los dos participantes

        #En estos dos ciclos whiles es donde se generaran los cartones con numeros aleatoreos para los 2 jugadores haciendo el mismo metodo que en el primer if
        while len(carton1) < 26:
            numero = random.randint(1, 99) #En este ciclo while hacemos que genere un numero aleatorio entre el 1y y 99en la variable "numero"
            if numero not in carton1:
                carton1.append(numero)
        while len(carton2) < 26:
            numero = random.randint(1, 99)#En este ciclo while hacemos que genere un numero aleatorio entre el 1y y 99en la variable "numero"
            if numero not in carton2:
                carton2.append(numero)
        carton1[13]=0
        carton2[13]=0  #De igual manera en todos los cartones en la posicion del numero 13 se igualara a cero
        
    if(nJugadores==3):#si hay tres jugadores entonces se generara tres cartones para los tres participantes
        #En estos 3 ciclos whiles es donde se generaran los cartones con numeros aleatoreos 
        # para los 3 jugadores haciendo el mismo metodo que en los dos primeros if
        while len(carton1) < 26:
            numero = random.randint(1, 99)#En este ciclo while hacemos que genere un numero aleatorio entre el 1y y 99en la variable "numero"
            if numero not in carton1:
                carton1.append(numero)
        while len(carton2) < 26:
            numero = random.randint(1, 99)#En este ciclo while hacemos que genere un numero aleatorio entre el 1y y 99en la variable "numero"
            if numero not in carton2:
                carton2.append(numero)
        while len(carton3) < 26:
            numero = random.randint(1, 99)#En este ciclo while hacemos que genere un numero aleatorio entre el 1y y 99en la variable "numero"
            if numero not in carton3:
                carton3.append(numero)
        carton1[13]=0
        carton2[13]=0
        carton3[13]=0 #Igualamos a cero en la posicion 13 en los 3 cartones
          
    if(nJugadores==4):#si hay cuatrp jugadores entonces se generara cuatro cartones para los cuatro participantes
        #En estos 4 ciclos whiles es donde se generaran los cartones con numeros aleatoreos 
        # para los 4 jugadores haciendo el mismo metodo que en los tres primeros if
        while len(carton1) < 26:
            numero = random.randint(1, 99)
            if numero not in carton1:
                carton1.append(numero)
        while len(carton2) < 26:
            numero = random.randint(1, 99)
            if numero not in carton2:
                carton2.append(numero)
        while len(carton3) < 26:
            numero = random.randint(1, 99)
            if numero not in carton3:
                carton3.append(numero)
        while len(carton4) < 26:
            numero = random.randint(1, 99)
            if numero not in carton4:
                carton4.append(numero)
        carton1[13]=0
        carton2[13]=0
        carton3[13]=0
        carton4[13]=0 #Igualamos a cero en la posicion 13 en los 4 cartones



def imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores):
    '''
    Funcion que imprime el carto de los participantes segun el numero de jugadores

    Parametros
    ----------
    carton1    : Lista
    carton2    : Lista
    carton3    : Lista
    carton4    : Lista
        variables donde se generaran los 25 numeros para jugar al bingo
    nJugadores : int
        Variable entera que indica cuantos jugadores estan participando
    '''
    if (nJugadores==1):#En este if si solo hay un jugador solo se imprimira 1 carton para jugar
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m")#hacemos que las letras se impriman de color cian
        for i in range(1,len(carton1)):#con este for y segun el tamaño de la lista carton1(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton1[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0): #con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")   
        print("")

    if (nJugadores==2):#En este if si hay dos jugadores solo se imprimira 2 cartones para jugar
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m")#hacemos que las letras se impriman de color cian
        for i in range(1,len(carton1)):#con este for y segun el tamaño de la lista carton1(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton1[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m") #hacemos que las letras se impriman de color cian
        for i in range(1,len(carton2)):#con este for y segun el tamaño de la lista carton2(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton2[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

    if (nJugadores==3):#En este if si hay 3 jugadores solo se imprimira 3 cartones para jugar
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m")#hacemos que las letras se impriman de color cian
        for i in range(1,len(carton1)):#con este for y segun el tamaño de la lista carton1(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton1[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m")#hacemos que las letras se impriman de color cian
        for i in range(1,len(carton2)):#con este for y segun el tamaño de la lista carton2(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton2[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[2],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m") #hacemos que las letras se impriman de color cian
        for i in range(1,len(carton3)):#con este for y segun el tamaño de la lista carton3(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton3[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

    if (nJugadores==4):#En este if si hay 4 jugadores se imprimira 4 cartones para jugar
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m") #hacemos que las letras se impriman de color cian
        for i in range(1,len(carton1)):#con este for y segun el tamaño de la lista carton1(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton1[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m") #hacemos que las letras se impriman de color cian
        for i in range(1,len(carton2)):#con este for y segun el tamaño de la lista carton2(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton2[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[2],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m") #hacemos que las letras se impriman de color cian
        for i in range(1,len(carton3)):#con este for y segun el tamaño de la lista carton3(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton3[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[3],":")#Aqui se imprime el nombre del jugador
        print(chr(27)+"[1;36m") #hacemos que las letras se impriman de color cian
        for i in range(1,len(carton4)):#con este for y segun el tamaño de la lista carton4(calculamos el tamaño con la funcion len) imprimimos los numeros
            print(carton4[i]," ",end="")#se imprime los numeros generados para el carton
            if(i%5==0):#con este if hacemos que se impriman los numeros de manera que parezca una matriz
                print("")
        print("")

def bombo_generando_numeros(bombo):
    '''
    Funcion que genera un los numeros que van del 1 al 99 con los que se jugara el bingo

    Parametros
    ----------
    bombo : Lista
        variables donde se guardaran los numeros que genere el bombo

    Retorna
    -------
    Retorna la variable numero como entero
    '''
    while len(bombo) < 100:               # en este while mientras el tamaño del bombo sea menor a 100 entonces 
            numero = random.randint(1, 99)#generamos numeros aleatorios del 1 al 99
            if numero not in bombo:       #en donde si el numero generado no se encuentra en la lista entonces
                bombo.append(numero)      #se lo agregara a la lista y retornara el numero generado para ser comparado con los cartones
                return numero             #de los jugadores

def mensaje_ganador():
    '''
    Funcion que imprime en letras gigantes la palabra "BINGO" en color verde
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

    bombo=[]#se declara la lista bombo en donde se generaran los numeros del 1 al 99 para poder jugar el bingo
    nombresJugadores=[]#En esta lista es en donde se guardaran el numero de nombres ingresados por el o los usuarios(donde el maximo de nombres sera 4)
    print(chr(27)+"[1;33m"+"BIENVENIDO(S) AL JUEGO DEL BINGO!") #Esta linea imprime la bienvenida al juego en color amarillo haciendo uso de formato ascii
    imprimir_logo_del_juego()#Esta funcion imprime la palabra bingo la cual aparecera en la presentacion del juego
    print(chr(27)+"[1;31m"+"(MAXIMO 4 JUGADORES))")#Esta linea imprime la maxima cantidad de jugadores que podran participar en color rojo 
    print(chr(27)+"[;36m") #En este print hacemos que de ahora en adelante las letras se impriman de color cian

    nJugadores=ingreso_numero_de_jugadores()#en la variable "nJugadoresla vamos a igualar a una funcion en donde 
                                            #se ingresara un numero y en caso de que lo que se haya ingresado no sea un numero
                                            #entero entonces tendra que volver a ingresar un valor hasta que sea un numero entero

    while nJugadores<1 or nJugadores>4:             #En el ciclo repetitivo while esta la condicion que dice que si "nJugadores" sera menor a 1 o mayor a 4 
        nJugadores=ingreso_numero_de_jugadores()    #entonces tendra que volver a ingresar un numero ya que el juego te especifica que solo podras ingresar
                                                    #el 1,2,3 y 4

    ingreso_nombre_de_jugadores(nombresJugadores,nJugadores)#en esta funcion mandaremos como argumento el valor entero de nJugadores y la 
                                                            #lista "nombresJugadores" ya que segun el valor de nJugadores se ingresara un numero de
                                                            #nombres en la lista

    generacion_de_cartones(carton1,carton2,carton3,carton4,nJugadores)#se generan cartones para el numero de jugares que vayan a participar
    os.system("cls")#funcion que limpia la pantalla
    imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#imprimimos el numero de cartones segun el numero de participantes

    os.system("Pause")#pausamos el codigo hasta que se presione una tecla
    print(chr(27)+"[1;32m"+"EMPEZANDO EL JUEGO...") #imprimimos el mensaje de empezar el juego en color verde
    os.system("Pause")#pausamos el codigo hasta que se presione una tecla
    numeroDeBolas=0 #igualamos a la variable numeroDeBolas a cero para mas despues sumar 1 cada vez que se genera una bola hasta que sean 99

    while (numeroDeBolas<=99): #mientras la variable numeroDeBolas sea menor o igual a 99 entonces
        x=bombo_generando_numeros(bombo)#generamos una bola y guardamos el numero de esa bola en la variable "x"
        print(chr(27)+"[1;31m"+"EL BOMBO HA ARROJADO EL NUMERO: ",x) #se imprime el numero de la bola generada en color rojo
        if(nJugadores==1):#Si el numero de jugadores es 1 entonces 
            if(x in carton1):               #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton1[carton1.index(x)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                            #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
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

        if(nJugadores==2):#Si el numero de jugadores es 2 entonces 
            if(x in carton1):               #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton1[carton1.index(x)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                            #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
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

            if(x in carton2): #si el numero de la variable generada se encuentra dentro de la lista carton2 entonces
                carton2[carton2.index(x)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                            #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
            print("\x1b[1;33m"+"-------------------------")
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
            elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):#si las posiciones 11,12,14,15son igual a cero(una linea horizontal)
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
            elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una cruz)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una cruz)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 2 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
        
        if(nJugadores==3):#Si el numero de jugadores es 3 entonces 
            if(x in carton1):               #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton1[carton1.index(x)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                            #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
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
            if(x in carton2):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton2[carton2.index(x)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la
                                            #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
            print("\x1b[1;33m"+"-------------------------")
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
            if(x in carton3):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton3[carton3.index(x)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                        #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#imprime el carton de los participantes
            print("\x1b[1;33m"+"-------------------------")
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
            
        if(nJugadores==4):
            if(x in carton1):               #si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton1[carton1.index(x)]=0 #con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                            #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
                                            
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#se imprime los cartones segun el numero de jugadores
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
            if(x in carton2):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton2[carton2.index(x)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la
                                        #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada 
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#imprime los cartones de los participantes
            print("\x1b[1;33m"+"-------------------------")
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
            if(x in carton3):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton3[carton3.index(x)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                        #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#imprime el carton de los participantes
            print("\x1b[1;33m"+"-------------------------")
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
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[5]==0 and carton3[10]==0 and carton3[15]==0 and carton3[20]==0 and carton3[25]==0):#si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[1]==0 and carton3[2]==0 and carton3[3]==0 and carton3[4]==0 and carton3[5]==0):#si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[6]==0 and carton3[7]==0 and carton3[8]==0 and carton3[9]==0 and carton3[10]==0):#si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[11]==0 and carton3[12]==0  and carton3[14]==0 and carton3[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[16]==0 and carton3[17]==0 and carton3[18]==0 and carton3[19]==0 and carton3[20]==0):#si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[21]==0 and carton3[22]==0 and carton3[23]==0 and carton3[24]==0 and carton3[25]==0):#si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[1]==0 and carton3[7]==0  and carton3[19]==0 and carton3[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton3[5]==0 and carton3[9]==0  and carton3[17]==0 and carton3[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 3 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            if(x in carton4):#si el numero de la variable generada se encuentra dentro de la lista carton1 entonces
                carton4[carton4.index(x)]=0#con la ayuda de la funcion index la cual nos dice la posicion de donde se encuentra el valor de la 
                                        #variable x en la lista vamos a reemplazar ese numero a cero lo cual significa que ya ha sido marcada
            imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)#imprime el carton de los participantes
            print("\x1b[1;33m"+"-------------------------")
            if(carton4[1]==0 and carton4[6]==0 and carton4[11]==0 and carton4[16]==0 and carton4[21]==0):#si las posiciones 1,6,11,16,21 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[2]==0 and carton4[7]==0 and carton4[12]==0 and carton4[17]==0 and carton4[22]==0):#si las posiciones 2,7,12,17,22 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[3]==0 and carton4[8]==0 and carton4[18]==0 and carton4[23]==0):#si las posiciones 3,8,18,23 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[4]==0 and carton4[9]==0 and carton4[14]==0 and carton4[19]==0 and carton4[24]==0):#si las posiciones 4,9,14,19,24 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[5]==0 and carton4[10]==0 and carton4[15]==0 and carton4[20]==0 and carton4[25]==0):#si las posiciones 5,10,15,20,25 son igual a cero(una linea vertical)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[1]==0 and carton4[2]==0 and carton4[3]==0 and carton4[4]==0 and carton4[5]==0):#si las posiciones 1,2,3,4,5 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break
            elif(carton4[6]==0 and carton4[7]==0 and carton4[8]==0 and carton4[9]==0 and carton4[10]==0):#si las posiciones 6,7,8,9,10 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[11]==0 and carton4[12]==0  and carton4[14]==0 and carton4[15]==0):#si las posiciones 11,12,14,15 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[16]==0 and carton4[17]==0 and carton4[18]==0 and carton4[19]==0 and carton4[20]==0):#si las posiciones 16,17,18,19,20 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[21]==0 and carton4[22]==0 and carton4[23]==0 and carton4[24]==0 and carton4[25]==0):#si las posiciones 21,22,23,24,25 son igual a cero(una linea horizontal)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[1]==0 and carton4[7]==0  and carton4[19]==0 and carton4[25]==0):#si las posiciones 1,7,19,25 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
            elif(carton4[5]==0 and carton4[9]==0  and carton4[17]==0 and carton4[21]==0):#si las posiciones 5,9,17,21 son igual a cero(una equis)
                mensaje_ganador()#entonces se imprime la palabra bingo como señal de que el jugador 4 ha ganado
                print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) #se imprime el nombre del jugador ganador en color amarillo
                break#con este break rompemos el ciclo repetitivo finalizando el programa
                
        os.system("Pause")#pausamos el codigo hasta aplastar una tecla
    print()

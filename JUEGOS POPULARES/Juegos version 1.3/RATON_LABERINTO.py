import os #importamos os para usar la funcion os.system("pause") y os.system("cls")
import time #importamos time para usar la funcion time.sleep
import sys #importamos sys para usar sys.exit()
"""
Raton en el laberinto, consiste en mover al raton con datos ingresados por el usuario hasta que el raton
salga del laberinto 

Autores:
Luis Fernando Cueva Flores
Lisbeth Adali Carvajal Escobar
Erick Patricio Ramirez Ortiz

Verisión:
VER.1.3
"""
def dibujo_presentacion_del_juego():
    '''
    Imprime el dibujo de una cabeza de raton al inicio del juego.

    Parametros:
    ------------
        Esta funcion no tiene parametros.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    print(chr(27)+"[1;33m"+"BIENVENIDO AL JUEGO DE RATON EN EL LABERINTO") #imprime mensaje de bienvenida en color amarillo
    print("\033[1;36m")#imprime las letras en color cian
    print("        █████           █████")
    print("       ██    ██       ██     ██")
    print("      ██      ████████        ██")
    print("       ██    ██       ██     ██")
    print("         ████           █████")
    print(chr(27)+"[1;37m"+"       ███         ███",chr(27)+"[1;36m"+"    ██") 
    print("\033[1;31m",end="")
    print("    ███ ",chr(27)+"[1;36m"+"                ██")
    print("\033[1;36m",end="")
    print("       ███████████       ██")
    print("            ██           ██")
    print("            ██           ██")


def elegir_movimiento_del_raton():
    '''
    Funcion donde se valida si es que el numero ingresado por el jugador es entero, si lo que se ingresó no es un numero
    entero entonces el jugador tendra que volver a ingresar un numero

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        Una vez que el numero ingresado haya sido validado, será la variable movimiento raton la que se retornará como entero
    '''
    #mientras sea verdadero se ingresara un dato en la variable raton, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el jugador debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            movimiento_raton=int(input("Elija una opcion: "))
            break#rempemos ciclo repetitivo
        except ValueError:
            print("No ha ingresado un numero entero.")
    #retornamos la variable movimiento_raton como int
    return movimiento_raton

def imprimir_mapa(mapa):
    '''
    Funcion que imprime el mapa segun el numero de filas y columnas, donde 1 es el camino por donde puede pasar, 2 es el raton y cero es pared

    Parametros:
    ------------
        mapa: lista
            Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato

    '''
    for i in range (8):
        for j in range(11):
            #si la pisición del mapa[i][j] es 1 entonces se imprimira "█" en color blanco
            if(mapa[i][j]==1):
                print(chr(27)+"[1;37m"+"█",end="")
            #si la pisición del mapa[i][j] es 2 entonces se imprimira "█" en color verde
            elif(mapa[i][j]==2):
                print(chr(27)+"[1;32m"+"█",end="") 
            #caso contrario se imprimira "█" en color morado
            else:
                print(chr(27)+"[1;35m"+"█",end="")
        #imprime un salto de linea
        print("")

def movimiento_del_raton_arriba(mapa):
    '''
    Funcion que permite que el raton se mueva hacia arriba dentro del mapa

    Parametros:
    ------------
        mapa: lista
            Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa 
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                posicionFila=i                           #igualaremos posicionFila y posicionColumna con i e j
                posicionColumna=j
                
    if(mapa[posicionFila-1][posicionColumna]==1):#entonces para mover al rato arriba hacemos uso de la formula (posicionFila-1)(posicionColumna) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[posicionFila-1][posicionColumna]=2  #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[posicionFila][posicionColumna]=1    #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                                 #haciendo ver que el raton se ha movido de posicion

def movimiento_del_raton_abajo(mapa):
    '''
    Funcion que permite que el raton se mueva hacia abajo dentro del mapa

    Parametros:
    ------------
        mapa: lista
            Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                posicionFila=i                #igualaremos posicionFila y posicionColumna con i e j 
                posicionColumna=j                           
                
    if(mapa[posicionFila+1][posicionColumna]==1):#entonces para mover al rato abajo hacemos uso de la formula (posicionFila+1)(posicionColumna) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[posicionFila+1][posicionColumna]=2  #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[posicionFila][posicionColumna]=1    #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                                 #haciendo ver que el raton se ha movido de posicion

def movimiento_del_raton_izquierda(mapa):
    '''
    Funcion que permite que el raton se mueva hacia la izquierda dentro del mapa

    Parametros:
    -------------
        mapa: lista
            Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton
    
    Retorna:
    -------------
        Esta funcion no retorna ningun tipo de dato
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                posicionFila=i                #igualaremos posicionFila y b con i e j
                posicionColumna=j
                
    if(mapa[posicionFila][posicionColumna-1]==1):#entonces para mover al rato abajo hacemos uso de la formula (posicionFila)(posicionColumna-1) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[posicionFila][posicionColumna-1]=2  #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[posicionFila][posicionColumna]=1    #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                                 #haciendo ver que el raton se ha movido de posicion

def movimiento_del_raton_derecha(mapa):
    '''
    Funcion que permite que el raton se mueva hacia la derecha dentro del mapa

    Parametros:
    -------------
        mapa: lista
         Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton

    Retorna:
    -------------
        Esta funcion no retorna ningun tipo de dato
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa 
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                aposicionFila=i               #igualaremos posicionFila y posicionColumna con i e j
                posicionColumna=j
                
    if(mapa[aposicionFila][posicionColumna+1]==1):#entonces para mover al rato abajo hacemos uso de la formula (posicionFila)(posicionColumna+1) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[aposicionFila][posicionColumna+1]=2  #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[aposicionFila][posicionColumna]=1    #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                                  #haciendo ver que el raton se ha movido de posicion

def mensaje_ganador():
    '''
    Funcion que imprime "GANASTE" en color verde una vez finalizado el juego

    Parametros:
    -------------
        Esta funcion no tiene parametros

    Retorna:
    -------------
        Esta funcion no retorna ningun tipo de dato

    '''
    print(chr(27)+"[1;32m")#Print que hace que los siguientes caracteres se impriman en color verde
    print("███████████   ███████████   ██         ██   ███████████   ███████████   ███████████   ███████████")
    print("██            ██       ██   ████       ██   ██       ██   ██                ██        ██")
    print("██            ██       ██   ██ ██      ██   ██       ██   ██                ██        ██")
    print("██            ██       ██   ██  ██     ██   ██       ██   ██                ██        ██")
    print("██     ████   ███████████   ██   ██    ██   ███████████   ███████████       ██        ███████████")
    print("██       ██   ██       ██   ██    ██   ██   ██       ██            ██       ██        ██")
    print("██       ██   ██       ██   ██     ██  ██   ██       ██            ██       ██        ██")
    print("██       ██   ██       ██   ██      ██ ██   ██       ██            ██       ██        ██")
    print("███████████   ██       ██   ██       ████   ██       ██   ███████████       ██        ███████████")   

def menu_eleccion_de_movimiento():
    print(chr(27)+"[1;33m"+"Hacia donde quieres mover el raton?")#preguntamos hacia donde quiere mover el raton
    print("\033[;36m")#cian
    print("1. Arriba")#imprimimos el menu en color cian
    print("2. Abajo")
    print("3. Izquierda")
    print("4. Derecha")

if __name__ == '__main__':
#definimos el mapa como una matriz en donde "0" es pared, "1" es por donde puede pasar el raton y "2" el raton
    mapa = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #definimos final_laberinto como falso para que el juego siga corriendo hasta llegar al final del laberinto
    final_laberinto=False 
    #imprimos el dibujo del raton al incio del juego
    dibujo_presentacion_del_juego()
    #imprime salto de linea
    print("")
    #hacemos que de ahora en adelantes las letras sean color verde
    print(chr(27)+"[1;32m") 
    #Pausamos el codigo hasta aplastar una tecla
    os.system("pause") 
    print(chr(27)+"[1;37m"+"EMPEZANDO EL JUEGO")
    #hacemos que el codigo tenga un pequeño retraso para simular la carga del juego
    time.sleep(1)
    #limpiamos pantalla
    os.system("cls")

    #imprimos que el ratos es "█" en color verde
    print("Ustes es: ",chr(27)+"[1;32m"+"█")
    #imprimimos el mapa remplazando los numeros por colores
    imprimir_mapa(mapa)
    #mientras aun no se llegue al final del laberinto entonces:
    while(final_laberinto==False):
        
        menu_eleccion_de_movimiento()
        #llamamos a la funcion elegir_movimiento_del_raton() para igualarla a "mov_raton" una vez el dato ingresado sea validado
        mov_raton=elegir_movimiento_del_raton()
        #en este ciclo repetitivo validamos que solo se ingrese numeros mayor a 1 o menor a 4
        while (mov_raton<1 or mov_raton>4):
            #en caso de no cumpla entonces tendremos que volver a ingresar un numero
            mov_raton=elegir_movimiento_del_raton()
        #si el jugador decidió moverse hacia arriba entonces    
        if(mov_raton==1):
            #limpiamos pantalla
            os.system("cls")
            #hacemos uso de esta funcion para mover el raton una posicion arriba
            movimiento_del_raton_arriba(mapa)
            #imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            imprimir_mapa(mapa)
        #si el jugador decidió moverse hacia abajo entonces
        if(mov_raton==2):
            #limpiamos pantalla
            os.system("cls")
            #hacemos uso de esta funcion para mover el raton una posicion abajo
            movimiento_del_raton_abajo(mapa)
            #imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            imprimir_mapa(mapa)
            #si el jugador decidió moverse hacia la izquierda entonces:
        if(mov_raton==3):
            #limpiamos pantalla
            os.system("cls")
            #hacemos uso de esta funcion para mover el raton una posicion a la izquierda
            movimiento_del_raton_izquierda(mapa)
            #imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            imprimir_mapa(mapa)
        #si el jugador decidió moverse hacia la derecha entonces
        if(mov_raton==4):
            #limpiamos pantalla
            os.system("cls")
            #hacemos uso de esta funcion para mover el raton una posicion a la derecha
            movimiento_del_raton_derecha(mapa)
            #imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            imprimir_mapa(mapa)
            #si el raton llego a esta posicion(final del laberinto) entonces
            if(mapa[6][10]==2):
                #imprimimos el mensaje ganador
                mensaje_ganador()
                #finalizamos la ejecucion del codigo
                sys.exit()
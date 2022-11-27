import os #importamos os para usar la funcion os.system("pause") y os.system("cls")
import time #importamos time para usar la funcion time.sleep
import sys #importamos sys para usar sys.exit()
os.system("cls")#funcion para limpiar la pantalla
"""
Raton en el laberinto, consiste en mover al raton hasta que este salga del laberinto 

Autores:
Luis Cueva
Lisbeth Coral
Erick Ramirez

Verisión:
VER.2
"""

def dibujo_presentacion_del_juego():
    '''
    Imprime el dibujo de una cabeza de raton al inicio del juego
    '''
    print("\033[1;36m")
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
    Funcion donde se valida si es que el numero ingresado por el jugador es entero, si lo que se ingreso no es un numero
    entero entonces el jugador tendra que volver a ingresar un numero

    Retorna
    -------
    Una vez que el numero ingresado haya sido validado, será la variable movimiento raton la que se retornará
    Returns True if the vehicle with the specified plate can be on the road at the specified date and time, otherwise False
    '''
    #mientras sea verdadero se ingresara un dato en la variable raton, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el jugador debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            movimiento_raton=int(input("Elija una opcion: "))
            break
        except ValueError:
            print("No ha ingresado un numero entero.")
    #retornamos la variable movimiento_raton
    return movimiento_raton

def imprimir_mapa(mapa):
    '''
    Funcion que imprime el mapa segun el numero de filas y columnas, donde 1 es el camino por donde puede pasar, 2 es el raton y cero es pared

    Parametros
    ----------
    mapa: lista
        Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton
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

#
def movimiento_del_raton_arriba(mapa):
    '''
    Funcion que permite que el raton se mueva hacia arriba dentro del mapa

    Parametros
    ----------
    mapa: lista
        Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa 
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                a=i                           #igualaremos a y b con i e j
                b=j
                
    if(mapa[a-1][b]==1):                      #entonces para mover al rato arriba hacemos uso de la formula (a-1)(b) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[a-1][b]=2                        #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[a][b]=1                          #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                              #haciendo ver que el raton se ha movido de posicion

def movimiento_del_raton_abajo(mapa):
    '''
    Funcion que permite que el raton se mueva hacia abajo dentro del mapa

    Parametros
    ----------
    mapa: lista
        Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                a=i                           #igualaremos a y b con i e j 
                b=j                           
                
    if(mapa[a+1][b]==1):                      #entonces para mover al rato abajo hacemos uso de la formula (a+1)(b) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[a+1][b]=2                        #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[a][b]=1                          #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                              #haciendo ver que el raton se ha movido de posicion

def movimiento_del_raton_izquierda(mapa):
    '''
    Funcion que permite que el raton se mueva hacia la izquierda dentro del mapa

    Parametros
    ----------
    mapa: lista
        Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                a=i                           #igualaremos a y b con i e j
                b=j
                
    if(mapa[a][b-1]==1):                      #entonces para mover al rato abajo hacemos uso de la formula (a)(b-1) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[a][b-1]=2                        #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[a][b]=1                          #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                              #haciendo ver que el raton se ha movido de posicion

def movimiento_del_raton_derecha(mapa):
    '''
    Funcion que permite que el raton se mueva hacia la derecha dentro del mapa

    Parametros
    ----------
    mapa: lista
        Una lista llena de 0,1,2 donde 0 es pared, 1 es el camino por donde puede pasar y 2 es el raton
    '''
    raton = 2 #definimos a raton como 2 para distinguirlo dentro del mapa
    for i in range(len(mapa)):                #segun el tamaño del mapa 
        for j in range(len(mapa[i])):         #y tamaño de las filas del mapa
            if mapa[i][j] == raton:           #buscamos la posicion del raton
                print(i,j)                    #una vez tenemos la posicion del raton
                a=i                           #igualaremos a y b con i e j
                b=j
                
    if(mapa[a][b+1]==1):                      #entonces para mover al rato abajo hacemos uso de la formula (a)(b+1) donde si es igual 1(camino por donde si puede pasar el raton)
        mapa[a][b+1]=2                        #sera reemplazado 1(camino por donde puede pasar) por 2(raton)
        mapa[a][b]=1                          #y donde estaba el raton(2) sera reemplazado por camino donde se puede pasar(1)
                                              #haciendo ver que el raton se ha movido de posicion

def mensaje_ganador():
    '''
    Funcion que imprime "GANASTE" en color verde una vez finalizado el juego

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

    final_laberinto=False #definimos final_laberinto como falso para que el juego siga corriendo hasta llegar al final del laberinto
    print(chr(27)+"[1;33m"+"BIENVENIDO AL JUEGO DE RATON EN EL LABERINTO") #imprime mensaje de bienvenida en color amarillo
    dibujo_presentacion_del_juego()#imprimos el dibujo del raton al incio del juego
    print("")#imprime salto de linea
    print(chr(27)+"[1;32m") #hacemos que de ahora en adelantes las letras sean color verde
    os.system("pause") #Pausamos el codigo hasta aplastar una tecla
    print(chr(27)+"[1;37m"+"EMPEZANDO EL JUEGO")
    time.sleep(1)#hacemos que el codigo tenga un pequeño retraso para simular la carga del juego
    os.system("cls")#limpiamos pantalla


    print("Ustes es: ",chr(27)+"[1;32m"+"█")#imprimos que el ratos es "█" en color verde
    imprimir_mapa(mapa)#imprimimos el mapa remplazando los numeros por colores
    while(final_laberinto==False):#mientras aun no se llegue al final del laberinto entonces:
        print(chr(27)+"[1;33m"+"Hacia donde quieres mover el raton?")#preguntamos hacia donde quiere mover el raton
        print("\033[;36m")#cian
        print("1. Arriba")#imprimimos el menu en color cian
        print("2. Abajo")
        print("3. Izquierda")
        print("4. Derecha")

        mov_raton=elegir_movimiento_del_raton()#llamamos a la funcion elegir_movimiento_del_raton() para igualarla a "mov_raton" una vez el dato ingresado sea validado
        while (mov_raton<1 or mov_raton>4):#en este ciclo repetitivo validamos que solo se ingrese numeros mayor a 1 o menor a 4
            mov_raton=elegir_movimiento_del_raton()#en caso de no cumpla entonces tendremos que volver a ingresar un numero
            
        if(mov_raton==1):#si el jugador decidió moverse hacia arriba entonces
            os.system("cls")#limpiamos pantalla
            movimiento_del_raton_arriba(mapa)#hacemos uso de esta funcion para mover el raton una posicion arriba
            imprimir_mapa(mapa)#imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            if(mapa[6][10]==2):#si el raton llego a esta posicion(final del laberinto) entonces
                mensaje_ganador()#imprimimos el mensaje ganador
                sys.exit()#finalizamos la ejecucion del codigo
        if(mov_raton==2):#si el jugador decidió moverse hacia abajo entonces
            os.system("cls")#limpiamos pantalla
            movimiento_del_raton_abajo(mapa)#hacemos uso de esta funcion para mover el raton una posicion abajo
            imprimir_mapa(mapa)#imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            if(mapa[6][10]==2):#si el raton llego a esta posicion(final del laberinto) entonces
                mensaje_ganador()#imprimimos el mensaje ganador
                sys.exit()##finalizamos la ejecucion del codigo
        if(mov_raton==3):#si el jugador decidió moverse hacia la izquierda entonces:
            os.system("cls")#limpiamos pantalla
            movimiento_del_raton_izquierda(mapa)#hacemos uso de esta funcion para mover el raton una posicion a la izquierda
            imprimir_mapa(mapa)#imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            if(mapa[6][10]==2):#si el raton llego a esta posicion(final del laberinto) entonces
                mensaje_ganador()#imprimimos el mensaje ganador
                sys.exit()##finalizamos la ejecucion del codigo
        if(mov_raton==4):#si el jugador decidió moverse hacia la derecha entonces
            os.system("cls")#limpiamos pantalla
            movimiento_del_raton_derecha(mapa)#hacemos uso de esta funcion para mover el raton una posicion a la derecha
            imprimir_mapa(mapa)#imprimimos el mapa donde se esta jugando con la posicion del raton mas actual
            if(mapa[6][10]==2):#si el raton llego a esta posicion(final del laberinto) entonces
                mensaje_ganador()#imprimimos el mensaje ganador
                sys.exit()##finalizamos la ejecucion del codigo

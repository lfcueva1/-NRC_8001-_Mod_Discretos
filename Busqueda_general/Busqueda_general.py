
#libreria que uso para pausar o limpiar pantalla
import os
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

def crear_unir_nodos():
    '''
    Funcion que crea y une a los nodos 
    Parametros:
        esta funcion no tiene parametros
    Retorna:
        grafo : list
    '''
    # Crear grafo
    grafo,costo = [[] for i in range(35)],{}
    terminal_quitumbe=0
    condor_ñam=1
    amaru_ñam=2
    moran_malverde=3
    turubamba=4
    quimiag=5
    mercado_mayorista=6
    solanda=7
    ajavi=8
    la_internacional=9
    quito_sur=10
    españa=11
    el_calzado=12
    el_recreo=13
    #uniendo nodos
    grafo[terminal_quitumbe].append(condor_ñam)
    grafo[condor_ñam].append(terminal_quitumbe)
    grafo[condor_ñam].append(amaru_ñam)
    grafo[amaru_ñam].append(condor_ñam)
    grafo[amaru_ñam].append(moran_malverde)
    grafo[moran_malverde].append(amaru_ñam)
    grafo[moran_malverde].append(turubamba)
    grafo[turubamba].append(moran_malverde)
    grafo[turubamba].append(quimiag)
    grafo[quimiag].append(turubamba)
    grafo[quimiag].append(mercado_mayorista)
    grafo[mercado_mayorista].append(quimiag)
    grafo[mercado_mayorista].append(solanda)
    grafo[solanda].append(mercado_mayorista)
    grafo[solanda].append(ajavi)
    grafo[ajavi].append(solanda)
    grafo[ajavi].append(la_internacional)
    grafo[la_internacional].append(ajavi)
    grafo[la_internacional].append(quito_sur)
    grafo[quito_sur].append(la_internacional)
    grafo[quito_sur].append(españa)
    grafo[españa].append(quito_sur)
    grafo[españa].append(el_calzado)
    grafo[el_calzado].append(españa)
    grafo[el_calzado].append(el_recreo)
    grafo[el_recreo].append(el_calzado)
    return grafo
def menu_estacion():
    '''
    Imprime un menu de opciones que permite seleccionar cualquier estacion del sistema de transporte metropolitano

    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        estacion : str
    '''
    #imprimo los sistemas de transporte
    

    print("Elija la estacion")
    print("1.  Terminal Quitumbe")
    print("2.  Condor ñam")
    print("3.  Amaru ñam")
    print("4.  Moran Malverde")
    print("5.  Turubamba")
    print("6.  Quimiag")
    print("7.  Mercado Mayorista")
    print("8.  Solanda")
    print("9.  Ajavi")
    print("10. La internacional")
    print("11. Quito sur")
    print("12. España")
    print("13. El Calzado")
    print("14. El Recreo")
    print("Elija una opcion: ",end="")
    #ingresamos una opcion por teclado
    opcion2=validar_numeros_enteros()
    #validamos que ingrese numeros dentro del menu
    while(opcion2<1 or opcion2>42):
        print("Elija una opcion dentro del rango: ",end="")
        opcion2=validar_numeros_enteros()
    #dependiendo de la seleccion de estacion le dara el nombre de esa estacion a una variable
    if(opcion2==1):
        estacion=0
    if(opcion2==2):
        estacion=1
    if(opcion2==3):
        estacion=2
    if(opcion2==4):
        estacion=3
    if(opcion2==5):
        estacion=4
    if(opcion2==6):
        estacion=5
    if(opcion2==7):
        estacion=6
    if(opcion2==8):
        estacion=7
    if(opcion2==9):
        estacion=8
    if(opcion2==10):
        estacion=9
    if(opcion2==11):
        estacion=10
    if(opcion2==12):
        estacion=11
    if(opcion2==13):
        estacion=12
    if(opcion2==14):
        estacion=13  
    #retornamos la estacion
    return estacion
def ubicaciones(ruta_trole):
    '''
    Funcion que de el nombre de una ubicacion a una lista segun el valor que tenga
    Parametros:
        ruta_trole : lista
    Retorna: 
        ruta_trole : lista
    '''
    #recorremos la lista entera y damos el nombre de la ubicacion dependiendo el numero que tenga el nodo
    for i in camino:
        if(i==0):
            ruta_trole.append("Terminal Quitumbe")
        if(i==1):
            ruta_trole.append("Condor ñam")
        if(i==2):
            ruta_trole.append("Amaru ñam")
        if(i==3):
            ruta_trole.append("Moran Malverde")
        if(i==4):
            ruta_trole.append("Turubamba")
        if(i==5):
            ruta_trole.append("Quimiag")
        if(i==6):
            ruta_trole.append("Mercado Mayorista")
        if(i==7):
            ruta_trole.append("Solanda")    
        if(i==8):
            ruta_trole.append("Ajavi")
        if(i==9):
            ruta_trole.append("La internacional")   
        if(i==10):
            ruta_trole.append("Quito sur") 
        if(i==11):
            ruta_trole.append("España") 
        if(i==12):
            ruta_trole.append("El Calzado")  
        if(i==13):
            ruta_trole.append("El Recreo") 

    #retornamos el camino
    return ruta_trole
def busqueda_en_anchura(grafo, costo, inicio, fin):
    '''
    Funcion que busca el camino mas corto en las ubicaciones de la espe
    Parametros:
        grafo : lista
        costo : diccionario
        inicio : int
        fin : int
    Retorna:
        float('inf') : float
        [] : lista
        
    '''
    #variable tipo cola que almacena tupplas con tres elementos: (1) la distancia del nodo 
    #de origen al nodo actual, (2) el nodo actual, y (3) el camino desde el nodo de origen hasta el nodo actual. 
    cola = [(0, inicio, [])]
    #variable que lleva el registro de los nodos que se han visitado durante la búsqueda.
    visitados = set()
    #recorremos la cola mientras no este vacia
    while cola:
        #Se toma el primer elemento de la cola (el nodo con la distancia mínima hasta ese momento)
        (dist, actual, camino) = cola.pop(0)
        #Si el nodo actual es el nodo de destino fin
        if actual == fin:
            #se devuelve la distancia total y el camino desde el nodo de origen hasta el nodo de destino.
            return dist, camino + [actual]
        #Si el nodo actual ha sido visitado previamente
        if actual in visitados:
            #se omite este nodo y se continúa con el siguiente.
            continue
        #Se agrega el nodo actual al conjunto de nodos visitados.
        visitados.add(actual)
        #Se recorre sobre los vecinos del nodo actual.
        for vecino in grafo[actual]:
            #Se obtiene el costo para llegar desde el nodo actual hasta su vecino, o se asigna un costo predeterminado 
            #de 1 si no se encuentra en el diccionario costo.
            costo_vecino = costo.get((actual, vecino), 1)
            #Se agrega una nueva tupla a la cola con la nueva distancia total, el vecino y el camino actualizado 
            # (agregando el nodo actual al camino).
            cola.append((dist + costo_vecino, vecino, camino + [actual]))
    #Si no se encuentra un camino desde el nodo de origen hasta el nodo de destino, se devuelve una distancia infinita y un camino vacío.
    return float('inf'), []
if __name__ == '__main__':
    #declaro una lista vacia la cual usare para agregar las ubicaciones por donde el usuario tendra que pasar para llegar a su destino
    ruta_trole=[]
    #creo y uno los nodos
    grafo=crear_unir_nodos()
    #creo un diccionario para el costo
    costo={}
    print("Indique el punto de inicio de las estaciones del trolebus")
    #imprimo el menu de la estacion donde inicia el viaje
    inicio=menu_estacion()
    #limpio pantalla
    os.system("cls")
    print("Hacia que estacion desea ir?")
    #imprimo el menu de la estacion hacia donde quiere ir el usuario
    final=menu_estacion()
    #si el usuario pone la misma localizacion imprimira un mensaje de que ya se encuentra en esa posicion
    if(inicio==final):
        print("Usted ya se encuentra en esta posicion")
    #caso contario, busca al ruta que debera tomar el usuario para llegar a su destino
    else:
        #buscamos la ruta mas corta con la ayuda de los nodos
        costo_1,camino=busqueda_en_anchura(grafo,costo,inicio,final)
        #agrego los caminos a la lista
        ruta_trole=ubicaciones(ruta_trole)
        print("El costo es: ",costo_1)
        print("El camino que debes tomar es:", ruta_trole)

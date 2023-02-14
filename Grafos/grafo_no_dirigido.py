"""
Programa de grafo dirigido donde el usuario ingresa el nodo de origen y el nodo de destino y dependiendo
de la union del nodo imprime si se puede llegar hasta ahi

Autores:
Luis Fernando Cueva Flores

Versión:
VER.1
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

def crear_unir_nodos():
    '''
    Funcion que crea y une a los nodos 
    Parametros:
        
    Retorna:
        Esta funcion no retorna ningun tipo de dato
    '''
    # Crear grafo dirigido
    grafo = [[] for i in range(4)]
    nodoA=0
    nodoB=1
    nodoC=2
    nodoD=3
    #uniendo nodos
    grafo[nodoA].append(nodoB)
    grafo[nodoA].append(nodoD)
    grafo[nodoB].append(nodoA)
    grafo[nodoC].append(nodoA)
    grafo[nodoC].append(nodoD)
    grafo[nodoD].append(nodoA)
    grafo[nodoD].append(nodoC)
    #retorno el grafo
    return grafo

def puede_llegar(grafo, origen, destino):
    '''
    Funcion que verifica si es posible llegar de un nodo a otro en el grafo dirigido

    Parametros:
        grafo: lista
        origen: int
        destino: int
    Retorna:
        True si es posible llegar de origen a destino
        False en caso contrario
    '''
    #lista que representa la cola de nodos por visitar y se inicializa con el nodo de origen.
    cola = [origen]
    #conjunto para almacenar los nodos que han sido visitados.
    visitados = set()
    #se recorre mientas la lista no este vacia
    while cola:
        #se obtiene el primer elemento de la cola y se asigna a la variable nodo.
        nodo = cola.pop(0)
        #se verifica si el nodo actual es el destino.
        if nodo == destino:
            #Si es así, la función retorna True.
            return True
        #se agrega el nodo a la lista de nodos visitados.
        visitados.add(nodo)
        #recorrenomos el grafo
        for vecino in grafo[nodo]:
            #si el vecino no ha sido visitado anteriormente.
            if vecino not in visitados:
                #se agrega a la cola para ser visitado en una próxima iteración.
                cola.append(vecino)
    #si se recorrieron todos los nodos y no se encontró un camino hasta el destino, la función retorna False.
    return False
if __name__ == '__main__':
    #creo y uno los nodos
    grafo = crear_unir_nodos()
    #imprimo la forma en la que estan unidos los nodos
    print("Los nodos estan conectados de esta forma: \nNodo A -> Nodo B, Nodo A -> Nodo D")
    print("Nodo B -> Nodo A\nNodo C -> Nodo A,Nodo C -> Nodo D\nNodo D -> Nodo A,Nodo D -> Nodo C")
    #imprimo el menu de nodos
    print("1: Nodo A\n2: Nodo B\n3: Nodo C\n4: Nodo D")
    print("Ingrese el nodo de origen: ",end="")
    #ingresa el nodo de origen
    origen = validar_numeros_enteros()
    #valido que solo ingrese una opcion dentro del rango
    while(origen<1 or origen>4):
        print("Ingrese una opcion valida: ",end="")
        origen = validar_numeros_enteros()
    #ingresa el nodo de destino  
    print("Ingrese el nodo destino: ",end="")
    destino = validar_numeros_enteros()
    #valido que solo ingrese una opcion dentro del rango
    while(destino<1 or destino>4):
        print("Ingrese una opcion valida: ",end="")
        destino = validar_numeros_enteros()
    #si la funcion retorna true imprime que si se puede llegar a ese nodo
    if puede_llegar(grafo, origen, destino):
        print("Se puede llegar de", origen, "a", destino)
    #caso contrario se imprime que no se puede llegar a ese nodo de destino
    else:
        print("No se puede llegar de", origen, "a", destino)
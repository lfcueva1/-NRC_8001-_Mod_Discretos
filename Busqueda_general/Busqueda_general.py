#libreria que uso para la creacion y union de nodos
import networkx as nx
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
def rutas_Quito():
    '''
    Funcion que crea los nodos que utiliza el programa como las estaciones del sistema de transporte
    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        rutas: nx.graph
    '''
    # Crear grafo
    rutas = nx.Graph()
    rutas.add_node("Terminal Quitumbe")
    #trole
    rutas.add_node("Condor ñam")
    rutas.add_node("Amaru ñam")
    rutas.add_node("Moran Malverde")
    rutas.add_node("Turubamba")
    rutas.add_node("Quimiag")
    rutas.add_node("Mercado Mayorista")
    rutas.add_node("Solanda")
    rutas.add_node("Ajavi")
    rutas.add_node("La internacional")
    rutas.add_node("Quito sur")
    rutas.add_node("España")
    rutas.add_node("El Calzado")
    #ESTACION
    rutas.add_node("El Recreo")
    rutas.add_node("Villaflora")
    rutas.add_node("Chimbacaye")
    rutas.add_node("La colina")
    rutas.add_node("Jefferson Perez")
    rutas.add_node("La Recoleta")
    rutas.add_node("Cumandá")
    rutas.add_node("Sto. Domingo")
    rutas.add_node("Plaza Chica")
    rutas.add_node("Plaza Marin")
    rutas.add_node("Plaza del teatro")
    rutas.add_node("Hermano Miguel")
    rutas.add_node("Banco central")
    rutas.add_node("Alameda")
    rutas.add_node("El Ejido")
    rutas.add_node("La Mariscal")
    rutas.add_node("Sta. Clara")
    rutas.add_node("Colón")
    rutas.add_node("Cuero y Caicedo")
    rutas.add_node("Mariana de Jesus")
    rutas.add_node("El Florón")
    rutas.add_node("Estadio")
    rutas.add_node("La Y")
    rutas.add_node("Plaza de Toros")
    rutas.add_node("El labrador")
    rutas.add_node("Parque Kenedy")
    rutas.add_node("Del maestro")
    rutas.add_node("Parquenor")
    rutas.add_node("Terminal Interprovincial Carcelén")
    #ecovia
    rutas.add_node("Terminal Sur ecovia")
    rutas.add_node("Santo Tomas")
    rutas.add_node("San Jose de Guamani Caupicho")
    rutas.add_node("El Beaterio Nueva Aurora II")
    rutas.add_node("La Bretaña")
    rutas.add_node("Guayanay Ñam")
    rutas.add_node("El Capulí")
    rutas.add_node("Otoya")
    rutas.add_node("Quilallacta")
    rutas.add_node("Pacarillacta")
    rutas.add_node("Puente de guajaló")
    rutas.add_node("San Cristobal")
    rutas.add_node("Ayapamba")
    rutas.add_node("El Comercio")
    rutas.add_node("San Bartolo")
    rutas.add_node("Epiclachima")
    rutas.add_node("Pujilí")
    rutas.add_node("Estadio Chimbacalle")
    rutas.add_node("Teatro Mexico")
    rutas.add_node("Colegio Montufar")
    #ESTACION
    rutas.add_node("El playón de la Marin")
    rutas.add_node("Marin Central")

    rutas.add_node("Simon Bolivar")
    rutas.add_node("Eugenio Espejo")
    rutas.add_node("Casa de la cultura")
    rutas.add_node("Galo Plaza")
    rutas.add_node("De las universidades")
    rutas.add_node("Manuela Cañizares")
    rutas.add_node("Baca Ortiz")
    rutas.add_node("Orellana")
    rutas.add_node("La Paz")
    rutas.add_node("San Martin")
    rutas.add_node("Bellavista")
    rutas.add_node("Eloy ALfaro")
    rutas.add_node("Benalcazar")
    rutas.add_node("Naciones Unidas")
    rutas.add_node("24 de Mayo")
    rutas.add_node("Los Sauces")
    rutas.add_node("Jipijapa")
    rutas.add_node("Terminal Rio Coca")
    #CORREDORES
    rutas.add_node("Hacienda el Carmen")
    rutas.add_node("Fundeporte")
    rutas.add_node("Chillogallo")
    rutas.add_node("Sta. Rita")
    rutas.add_node("Sta. Barbara")
    rutas.add_node("Mena Dos")
    rutas.add_node("Biloxi")
    rutas.add_node("La santiago")
    rutas.add_node("Alonso de angulo")
    rutas.add_node("El Pintado")
    rutas.add_node("La Magdanela")
    rutas.add_node("Estacion metro Magdalena")
    rutas.add_node("La Mascota")
    rutas.add_node("Dos Puntes Norte-Sur")
    rutas.add_node("Dos Puntes Sur-Norte")
    rutas.add_node("San Diego")
    rutas.add_node("San Roque Norte-Sur")
    rutas.add_node("San Roque Sur-Norte")
    rutas.add_node("El Tejar")
    rutas.add_node("IESS")
    rutas.add_node("Universidad Central")
    rutas.add_node("Escuela Espejo")
    rutas.add_node("Santa Prisca")
    rutas.add_node("Concejo Provincial")
    rutas.add_node("Perez Guerrero")
    rutas.add_node("Seminario Mayor")
    rutas.add_node("San Gabriel")
    rutas.add_node("La Mañosca")
    rutas.add_node("Brasil")
    rutas.add_node("La Y")
    rutas.add_node("Edmundo Carvajal")
    rutas.add_node("La Concepcion")
    rutas.add_node("Aereopuerto")
    rutas.add_node("La Florida")
    rutas.add_node("Base Aérea")
    rutas.add_node("Vaca de Castro")
    rutas.add_node("Del Maestro")
    rutas.add_node("Cotocollao")
    rutas.add_node("La Delicia")
    rutas.add_node("Terminal la Ofelia")
    #retorno los nodos
    return rutas
def unir_nodos(rutas):
    '''
    Funcion que une los nodos creados para graficas las rutas de las estaciones

    Parametros:
        rutas : nx.graph
    Retorna:
        rutas : nx.graph
    '''
    rutas = nx.Graph()
    rutas.add_edge("Terminal Quitumbe","Condor ñam")
    rutas.add_edge("Condor ñam","Amaru ñam")
    rutas.add_edge("Amaru ñam","Moran Malverde")
    rutas.add_edge("Moran Malverde","Turubamba")
    rutas.add_edge("Turubamba","Quimiag")
    rutas.add_edge("Quimiag","Mercado Mayorista")
    rutas.add_edge("Mercado Mayorista","Solanda")
    rutas.add_edge("Solanda","Ajavi")
    rutas.add_edge("Ajavi","La internacional")
    rutas.add_edge("La internacional","Quito sur")
    rutas.add_edge("Quito sur","España")
    rutas.add_edge("España","El Calzado")
    rutas.add_edge("El Calzado","El Recreo")
    rutas.add_edge("El Recreo","Villaflora")
    rutas.add_edge("Villaflora","Chimbacaye")
    rutas.add_edge("Chimbacaye","La colina")
    rutas.add_edge("La colina","La Recoleta")
    rutas.add_edge("La Recoleta","Jefferson Perez")
    rutas.add_edge("Jefferson Perez","Chimbacaye")
    rutas.add_edge("La Recoleta","Cumandá")
    rutas.add_edge("Cumandá","Sto. Domingo")
    rutas.add_edge("Sto. Domingo","Plaza Marin")
    rutas.add_edge("Plaza Marin","Hermano Miguel")
    rutas.add_edge("Hermano Miguel","Alameda")
    rutas.add_edge("Alameda","Banco central")
    rutas.add_edge("Banco central","Plaza del teatro")
    rutas.add_edge("Plaza del teatro","Plaza Chica")
    rutas.add_edge("Plaza Chica","Sto. Domingo")
    rutas.add_edge("Alameda","El Ejido")
    rutas.add_edge("El Ejido","La Mariscal")
    rutas.add_edge("La Mariscal","Sta. Clara")
    rutas.add_edge("Sta. Clara","Colón")
    rutas.add_edge("Colón","Cuero y Caicedo")
    rutas.add_edge("Cuero y Caicedo","Mariana de Jesus")
    rutas.add_edge("Mariana de Jesus","El Florón")
    rutas.add_edge("El Florón","Estadio")
    rutas.add_edge("Estadio","La Y")
    rutas.add_edge("La Y","Plaza de Toros")
    rutas.add_edge("Plaza de Toros","El labrador")
    rutas.add_edge("Plaza de Toros","Parque Kenedy")
    rutas.add_edge("Parque Kenedy","Del maestro")
    rutas.add_edge("Del maestro","Parquenor")
    rutas.add_edge("Parquenor","Terminal Interprovincial Carcelén")
    #corredor
    rutas.add_edge("Terminal Quitumbe","Hacienda el Carmen")
    rutas.add_edge("Hacienda el Carmen","Fundeporte")
    rutas.add_edge("Fundeporte","Chillogallo")
    rutas.add_edge("Chillogallo","Sta. Rita")
    rutas.add_edge("Sta. Rita","Sta. Barbara")
    rutas.add_edge("Sta. Barbara","Mena Dos")
    rutas.add_edge("Mena Dos","Biloxi")
    rutas.add_edge("Biloxi","La santiago")
    rutas.add_edge("La santiago","Alonso de angulo")
    rutas.add_edge("Alonso de angulo","El Pintado")
    rutas.add_edge("El Pintado","La Magdanela")
    rutas.add_edge("La Magdanela","La Mascota")
    rutas.add_edge("La Mascota","Dos Puntes Sur-Norte")
    rutas.add_edge("Dos Puntes Sur-Norte","San Diego")
    rutas.add_edge("San Diego","Dos Puntes Norte-Sur")
    rutas.add_edge("San Diego","San Roque Sur-Norte")
    rutas.add_edge("San Roque Sur-Norte","El Tejar")
    rutas.add_edge("El Tejar","San Roque Norte-Sur")
    rutas.add_edge("El Tejar","IESS")
    rutas.add_edge("IESS","Universidad Central")
    rutas.add_edge("Universidad Central","Seminario Mayor")
    rutas.add_edge("Seminario Mayor","Perez Guerrero")
    rutas.add_edge("Perez Guerrero","Escuela Espejo")
    rutas.add_edge("Escuela Espejo","Concejo Provincial")
    rutas.add_edge("Concejo Provincial","Santa Prisca")
    rutas.add_edge("Santa Prisca","IESS")
    rutas.add_edge("Seminario Mayor","San Gabriel")
    rutas.add_edge("San Gabriel","La Mañosca")
    rutas.add_edge("La Mañosca","Brasil")
    rutas.add_edge("Brasil","La Y")
    rutas.add_edge("La Y","Edmundo Carvajal")
    rutas.add_edge("Edmundo Carvajal","La Concepcion")
    rutas.add_edge("La Concepcion","Aereopuerto")
    rutas.add_edge("Aereopuerto","La Florida")
    rutas.add_edge("La Florida","Base Aérea")
    rutas.add_edge("Base Aérea","")
    rutas.add_edge("La Concepcion","Vaca de Castro")
    rutas.add_edge("Vaca de Castro","Del Maestro")
    rutas.add_edge("Del Maestro","Cotocollao")
    rutas.add_edge("Cotocollao","La Delicia")
    rutas.add_edge("La Delicia","Terminal la Ofelia")
    #ecovia
    rutas.add_edge("Terminal Sur ecovia","Santo Tomas")
    rutas.add_edge("Santo Tomas","")
    rutas.add_edge("San Jose de Guamani Caupicho","El Beaterio Nueva Aurora II")
    rutas.add_edge("El Beaterio Nueva Aurora II","La Bretaña")
    rutas.add_edge("La Bretaña","Guayanay Ñam")
    rutas.add_edge("Guayanay Ñam","El Capulí")
    rutas.add_edge("El Capulí","Otoya")
    rutas.add_edge("Otoya","Quilallacta")
    rutas.add_edge("Terminal Quitumbe","Quilallacta")
    rutas.add_edge("El Capulí","Pacarillacta")
    rutas.add_edge("Pacarillacta","Puente de guajaló")
    rutas.add_edge("Puente de guajaló","San Cristobal")
    rutas.add_edge("San Cristobal","Ayapamba")
    rutas.add_edge("Ayapamba","El Comercio")
    rutas.add_edge("El Comercio","San Bartolo")
    rutas.add_edge("San Bartolo","Epiclachima")
    rutas.add_edge("Epiclachima","Pujilí")
    rutas.add_edge("Pujilí","El Recreo")
    rutas.add_edge("El Recreo","Estadio Chimbacalle")
    rutas.add_edge("Estadio Chimbacalle","Teatro Mexico")
    rutas.add_edge("Teatro Mexico","Colegio Montufar")
    rutas.add_edge("Colegio Montufar","El playón de la Marin")
    rutas.add_edge("El playón de la Marin","Marin Central")
    rutas.add_edge("Marin Central","Concejo Provincial")
    rutas.add_edge("Marin Central","Simon Bolivar")
    rutas.add_edge("Simon Bolivar","Eugenio Espejo")
    rutas.add_edge("Eugenio Espejo","De las universidades")
    rutas.add_edge("De las universidades","Manuela Cañizares")
    rutas.add_edge("Manuela Cañizares","Galo Plaza")
    rutas.add_edge("Galo Plaza","Casa de la cultura")
    rutas.add_edge("Casa de la cultura","Eugenio Espejo")
    rutas.add_edge("Manuela Cañizares","Baca Ortiz")
    rutas.add_edge("Baca Ortiz","Orellana")
    rutas.add_edge("Orellana","La Paz")
    rutas.add_edge("La Paz","San Martin")
    rutas.add_edge("San Martin","Bellavista")
    rutas.add_edge("Bellavista","Eloy ALfaro")
    rutas.add_edge("Eloy ALfaro","Benalcazar")
    rutas.add_edge("Benalcazar","Naciones Unidas")
    rutas.add_edge("Naciones Unidas","24 de Mayo")
    rutas.add_edge("24 de Mayo","Los Sauces")
    rutas.add_edge("Los Sauces","Jipijapa")
    rutas.add_edge("Jipijapa","Terminal Rio Coca")
    rutas.add_edge("El labrador","Terminal Rio Coca")
    rutas.add_edge("Terminal la Ofelia","Terminal Interprovincial Carcelén")
    rutas.add_edge("Estacion metro Magdalena","La Magdanela")
    rutas.add_edge("Estacion metro Magdalena","Villaflora")
    rutas.add_edge("Villaflora","Estadio Chimbacalle")
    return rutas

def buscar_ruta(inicio,final,rutas):
    '''
    Funcion que busca la ruta mas corta para el usuario

    Parametros:
        inicio: str
        final : str
        rutas : nx.graph
    Retorna:
        camino : nx
    '''
    #busco la ruta mas corta
    camino = nx.shortest_path(rutas, inicio, final)
    #imprimo la informacion sobre la ruta que el usuario debe tomar
    print("La ruta que debe tomar para ir de", inicio, " a ",final, " es:", camino)
    #retorno la ruta
    return camino

def menu_estacion():
    '''
    Imprime un menu de opciones que permite seleccionar cualquier estacion del sistema de transporte metropolitano

    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        estacion : str
    '''
    #imprimo los sistemas de transporte
    print("1. Trolebus")
    print("2. Corredor")
    print("3. Ecovia")
    print("Elija una opcion: ",end="")
    #ingresamos la opcion por teclado
    opcion=validar_numeros_enteros()
    #validamos que solo ingrese numeros del menu
    while(opcion<1 or opcion>3):
        print("Elija una opcion dentro del rango: ",end="")
        opcion=validar_numeros_enteros()
    #si ingreso el sistema de trolebus preguntamos en que estacion esta
    if(opcion==1):
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
        print("15. Villaflora")
        print("16. Chimbacaye")
        print("17. La colina")
        print("18. Jefferson Perez")
        print("19. La Recoleta")
        print("20. Cumandá")
        print("21. Sto. Domingo")
        print("22. Plaza Chica")
        print("23. Plaza Marin")
        print("24. Plaza del teatro")
        print("25. Hermano Miguel")
        print("26. Banco central")
        print("27. Alameda")
        print("28. El Ejido")
        print("29. La Mariscal")
        print("30. Sta. Clara")
        print("31. Colón")
        print("32. Cuero y Caicedo")
        print("33. Mariana de Jesus")
        print("34. El Florón")
        print("35. Estadio")
        print("36. La Y")
        print("37. Plaza de Toros")
        print("38. El labrador")
        print("39. Parque Kenedy")
        print("40. Del maestro")
        print("41. Parquenor")
        print("42. Terminal Interprovincial Carcelén")
        print("Elija una opcion: ",end="")
        #ingresamos una opcion por teclado
        opcion2=validar_numeros_enteros()
        #validamos que ingrese numeros dentro del menu
        while(opcion2<1 or opcion2>42):
            print("Elija una opcion dentro del rango: ",end="")
            opcion2=validar_numeros_enteros()
        #dependiendo de la seleccion de estacion le dara el nombre de esa estacion a una variable
        if(opcion2==1):
            estacion="Terminal Quitumbe"
        if(opcion2==2):
            estacion="Condor ñam"
        if(opcion2==3):
            estacion="Amaru ñam"
        if(opcion2==4):
            estacion="Moran Malverde"
        if(opcion2==5):
            estacion="Turubamba"
        if(opcion2==6):
            estacion="Quimiag"
        if(opcion2==7):
            estacion="Mercado Mayorista"
        if(opcion2==8):
            estacion="Solanda"
        if(opcion2==9):
            estacion="Ajavi"
        if(opcion2==10):
            estacion="La internacional"
        if(opcion2==11):
            estacion="Quito sur"
        if(opcion2==12):
            estacion="España"
        if(opcion2==13):
            estacion="El Calzado"
        if(opcion2==14):
            estacion="El Recreo"
        if(opcion2==15):
            estacion="Villaflora"
        if(opcion2==16):
            estacion="Chimbacaye"
        if(opcion2==17):
            estacion="La colina"
        if(opcion2==18):
            estacion="Jefferson Perez"
        if(opcion2==19):
            estacion="La Recoleta"
        if(opcion2==20):
            estacion="Cumandá"
        if(opcion2==21):
            estacion="Sto. Domingo"
        if(opcion2==22):
            estacion="Plaza Chica"
        if(opcion2==23):
            estacion="Plaza Marin"
        if(opcion2==24):
            estacion="Plaza del teatro"
        if(opcion2==25):
            estacion="Hermano Miguel"
        if(opcion2==26):
            estacion="Banco central"
        if(opcion2==27):
            estacion="Alameda"
        if(opcion2==28):
            estacion="El Ejido"
        if(opcion2==29):
            estacion="La Mariscal"
        if(opcion2==30):
            estacion="Sta. Clara"
        if(opcion2==31):
            estacion="Colón"
        if(opcion2==32):
            estacion="Cuero y Caicedo"
        if(opcion2==33):
            estacion="Mariana de Jesus"
        if(opcion2==34):
            estacion="El Florón"
        if(opcion2==35):
            estacion="Estadio"
        if(opcion2==36):
            estacion="La Y"
        if(opcion2==37):
            estacion="Plaza de Toros"
        if(opcion2==38):
            estacion="El labrador"
        if(opcion2==39):
            estacion="Parque Kenedy"
        if(opcion2==40):
            estacion="Del maestro"
        if(opcion2==41):
            estacion="Parquenor"
        if(opcion2==42):
            estacion="Terminal Interprovincial Carcelén"
        #retornamos la estacion
        return estacion
    #si el usuario eligio el sistema corredores
    if(opcion==2):
        print("Elija la estacion")
        print("1.  Hacienda el Carmen")
        print("2.  Fundeporte")
        print("3.  Chillogallo")
        print("4.  Sta. Rita")
        print("5.  Sta. Barbara")
        print("6.  Mena Dos")
        print("7.  Biloxi")
        print("8.  La Santiago")
        print("9.  Alonso de angulo")
        print("10. El Pintado")
        print("11. La Magdalena")
        print("12. Estacion Metro Magnadela")
        print("13. La Mascota")
        print("14. Dos Puentes Sur-Norte")
        print("15. Dos Puentes Norte-Sur")
        print("16. San Diego")
        print("17. San Roque Norte-Sur")
        print("18. San Roque Sur-Norte")
        print("19. El Tejar")
        print("20. IESS")
        print("21. Universidad Central")
        print("22. Seminario Mayor")
        print("23. Perez Guerrero")
        print("24. Escuela Espejo")
        print("25. Concejo Provincial")
        print("26. Santa Prisca")
        print("27. San gabriel")
        print("28. La Mañosca")
        print("29. Brasil")
        print("30. La Y")
        print("31. Edmundo Carvajal")
        print("32. La Concepcion")
        print("33. Aereopuerto")
        print("34. La Florida")
        print("35. Base Aérea")
        print("36. Vaca de Castro")
        print("37. Del Maestro")
        print("38. Cotocollao")
        print("39. La Delicia")
        print("40. Terminal la ofelia")
        print("Elija una opcion: ",end="")
        #ingresamos una opcion del menu por teclado
        opcion3=validar_numeros_enteros()
        #validamos que solo ingrese opciones dentro del menu
        while(opcion3<1 or opcion3>40):
            print("Elija una opcion dentro del rango: ",end="")
            opcion3=validar_numeros_enteros()
        #dependiendo de la seleccion de estacion le dara el nombre de esa estacion a una variable
        if(opcion3==1):
            estacion="Hacienda el Carmen"
        if(opcion3==2):
            estacion="Fundeporte"
        if(opcion3==3):
            estacion="Chillogallo"
        if(opcion3==4):
            estacion="Sta. Rita"
        if(opcion3==5):
            estacion="Sta. Barbara"
        if(opcion3==6):
            estacion="Mena Dos"
        if(opcion3==7):
            estacion="Biloxi"
        if(opcion3==8):
            estacion="La santiago"
        if(opcion3==9):
            estacion="Alonso de angulo"
        if(opcion3==10):
            estacion="El Pintado"
        if(opcion3==11):
            estacion="La Magdanela"
        if(opcion3==12):
            estacion="Estacion metro Magdalena"
        if(opcion3==13):
            estacion="La Mascota"
        if(opcion3==14):
            estacion="Dos Puntes Sur-Norte"
        if(opcion3==15):
            estacion="Dos Puntes Norte-Sur"
        if(opcion3==16):
            estacion="San Diego"
        if(opcion3==17):
            estacion="San Roque Norte-Sur"
        if(opcion3==18):
            estacion="San Roque Sur-Norte"
        if(opcion3==19):
            estacion="El Tejar"
        if(opcion3==20):
            estacion="IESS"
        if(opcion3==21):
            estacion="Universidad Central"
        if(opcion3==22):
            estacion="Seminario Mayor"
        if(opcion3==23):
            estacion="Perez Guerrero"
        if(opcion3==24):
            estacion="Escuela Espejo"
        if(opcion3==25):
            estacion="Concejo Provincial"
        if(opcion3==26):
            estacion="Santa Prisca"
        if(opcion3==27):
            estacion="San Gabriel"
        if(opcion3==28):
            estacion="La Mañosca"
        if(opcion3==29):
            estacion="Brasil"
        if(opcion3==30):
            estacion="La Y"
        if(opcion3==31):
            estacion="Edmundo Carvajal"
        if(opcion3==32):
            estacion="La Concepcion"
        if(opcion3==33):
            estacion="Aereopuerto"
        if(opcion3==34):
            estacion="La Florida"
        if(opcion3==35):
            estacion="Base Aérea"
        if(opcion3==36):
            estacion="Vaca de Castro"
        if(opcion3==37):
            estacion="Del Maestro"
        if(opcion3==38):
            estacion="Cotocollao"
        if(opcion3==39):
            estacion="La Delicia"
        if(opcion3==40):
            estacion="Terminal la Ofelia"
        #retornamos la estacion
        return estacion
    #si elijió el sistema ecovia
    if(opcion==3):
        #imprime el menu de estaciones
        print("Elija la estacion")
        print("1.  Terminal Sur ecovia")
        print("2.  Santo Tomas")
        print("3.  San Jose de Guamani Caupicho")
        print("4.  El Beaterio Nueva Aurora II")
        print("5.  La Bretaña")
        print("6.  Guayanay Ñam")
        print("7.  El Capulí")
        print("8.  Otoya")
        print("9.  Quilallacta")
        print("10. Pacarillacta")
        print("11. Puente de guajaló")
        print("12. San Cristobal")
        print("13. Ayapamba")
        print("14. El Comercio")
        print("15. San Bartolo")
        print("16. Epiclachima")
        print("17. Pujilí")
        print("18. El Recreo")
        print("19. Estadio Chimbacalle")
        print("20. Teatro Mexico")
        print("21. Colegio Montufar")
        print("22. El playón de la Marin")
        print("23. Marin Central")
        print("24. Simon Bolivar")
        print("25. Eugenio Espejo")
        print("26. Casa de la cultura")
        print("27. Galo Plaza")
        print("28. De las universidades")
        print("29. Manuela Cañizares")
        print("30. Baca Ortiz")
        print("31. Orellana")
        print("32. La Paz")
        print("33. San Martin")
        print("34. Bellavista")
        print("35. Eloy ALfaro")
        print("36. Benalcazar")
        print("37. Naciones Unidas")
        print("38. 24 de Mayo")
        print("39. Los Sauces")
        print("40. Jipijapa")
        print("41. Terminal Rio Coca")
        print("42. Terminal Quitumbe")
        print("Elija una opcion: ",end="")
        #ingresamos una opcion del menu por teclado
        opcion4=validar_numeros_enteros()
        #validamos que solo ingrese opciones del menu
        while(opcion4<1 or opcion4>42):
            print("Elija una opcion dentro del rango: ",end="")
            opcion4=validar_numeros_enteros()
        #dependiendo de la seleccion de estacion le dara el nombre de esa estacion a una variable
        if(opcion4==1):
            estacion="Terminal Sur ecovia"
        if(opcion4==2):
            estacion="Santo Tomas"
        if(opcion4==3):
            estacion="San Jose de Guamani Caupicho"
        if(opcion4==4):
            estacion="El Beaterio Nueva Aurora II"
        if(opcion4==5):
            estacion="La Bretaña"
        if(opcion4==6):
            estacion="Guayanay Ñam"
        if(opcion4==7):
            estacion="El Capulí"
        if(opcion4==8):
            estacion="Otoya"
        if(opcion4==9):
            estacion="Quilallacta"
        if(opcion4==10):
            estacion="Pacarillacta"
        if(opcion4==11):
            estacion="Puente de guajaló"
        if(opcion4==12):
            estacion="San Cristobal"
        if(opcion4==13):
            estacion="Ayapamba"
        if(opcion4==14):
            estacion="El Comercio"
        if(opcion4==15):
            estacion="San Bartolo"
        if(opcion4==16):
            estacion="Epiclachima"
        if(opcion4==17):
            estacion="Pujilí"
        if(opcion4==18):
            estacion="El Recreo"
        if(opcion4==19):
            estacion="Estadio Chimbacalle"
        if(opcion4==20):
            estacion="Teatro Mexico"
        if(opcion4==21):
            estacion="Colegio Montufar"
        if(opcion4==22):
            estacion="El playón de la Marin"
        if(opcion4==23):
            estacion="Marin Central"
        if(opcion4==24):
            estacion="Simon Bolivar"
        if(opcion4==25):
            estacion="Eugenio Espejo"
        if(opcion4==26):
            estacion="Casa de la cultura"
        if(opcion4==27):
            estacion="Galo Plaza"
        if(opcion4==28):
            estacion="De las universidades"
        if(opcion4==29):
            estacion="Manuela Cañizares"
        if(opcion4==30):
            estacion="Baca Ortiz"
        if(opcion4==31):
            estacion="Orellana"
        if(opcion4==32):
            estacion="La Paz"
        if(opcion4==33):
            estacion="San Martin"
        if(opcion4==34):
            estacion="Bellavista"
        if(opcion4==35):
            estacion="Eloy ALfaro"
        if(opcion4==36):
            estacion="Benalcazar"
        if(opcion4==37):
            estacion="Naciones Unidas"
        if(opcion4==38):
            estacion="24 de Mayo"
        if(opcion4==39):
            estacion="Los Sauces"
        if(opcion4==40):
            estacion="Jipijapa"
        if(opcion4==41):
            estacion="Terminal Rio Coca"
        if(opcion4==42):
            estacion="Terminal Quitumbe"   
        #retornamos estacion
        return estacion
def menu_horario_dia():
    '''
    Funcion que pide al usuario que dia y a que hora usará el sistema de transporte
    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        dia : int
        horario : int
    '''
    print("Que dia utilizara el servicio de transporte?")
    print("1. Lunes")
    print("2. Martes")
    print("3. Miercoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sabado")
    print("7. Domingo\nElija una opcion: ",end="")
    #Ingreso el dia
    dia=validar_numeros_enteros()
    #valido que el dia sea lunes,martes,mmiercoles,jueves,viernes,sabado,domingo
    while(dia<1 or dia>7):
        print("Ingrese numeros dentro del rango: ",end="")
        horario=validar_numeros_enteros()
    print("Ingrese a que hora utilizara el servicio de transporte(enteros entre 1 y 24): ",end="")
    #ingreso la hora del uso de servicio
    horario=validar_numeros_enteros()
    #valido que solo sean numeros enteros
    while(horario<1 or horario>24):
        print("Ingrese numeros dentro del rango: ",end="")
        horario=validar_numeros_enteros()
    #limpio pantala
    os.system("cls")
    #retorno el dia y hora
    return dia,horario
def calcular_costo(dia,horario,camino):
    '''
    Funcion que calcula el costo dependiendo el dia y hora de uso del sistema de transporte
    Parametros:
        dia : int
        horario : int
        camino : nx
    Retorna:
        Esta funcion no retorna ningun tipo de dato
    '''
    #declaramos variable costo en cero para usarla como contador
    costo=0
    #si usa el transporte de lunes a vieres antes de las 5 odespues de las 9 o si lo usa sabado y domingo antes de las 5 o despues de las 8
    if((dia==1 and horario<5 and horario>21) or (dia==2 and horario<5 and horario>21) or (dia==3 and horario<5 and horario>21) or (dia==4 and horario<5 and horario>21) or (dia==5 and horario<5 and horario>21) or (dia==6 and horario<5 and horario>20) or (dia==7 and horario<5 and horario>20)):
        #imprimir mensajes de que las estaciones estan cerradas
        print("Las estaciones a esa hora estan cerradas")
        print("Abriendo estaciones...")
        #aumentamos el costo en +1 por abrir las estaciones
        costo=costo+1
        #aumentamos el costo dependiendo de las estaciones por las cuales pasara el usuario para llegar a su destino
        for i in range(len(camino) - 1):
            costo += 1
        print("Estaciones abiertas")
        
    else:
        #aumentamos en 1 por cada estacion por la que pase el usuario
        for i in range(len(camino) - 1):
            costo += 1
    #imprimo el costo
    print("El costo total es:", costo)
if __name__ == '__main__':
    #creo los nodos que voy a utilizar durante el programa
    rutas=rutas_Quito()
    #uno los nodos dependiendo de las estaciones
    rutas=unir_nodos(rutas)
    #imprimo informacion sobre los nodos
    print(rutas)
    #pregunta al usuario en que dia y a que hora se subira a una estacion
    dia,horario=menu_horario_dia()
    print("Indique el punto de inicio")
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
        camino=buscar_ruta(inicio,final,rutas)
        #calculamos el costo por utilizar este servicio
        calcular_costo(dia,horario,camino)
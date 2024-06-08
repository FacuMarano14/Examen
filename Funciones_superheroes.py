from data_stark import *
from os import system
from Superheroes.Funciones import *

def limpiar_pantalla():
    """Limpia la pantalla
    """
    system("cls")
#-------------------------------------------------------------------------------------------------------------------------------------
def pausar():
    """Pausa la animacion entre operaciones
    """
    system("pause")
#-------------------------------------------------------------------------------------------------------------------------------------
def menu()-> str:
    """Menu de opciones

    Args:
        a (int): Ingresa un numero del 1 al 8

    Returns:
        str: _description_
    """
    limpiar_pantalla()
    print("Menu de opciones")
    print("1 - Nombres")
    print("2 - Nombres y Altura")
    print("3 - Superheroe mas Alto")
    print("4 - Superheroe mas Bajo")
    print("5 - Promedio de Altura")
    print("6 - Nombre de mas Bajo y Alto")
    print("7 - Mas y Menos Pesado")
    print("8 - Masculinos")
    print("9 - Femeninas")
    print("10 - Maculino mas alto")
    print("11 - Femenina mas alta")
    print("12 - Masculino mas bajo")
    print("13 - Femenina mas baja")
    print("14 - Altura promedio masculinos")
    print("15 - Altura promedio femeninas")
    print("16 - Nombres mas alto y mas bajo Masculino y Femenino")
    print("17 - Tipos de Color de Ojos")
    print("18 - Tipos de Color de Pelo")
    print("19 - Tipo de Inteligencia")
    print("20 - Agrupar por color de Ojos")
    print("21 - Agrupar por color de Pelo")
    print("22 - Agrupar por inteligencia")
    print("23 - Salir")
    opcion = input("Ingrese opcion: ")
    return opcion
#------------------------------------------------------------------------------------------------------
def stark_normalizar_datos(lista_heroes: list[dict])-> bool:
    
    if lista_heroes != []:

        retorno = False
        for i in range(len(lista_heroes)):

            if type(lista_heroes[i]["altura"]) != float:
                altura_float = float(lista_heroes[i]["altura"])
                lista_heroes[i]["altura"] = altura_float
                retorno = True

            if type(lista_heroes[i]["peso"]) != float:
                lista_heroes[i]["peso"] = float(lista_heroes[i]["peso"])
                retorno = True

            if type(lista_heroes[i]["fuerza"]) != int:
                lista_heroes[i]["fuerza"] = int(lista_heroes[i]["fuerza"])
                retorno = True

        return retorno

    else:
        return retorno
#------------------------------------------------------------------------------------------------------
def mostrar_campo_superheroes(campo, lista:list):
    for el in lista:
        print(el[campo])
#------------------------------------------------------------------------------------------------------
def mostrar_dos_campos_superheroes(campo_1, campo_2, lista:list):
    for el in lista:
        print(el[campo_1], el[campo_2])
#------------------------------------------------------------------------------------------------------
def filtrar_superheroes_campo(campo, valor, lista):
    lista_retorno = []
    for el in lista:
        if [campo] == valor:
            lista_retorno.append(el)
    return lista_retorno
#------------------------------------------------------------------------------------------------------
def mapear_lista(procesadora, lista:list):
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno

#------------------------------------------------------------------------------------------------------
def sacar_mayor_altura(lista:list):
    if not isinstance(lista,list): raise TypeError ("Debe ser una lista")
    for _ in lista:
        nombre_altura_superheroe = mapear_lista(lambda altura: (altura["altura"], altura["nombre"]), lista)
        mayor_altura = calcular_mayor(nombre_altura_superheroe)
    mensaje = f"La mayor altura es de {mayor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def sacar_mayor_menor_peso(lista:list):
    if not isinstance(lista,list): raise TypeError ("Debe ser una lista")
    for _ in lista:
        nombre_peso_superheroe = mapear_lista(lambda nombre: (nombre["peso"], (nombre["nombre"])), lista)
        mayor_peso = calcular_mayor(nombre_peso_superheroe)
    
    if not isinstance(lista,list): raise TypeError ("Debe ser una lista")
    for _ in lista:
        nombre_peso_superheroe = mapear_lista(lambda nombre: (nombre["peso"], (nombre["nombre"])), lista)
        menor_peso = calcular_menor(nombre_peso_superheroe)
    mensaje = f"El mayor peso es de {mayor_peso} y el menor es de {menor_peso}"
    return mensaje
#------------------------------------------------------------------------------------------------------

def super_mayor_menor_altura(lista:list):
    mayor_altura = sacar_mayor_altura(lista)
    menor_altura = sacar_menor_altura(lista)
    mensaje = f"{mayor_altura}{menor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------

def sacar_menor_altura(lista:list):
    if not isinstance(lista,list): raise TypeError ("Debe ser una lista")
    for _ in lista:
        nombre_altura_superheroe = mapear_lista(lambda nombre: (nombre["altura"], (nombre["nombre"])), lista)
        menor_altura = calcular_menor(nombre_altura_superheroe)
    mensaje = f"La menor altura es de {menor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def sacar_menor_peso(lista:list):
    if not isinstance(lista,list): raise TypeError ("Debe ser una lista")
    for _ in lista:
        nombre_peso_superheroe = mapear_lista(lambda nombre: (nombre["peso"], (nombre["nombre"])), lista)
        menor_peso = calcular_menor(nombre_peso_superheroe)
    mensaje = f"El menor peso es de {menor_peso}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def altura_promedio_superheroes(lista:list):
    for _ in lista:
        altura_total = mapear_lista(lambda altura: (altura["altura"]), lista)
        promedio = calcular_promedio4(altura_total)
    return promedio
#------------------------------------------------------------------------------------------------------
def calcular_mayor(lista:list)->int:

    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero > num_mayor :
            num_mayor = numero
            flag = True
    return num_mayor
#------------------------------------------------------------------------------------------------------
def calcular_menor(lista:list)->int:
    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero < num_menor :
            num_menor = numero
            flag = True
    return num_menor
#------------------------------------------------------------------------------------------------------
def filtrar_listas(funcion,lista:list)->list:                      
    lista_retorno = []
    for el in lista:
        if funcion(el): 
            lista_retorno.append((el))
    return lista_retorno

#------------------------------------------------------------------------------------------------------
def super_masculinos(lista:list):
    supers_masculinos = filtrar_listas(lambda sup: sup["genero"] == "M", lista)
    mostrar_campo_superheroes("nombre", supers_masculinos)
#------------------------------------------------------------------------------------------------------
def super_femeninos(lista:list):
    supers_femeninos = filtrar_listas(lambda sup: sup["genero"] == "F", lista)
    mostrar_campo_superheroes("nombre", supers_femeninos)
#------------------------------------------------------------------------------------------------------
def super_alto_masculino(lista:list):
    supers_masculinos = filtrar_listas(lambda sup: sup["genero"] == "M", lista)
    nombre_altura_superheroe = mapear_lista(lambda altura: (altura["altura"], altura["nombre"]), supers_masculinos)
    mayor_altura = calcular_mayor(nombre_altura_superheroe)
    mensaje = f"El superheroe masculino mas alto es {mayor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def super_alto_femenino(lista:list):
    supers_femeninos = filtrar_listas(lambda sup: sup["genero"] == "F", lista)
    nombre_altura_superheroe = mapear_lista(lambda altura: (altura["altura"], altura["nombre"]), supers_femeninos)
    mayor_altura = calcular_mayor(nombre_altura_superheroe)
    mensaje = f"El superheroe femenino mas alto es {mayor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def super_bajo_masculino(lista:list):
    supers_masculinos = filtrar_listas(lambda sup: sup["genero"] == "M", lista)
    nombre_altura_superheroe = mapear_lista(lambda altura: (altura["altura"], altura["nombre"]), supers_masculinos)
    menor_altura = calcular_menor(nombre_altura_superheroe)
    mensaje = f"El superheroe masculino mas bajo es {menor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def super_bajo_femenino(lista:list):
    supers_femeninos = filtrar_listas(lambda sup: sup["genero"] == "F", lista)
    nombre_altura_superheroe = mapear_lista(lambda altura: (altura["altura"], altura["nombre"]), supers_femeninos)
    menor_altura = calcular_menor(nombre_altura_superheroe)
    mensaje = f"El superheroe femenino mas bajo es {menor_altura}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def altura_promedio_superheroes_masc(lista:list):
    for _ in lista:
        supers_masculinos = filtrar_listas(lambda sup: (sup["genero"] == "M"), lista)
        altura_total = mapear_lista(lambda altura: (altura["altura"]), supers_masculinos)
        promedio = calcular_promedio4(altura_total)
    return promedio
#------------------------------------------------------------------------------------------------------
def altura_promedio_superheroes_fem(lista:list):
    for _ in lista:
        supers_femeninos = filtrar_listas(lambda sup: (sup["genero"] == "F"), lista)
        altura_total = mapear_lista(lambda altura: (altura["altura"]), supers_femeninos)
        promedio = calcular_promedio4(altura_total)
    return promedio
#------------------------------------------------------------------------------------------------------
def max_min_promedio_altura_masc(lista:list):
    mayor_altura_masc = super_alto_masculino(lista)
    menor_altura_masc = super_bajo_masculino(lista)
    promedio_altura_masc = altura_promedio_superheroes_masc(lista)
    mensaje = f"{mayor_altura_masc}, {menor_altura_masc} y el promedio de altura es {promedio_altura_masc}"
    return mensaje
#------------------------------------------------------------------------------------------------------
def mostrar_max_min_prom(lista:list):
    mas_alto_m = super_alto_masculino(lista)
    mas_alto_f = super_alto_femenino(lista)
    mas_bajo_m = super_bajo_masculino(lista)
    mas_bajo_f = super_bajo_femenino(lista)
    prom_alt_m = altura_promedio_superheroes_masc(lista)
    prom_alt_f = altura_promedio_superheroes_fem(lista)

    print(f"{mas_alto_m}\n")
    print(f"{mas_alto_f}\n")
    print(f"{mas_bajo_m}\n")
    print(f"{mas_bajo_f}\n")
    print(f"Promedio altura M: {prom_alt_m}\n")
    print(f"Promedio altura F: {prom_alt_f}\n")
#------------------------------------------------------------------------------------------------------
def tipo_color_ojos(lista:list):
    colores_ojos = {}

    for heroe in lista:
        color = heroe.get("color_ojos", "color_pelo")
        if color in colores_ojos:
            colores_ojos[color] += 1
        else:
            colores_ojos[color] = 1

    for color, cant in colores_ojos.items():
        print(f"{color}, {cant}")
    
#------------------------------------------------------------------------------------------------------
def tipo_color_pelo(lista:list):
    colores_pelo = {}

    for heroe in lista:
        color = heroe.get("color_pelo", "")
        if color in colores_pelo:
            colores_pelo[color] += 1
        else:
            colores_pelo[color] = 1

    for color, cant in colores_pelo.items():
        print(f"{color}, {cant}")
#------------------------------------------------------------------------------------------------------
def tipo_inteligencia(lista:list):
    inteligencia = {}

    for heroe in lista:
        intel = heroe.get("inteligencia", "No tiene")
        contador = 0
        if intel in inteligencia:
            inteligencia[intel] += 1
        elif intel == "":
            contador += 1
            intel = "No tiene"
            print(intel, contador)
        else:
            inteligencia[intel] = 1

    for color, cant in inteligencia.items():
        print(f"{color}, {cant}")
#------------------------------------------------------------------------------------------------------
def agrupar_ojos(target:str, lista:list):
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_ojos = filtrar_listas(lambda tipo: (tipo["color_ojos"] == target), lista)
    nombre_ojos = mapear_lista(lambda nom: nom["nombre"], lista_ojos)
    return nombre_ojos

def agrupar_pelo(target:str, lista:list):
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_pelo = filtrar_listas(lambda tipo: (tipo["color_pelo"] == target), lista)
    nombre_pelo = mapear_lista(lambda nom: nom["nombre"], lista_pelo)
    return nombre_pelo

def agrupar_inteligencia(target:str, lista:list):
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_inteligencia = filtrar_listas(lambda tipo: (tipo["inteligencia"] == target), lista)
    nombre_inteligencia = mapear_lista(lambda nom: nom["nombre"], lista_inteligencia)
    return nombre_inteligencia
def duplicar (numero:int)->int:
    numero = numero * 2
    return numero
    
#-------------------------------------------------------------------------------------

def duplicar_valores(listas:list)->None:
    for i in range(len(listas)):
        listas [i] = listas [ i] * 2

#-------------------------------------------------------------------------------------


def mostrar_lista(lista:list)->None:
    for el in lista:
        print(el,end=" ")
    print()

#-------------------------------------------------------------------------------------


def cargar_lista_enteros_random(lista:list, cant:int, desde:int, hasta:int)->None:
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))

#-------------------------------------------------------------------------------------


def crear_lista_enteros_random(cant:int, desde:int, hasta:int)->list:
    from random import randint
    lista = [ ]
    for _ in range(cant):
        lista.append(randint(desde, hasta))  
    return lista

#-------------------------------------------------------------------------------------


def totalizar_listas(lista:list)->int:
    total = 0
    for numero in lista:
        total += numero
    return total

#-------------------------------------------------------------------------------------

def calcular_promedio4(lista:list)->float:
    total = 0
    vuelta = 0
    for numero in lista:
        total += numero
        vuelta += 1

    promedio = total / vuelta
    return promedio

def calcular_promedio_2(lista:list)->float:
    
    return totalizar_listas(lista) / len(lista)

def calcular_promedio_3(lista:list)->float:
    cant = len(lista)
    if cant == 0:
        raise ValueError("No esta definido el promedio de una lista vacia")
    return totalizar_listas(lista) / cant

def calcular_promedio(a:int, b:int)->float:
    promedio = (a+b) / 2
    return promedio
#-------------------------------------------------------------------------------------
def calcular_promedio_numero(numero: int, cant: int):
    if numero != 0 and cant != 0:
        resultado = numero / cant
        return resultado
    else:
        print("No hay nadie en este sector")
#-------------------------------------------------------------------------------------
def calcular_mayor(lista:list)->int:

    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero > num_mayor :
            num_mayor = numero
            flag = True
    return num_mayor
#------------------------------------------------------------------------------------
def calcular_menor(lista:list)->int:
    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero < num_menor :
            num_menor = numero
            flag = True
    return num_menor
#------------------------------------------------------------------------------------
def entero_in_lista(lista:list, target:int)->bool:
    for numero in lista:
        if numero == target:
            target = True
            return True
    return False

#-----------------------------------------------------------------------------------
def buscar_in_lista(lista:list, target:int)->bool:
    for numero in lista:
        if numero == target:
            target = True
            return True
    return False
#-----------------------------------------------------------------------------------
def buscar_numero_lista(lista:list, target:int)->int:
    resultado = -1
    for i in range(lista):
        if lista[i] == target:
            resultado = i
            break
    return resultado
#busca el elemento y te dice en que posicion esta, sino esta posicion es -1 (ver como lo hacen en clase)
#-----------------------------------------------------------------------------------
def contar_in_lista(lista:list, target:int)->int:
    elemento = 0
    for numero in lista:
        if numero == target:
            elemento += 1
    return elemento
#busca el elemento y te dice cuantas veces esta

#-----------------------------------------------------------------------------------
def buscar_in_lista(lista: list, target: int) -> int:
    indice = -1
    for i in range(len(lista)):
        if lista[i] == target:
            indice = i
            break
    return indice
#-----------------------------------------------------------------------------------
def validar_lista(lista:list)->None:
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")
    return True
#-----------------------------------------------------------------------------------
def swap_lista(lista:list,i:int,j:int)->None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
#-----------------------------------------------------------------------------------
def ordenar_lista(lista:list, asc:bool=True)->None:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (asc and lista[i] > lista[j]) or (not asc and lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

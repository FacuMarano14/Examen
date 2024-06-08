from data_stark import *
from Funciones_superheroes import *


stark_normalizar_datos(lista_personajes)

seguir = True
flag_opcion = False

while seguir == True:
    match menu():
        case "1":
            mostrar_campo_superheroes("nombre", lista_personajes)
            pausar()
        case "2":
            mostrar_dos_campos_superheroes("nombre", "altura", lista_personajes)
            pausar()
        case "3":
            mayor_altura = sacar_mayor_altura(lista_personajes)
            print(mayor_altura)
            pausar()
        case "4":
            menor_altura = sacar_menor_altura(lista_personajes)
            print(menor_altura)
            pausar()
        case "5":
            promedio_altura = altura_promedio_superheroes(lista_personajes)
            print(promedio_altura)
            pausar()
        case "6":
            mayor_menor_altura = super_mayor_menor_altura(lista_personajes)
            print(mayor_menor_altura)
            pausar()
        case "7":
            mayor_menor_peso = sacar_mayor_menor_peso(lista_personajes)
            print(mayor_menor_peso)
            pausar()
        case "8":
            super_masculinos(lista_personajes)
            pausar()
        case "9":
            super_femeninos(lista_personajes)
            pausar()
        case "10":
            super_alto_masc = super_alto_masculino(lista_personajes)
            print(super_alto_masc)
            pausar()
        case "11":
            super_alto_fem = super_alto_femenino(lista_personajes)
            print(super_alto_fem)
            pausar()
        case "12":
            super_bajo_masc = super_bajo_masculino(lista_personajes)
            print(super_bajo_masc)
            pausar()
        case "13":
            super_bajo_fem = super_bajo_femenino(lista_personajes)
            print(super_bajo_fem)
            pausar()
        case "14":
            altura_promedio_masc = altura_promedio_superheroes_masc(lista_personajes)
            print(altura_promedio_masc)
            pausar()
        case "15":
            altura_promedio_fem = altura_promedio_superheroes_fem(lista_personajes)
            print(altura_promedio_fem)
            pausar()
        case "16":
            mostrar_max_min_prom(lista_personajes)
            pausar()
        case "17":
            colores_ojos = tipo_color_ojos(lista_personajes)
            print(colores_ojos)
            pausar()
        case "18":
            colores_pelo = tipo_color_pelo(lista_personajes)
            print(colores_pelo)
            pausar()
        case "19":
            tipo_int = tipo_inteligencia(lista_personajes)
            print(tipo_int)
            pausar()
        case "20":
            agrupar = agrupar_ojos("Blue", lista_personajes)
            print(agrupar)
            pausar()
        case "21":
            agrupar = agrupar_pelo("Brown", lista_personajes)
            print(agrupar)
            pausar()
        case "22":
            agrupar = agrupar_inteligencia("average", lista_personajes)
            print(agrupar)
            pausar()
        case "23":
            seguir = False
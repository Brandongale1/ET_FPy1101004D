def menu_cine():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    return menu_cine
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_genero(genero, peliculas, cartelera):
    total = 0
    genero_buscado = genero.strip().lower()
    for codigo, datos in peliculas.items():
        genero_pelicula = datos[1].lower()
        if genero_pelicula == genero_buscado:
            cupos = cartelera[codigo][1]
            total += cupos
            
    print(f"El total de cupos disponibles es: {total}")
    return cupos_genero

def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    for codigo, datos in cartelera.items():
        precio = datos[0]
        cupos = datos[1]
        if p_min <= precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(f"{titulo}-{codigo}")
    resultados.sort()
    if len(resultados) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print(f"Las películas encontradas son: {resultados}")

def buscar_codigo(codigo, diccionario):
    
    return codigo.upper() in diccionario

def actualizar_precio(codigo, nuevo_precio, cartelera):
    
    codigo = codigo.upper()
    if buscar_codigo(codigo, cartelera):
        cartelera[codigo][0] = nuevo_precio
        return True
    else:
        return False

def eliminar_pelicula(codigo, peliculas, cartelera):
    """Elimina la película de ambos diccionarios si el código existe."""
    codigo = codigo.upper()
    if buscar_codigo(codigo, peliculas):
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    else:
        return False







peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    
}
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
    }




while True:
    menu_cine()
    opcion=leer_opcion()
    if  opcion== 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero, peliculas, cartelera)
    elif  opcion== 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min < 0 or p_max < 0 or p_min > p_max:
                        print("Debe ingresar valores enteros")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, peliculas, cartelera)
    elif  opcion== 3:
            print("nada")
    elif  opcion== 4:
            print("nada")
    elif  opcion== 5:
            codigo = input("Ingrese código de película: ")
            if eliminar_pelicula(codigo, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")
    elif  opcion== 6:
            print("Programa finalizado.")
            break

def datos_archivo (linea): 
    datos= linea.strip (). split (",")
    
    id_participante=int(datos[0])
    fecha = datos[1]
    app = datos[2]
    cantidad_uso = int (datos[3])
    tiempo_uso = float (datos[4])
    
    lista_valores= [id_participante, fecha, app, cantidad_uso, tiempo_uso]
    return lista_valores
   








def cargar_datos(ruta: str) -> list:
    """
    Qué hace:
    Lee un archivo CSV y devuelve una lista de registros.

    Parámetros:
    - ruta (str): ruta del archivo

    Retorna:
    - list: lista de diccionarios con los datos
    """

    datos = []

    with open(ruta, "r") as archivo:

        next(archivo)  # saltear encabezado

        for linea in archivo:

            lista_valores = parsear_linea(linea)

            if len(lista_valores) < 5:
                continue  # evita errores

            registro = {
                "id_participante": lista_valores[0],
                "fecha": lista_valores[1],
                "app": lista_valores[2],
                "cantidad_uso": lista_valores[3],
                "tiempo_uso": lista_valores[4]
            }

            datos.append(registro)


    return datos

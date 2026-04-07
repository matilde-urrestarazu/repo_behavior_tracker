def filtrar_por_participante(datos, id_participante):
    
    '''
    La función obtiene los datos de un participante especifico, ignorando los demás.
    
    parametros:
        datos (list): lista con la informacion de todos los participantes
        id_participante (int): numero que identifica al participante cuyos datos se quiere obtener 
    return:
        datos_participante (list): datos del participante filtrado

    '''
    datos_participante = []
    for registro in datos:     
       if id_participante == registro["id_participante"]:
            datos_participante.append(registro)
    return datos_participante

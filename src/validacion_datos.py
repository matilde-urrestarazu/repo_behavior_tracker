def validar_registro(registro: dict) -> bool:
    """
    Verifica que un registro tenga datos válidos.
    """

    # verificar que existan las claves
    if "id_participante" not in registro:
        return False
    if "fecha" not in registro:
        return False
    if "app" not in registro:
        return False
    if "cantidad_uso" not in registro:
        return False
    if "tiempo_uso" not in registro:
        return False

    # verificar que no estén vacíos
    if registro["app"] == "":
        return False
    
# verificar valores numéricos positivos
    if registro["id_participante"] < 0:
        return False
    if registro["cantidad_uso"] < 0:
        return False
    if registro["tiempo_uso"] < 0:
        return False

    return True
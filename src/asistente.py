import pandas as pd

def analizar_perfil(cliente):
    """
    Analiza la información disponible del perfil
    de una cliente y genera una interpretación
    basada únicamente en los datos registrados.
    """

    nombre = cliente.get("nombre", "Cliente")
    tipo_piel = cliente.get("tipo_piel")
    tono_base = cliente.get("tono_base")
    ciudad = cliente.get("ciudad")

    observaciones = []
    acciones = []

    # --------------------------------------------------------
    # TIPO DE PIEL
    # --------------------------------------------------------

    if tipo_piel and str(tipo_piel).strip():

        observaciones.append(
            f"Tipo de piel registrado: {tipo_piel}."
        )

    else:

        observaciones.append(
            "No hay un tipo de piel registrado."
        )

        acciones.append(
            "Completar el tipo de piel durante el próximo contacto."
        )

    # --------------------------------------------------------
    # TONO DE BASE
    # --------------------------------------------------------

    if tono_base and str(tono_base).strip():

        observaciones.append(
            f"Tono de base registrado: {tono_base}."
        )

    else:

        observaciones.append(
            "No hay un tono de base registrado."
        )

        acciones.append(
            "Completar el tono de base si la información está disponible."
        )

    # --------------------------------------------------------
    # CIUDAD
    # --------------------------------------------------------

    if ciudad and str(ciudad).strip():

        observaciones.append(
            f"Ciudad registrada: {ciudad}."
        )

    else:

        observaciones.append(
            "No hay una ciudad registrada."
        )

        acciones.append(
            "Completar la ciudad de la cliente."
        )

    # --------------------------------------------------------
    # PERFIL COMPLETO
    # --------------------------------------------------------

    datos_principales = [
        tipo_piel,
        tono_base,
        ciudad
    ]

    datos_completos = all(
        pd is not None
        and str(pd).strip() != ""
        and str(pd).lower() != "nan"
        for pd in datos_principales
    )

    if datos_completos:

        acciones.append(
            "El perfil contiene los principales datos disponibles."
        )

    # --------------------------------------------------------
    # RESULTADO
    # --------------------------------------------------------

    return {
        "nombre": nombre,
        "observaciones": observaciones,
        "acciones": acciones,
        "perfil_completo": datos_completos
    }
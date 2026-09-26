import pandas as pd
from pathlib import Path


RUTA_PRODUCTOS = Path("data/processed/productos.csv")


def cargar_productos():
    """
    Carga la base de conocimiento de productos.
    """
    if not RUTA_PRODUCTOS.exists():
        return pd.DataFrame()

    return pd.read_csv(RUTA_PRODUCTOS)


def tiene_dato(valor):
    """
    Comprueba si un campo contiene información válida.
    """
    return (
        valor is not None
        and not pd.isna(valor)
        and str(valor).strip() != ""
        and str(valor).lower() != "nan"
    )


def buscar_productos_compatibles(tipo_piel, tono_base):
    """
    Busca productos compatibles con el perfil de la cliente
    y explica el motivo de cada coincidencia.
    """

    productos = cargar_productos()

    if productos.empty:
        return []

    if not tiene_dato(tipo_piel):
        return []

    tipo_piel = str(tipo_piel).strip().lower()

    if tiene_dato(tono_base):
        tono_base = str(tono_base).strip().upper()
    else:
        tono_base = ""

    productos["tipo_piel_normalizado"] = (
        productos["tipo_piel"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    productos["tono_base_normalizado"] = (
        productos["tono_base"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.upper()
    )

    recomendaciones = []

    for _, producto in productos.iterrows():

        producto_piel = producto["tipo_piel_normalizado"]
        producto_tono = producto["tono_base_normalizado"]

        coincide_piel = (
            producto_piel == tipo_piel
        )

        coincide_tono = (
            producto_tono == tono_base
        )

        producto_sin_tono = (
            producto_tono in ["", "TODOS", "NO APLICA"]
        )

        # Coincidencia directa:
        # piel + tono
        if coincide_piel and coincide_tono:

            motivo = (
                "Coincide con el tipo de piel "
                "y el tono registrados."
            )

            nivel = "Coincidencia directa"

        # Coincidencia complementaria:
        # piel, pero producto sin tono
        elif coincide_piel and producto_sin_tono:

            motivo = (
                "Coincide con el tipo de piel. "
                "Este producto no requiere un tono específico."
            )

            nivel = "Complemento por tipo de piel"

        else:
            continue

        recomendaciones.append({
            "producto_id": producto["producto_id"],
            "nombre": producto["nombre"],
            "categoria": producto["categoria"],
            "beneficio": producto["beneficio"],
            "descripcion": producto["descripcion"],
            "motivo": motivo,
            "nivel": nivel,
        })

    return recomendaciones

def analizar_perfil(cliente):
    """
    Analiza la información disponible del perfil
    y genera una interpretación orientada al seguimiento
    comercial.

    Las recomendaciones de productos se generan únicamente
    a partir de la información registrada en el CRM y de la
    base de conocimiento de productos.
    """

    nombre = cliente.get("nombre", "Cliente")
    tipo_piel = cliente.get("tipo_piel")
    tono_base = cliente.get("tono_base")
    ciudad = cliente.get("ciudad")

    observaciones = []
    acciones = []

    piel_disponible = tiene_dato(tipo_piel)
    tono_disponible = tiene_dato(tono_base)
    ciudad_disponible = tiene_dato(ciudad)

    # -----------------------------------
    # Interpretación del perfil
    # -----------------------------------

    if piel_disponible:
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

    if tono_disponible:
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

    if ciudad_disponible:
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

    # -----------------------------------
    # Estado del perfil
    # -----------------------------------

    datos_completos = (
        piel_disponible
        and tono_disponible
        and ciudad_disponible
    )

    if datos_completos:

        estado = "Perfil preparado para recomendación"

        oportunidad = (
            "La información disponible permite "
            "personalizar el próximo contacto."
        )

        accion_recomendada = (
            "Revisar los productos compatibles con "
            "las características registradas."
        )

        acciones.append(
            "Revisar productos compatibles con el perfil."
        )

        acciones.append(
            "Contactar a la cliente y registrar "
            "el resultado del seguimiento."
        )

    else:

        estado = "Perfil pendiente de completar"

        oportunidad = (
            "Antes de realizar una recomendación "
            "personalizada, conviene completar "
            "la información disponible."
        )

        accion_recomendada = (
            "Completar los datos faltantes durante "
            "el próximo contacto."
        )

    # -----------------------------------
    # Recomendaciones de productos
    # -----------------------------------

    productos_recomendados = buscar_productos_compatibles(
        tipo_piel,
        tono_base,
    )

    if productos_recomendados:

        acciones.append(
            f"Se encontraron {len(productos_recomendados)} "
            "productos compatibles."
        )

    elif datos_completos:

        acciones.append(
            "No se encontraron productos compatibles "
            "en la base de conocimiento actual."
        )

    return {
        "nombre": nombre,
        "observaciones": observaciones,
        "acciones": acciones,
        "perfil_completo": datos_completos,
        "estado": estado,
        "oportunidad": oportunidad,
        "accion_recomendada": accion_recomendada,
        "productos_recomendados": productos_recomendados,
    }
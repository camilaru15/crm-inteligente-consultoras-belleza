import sys
from pathlib import Path

import streamlit as st
import pandas as pd

# Permite importar módulos desde la carpeta raíz del proyecto
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent

if str(RAIZ_PROYECTO) not in sys.path:
    sys.path.append(str(RAIZ_PROYECTO))

from src.database import (
    inicializar_base_datos,
    agregar_cliente,
    agregar_fecha_alta_si_no_existe,
    cargar_clientes_desde_dataframe,
    obtener_clientes,
    actualizar_cliente,
    guardar_seguimiento,
    obtener_seguimientos,
)

from src.asistente import analizar_perfil

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="CRM Inteligente",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>

    /* =========================================
       FONDO GENERAL DE LA APLICACIÓN
       ========================================= */

    .stApp {
        background-color: #F7F5FC !important;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #F7F5FC !important;
    }

    [data-testid="stAppViewContainer"] .main {
        background-color: #F7F5FC !important;
    }

    .block-container {
        background-color: #F7F5FC !important;
        padding-top: 2rem;
    }


    /* =========================================
       BARRA LATERAL
       ========================================= */

    [data-testid="stSidebar"] {
        background-color: #F7F5FC !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        background-color: #F7F5FC !important;
    }


    /* =========================================
       HEADER SUPERIOR
       ========================================= */

    [data-testid="stHeader"] {
        background-color: #F7F5FC !important;
    }


    /* =========================================
       TARJETAS KPI
       ========================================= */

    .kpi-card {
        padding: 18px 20px;
        border-radius: 14px;
        min-height: 120px;
        border: 1px solid rgba(30, 55, 100, 0.08);
        box-sizing: border-box;
    }

    .kpi-card .kpi-title {
        font-size: 13px;
        color: #243B64;
        margin-bottom: 6px;
    }

    .kpi-card .kpi-value {
        font-size: 30px;
        font-weight: 700;
        color: #203A63;
        line-height: 1.1;
    }

    .kpi-card .kpi-subtitle {
        font-size: 11px;
        color: #52627A;
        margin-top: 7px;
        line-height: 1.2;
    }
    
    .kpi-icon {
    font-size: 22px;
    margin-bottom: 6px;
    line-height: 1;
    }
    
    .kpi-clientes {
    background-color: #EEE9FF;
    border-color: #DDD2FF;
    }

    .kpi-completos {
        background-color: #FFF1F7;
        border-color: #F5DCE9;
    }

    .kpi-ciudades {
        background-color: #EEF7FF;
        border-color: #D7EAFB;
    }

    .kpi-piel {
        background-color: #EEFFF8;
        border-color: #D3F3E6;
    }

    .kpi-incompletos {
        background-color: #FFF9E8;
        border-color: #F3E5B5;
    }
    /* =========================================
       CAJA DEL ASISTENTE
       ========================================= */

    .assistant-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E6E8EC;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CARGA DE DATOS
# ============================================================

RUTA_DATOS_PUBLICOS = Path("data/processed/clientes.csv")

RUTA_DATOS_PRIVADOS = Path("data/processed/clientes_privados.csv")

def formatear_celular(valor):
    if pd.isna(valor):
        return ""

    texto = str(valor).strip()

    if texto.endswith(".0") and texto[:-2].isdigit():
        texto = texto[:-2]

    return texto
  
@st.cache_data
def cargar_datos():

    # Dataset privado disponible durante el
    # desarrollo local
    if RUTA_DATOS_PRIVADOS.exists():

        return pd.read_csv(RUTA_DATOS_PRIVADOS)

    # Dataset anonimizado para entornos
    # donde no existen datos privados
    return pd.read_csv(RUTA_DATOS_PUBLICOS)


df = cargar_datos()

inicializar_base_datos()

agregar_fecha_alta_si_no_existe()

cargar_clientes_desde_dataframe(df)

df = obtener_clientes()

df["celular"] = df["celular"].apply(
    formatear_celular
)

# ============================================================
# TÍTULO
# ============================================================

st.title("CRM Inteligente para Consultoras de Belleza")

st.write("Gestión de clientes, perfiles y seguimiento comercial.")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 💄 CRM Inteligente")

    st.divider()

    opcion = st.radio(
        "Navegación",
        [
            "Inicio",
            "Clientes",
            "Segmentos",
            "Análisis",
            "Seguimiento",
        ],
    )

    st.divider()

    st.caption("MVP · Datos anonimizados")


# ============================================================
# PÁGINA INICIO
# ============================================================

if opcion == "Inicio":

    col1, col2, col3, col4, col5 = st.columns(5)

    total_clientes = len(df)

    # ---------------------------------------------------------
    # COMPLETITUD REAL DEL PERFIL
    # ---------------------------------------------------------

    campos_completitud = [
        "tipo_piel",
        "tono_base",
        "ciudad"
    ]

    datos_completitud = (
        df[campos_completitud]
        .fillna("")
        .astype(str)
        .apply(lambda columna: columna.str.strip())
    )

    perfiles_completos = (
        datos_completitud
        .ne("")
        .all(axis=1)
        .sum()
    )

    clientes_incompletos = (
        total_clientes - perfiles_completos
    )

    porcentaje_completos = (
    round(perfiles_completos / total_clientes * 100, 1)
    if total_clientes > 0
    else 0
    )

    porcentaje_incompletos = (
        round(clientes_incompletos / total_clientes * 100, 1)
        if total_clientes > 0
        else 0
    )
    # ---------------------------------------------------------
    # DISTRIBUCIONES
    # ---------------------------------------------------------

    ciudades = (
        df["ciudad"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    ciudades = ciudades[
        ciudades != ""
    ].nunique()

    tipos_piel = (
        df["tipo_piel"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    tipos_piel = tipos_piel[
        tipos_piel != ""
    ].nunique()
    
# =========================
# TARJETAS KPI
# =========================

    with col1:
        
        st.markdown(
            f"""
            <div class="kpi-card kpi-clientes">
                <div class="kpi-icon">👥</div>
                <div class="kpi-title">Clientes registrados</div>
                <div class="kpi-value">{total_clientes}</div>
                <div class="kpi-subtitle">Base actual de clientes</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="kpi-card kpi-completos">
                <div class="kpi-icon">👤</div>
                <div class="kpi-title">Perfiles completos</div>
                <div class="kpi-value">{perfiles_completos}</div>
                <div class="kpi-subtitle">{porcentaje_completos}% del total</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="kpi-card kpi-ciudades">
                <div class="kpi-icon">📍</div>
                <div class="kpi-title">Ciudades</div>
                <div class="kpi-value">{ciudades}</div>
                 <div class="kpi-subtitle">Ciudades registradas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="kpi-card kpi-piel">
                <div class="kpi-icon">🧴</div>
                <div class="kpi-title">Tipos de piel</div>
                <div class="kpi-value">{tipos_piel}</div>
                <div class="kpi-subtitle">Categorías registradas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col5:

      st.markdown(
          f"""
          <div class="kpi-card kpi-incompletos">
              <div class="kpi-icon">⚠️</div>
              <div class="kpi-title">Información incompleta</div>
              <div class="kpi-value">{clientes_incompletos}</div>
              <div class="kpi-subtitle">{porcentaje_incompletos}% del total</div>
          </div>
          """,
          unsafe_allow_html=True,
      )
    
    st.markdown(
    "<div style='height: 18px;'></div>",
    unsafe_allow_html=True
    )
    
    if clientes_incompletos > 0:

      st.warning(
          f"{clientes_incompletos} clientes tienen "
          "información incompleta. "
          "Puedes revisar sus perfiles para "
          "completar los datos disponibles."
      )
    st.markdown(
    "<div style='height: 28px;'></div>",
    unsafe_allow_html=True
    )
    

    st.divider()

    st.subheader("Clientes")

    # --------------------------------------------------------
    # BÚSQUEDA
    # --------------------------------------------------------

    texto_busqueda = st.text_input(
        "Buscar cliente",
        placeholder="Ej. Laura ...",
    )

    df_filtrado = df.copy()

    if texto_busqueda:
        df_filtrado = df_filtrado[
            df_filtrado["nombre"].str.contains(
                texto_busqueda,
                case=False,
                na=False,
            )
        ]

    # --------------------------------------------------------
    # FILTROS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        tipos = ["Todos"] + sorted(df["tipo_piel"].dropna().unique().tolist())

        filtro_piel = st.selectbox(
            "Tipo de piel",
            tipos,
        )

    with col2:
        tonos = ["Todos"] + sorted(df["tono_base"].dropna().unique().tolist())

        filtro_tono = st.selectbox(
            "Tono de base",
            tonos,
        )

    with col3:
        ciudades_lista = ["Todas"] + sorted(df["ciudad"].dropna().unique().tolist())

        filtro_ciudad = st.selectbox(
            "Ciudad",
            ciudades_lista,
        )

    if filtro_piel != "Todos":
        df_filtrado = df_filtrado[df_filtrado["tipo_piel"] == filtro_piel]

    if filtro_tono != "Todos":
        df_filtrado = df_filtrado[df_filtrado["tono_base"] == filtro_tono]

    if filtro_ciudad != "Todas":
        df_filtrado = df_filtrado[df_filtrado["ciudad"] == filtro_ciudad]


    # --------------------------------------------------------
    # TABLA + FICHA LATERAL
    # --------------------------------------------------------

    col_tabla, col_ficha = st.columns(
        [2.1, 1],
        gap="large"
    )

    # ========================================================
    # TABLA DE CLIENTES
    # ========================================================

    with col_tabla:

        st.caption(
            f"Mostrando {len(df_filtrado)} clientes"
        )

        if len(df_filtrado) > 0:

            clientes_por_pagina = 10

            total_paginas = max(
                1,
                (len(df_filtrado) - 1)
                // clientes_por_pagina + 1
            )

            if "pagina_clientes" not in st.session_state:
                st.session_state.pagina_clientes = 1

            if (
                st.session_state.pagina_clientes
                > total_paginas
            ):
                st.session_state.pagina_clientes = (
                    total_paginas
                )

            pagina_actual = (
                st.session_state.pagina_clientes
            )

            inicio = (
                pagina_actual - 1
            ) * clientes_por_pagina

            fin = inicio + clientes_por_pagina

            df_pagina = df_filtrado.iloc[inicio:fin]

            # ------------------------------------------------
            # ENCABEZADOS
            # ------------------------------------------------

            columnas_tabla = st.columns(
                [1.3, 2.3, 1.7, 1.7, 1.7, 1.7, 1.2]
            )

            encabezados = [
                "ID",
                "Nombre",
                "Celular",
                "Tipo de piel",
                "Tono de base",
                "Ciudad",
                "Acción"
            ]

            for columna, encabezado in zip(
                columnas_tabla,
                encabezados
            ):

                columna.markdown(
                    f"**{encabezado}**"
                )

            st.divider()

            # ------------------------------------------------
            # FILAS
            # ------------------------------------------------

            for _, fila in df_pagina.iterrows():

                columnas = st.columns(
                    [
                        1.3,
                        2.3,
                        1.7,
                        1.7,
                        1.7,
                        1.7,
                        1.2
                    ]
                )

                cliente_id = fila["cliente_id"]

                nombre = (
                    "Sin nombre"
                    if pd.isna(fila["nombre"])
                    else str(fila["nombre"])
                )

                celular = (
                    "Sin información"
                    if pd.isna(fila["celular"])
                    else str(fila["celular"])
                )

                tipo_piel = (
                    "Sin información"
                    if pd.isna(fila["tipo_piel"])
                    else str(fila["tipo_piel"])
                )

                tono_base = (
                    "Sin información"
                    if pd.isna(fila["tono_base"])
                    else str(fila["tono_base"])
                )

                ciudad = (
                    "Sin información"
                    if pd.isna(fila["ciudad"])
                    else str(fila["ciudad"])
                )

                columnas[0].write(cliente_id)
                columnas[1].write(nombre)
                columnas[2].write(celular)
                columnas[3].write(tipo_piel)
                columnas[4].write(tono_base)
                columnas[5].write(ciudad)

                if columnas[6].button(
                    "Ver ficha",
                    key=f"ver_{cliente_id}"
                ):

                    st.session_state[
                        "cliente_seleccionado_id"
                    ] = cliente_id

                    st.rerun()

                st.divider()

            # ------------------------------------------------
            # PAGINACIÓN
            # ------------------------------------------------

            col_anterior, col_pagina, col_siguiente = (
                st.columns([1, 2, 1])
            )

            with col_anterior:

                if st.button(
                    "← Anterior",
                    disabled=pagina_actual <= 1,
                    key="pagina_anterior"
                ):

                    st.session_state.pagina_clientes -= 1
                    st.rerun()

            with col_pagina:

                st.markdown(
                    f"""
                    <div style="text-align:center;">
                        Página {pagina_actual}
                        de {total_paginas}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col_siguiente:

                if st.button(
                    "Siguiente →",
                    disabled=pagina_actual >= total_paginas,
                    key="pagina_siguiente"
                ):

                    st.session_state.pagina_clientes += 1
                    st.rerun()

        else:

            st.info(
                "No se encontraron clientes con "
                "los filtros seleccionados."
            )

# ========================================================
#  FICHA LATERAL
# ========================================================
    with col_ficha:

        if "cliente_seleccionado_id" in st.session_state:

            cliente_id = st.session_state[
                "cliente_seleccionado_id"
            ]

            cliente_df = df[
                df["cliente_id"] == cliente_id
            ]

            if not cliente_df.empty:

                cliente = cliente_df.iloc[0]

                # =================================================
                # DATOS BÁSICOS
                # =================================================

                nombre = (
                    "Sin nombre"
                    if pd.isna(cliente["nombre"])
                    else str(cliente["nombre"])
                )

                celular = formatear_celular(
                    cliente["celular"]
                )

                if not celular:
                    celular = "Sin información"

                ciudad = (
                    "Sin información"
                    if pd.isna(cliente["ciudad"])
                    else str(cliente["ciudad"])
                )

                tipo_piel = (
                    "Sin información"
                    if pd.isna(cliente["tipo_piel"])
                    else str(cliente["tipo_piel"])
                )

                tono_base = (
                    "Sin información"
                    if pd.isna(cliente["tono_base"])
                    else str(cliente["tono_base"])
                )

                # =================================================
                # CAMPOS FALTANTES
                # =================================================

                campos_faltantes = []

                campos_obligatorios = {
                    "tipo_piel": "Tipo de piel",
                    "tono_base": "Tono de base",
                    "ciudad": "Ciudad"
                }

                for campo, nombre_campo in (
                    campos_obligatorios.items()
                ):

                    valor = cliente[campo]

                    if (
                        pd.isna(valor)
                        or str(valor).strip() == ""
                        or str(valor).lower() == "nan"
                    ):

                        campos_faltantes.append(
                            nombre_campo
                        )

                perfil_completo = (
                    len(campos_faltantes) == 0
                )

                # =================================================
                # CONTENEDOR PRINCIPAL
                # =================================================

                with st.container(border=True):

                    # -------------------------------------------------
                    # CABECERA
                    # -------------------------------------------------

                    col_titulo, col_cerrar = st.columns(
                        [4, 1]
                    )

                    with col_titulo:

                        st.markdown(
                            "### 👤 Ficha del cliente"
                        )

                        st.markdown(
                            f"## {nombre}"
                        )

                        st.caption(
                            f"ID: {cliente_id}"
                        )

                    with col_cerrar:

                        if st.button(
                            "✕",
                            key=f"cerrar_{cliente_id}",
                            help="Cerrar ficha"
                        ):

                            del st.session_state[
                                "cliente_seleccionado_id"
                            ]

                            st.rerun()

                    # -------------------------------------------------
                    # ESTADO
                    # -------------------------------------------------

                    if perfil_completo:

                        st.success(
                            "✓ Perfil completo"
                        )

                    else:

                        st.warning(
                            "⚠ Perfil incompleto"
                        )

                        st.caption(
                            "Falta: "
                            + ", ".join(
                                campos_faltantes
                            )
                        )

                    st.divider()

                    # -------------------------------------------------
                    # INFORMACIÓN DE CONTACTO
                    # -------------------------------------------------

                    st.markdown(
                        "#### Información de contacto"
                    )

                    col_dato1, col_dato2 = st.columns(2)

                    with col_dato1:

                        st.caption("Celular")

                        st.write(
                            f"📞 {celular}"
                        )

                    with col_dato2:

                        st.caption("Ciudad")

                        st.write(
                            f"📍 {ciudad}"
                        )

                    # -------------------------------------------------
                    # CARACTERÍSTICAS
                    # -------------------------------------------------

                    st.markdown(
                        "#### Características"
                    )

                    col_dato1, col_dato2 = st.columns(2)

                    with col_dato1:

                        st.caption(
                            "Tipo de piel"
                        )

                        st.write(
                            tipo_piel
                        )

                    with col_dato2:

                        st.caption(
                            "Tono de base"
                        )

                        st.write(
                            tono_base
                        )

                    # -------------------------------------------------
                    # ASISTENTE
                    # -------------------------------------------------

                    st.divider()

                    st.markdown(
                        "#### 🤖 Asistente Inteligente"
                    )

                    resultado_asistente = (
                        analizar_perfil(cliente)
                    )

                    for observacion in (
                        resultado_asistente[
                            "observaciones"
                        ]
                    ):

                        st.write(
                            f"• {observacion}"
                        )

                    if resultado_asistente[
                        "acciones"
                    ]:

                        st.markdown(
                            "**Acciones sugeridas**"
                        )

                        for accion in (
                            resultado_asistente[
                                "acciones"
                            ]
                        ):

                            st.write(
                                f"• {accion}"
                            )

                    # -------------------------------------------------
                    # EDICIÓN
                    # -------------------------------------------------

                    st.divider()

                    editar = st.toggle(
                        "Editar información",
                        key=f"editar_{cliente_id}"
                    )

                    if editar:

                        with st.form(
                            f"formulario_cliente_{cliente_id}"
                        ):

                            st.markdown(
                                "#### Actualizar perfil"
                            )

                            nombre_editado = (
                                st.text_input(
                                    "Nombre",
                                    value=(
                                        ""
                                        if pd.isna(
                                            cliente["nombre"]
                                        )
                                        else str(
                                            cliente["nombre"]
                                        )
                                    )
                                )
                            )

                            celular_editado = (
                                st.text_input(
                                    "Celular",
                                    value=(
                                        ""
                                        if pd.isna(
                                            cliente["celular"]
                                        )
                                        else formatear_celular(
                                            cliente["celular"]
                                        )
                                    )
                                )
                            )

                            tipo_piel_editado = (
                                st.text_input(
                                    "Tipo de piel",
                                    value=(
                                        ""
                                        if pd.isna(
                                            cliente["tipo_piel"]
                                        )
                                        else str(
                                            cliente["tipo_piel"]
                                        )
                                    )
                                )
                            )

                            tono_base_editado = (
                                st.text_input(
                                    "Tono de base",
                                    value=(
                                        ""
                                        if pd.isna(
                                            cliente["tono_base"]
                                        )
                                        else str(
                                            cliente["tono_base"]
                                        )
                                    )
                                )
                            )

                            ciudad_editada = (
                                st.text_input(
                                    "Ciudad",
                                    value=(
                                        ""
                                        if pd.isna(
                                            cliente["ciudad"]
                                        )
                                        else str(
                                            cliente["ciudad"]
                                        )
                                    )
                                )
                            )

                            guardar = (
                                st.form_submit_button(
                                    "Guardar cambios",
                                    type="primary"
                                )
                            )

                            if guardar:

                                actualizar_cliente(
                                    cliente_id,
                                    nombre_editado.strip(),
                                    celular_editado.strip(),
                                    tipo_piel_editado.strip(),
                                    tono_base_editado.strip(),
                                    ciudad_editada.strip()
                                )

                                st.success(
                                    "Perfil actualizado correctamente."
                                )

                                st.rerun()

                    # -------------------------------------------------
                    # SEGUIMIENTO
                    # -------------------------------------------------

                    st.divider()

                    st.markdown(
                        "#### 📝 Seguimiento"
                    )

                    nota_cliente = st.text_area(
                        "Nueva nota",
                        placeholder=(
                            "Ej. Se contactó a la cliente "
                            "para consultar si necesita "
                            "reposición."
                        ),
                        height=90,
                        key=f"nota_{cliente_id}"
                    )

                    if st.button(
                        "Guardar seguimiento",
                        type="primary",
                        key=f"guardar_{cliente_id}"
                    ):

                        if nota_cliente.strip():

                            guardar_seguimiento(
                                cliente_id,
                                nota_cliente.strip()
                            )

                            st.success(
                                "Seguimiento guardado correctamente."
                            )

                            st.rerun()

                        else:

                            st.warning(
                                "Escribe una nota antes de guardar."
                            )

                    # -------------------------------------------------
                    # HISTORIAL
                    # -------------------------------------------------

                    historial_cliente = (
                        obtener_seguimientos(
                            cliente_id
                        )
                    )

                    if historial_cliente:

                        st.markdown(
                            "**Historial de seguimiento**"
                        )

                        for fecha, texto in (
                            historial_cliente
                        ):

                            st.caption(
                                fecha
                            )

                            st.write(
                                texto
                            )

                            st.divider()

                    else:

                        st.info(
                            "No hay seguimientos registrados."
                        )

        else:

            # =========================================================
            # PANEL VACÍO
            # =========================================================

            with st.container(border=True):

                st.markdown(
                    "### 👤 Ficha del cliente"
                )

                st.markdown(
                    """
                    <div style="
                        border-radius: 12px;
                        background-color: #EEF2FF;
                        padding:10px 10px;
                        margin-bottom:20px
                    ">
                    <strong>
                    Selecciona una cliente
                    </strong>>
                    Pulsa <strong>Ver ficha</strong>
                    en cualquier cliente de la tabla
                    para consultar su información.
                    """,
                    unsafe_allow_html=True,
                )

# ============================================================
# CLIENTES
# ============================================================

elif opcion == "Clientes":

    st.header("Clientes")

    st.write("Consulta y gestión de los perfiles disponibles.")

    col_titulo, col_boton = st.columns([4, 1])

    with col_boton:
        agregar_nuevo = st.button(
            "＋ Agregar cliente",
            use_container_width=True
        )

    if agregar_nuevo:
        st.session_state["mostrar_formulario_cliente"] = True

    if st.session_state.get("mostrar_formulario_cliente", False):

        st.subheader("Agregar nueva cliente")

        with st.form("form_agregar_cliente"):

            col1, col2 = st.columns(2)

            with col1:
                nombre = st.text_input("Nombre")
                celular = st.text_input("Celular")
                ciudad = st.text_input("Ciudad")

            with col2:
                tipo_piel = st.text_input("Tipo de piel")
                tono_base = st.text_input("Tono de base")

            col_guardar, col_cancelar = st.columns(2)

            with col_guardar:
                guardar = st.form_submit_button(
                    "Guardar cliente",
                    use_container_width=True
                )

            with col_cancelar:
                cancelar = st.form_submit_button(
                    "Cancelar",
                    use_container_width=True
                )

        if cancelar:
            st.session_state["mostrar_formulario_cliente"] = False
            st.rerun()

        if guardar:

            if not nombre.strip():
                st.warning("El nombre es obligatorio.")

            else:
                nuevo_id = f"CLIENTE_{len(df) + 1:03d}"

                agregar_cliente(
                    cliente_id=nuevo_id,
                    nombre=nombre.strip(),
                    celular=celular.strip(),
                    tipo_piel=tipo_piel.strip(),
                    tono_base=tono_base.strip(),
                    ciudad=ciudad.strip(),
                )

                st.session_state["mostrar_formulario_cliente"] = False

                st.success(
                    f"Cliente {nombre.strip()} agregado correctamente."
                )

                st.rerun()
                
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# SEGMENTOS
# ============================================================

elif opcion == "Segmentos":

    st.header("Segmentación")

    st.write(
        "Distribución descriptiva de clientes según las "
        "características disponibles actualmente en sus perfiles."
    )

    total_clientes = len(df)

    # ---------------------------------------------------------
    # 1. RESUMEN DE SEGMENTACIÓN
    # ---------------------------------------------------------

    st.subheader("Resumen")

    col1, col2, col3 = st.columns(3)

    with col1:

        segmentos_piel = (
            df["tipo_piel"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        segmentos_piel = segmentos_piel[
            segmentos_piel != ""
        ].nunique()

        st.metric(
            "Tipos de piel",
            segmentos_piel
        )

    with col2:

        segmentos_tono = (
            df["tono_base"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        segmentos_tono = segmentos_tono[
            segmentos_tono != ""
        ].nunique()

        st.metric(
            "Tonos de base",
            segmentos_tono
        )

    with col3:

        segmentos_ciudad = (
            df["ciudad"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        segmentos_ciudad = segmentos_ciudad[
            segmentos_ciudad != ""
        ].nunique()

        st.metric(
            "Ciudades",
            segmentos_ciudad
        )

    # ---------------------------------------------------------
    # 2. SEGMENTACIÓN POR TIPO DE PIEL
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Segmentación por tipo de piel")

    piel = (
        df["tipo_piel"]
        .fillna("Sin información")
        .astype(str)
        .str.strip()
    )

    piel = piel.replace(
        "",
        "Sin información"
    )

    conteo_piel = (
        piel
        .value_counts()
        .reset_index()
    )

    conteo_piel.columns = [
        "Tipo de piel",
        "Clientes"
    ]

    conteo_piel["% clientes"] = (
        conteo_piel["Clientes"]
        / total_clientes
        * 100
    ).round(1)

    col1, col2 = st.columns(2)

    with col1:

        st.dataframe(
            conteo_piel,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.bar_chart(
            conteo_piel.set_index(
                "Tipo de piel"
            )["Clientes"]
        )

    # ---------------------------------------------------------
    # 3. SEGMENTACIÓN POR TONO DE BASE
    # ---------------------------------------------------------

    st.subheader("Segmentación por tono de base")

    tono = (
        df["tono_base"]
        .fillna("Sin información")
        .astype(str)
        .str.strip()
    )

    tono = tono.replace(
        "",
        "Sin información"
    )

    conteo_tono = (
        tono
        .value_counts()
        .reset_index()
    )

    conteo_tono.columns = [
        "Tono de base",
        "Clientes"
    ]

    conteo_tono["% clientes"] = (
        conteo_tono["Clientes"]
        / total_clientes
        * 100
    ).round(1)

    col1, col2 = st.columns(2)

    with col1:

        st.dataframe(
            conteo_tono,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.bar_chart(
            conteo_tono.set_index(
                "Tono de base"
            )["Clientes"]
        )

    # ---------------------------------------------------------
    # 4. SEGMENTACIÓN POR CIUDAD
    # ---------------------------------------------------------

    st.subheader("Segmentación por ciudad")

    ciudad = (
        df["ciudad"]
        .fillna("Sin información")
        .astype(str)
        .str.strip()
    )

    ciudad = ciudad.replace(
        "",
        "Sin información"
    )

    conteo_ciudad = (
        ciudad
        .value_counts()
        .reset_index()
    )

    conteo_ciudad.columns = [
        "Ciudad",
        "Clientes"
    ]

    conteo_ciudad["% clientes"] = (
        conteo_ciudad["Clientes"]
        / total_clientes
        * 100
    ).round(1)

    col1, col2 = st.columns(2)

    with col1:

        st.dataframe(
            conteo_ciudad,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.bar_chart(
            conteo_ciudad.set_index(
                "Ciudad"
            )["Clientes"]
        )

    # ---------------------------------------------------------
    # 5. SEGMENTACIÓN COMBINADA
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Segmentación combinada")

    st.write(
        "Permite observar la relación entre las características "
        "registradas en los perfiles."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Tipo de piel × Tono de base**")

        cruce_piel_tono = pd.crosstab(
            piel,
            tono
        )

        st.dataframe(
            cruce_piel_tono,
            use_container_width=True
        )

    with col2:

        st.markdown("**Ciudad × Tipo de piel**")

        cruce_ciudad_piel = pd.crosstab(
            ciudad,
            piel
        )

        st.dataframe(
            cruce_ciudad_piel,
            use_container_width=True
        )

    # ---------------------------------------------------------
    # 6. FILTRO INTERACTIVO
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Explorar un segmento")

    filtro_col1, filtro_col2 = st.columns(2)

    with filtro_col1:

        opciones_piel = [
            "Todos"
        ] + sorted(
            [
                valor
                for valor in piel.unique()
                if valor != "Sin información"
            ]
        )

        filtro_piel = st.selectbox(
            "Tipo de piel",
            opciones_piel
        )

    with filtro_col2:

        opciones_ciudad = [
            "Todas"
        ] + sorted(
            [
                valor
                for valor in ciudad.unique()
                if valor != "Sin información"
            ]
        )

        filtro_ciudad = st.selectbox(
            "Ciudad",
            opciones_ciudad
        )

    segmento = df.copy()

    if filtro_piel != "Todos":

        segmento = segmento[
            segmento["tipo_piel"]
            .fillna("")
            .astype(str)
            .str.strip()
            == filtro_piel
        ]

    if filtro_ciudad != "Todas":

        segmento = segmento[
            segmento["ciudad"]
            .fillna("")
            .astype(str)
            .str.strip()
            == filtro_ciudad
        ]

    st.metric(
        "Clientes en el segmento",
        len(segmento)
    )

    if len(segmento) > 0:

        columnas_segmento = [
            "cliente_id",
            "nombre",
            "tipo_piel",
            "tono_base",
            "ciudad"
        ]

        st.dataframe(
            segmento[columnas_segmento],
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No hay clientes que coincidan con "
            "los filtros seleccionados."
        )

    # ---------------------------------------------------------
    # 7. INTERPRETACIÓN
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Interpretación")

    st.write(
        "La segmentación actual es descriptiva y utiliza "
        "únicamente la información disponible en los perfiles."
    )

    st.write(
        "Los segmentos permiten organizar la información "
        "de clientes y facilitar su exploración dentro del CRM."
    )

    st.write(
        "Cuando exista suficiente histórico real de ventas, "
        "esta segmentación podrá complementarse con variables "
        "de comportamiento de compra, análisis RFM y modelos "
        "de predicción de recompra."
    )


# ============================================================
# ANÁLISIS
# ============================================================

elif opcion == "Análisis":

    st.header("Análisis")

    st.info(
        "Este análisis describe la composición y calidad de la "
        "base actual de clientes. Los análisis de RFM y la "
        "predicción de recompra se incorporarán cuando exista "
        "suficiente histórico real de ventas."
    )

    # ---------------------------------------------------------
    # 1. RESUMEN GENERAL
    # ---------------------------------------------------------

    st.subheader("Resumen de la base de clientes")

    total_clientes = len(df)

    if "fecha_alta" in df.columns:

        fechas = pd.to_datetime(
            df["fecha_alta"],
            errors="coerce"
        )

        hoy = pd.Timestamp.today().normalize()

        altas_30_dias = (
            fechas >= hoy - pd.Timedelta(days=30)
        ).sum()

        altas_mes_actual = (
            (fechas.dt.year == hoy.year)
            & (fechas.dt.month == hoy.month)
        ).sum()

    else:

        altas_30_dias = 0
        altas_mes_actual = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Clientes registrados",
            total_clientes
        )

    with col2:
        st.metric(
            "Altas últimos 30 días",
            int(altas_30_dias)
        )

    with col3:
        st.metric(
            "Altas mes actual",
            int(altas_mes_actual)
        )

    st.caption(
        "Las altas de los clientes históricos corresponden a la "
        "fecha de migración al CRM y no representan necesariamente "
        "su fecha real de incorporación."
    )

    # ---------------------------------------------------------
    # 2. DISTRIBUCIÓN POR CIUDAD
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Distribución geográfica")

    ciudad_df = (
        df["ciudad"]
        .fillna("Sin información")
        .astype(str)
        .str.strip()
    )

    ciudad_df = ciudad_df.replace(
        "",
        "Sin información"
    )

    distribucion_ciudades = (
        ciudad_df
        .value_counts()
        .reset_index()
    )

    distribucion_ciudades.columns = [
        "Ciudad",
        "Clientes"
    ]

    distribucion_ciudades["%"] = (
        distribucion_ciudades["Clientes"]
        / total_clientes
        * 100
    ).round(1)

    col1, col2 = st.columns(2)

    with col1:

        st.dataframe(
            distribucion_ciudades,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.bar_chart(
            distribucion_ciudades.set_index("Ciudad")["Clientes"]
        )

    # ---------------------------------------------------------
    # 3. DISTRIBUCIÓN POR TIPO DE PIEL
    # ---------------------------------------------------------

    st.subheader("Distribución por tipo de piel")

    piel_df = (
        df["tipo_piel"]
        .fillna("Sin información")
        .astype(str)
        .str.strip()
    )

    piel_df = piel_df.replace(
        "",
        "Sin información"
    )

    distribucion_piel = (
        piel_df
        .value_counts()
        .reset_index()
    )

    distribucion_piel.columns = [
        "Tipo de piel",
        "Clientes"
    ]

    distribucion_piel["%"] = (
        distribucion_piel["Clientes"]
        / total_clientes
        * 100
    ).round(1)

    col1, col2 = st.columns(2)

    with col1:

        st.dataframe(
            distribucion_piel,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.bar_chart(
            distribucion_piel.set_index(
                "Tipo de piel"
            )["Clientes"]
        )

    # ---------------------------------------------------------
    # 4. DISTRIBUCIÓN POR TONO DE BASE
    # ---------------------------------------------------------

    st.subheader("Distribución por tono de base")

    tono_df = (
        df["tono_base"]
        .fillna("Sin información")
        .astype(str)
        .str.strip()
    )

    tono_df = tono_df.replace(
        "",
        "Sin información"
    )

    distribucion_tono = (
        tono_df
        .value_counts()
        .reset_index()
    )

    distribucion_tono.columns = [
        "Tono de base",
        "Clientes"
    ]

    distribucion_tono["%"] = (
        distribucion_tono["Clientes"]
        / total_clientes
        * 100
    ).round(1)

    col1, col2 = st.columns(2)

    with col1:

        st.dataframe(
            distribucion_tono,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.bar_chart(
            distribucion_tono.set_index(
                "Tono de base"
            )["Clientes"]
        )

    # ---------------------------------------------------------
    # 5. RELACIÓN ENTRE VARIABLES
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Relaciones entre características")

    st.write(
        "Estas tablas permiten observar cómo se distribuyen "
        "las características de los clientes y sirven como base "
        "para una segmentación descriptiva."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Ciudad × Tipo de piel**")

        ciudad_piel = pd.crosstab(
            ciudad_df,
            piel_df
        )

        st.dataframe(
            ciudad_piel,
            use_container_width=True
        )

    with col2:

        st.markdown("**Tipo de piel × Tono de base**")

        piel_tono = pd.crosstab(
            piel_df,
            tono_df
        )

        st.dataframe(
            piel_tono,
            use_container_width=True
        )

    # ---------------------------------------------------------
    # 6. CALIDAD DE LA INFORMACIÓN
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Calidad de los perfiles")

    campos_perfil = [
        "tipo_piel",
        "tono_base",
        "ciudad"
    ]

    nombres_campos = {
        "tipo_piel": "Tipo de piel",
        "tono_base": "Tono de base",
        "ciudad": "Ciudad"
    }

    calidad = []

    for campo in campos_perfil:

        valores = (
            df[campo]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        disponibles = (
            valores != ""
        ).sum()

        faltantes = (
            valores == ""
        ).sum()

        calidad.append(
            {
                "Campo": nombres_campos[campo],
                "Valores disponibles": disponibles,
                "Valores faltantes": faltantes,
                "% completo": round(
                    disponibles / total_clientes * 100,
                    1
                )
            }
        )

    calidad_df = pd.DataFrame(calidad)

    st.dataframe(
        calidad_df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------------------------------------------------
    # 7. CLIENTES INCOMPLETOS
    # ---------------------------------------------------------

    clientes_incompletos = []

    for _, cliente in df.iterrows():

        faltantes = []

        for campo in campos_perfil:

            valor = cliente[campo]

            if (
                pd.isna(valor)
                or str(valor).strip() == ""
                or str(valor).lower() == "nan"
            ):

                faltantes.append(
                    nombres_campos[campo]
                )

        if faltantes:

            nombre = cliente["nombre"]

            if (
                pd.isna(nombre)
                or str(nombre).strip() == ""
            ):
                nombre = "Sin nombre"

            clientes_incompletos.append(
                {
                    "cliente_id": cliente["cliente_id"],
                    "nombre": nombre,
                    "Información faltante": ", ".join(
                        faltantes
                    )
                }
            )

    incompletos_df = pd.DataFrame(
        clientes_incompletos
    )

    st.subheader(
        "Clientes que requieren actualización"
    )

    if len(incompletos_df) > 0:

        st.warning(
            f"Hay {len(incompletos_df)} clientes "
            "con información incompleta."
        )

        st.dataframe(
            incompletos_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "Todos los perfiles contienen "
            "la información disponible."
        )

    # ---------------------------------------------------------
    # 8. DETALLE DE UN PERFIL INCOMPLETO
    # ---------------------------------------------------------

    if len(incompletos_df) > 0:

        st.divider()

        st.subheader(
            "Detalle de información pendiente"
        )

        def mostrar_cliente_analisis(cid):

            fila = incompletos_df[
                incompletos_df["cliente_id"] == cid
            ].iloc[0]

            nombre = fila["nombre"]

            if (
                pd.isna(nombre)
                or str(nombre).strip() == ""
            ):
                nombre = "Sin nombre"

            return f"{nombre} ({cid})"

        cliente_id_analisis = st.selectbox(
            "Seleccionar cliente",
            incompletos_df["cliente_id"].tolist(),
            format_func=mostrar_cliente_analisis
        )

        cliente_analisis = df[
            df["cliente_id"] == cliente_id_analisis
        ].iloc[0]

        faltantes_cliente = []

        for campo in campos_perfil:

            valor = cliente_analisis[campo]

            if (
                pd.isna(valor)
                or str(valor).strip() == ""
                or str(valor).lower() == "nan"
            ):

                faltantes_cliente.append(
                    nombres_campos[campo]
                )

        st.warning(
            "A esta cliente le falta: "
            + ", ".join(faltantes_cliente)
        )

        st.info(
            "Para completar el perfil, ve a "
            "Inicio → Detalle del cliente, "
            "selecciona esta cliente y utiliza "
            "el formulario de edición."
        )

    # ---------------------------------------------------------
    # 9. INTERPRETACIÓN
    # ---------------------------------------------------------

    st.divider()

    st.subheader("Interpretación")

    st.write(
        "El análisis permite conocer la composición actual "
        "de la base de clientes según ciudad, tipo de piel "
        "y tono de base."
    )

    st.write(
        "Las tablas cruzadas permiten identificar patrones "
        "descriptivos entre las características disponibles "
        "y pueden servir como apoyo para la segmentación "
        "comercial."
    )

    st.write(
        "El análisis de calidad permite detectar perfiles "
        "que requieren actualización y priorizar la "
        "completitud de la información."
    )

    st.write(
        "La incorporación de nuevos clientes actualiza "
        "automáticamente los indicadores y distribuciones."
    )

    st.write(
        "El análisis RFM y la predicción de recompra quedan "
        "como una ampliación futura, condicionada a disponer "
        "de un histórico real de transacciones con fechas, "
        "productos e importes suficientes."
    )

# ============================================================
# SEGUIMIENTO
# ============================================================

elif opcion == "Seguimiento":

    st.header("Seguimiento")

    st.write("Registra y consulta acciones de seguimiento de cada cliente.")

    # Crear opciones de cliente
    clientes_disponibles = df["cliente_id"].tolist()

    # Si tenemos nombres en el dataset privado,
    # los mostramos para facilitar la búsqueda.
    if "nombre" in df.columns:

        nombres = dict(zip(df["cliente_id"], df["nombre"]))

        cliente_id = st.selectbox(
            "Cliente",
            clientes_disponibles,
            format_func=lambda cid: (f"{nombres.get(cid, 'Sin nombre')} ({cid})"),
        )

    else:

        cliente_id = st.selectbox("Cliente", clientes_disponibles)

    st.subheader("Nueva nota")

    nota = st.text_area(
        "Nota de seguimiento",
        placeholder=(
            "Ej. Se contactó a la cliente para " "consultar si necesita reposición."
        ),
        height=120,
    )

    if st.button("Guardar seguimiento", type="primary"):

        if nota.strip():

            guardar_seguimiento(cliente_id, nota.strip())

            st.success("Seguimiento guardado correctamente.")

        else:

            st.warning("Escribe una nota antes de guardar.")

    st.divider()

    st.subheader("Historial de seguimiento")

    seguimientos = obtener_seguimientos(cliente_id)

    if seguimientos:

        for fecha, texto in seguimientos:

            st.markdown(f"**{fecha}**")

            st.write(texto)

            st.divider()

    else:

        st.info("No hay seguimientos registrados " "para este cliente.")

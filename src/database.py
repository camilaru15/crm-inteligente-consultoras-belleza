import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("data/crm.db")


def conectar():
    """Crea una conexión con la base de datos local."""
    DB_PATH.parent.mkdir(parents=True,exist_ok=True)
    return sqlite3.connect(DB_PATH)


def inicializar_base_datos():
    """Crea las tablas necesarias si no existen."""

    conn = conectar()
    cursor = conn.cursor()
    
# --------------------------------------------------------
# TABLA DE CLIENTES
# --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            cliente_id TEXT PRIMARY KEY,
            nombre TEXT,
            celular TEXT,
            tipo_piel TEXT,
            tono_base TEXT,
            ciudad TEXT,
            fecha_alta TEXT
        )
        """
    )

# --------------------------------------------------------
# TABLA DE SEGUIMIENTOS
# --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS seguimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id TEXT NOT NULL,
            nota TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()

def agregar_fecha_alta_si_no_existe():
    """
    Añade la columna fecha_alta a bases de datos
    creadas con una versión anterior de la aplicación.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(clientes)")
    columnas = [fila[1] for fila in cursor.fetchall()]

    if "fecha_alta" not in columnas:
        cursor.execute(
            "ALTER TABLE clientes ADD COLUMN fecha_alta TEXT"
        )

        cursor.execute(
            """
            UPDATE clientes
            SET fecha_alta = ?
            WHERE fecha_alta IS NULL
            """,
            (datetime.now().strftime("%Y-%m-%d"),)
        )

    conn.commit()
    conn.close()

def cargar_clientes_desde_dataframe(df):
    """
    Carga los clientes iniciales desde el DataFrame
    si todavía no existen en SQLite.
    """

    conn = conectar()
    cursor = conn.cursor()

    for _, cliente in df.iterrows():
        
        fecha_alta = cliente.get("fecha_alta")

        if fecha_alta is None or str(fecha_alta).strip() == "":
           fecha_alta = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """
            INSERT OR IGNORE INTO clientes (
                cliente_id,
                nombre,
                celular,
                tipo_piel,
                tono_base,
                ciudad,
                fecha_alta
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cliente["cliente_id"],
                cliente.get("nombre"),
                cliente.get("celular"),
                cliente.get("tipo_piel"),
                cliente.get("tono_base"),
                cliente.get("ciudad"),
                fecha_alta,
            )
        )

    conn.commit()
    conn.close()

def agregar_cliente(
    cliente_id,
    nombre,
    celular,
    tipo_piel,
    tono_base,
    ciudad
):
    """Añade una nueva cliente al CRM."""
    conn = conectar()
    cursor = conn.cursor()

    fecha_alta = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        INSERT INTO clientes (
            cliente_id,
            nombre,
            celular,
            tipo_piel,
            tono_base,
            ciudad,
            fecha_alta
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            cliente_id,
            nombre,
            celular,
            tipo_piel,
            tono_base,
            ciudad,
            fecha_alta,
        )
    )

    conn.commit()
    conn.close()

def obtener_clientes():
    """Obtiene todos los clientes almacenados en SQLite."""

    conn = conectar()

    df = __import__("pandas").read_sql_query(
        """
        SELECT
            cliente_id,
            nombre,
            celular,
            tipo_piel,
            tono_base,
            ciudad,
            fecha_alta
        FROM clientes
        ORDER BY cliente_id
        """,
        conn
    )

    conn.close()

    return df


def actualizar_cliente(
    cliente_id,
    nombre,
    celular,
    tipo_piel,
    tono_base,
    ciudad
):
    """Actualiza la información de un cliente."""

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE clientes
        SET
            nombre = ?,
            celular = ?,
            tipo_piel = ?,
            tono_base = ?,
            ciudad = ?
        WHERE cliente_id = ?
        """,
        (
            nombre,
            celular,
            tipo_piel,
            tono_base,
            ciudad,
            cliente_id,
        )
    )

    conn.commit()
    conn.close()


def guardar_seguimiento(cliente_id, nota):
    """Guarda una nota asociada a un cliente."""

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO seguimientos (cliente_id, nota)
        VALUES (?, ?)
        """,
        (cliente_id, nota)
    )

    conn.commit()
    conn.close()


def obtener_seguimientos(cliente_id):
    """Obtiene el historial de seguimiento de un cliente."""

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT fecha, nota
        FROM seguimientos
        WHERE cliente_id = ?
        ORDER BY fecha DESC
        """,
        (cliente_id,)
    )

    resultados = cursor.fetchall()

    conn.close()

    return resultados
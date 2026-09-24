import pandas as pd
from pathlib import Path


# Rutas del proyecto

archivo_entrada = Path("data/raw/PERFILES DIGITALES.xlsx")

archivo_publico = Path(
    "data/processed/clientes.csv"
)

archivo_privado = Path(
    "data/processed/clientes_privados.csv"
)


# Crear carpeta de salida
archivo_publico.parent.mkdir(
    parents=True,
    exist_ok=True
)



# Leer datos originales
df = pd.read_excel(archivo_entrada)


# Crear identificador anónimo para cada cliente
df["cliente_id"] = [
    f"CLIENTE_{i:03d}"
    for i in range(1, len(df) + 1)
]


#Dataset privado
df_privado = df[
    [
        "cliente_id",
        "NOMBRE",
        "CELULAR",
        "TIPO PIEL",
        "TONO BASE",
        "CIUDAD",
    ]
].copy()


df_privado = df_privado.rename(
    columns={
        "NOMBRE": "nombre",
        "CELULAR": "celular",
        "TIPO PIEL": "tipo_piel",
        "TONO BASE": "tono_base",
        "CIUDAD": "ciudad",
    }
)


df_privado.to_csv(
    archivo_privado,
    index=False,
    encoding="utf-8-sig"
)


#Dataset publico/anonimizado

df_publico = df[
    [
        "cliente_id",
        "TIPO PIEL",
        "TONO BASE",
        "CIUDAD",
    ]
].copy()


df_publico = df_publico.rename(
    columns={
        "TIPO PIEL": "tipo_piel",
        "TONO BASE": "tono_base",
        "CIUDAD": "ciudad",
    }
)


df_publico.to_csv(
    archivo_publico,
    index=False,
    encoding="utf-8-sig"
)

#Resultado de los datos procesados
print("Datos procesados correctamente.")
print(f"Clientes procesados: {len(df)}")
print(f"Archivo público: {archivo_publico}")
print(f"Archivo privado: {archivo_privado}")
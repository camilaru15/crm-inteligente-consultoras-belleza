# CRM Inteligente para Consultoras de Belleza

Sistema web desarrollado como proyecto de Máster en Data Science e
Inteligencia Artificial para apoyar la gestión, análisis y seguimiento
de clientes de consultoras de belleza.

## Descripción

Las consultoras de belleza pueden gestionar cientos de clientes mediante
contactos, hojas de cálculo y aplicaciones de mensajería. Esta
información puede quedar dispersa y dificultar el seguimiento, la
actualización de perfiles y la personalización de acciones comerciales.

Este proyecto propone un **CRM inteligente** que centraliza la
información de las clientes y permite:

-   Gestionar perfiles de clientes.
-   Consultar y filtrar la cartera de clientes.
-   Detectar información incompleta.
-   Consultar fichas individuales.
-   Registrar seguimientos comerciales.
-   Mantener un historial de seguimientos.
-   Analizar la información disponible del perfil.
-   Generar recomendaciones de productos a partir de reglas y una base
    de conocimiento controlada.
-   Proponer una próxima acción de seguimiento.

El proyecto se plantea como un **MVP funcional**, preparado para
incorporar capacidades analíticas más avanzadas cuando exista suficiente
histórico real de compras.

## Objetivo

Desarrollar una herramienta que permita transformar una base de
contactos y perfiles de clientes en un sistema estructurado de gestión y
apoyo a la toma de decisiones comerciales.

### Objetivos específicos

1.  Centralizar la información de las clientes.
2.  Mejorar la calidad y completitud de los perfiles.
3.  Facilitar la consulta y actualización de la información.
4.  Apoyar el seguimiento comercial.
5.  Incorporar un asistente inteligente basado en los datos disponibles.
6.  Preparar la arquitectura para futuras funcionalidades de
    segmentación avanzada, análisis RFM y predicción de recompra.

## Funcionalidades

### Gestión de clientes

Cada ficha puede contener:

-   Identificador de cliente.
-   Nombre.
-   Número de teléfono.
-   Ciudad.
-   Tipo de piel.
-   Tono de base.
-   Fecha de alta.
-   Estado de completitud del perfil.

### Calidad de datos

El sistema muestra indicadores sobre:

-   Clientes registrados.
-   Perfiles completos.
-   Ciudades.
-   Tipos de piel.
-   Información incompleta.

### Búsqueda y filtros

Permite localizar clientes y filtrar por:

-   Tipo de piel.
-   Tono de base.
-   Ciudad.

### Seguimiento comercial

Permite registrar notas de seguimiento asociadas a cada cliente y
consultar su historial.

### Asistente inteligente

El asistente genera:

-   Interpretación del perfil.
-   Identificación de información faltante.
-   Oportunidad comercial.
-   Productos compatibles según la base de conocimiento.
-   Próxima acción recomendada.
-   Acciones sugeridas.

Las recomendaciones se basan en los datos registrados en el CRM y en una
base de conocimiento definida para el prototipo. El asistente no
sustituye la decisión de la consultora.

## Datos disponibles

Los datos actuales corresponden principalmente a perfiles de clientes:

-   Identificador.
-   Nombre.
-   Celular.
-   Tipo de piel.
-   Tono de base.
-   Ciudad.

El conjunto disponible **no contiene un histórico suficiente de
transacciones fechadas** para validar un modelo de predicción de
recompra.

Por esta razón, la versión actual no presenta la predicción de recompra
como un modelo validado.

Cuando exista un histórico real y suficiente podrán incorporarse:

-   Fecha de compra.
-   Producto adquirido.
-   Importe.
-   Identificador de transacción.
-   Número de compras.
-   Intervalos entre compras.
-   Indicadores de recompra.

Esto permitiría desarrollar análisis RFM y, posteriormente, modelos de
predicción de recompra.

## 🏗️ Arquitectura

``` text
crm-inteligente-consultoras-belleza/
│
├── app/
│   └── app.py
├── assets/
├── data/
│   ├── raw/
│   ├── processed/
│   │   ├── clientes.csv
│   │   └── productos.csv
│   └── gold/
├── docs/
│   └── entregas/
├── notebooks/
├── src/
│   ├── database.py
│   ├── asistente.py
│   └── preparar_datos.py
├── .gitignore
└── README.md
```

## 🛠️ Tecnologías

-   **Python 3.13.1**
-   **Streamlit**
-   **Pandas**
-   **SQLite**
-   **OpenPyXL**
-   **Git / GitHub**

## Base de datos

La aplicación utiliza SQLite.

### Tabla `clientes`

``` text
cliente_id
nombre
celular
tipo_piel
tono_base
ciudad
fecha_alta
```

### Tabla `seguimientos`

``` text
id
cliente_id
nota
fecha
```

La base de datos local se genera en:

``` text
data/crm.db
```

Este archivo está excluido del repositorio.

## Funcionamiento del asistente

``` text
Perfil de cliente
       ↓
Comprobación de datos
       ↓
Interpretación
       ↓
Búsqueda de productos compatibles
       ↓
Oportunidad comercial
       ↓
Próxima acción
```

Las recomendaciones utilizan coincidencias controladas entre las
características del perfil y los atributos definidos en `productos.csv`.

## Privacidad

El proyecto distingue entre datos privados utilizados durante el
desarrollo y datos anonimizados destinados al repositorio.

Los archivos con información identificativa no deben publicarse en
GitHub.

El `.gitignore` excluye:

``` text
data/raw/
data/processed/clientes_privados.csv
*.db
*.sqlite
*.sqlite3
.env
.streamlit/secrets.toml
```

## Instalación

### 1. Clonar el repositorio

``` bash
git clone https://github.com/camilaru15/crm-inteligente-consultoras-belleza.git
cd crm-inteligente-consultoras-belleza
```

### 2. Crear entorno virtual

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias

``` powershell
pip install streamlit pandas openpyxl
```

### 4. Ejecutar

``` powershell
streamlit run app/app.py
```

## Flujo principal

``` text
Inicio
  ↓
Consultar indicadores
  ↓
Buscar / filtrar cliente
  ↓
Ver ficha
  ↓
Consultar información
  ↓
Analizar perfil
  ↓
Consultar recomendaciones
  ↓
Registrar seguimiento
```

##  Limitaciones actuales

La principal limitación del MVP es la disponibilidad de histórico de
compras.

Disponer de cientos de clientes no implica disponer de suficientes
observaciones para entrenar y validar un modelo de recompra.

Por ello:

-   No se utiliza información simulada para presentar un modelo
    predictivo final.
-   No se afirma que exista un modelo de predicción de recompra
    validado.
-   Las recomendaciones actuales se basan en información disponible y
    reglas controladas.
-   La predicción queda planteada como evolución futura condicionada a
    disponer de datos reales y fechados.

## Evolución futura

Con un histórico suficiente de transacciones, el sistema podría
incorporar:

### 1. Segmentación RFM

-   Recencia.
-   Frecuencia.
-   Valor monetario.

### 2. Predicción de recompra

Definir una ventana de recompra, por ejemplo:

``` text
30 días
60 días
90 días
```

y comprobar que existen suficientes ejemplos de clientes que recompran y
que no recompran.

### 3. Automatización del seguimiento

Generación de listas priorizadas de clientes para contactar.

### 4. Analítica avanzada

Dashboards y modelos de machine learning cuando los datos permitan
realizar una validación adecuada.

## Documentación

La documentación académica se encuentra en:

``` text
docs/entregas/
```

Incluye:

-   Idea y definición del producto.
-   Datos necesarios y viabilidad.
-   Modelo de datos.
-   Análisis y estrategia de modelado.
-   Diseño de la interfaz.

## Autora

**María Camila Rueda Cano**

Máster en Data Science e Inteligencia Artificial\
Máster en Geotecnología y Desarrollo de Proyectos SIG\
Ingeniería en Sistemas y Telecomunicaciones

## Estado

**MVP funcional en desarrollo/finalización académica.**

El núcleo actual demuestra:

> **Gestión de clientes → calidad de datos → consulta de perfiles →
> asistencia inteligente → recomendación controlada → seguimiento
> comercial.**

La arquitectura queda preparada para incorporar análisis de
comportamiento de compra y predicción cuando exista suficiente histórico
real para sustentarlos.

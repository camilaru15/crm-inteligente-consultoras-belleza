# 03. Modelo de datos

## 1. Resumen de la idea y de los datos

El proyecto consiste en desarrollar un **CRM inteligente para consultoras de belleza**, orientado a centralizar la información de los clientes, sus perfiles, el historial de compras y las interacciones comerciales, con el objetivo de facilitar el seguimiento de los clientes y apoyar la toma de decisiones comerciales.

El sistema se plantea de forma incremental. En una primera etapa, permitirá organizar y consultar la información de clientes y sus características. A medida que se incorporen nuevas ventas e interacciones, se podrá construir un histórico estructurado que permita realizar análisis de comportamiento, segmentación de clientes mediante RFM y, si la cantidad y calidad de los datos lo permiten, desarrollar posteriormente un modelo de predicción de recompra.

Actualmente se dispone de información de clientes y perfiles digitales, incluyendo datos como:

* Identificador o número de contacto del cliente.
* Nombre.
* Tipo de piel.
* Tono de base.
* Ciudad.

Estos datos permiten construir inicialmente la dimensión de clientes y su perfil, pero **no constituyen un histórico de ventas**, ya que no contienen de forma suficiente la fecha de compra, producto adquirido, cantidad, importe ni identificadores de transacción.

Por este motivo, la estructura de datos deberá estar preparada para incorporar posteriormente un histórico de ventas con información como:

* Identificador de la venta.
* Cliente asociado.
* Producto adquirido.
* Fecha de compra.
* Cantidad.
* Precio o importe de la venta.

También se contempla una estructura para registrar interacciones con los clientes, cuando esta información esté disponible, incluyendo fecha, canal, tipo de interacción y respuesta.

La disponibilidad de un histórico real de ventas será necesaria para construir métricas de comportamiento, como recencia, frecuencia y valor monetario, y para evaluar posteriormente si existe información suficiente para desarrollar un modelo de predicción de recompra.

El modelo de datos se diseñará, por tanto, para que el sistema pueda crecer progresivamente sin tener que modificar su estructura principal cada vez que se incorporen nuevos clientes, ventas o interacciones.

## 2. Tecnología y formato de almacenamiento

Para la primera versión del proyecto se utilizará **Python** como herramienta principal para la carga, limpieza, transformación y preparación de los datos.

Los datos de entrada actualmente disponibles se encuentran principalmente en formatos **CSV y Excel**, por lo que estos formatos se utilizarán como fuentes iniciales de la capa `raw`, conservando los datos originales sin aplicar transformaciones.

Para las capas `processed` y `gold` se priorizará el formato **Parquet**, debido a que permite conservar los tipos de datos de las columnas y resulta adecuado para procesos posteriores de análisis y tratamiento de datos.

La estructura de almacenamiento propuesta será:

```text
data/
├── raw/
├── processed/
└── gold/
```

### Capa raw

Contendrá los datos originales obtenidos de las fuentes disponibles, sin modificaciones. Esta capa permitirá conservar una copia de referencia de los datos de entrada y facilitar la trazabilidad de las transformaciones realizadas.

### Capa processed

Contendrá los datos después de aplicar los procesos de limpieza, normalización y transformación necesarios. En esta etapa se podrán corregir tipos de datos, tratar valores nulos, normalizar categorías y eliminar duplicados cuando corresponda.

### Capa gold

Contendrá los conjuntos de datos finales preparados para ser utilizados por los análisis, la segmentación RFM, los dashboards y, si posteriormente existe suficiente histórico real, los modelos predictivos.

La tecnología y los formatos podrán evolucionar en fases posteriores si el volumen y las necesidades del proyecto lo requieren. La prioridad en esta etapa es disponer de una estructura sencilla, reproducible y trazable que permita incorporar progresivamente nuevos clientes, ventas e interacciones.

## 3. Capas de datos

El sistema se organizará mediante tres capas principales: **raw, processed y gold**. Esta separación permitirá mantener la trazabilidad de los datos desde su origen hasta los conjuntos de datos utilizados para el análisis y la toma de decisiones.

```text id="8h7q2m"
Fuentes originales
       │
       ▼
     RAW
       │
       ▼
  PROCESSED
       │
       ▼
     GOLD
       │
       ├── Segmentación RFM
       ├── Dashboard
       └── Predicción de recompra*
```

* La predicción de recompra se incorporará únicamente si el histórico real disponible permite construir y validar un modelo de forma adecuada.

### 3.1. Capa Raw

La capa `raw` almacenará los datos tal como se reciben de las fuentes originales, sin realizar modificaciones sobre su contenido.

En esta primera versión se contemplan como fuentes:

* Archivo de clientes/perfiles digitales en formato Excel.
* Archivo de contactos en formato CSV.
* Futuras fuentes de ventas reales.
* Futuras fuentes de interacciones con clientes.

La información actualmente disponible permitirá alimentar principalmente la información de clientes y sus características de perfil.

Los archivos originales no deberán utilizarse directamente en el análisis cuando contengan información identificativa. Para el repositorio público se generarán versiones anonimizadas de los datos.

### 3.2. Capa Processed

La capa `processed` contendrá los datos después de aplicar los procesos de preparación necesarios para su utilización.

Entre las operaciones previstas se encuentran:

* Normalización de nombres de columnas.
* Conversión de tipos de datos.
* Tratamiento de valores nulos.
* Detección y tratamiento de registros duplicados.
* Normalización de categorías como tipo de piel, ciudad y categorías de productos.
* Estandarización de fechas.
* Eliminación o anonimización de información identificativa cuando sea necesario.
* Validación de las relaciones entre clientes, productos y ventas.
* Preparación de variables derivadas para el análisis.

En esta capa no se modificarán los archivos originales de `raw`, sino que se generarán conjuntos de datos limpios y estructurados.

### 3.3. Capa Gold

La capa `gold` contendrá los datos finales preparados para ser consumidos por los diferentes componentes analíticos del proyecto.

La estructura prevista estará formada por conjuntos de datos relacionados con:

* **Clientes:** información consolidada y anonimizada del perfil del cliente.
* **Productos:** catálogo y características de los productos comercializados.
* **Ventas:** histórico de transacciones realizadas por cada cliente.
* **Interacciones:** registro de comunicaciones e interacciones comerciales cuando esta información esté disponible.
* **Clientes_RFM:** variables de recencia, frecuencia y valor monetario calculadas a partir del histórico de ventas.
* **Segmentación:** clasificación de los clientes en segmentos según su comportamiento de compra.

La capa `gold` será el punto de consumo para los análisis, dashboards y procesos posteriores de modelado.

En el caso de la predicción de recompra, se añadirá un conjunto de datos específico para modelado únicamente cuando exista suficiente histórico real y se pueda definir de manera fiable la variable objetivo.

Por tanto, la capa `gold` se considera un **contrato de datos para las capas analíticas**, ya que deberá contener información limpia, estructurada y con definiciones claras antes de ser utilizada para generar conclusiones o modelos.

## 4. Definición de la capa Gold

La capa `gold` estará formada por conjuntos de datos estructurados y preparados para su consumo por los componentes analíticos del CRM.

El modelo se organizará principalmente alrededor de cuatro entidades principales:

```text id="7k3p1v"
clientes
    │
    ├───────────────┐
    │               │
    ▼               ▼
 ventas          interacciones
    │
    ▼
productos
```

A partir de estas entidades se generarán conjuntos de datos derivados para el análisis del comportamiento de los clientes.

### 4.1. Tabla `clientes`

Contendrá la información consolidada y anonimizada de los clientes.

Campos principales previstos:

| Campo            | Descripción                                                                |
| ---------------- | -------------------------------------------------------------------------- |
| `cliente_id`     | Identificador único y anonimizado del cliente                              |
| `nombre`         | Nombre del cliente, únicamente cuando sea necesario y en datos no públicos |
| `ciudad`         | Ciudad asociada al cliente                                                 |
| `tipo_piel`      | Tipo de piel registrado                                                    |
| `tono_base`      | Tono de base registrado                                                    |
| `fecha_registro` | Fecha de incorporación al CRM, cuando esté disponible                      |

En el repositorio público se utilizará un identificador anonimizado en lugar de teléfonos u otros datos directamente identificativos.

### 4.2. Tabla `productos`

Contendrá el catálogo de productos utilizados en las ventas.

Campos principales previstos:

| Campo               | Descripción                                  |
| ------------------- | -------------------------------------------- |
| `producto_id`       | Identificador único del producto             |
| `nombre_producto`   | Nombre o referencia del producto             |
| `categoria`         | Categoría del producto                       |
| `precio`            | Precio del producto                          |
| `duracion_estimada` | Duración estimada de uso cuando sea conocida |

La duración estimada podrá utilizarse posteriormente como información de apoyo para el seguimiento de posibles momentos de recompra, pero no se asumirá como una fecha real de recompra.

### 4.3. Tabla `ventas`

Contendrá el histórico de transacciones realizadas por los clientes.

Campos principales previstos:

| Campo          | Descripción                           |
| -------------- | ------------------------------------- |
| `venta_id`     | Identificador único de la transacción |
| `cliente_id`   | Cliente que realiza la compra         |
| `producto_id`  | Producto adquirido                    |
| `fecha_compra` | Fecha en la que se realizó la compra  |
| `cantidad`     | Cantidad adquirida                    |
| `precio`       | Precio aplicado en la venta           |
| `importe`      | Importe total de la línea de venta    |

Esta tabla será fundamental para construir posteriormente las métricas de comportamiento de compra.

### 4.4. Tabla `interacciones`

Permitirá registrar las interacciones comerciales con los clientes cuando esta información esté disponible.

Campos principales previstos:

| Campo              | Descripción                             |
| ------------------ | --------------------------------------- |
| `interaccion_id`   | Identificador único de la interacción   |
| `cliente_id`       | Cliente relacionado                     |
| `fecha`            | Fecha de la interacción                 |
| `canal`            | Canal utilizado                         |
| `tipo_interaccion` | Tipo de interacción realizada           |
| `respuesta`        | Respuesta o resultado de la interacción |

Esta información podrá utilizarse para complementar el análisis del comportamiento de los clientes.

### 4.5. Dataset `clientes_rfm`

A partir de la tabla `ventas` se calcularán las principales variables del análisis RFM:

| Campo        | Descripción                                |
| ------------ | ------------------------------------------ |
| `cliente_id` | Identificador del cliente                  |
| `recency`    | Tiempo transcurrido desde la última compra |
| `frequency`  | Número de compras realizadas               |
| `monetary`   | Valor monetario acumulado de las compras   |

Estas variables permitirán analizar el comportamiento de compra y construir una segmentación de clientes.

### 4.6. Dataset `segmentacion_clientes`

Contendrá el resultado de la segmentación basada inicialmente en las variables RFM.

Campos previstos:

| Campo        | Descripción                   |
| ------------ | ----------------------------- |
| `cliente_id` | Identificador del cliente     |
| `segmento`   | Segmento asignado             |
| `recency`    | Valor de recencia utilizado   |
| `frequency`  | Valor de frecuencia utilizado |
| `monetary`   | Valor monetario utilizado     |

La definición final de los segmentos dependerá de los datos reales disponibles y del método de segmentación seleccionado durante la fase de análisis.

### 4.7. Dataset de predicción de recompra

La predicción de recompra se considera una extensión del sistema y no un componente garantizado en esta fase.

Si el histórico real disponible permite construir suficientes ejemplos, se podrá generar un dataset específico para modelado que incluya variables relacionadas con el comportamiento anterior del cliente y una variable objetivo que indique si se produjo una recompra dentro del horizonte temporal definido.

La variable objetivo deberá definirse a partir de compras reales y no mediante datos simulados.

Si el histórico disponible no permite construir un conjunto de entrenamiento y validación suficientemente representativo, esta parte se mantendrá como **nice to have**, mientras que el CRM, el análisis RFM, la segmentación y el dashboard constituirán el núcleo funcional del proyecto.

## 5. Relaciones entre las entidades

El modelo de datos se plantea siguiendo una estructura relacional en la que el cliente constituye una de las entidades centrales del sistema.

Las principales relaciones serán:

```text
clientes 1 ─────────── N ventas N ─────────── 1 productos
    │
    │
    └────────── 1 ─────────── N interacciones
```

### 5.1. Relación entre `clientes` y `ventas`

Un cliente puede realizar ninguna, una o varias compras a lo largo del tiempo, mientras que cada venta debe estar asociada a un único cliente.

```text
clientes.cliente_id 1 ─────────── N ventas.cliente_id
```

Esta relación permitirá consultar el historial de compras de cada cliente y calcular posteriormente variables como recencia, frecuencia y valor monetario.

### 5.2. Relación entre `productos` y `ventas`

Un producto puede aparecer en múltiples ventas, mientras que cada registro de venta estará asociado a un producto concreto.

```text
productos.producto_id 1 ─────────── N ventas.producto_id
```

Esta relación permitirá analizar qué productos se venden, con qué frecuencia y qué productos o categorías están asociados al comportamiento de los clientes.

### 5.3. Relación entre `clientes` e `interacciones`

Un cliente puede tener múltiples interacciones comerciales a lo largo del tiempo, mientras que cada interacción estará asociada a un único cliente.

```text
clientes.cliente_id 1 ─────────── N interacciones.cliente_id
```

Esta relación permitirá complementar el historial de compras con información sobre las comunicaciones realizadas y sus resultados, siempre que estos datos estén disponibles.

### 5.4. Relación entre `clientes` y los datos derivados

Los datasets `clientes_rfm` y `segmentacion_clientes` se construirán a partir de la información relacionada con cada cliente.

```text
clientes
    │
    ├────────── 1 ─────────── 1 clientes_rfm
    │
    └────────── 1 ─────────── 1 segmentacion_clientes
```

La relación se plantea conceptualmente como uno a uno para la versión analítica, ya que cada cliente tendrá un único registro de métricas RFM y un único segmento dentro de una ejecución determinada del análisis.

Sin embargo, estos datasets serán **derivados**, por lo que no constituirán una fuente independiente de información. Su contenido se actualizará cuando se incorporen nuevas ventas y se vuelva a ejecutar el proceso de transformación.

### 5.5. Claves y reglas de integridad

Las relaciones principales utilizarán identificadores únicos:

* `cliente_id` será la clave primaria de `clientes`.
* `producto_id` será la clave primaria de `productos`.
* `venta_id` será la clave primaria de `ventas`.
* `interaccion_id` será la clave primaria de `interacciones`.

En la tabla `ventas`, `cliente_id` y `producto_id` actuarán como claves foráneas hacia las tablas correspondientes.

De forma equivalente, `cliente_id` en `interacciones` actuará como clave foránea hacia `clientes`.

Se deberá comprobar que las claves foráneas utilizadas en las tablas de hechos tengan correspondencia con los registros existentes en las tablas maestras. Esto permitirá evitar ventas o interacciones asociadas a clientes o productos inexistentes.

## 6. Diccionario de datos inicial

El siguiente diccionario define los principales campos previstos para las entidades de la capa `gold`. Se diferencia entre los campos que ya están presentes en las fuentes disponibles y aquellos que deberán incorporarse cuando se disponga de información adicional, especialmente del histórico real de ventas.

### 6.1. Tabla `clientes`

| Campo            | Tipo de dato | Descripción                                   | Regla / consideración                                                  |
| ---------------- | ------------ | --------------------------------------------- | ---------------------------------------------------------------------- |
| `cliente_id`     | string       | Identificador único y anonimizado del cliente | Obligatorio y único                                                    |
| `nombre`         | string       | Nombre del cliente                            | Solo para fuentes privadas; no se publicará información identificativa |
| `ciudad`         | string       | Ciudad asociada al cliente                    | Se normalizará la escritura de las categorías                          |
| `tipo_piel`      | string       | Tipo de piel registrado                       | Puede contener valores nulos                                           |
| `tono_base`      | string       | Tono de base registrado                       | Puede contener valores nulos                                           |
| `fecha_registro` | date         | Fecha de incorporación del cliente al CRM     | Campo previsto; actualmente no disponible                              |

Los campos `nombre`, `ciudad`, `tipo_piel` y `tono_base` proceden de la información de perfiles disponible actualmente. El identificador definitivo `cliente_id` se generará durante el proceso de anonimización.

### 6.2. Tabla `productos`

| Campo               | Tipo de dato    | Descripción                              | Regla / consideración                                          |
| ------------------- | --------------- | ---------------------------------------- | -------------------------------------------------------------- |
| `producto_id`       | string          | Identificador único del producto         | Obligatorio y único                                            |
| `nombre_producto`   | string          | Nombre o referencia del producto         | Debe estar normalizado                                         |
| `categoria`         | string          | Categoría a la que pertenece el producto | Se evitarán categorías duplicadas por diferencias de escritura |
| `precio`            | decimal         | Precio del producto                      | Debe ser numérico y no negativo                                |
| `duracion_estimada` | integer/decimal | Duración estimada del producto           | Solo se utilizará cuando exista información fiable             |

La tabla se incorporará al modelo cuando se disponga de un catálogo de productos asociado a las ventas reales.

### 6.3. Tabla `ventas`

| Campo          | Tipo de dato | Descripción                                     | Regla / consideración                           |
| -------------- | ------------ | ----------------------------------------------- | ----------------------------------------------- |
| `venta_id`     | string       | Identificador único de la venta                 | Obligatorio y único                             |
| `cliente_id`   | string       | Identificador del cliente que realizó la compra | Debe existir en `clientes`                      |
| `producto_id`  | string       | Identificador del producto adquirido            | Debe existir en `productos`                     |
| `fecha_compra` | date         | Fecha en la que se realizó la compra            | Obligatoria para análisis temporal              |
| `cantidad`     | integer      | Número de unidades adquiridas                   | Debe ser mayor que cero                         |
| `precio`       | decimal      | Precio aplicado al producto                     | Debe ser numérico y no negativo                 |
| `importe`      | decimal      | Importe total de la línea de venta              | Se podrá calcular a partir de cantidad y precio |

La tabla `ventas` es el componente principal que permitirá construir posteriormente el histórico de comportamiento de compra. Actualmente no se dispone de este histórico en los archivos analizados.

### 6.4. Tabla `interacciones`

| Campo              | Tipo de dato | Descripción                            | Regla / consideración                 |
| ------------------ | ------------ | -------------------------------------- | ------------------------------------- |
| `interaccion_id`   | string       | Identificador único de la interacción  | Obligatorio y único                   |
| `cliente_id`       | string       | Cliente relacionado con la interacción | Debe existir en `clientes`            |
| `fecha`            | date         | Fecha de la interacción                | Debe tener un formato de fecha válido |
| `canal`            | string       | Canal utilizado para contactar         | Categorías normalizadas               |
| `tipo_interaccion` | string       | Tipo de comunicación o interacción     | Categorías definidas previamente      |
| `respuesta`        | string       | Resultado o respuesta obtenida         | Puede contener valores nulos          |

Estos campos son previstos para una futura incorporación de información de seguimiento comercial.

### 6.5. Dataset `clientes_rfm`

| Campo        | Tipo de dato | Descripción                  | Regla / consideración                |
| ------------ | ------------ | ---------------------------- | ------------------------------------ |
| `cliente_id` | string       | Identificador del cliente    | Debe existir en `clientes`           |
| `recency`    | integer      | Días desde la última compra  | Calculado a partir de `fecha_compra` |
| `frequency`  | integer      | Número de compras realizadas | Calculado a partir de `ventas`       |
| `monetary`   | decimal      | Valor monetario acumulado    | Calculado a partir de `importe`      |

Este dataset será generado únicamente cuando exista un histórico de ventas real suficiente para calcular las métricas.

### 6.6. Dataset `segmentacion_clientes`

| Campo        | Tipo de dato | Descripción                   | Regla / consideración                 |
| ------------ | ------------ | ----------------------------- | ------------------------------------- |
| `cliente_id` | string       | Identificador del cliente     | Debe existir en `clientes`            |
| `segmento`   | string       | Segmento asignado al cliente  | Resultado del proceso de segmentación |
| `recency`    | integer      | Valor de recencia utilizado   | Procedente de RFM                     |
| `frequency`  | integer      | Valor de frecuencia utilizado | Procedente de RFM                     |
| `monetary`   | decimal      | Valor monetario utilizado     | Procedente de RFM                     |

La segmentación será un dataset derivado y dependerá de la disponibilidad y calidad del histórico de ventas.

### 6.7. Variable objetivo para la predicción de recompra

En caso de que los datos reales permitan desarrollar el modelo predictivo, se incorporará una variable objetivo que represente si el cliente realizó una recompra dentro del horizonte temporal definido para el proyecto.

| Campo      | Tipo de dato | Descripción                                                                 |
| ---------- | ------------ | --------------------------------------------------------------------------- |
| `recompra` | boolean      | Indica si el cliente realizó una nueva compra dentro del horizonte definido |

La definición definitiva del horizonte temporal y de esta variable dependerá del histórico real disponible. No se generará artificialmente a partir de datos simulados.

### 6.8. Identificadores y privacidad

Los identificadores utilizados en la capa analítica serán identificadores internos y anonimizados.

Los números de teléfono y otros datos directamente identificativos presentes en las fuentes originales no formarán parte de los datasets publicados en el repositorio.

El proceso de transformación deberá permitir mantener la relación entre las diferentes tablas mediante `cliente_id` sin exponer la identidad real de los clientes.

## 7. Problemas esperados de calidad de datos

A partir de la revisión de las fuentes disponibles y de las necesidades futuras del sistema, se identifican los siguientes problemas de calidad de datos que deberán considerarse durante el proceso de construcción de las capas `processed` y `gold`.

### 7.1. Valores nulos

En los perfiles de clientes existen campos con información incompleta.

Se han identificado valores ausentes principalmente en:

* `tipo_piel`
* `tono_base`
* `ciudad`
* `nombre`
* `celular`

Los valores nulos deberán analizarse según el significado del campo. No se sustituirán automáticamente por valores inventados, ya que esto podría introducir información incorrecta.

Para variables categóricas se podrá utilizar una categoría como `No informado` cuando sea necesario mantener el registro para el análisis.

### 7.2. Datos duplicados

Se deberá comprobar la existencia de registros duplicados tanto dentro de cada fuente como entre diferentes fuentes.

En particular, se detectaron casos en los que el número de celular aparece asociado a más de un registro en los perfiles disponibles. Estos casos deberán revisarse antes de utilizar el celular como referencia para identificar clientes.

El identificador definitivo del sistema será `cliente_id`, que deberá ser único y estable.

### 7.3. Información identificativa

Las fuentes actuales contienen información directamente identificativa, como nombres y números de teléfono.

Estos datos son necesarios únicamente para determinados usos privados del CRM y no deberán formar parte de los datos publicados en el repositorio del proyecto.

Antes de utilizar los datos en el entorno público se realizará un proceso de anonimización mediante identificadores internos, como `CLIENTE_001`, `CLIENTE_002`, etc.

### 7.4. Inconsistencias en categorías y textos

Los campos categóricos pueden presentar diferencias de escritura que representen el mismo valor.

Por ejemplo, una misma ciudad o categoría de producto podría aparecer con diferencias de mayúsculas, espacios, abreviaturas o escritura.

Durante el procesamiento se normalizarán los textos y se establecerán categorías controladas para evitar que una misma categoría sea contabilizada como diferentes valores.

### 7.5. Fechas y datos temporales

El histórico de ventas todavía no está disponible en las fuentes actuales.

Para que posteriormente sea posible realizar análisis temporales, RFM y predicción de recompra, las ventas deberán disponer de una `fecha_compra` válida.

Las fechas deberán almacenarse con un formato homogéneo y deberán validarse para detectar:

* Fechas inválidas.
* Fechas futuras no justificadas.
* Fechas con formatos diferentes.
* Registros sin fecha.
* Periodos de histórico insuficientes.

La ausencia de fechas de compra constituye actualmente una limitación importante para el análisis del comportamiento de compra.

### 7.6. Datos insuficientes para el análisis de recompra

Disponer de un número elevado de clientes no garantiza disponer de suficientes datos para entrenar un modelo predictivo.

Para la predicción de recompra será necesario contar con suficientes transacciones fechadas, clientes con compras repetidas y ejemplos que permitan distinguir entre clientes que realizaron y que no realizaron una recompra dentro del horizonte temporal definido.

Si estos datos no están disponibles en cantidad suficiente, la predicción no se incorporará como componente principal y el proyecto se centrará en el CRM, RFM, segmentación y dashboard.

### 7.7. Datos de productos incompletos

El modelo requiere información sobre los productos adquiridos, pero actualmente no se dispone de un histórico de ventas asociado a un catálogo estructurado.

Será necesario definir identificadores únicos de producto y normalizar información como:

* Nombre o referencia.
* Categoría.
* Precio.
* Duración estimada, cuando sea conocida.

La duración estimada de un producto no deberá interpretarse automáticamente como una fecha de recompra real.

### 7.8. Problemas de integración entre fuentes

Las fuentes actuales no presentan necesariamente un identificador común diseñado específicamente para el modelo.

Por ello, será necesario establecer una estrategia de identificación que permita relacionar los perfiles de clientes con las futuras ventas e interacciones.

El sistema utilizará `cliente_id` como identificador interno común. La correspondencia entre fuentes deberá validarse antes de integrar nuevos registros.

### 7.9. Cobertura limitada del comportamiento del cliente

Los datos de perfil permiten conocer determinadas características del cliente, pero no explican por sí mismos su comportamiento de compra.

Por ejemplo, conocer el tipo de piel o el tono de base no permite determinar cuándo comprará nuevamente un producto.

Para realizar análisis de comportamiento será necesario incorporar progresivamente información de ventas e interacciones reales.

### 7.10. Valores atípicos

Cuando se incorpore el histórico de ventas se deberán identificar posibles valores atípicos, como:

* Cantidades de productos inusualmente elevadas.
* Precios negativos o incorrectos.
* Importes incompatibles con cantidad y precio.
* Fechas anómalas.
* Compras excepcionalmente grandes.

Los valores atípicos no se eliminarán automáticamente. Primero se determinará si representan errores de registro o comportamientos reales.

### 7.11. Cambios y evolución de los datos

El CRM está diseñado para crecer con el tiempo. Por ello, pueden aparecer nuevos productos, nuevas categorías, nuevos clientes o cambios en la forma de registrar las interacciones.

Las transformaciones deberán ser suficientemente flexibles para incorporar estos cambios sin romper las relaciones existentes.

Se mantendrán reglas de validación para detectar cambios inesperados en la estructura o en los valores de los datos.

### 7.12. Principales limitaciones actuales

La principal limitación identificada en esta fase es la ausencia de un histórico estructurado de ventas.

Los datos actuales permiten comenzar a estructurar los perfiles de clientes, pero todavía no permiten calcular de forma válida las métricas RFM ni entrenar un modelo de predicción de recompra.

Por tanto, la disponibilidad, calidad y volumen del histórico real de ventas será un factor determinante para decidir qué funcionalidades analíticas pueden implementarse en la versión final del proyecto.

## 8. Limpieza y transformaciones previstas

Los procesos de limpieza y transformación se realizarán principalmente durante la construcción de las capas `processed` y `gold`. El objetivo será obtener datos consistentes, trazables y adecuados para el análisis, evitando modificar directamente las fuentes originales.

### 8.1. Normalización de nombres y estructuras

Los nombres de las columnas se normalizarán para utilizar una nomenclatura homogénea en todo el modelo.

Se utilizarán nombres en minúsculas, sin espacios ni caracteres especiales, siguiendo una estructura consistente, por ejemplo:

* `CELULAR` → `cliente_contacto` durante la etapa de preparación.
* `TIPO PIEL` → `tipo_piel`.
* `TONO BASE` → `tono_base`.

Posteriormente, el modelo utilizará los nombres definidos en el diccionario de datos, como `cliente_id`, `tipo_piel` y `tono_base`.

### 8.2. Anonimización de clientes

Antes de utilizar los datos en el repositorio público se eliminarán o transformarán los campos que permitan identificar directamente a una persona.

Los clientes serán representados mediante identificadores internos, por ejemplo:

```text
CLIENTE_001
CLIENTE_002
CLIENTE_003
```

La anonimización permitirá mantener las relaciones entre clientes, ventas e interacciones sin exponer números de teléfono u otra información identificativa.

Los archivos originales con información personal no deberán formar parte del repositorio público.

### 8.3. Tratamiento de valores nulos

Los valores ausentes se analizarán según el campo afectado y su importancia para el análisis.

Para variables categóricas, cuando sea necesario conservar el registro, se podrá utilizar una categoría como `No informado`.

No se utilizarán valores inventados para completar información desconocida.

En variables necesarias para determinados cálculos, como una fecha de compra requerida para un análisis temporal, un valor ausente podrá impedir que el registro sea utilizado en ese cálculo concreto.

### 8.4. Tratamiento de duplicados

Se realizarán comprobaciones de duplicidad antes de integrar los datos.

Los registros completamente duplicados podrán eliminarse cuando se confirme que representan el mismo registro.

En el caso de posibles duplicidades de clientes, no se eliminarán registros automáticamente. Se analizarán los campos disponibles para determinar si representan a la misma persona o a personas diferentes.

El `cliente_id` será único dentro del modelo final.

### 8.5. Normalización de categorías y textos

Los campos categóricos serán normalizados para evitar que diferencias de escritura generen categorías diferentes.

Se podrán aplicar transformaciones como:

* Eliminación de espacios innecesarios.
* Homogeneización de mayúsculas y minúsculas.
* Normalización de nombres de ciudades.
* Unificación de categorías equivalentes.
* Corrección de errores de escritura cuando puedan identificarse de forma fiable.

No se modificarán valores ambiguos sin disponer de información suficiente para determinar su significado.

### 8.6. Tratamiento de fechas

Cuando se incorporen datos de ventas e interacciones, las fechas se convertirán a un formato homogéneo y a un tipo de dato temporal.

Se realizarán validaciones para detectar:

* Fechas inválidas.
* Fechas futuras no justificadas.
* Fechas ausentes.
* Formatos inconsistentes.
* Registros fuera del periodo de análisis.

Las fechas serán especialmente importantes para calcular la recencia y para definir correctamente la variable objetivo de recompra.

### 8.7. Validación de datos numéricos

Los campos numéricos se convertirán a tipos adecuados y se validarán según las reglas definidas en el modelo.

Por ejemplo:

* `cantidad` deberá ser mayor que cero.
* `precio` no deberá ser negativo.
* `importe` deberá ser coherente con la cantidad y el precio.
* Los identificadores no deberán tratarse como variables numéricas cuando conceptualmente sean códigos.

Los valores anómalos se revisarán antes de decidir si deben corregirse, excluirse o conservarse.

### 8.8. Construcción de relaciones

Durante la integración se comprobará que las claves utilizadas como relaciones tengan correspondencia.

Por ejemplo:

```text
ventas.cliente_id → clientes.cliente_id
ventas.producto_id → productos.producto_id
interacciones.cliente_id → clientes.cliente_id
```

Los registros que hagan referencia a entidades inexistentes deberán ser revisados antes de incorporarse a la capa `gold`.

### 8.9. Variables derivadas

A partir del histórico real de ventas podrán calcularse variables adicionales para el análisis del comportamiento de los clientes.

Entre ellas:

* Días desde la última compra.
* Número total de compras.
* Gasto acumulado.
* Gasto medio por compra.
* Número de categorías de productos adquiridas.
* Categoría de producto más frecuente.

Estas variables se calcularán a partir de los datos disponibles y se documentará su fórmula para garantizar que puedan reproducirse.

### 8.10. Cálculo de RFM

Cuando exista suficiente histórico real de ventas, se calcularán las tres dimensiones del análisis RFM:

* **Recency:** tiempo transcurrido desde la última compra.
* **Frequency:** número de compras realizadas.
* **Monetary:** valor monetario de las compras.

Los cálculos se realizarán a partir de `fecha_compra` e `importe` y se almacenarán en el dataset `clientes_rfm`.

La metodología concreta para transformar estas variables en puntuaciones o segmentos se definirá durante la fase de análisis, en función de las características reales del conjunto de datos.

### 8.11. Preparación de la variable de recompra

Si existe suficiente histórico real, se construirá una variable objetivo que indique si un cliente realizó una nueva compra dentro del horizonte temporal definido para el proyecto.

La variable se obtendrá únicamente a partir de transacciones reales.

No se utilizarán datos simulados para generar artificialmente casos de recompra o no recompra con los que entrenar el modelo final.

### 8.12. Criterios para descartar registros

Un registro no será descartado únicamente por contener algún dato ausente.

La eliminación se realizará cuando exista una razón justificada, por ejemplo:

* Registro completamente duplicado.
* Datos claramente inválidos.
* Registro imposible de relacionar con las entidades necesarias para un análisis determinado.
* Información corrupta o incompatible con las reglas del modelo.

Cuando un registro sea descartado, se documentará el motivo para mantener la trazabilidad del proceso.

### 8.13. Trazabilidad

Las transformaciones realizadas deberán poder reproducirse mediante scripts o notebooks de procesamiento.

La separación entre `raw`, `processed` y `gold` permitirá conservar los datos originales, identificar qué transformaciones se han aplicado y obtener los datasets finales utilizados en los análisis.

Esto permitirá que, cuando se incorporen nuevos clientes, ventas o interacciones, el mismo proceso pueda ejecutarse nuevamente sin modificar manualmente los datos originales.

## 9. Riesgos del modelo de datos

El modelo de datos propuesto permite estructurar progresivamente la información necesaria para el CRM, pero existen algunos riesgos y limitaciones que deberán controlarse durante el desarrollo.

### 9.1. Insuficiencia de histórico de ventas

El principal riesgo identificado es la disponibilidad limitada de información transaccional.

Los datos actualmente disponibles permiten estructurar información básica de clientes y perfiles, pero no contienen un histórico de ventas suficientemente estructurado para garantizar desde este momento la construcción de métricas RFM o de un modelo predictivo de recompra.

Este riesgo afecta principalmente a las tablas `ventas` y a los datasets derivados de ella.

**Mitigación:** el modelo se ha diseñado para incorporar progresivamente nuevas transacciones reales. La predicción de recompra solo se implementará si el volumen, la antigüedad y la variedad del histórico permiten obtener resultados fiables.

### 9.2. Riesgo de datos identificativos

Las fuentes actuales contienen información como nombres y números de teléfono.

La utilización de estos datos sin las medidas adecuadas podría suponer un riesgo de privacidad y dificultar la publicación del proyecto en un repositorio público.

**Mitigación:** los datos utilizados en el repositorio serán anonimizados mediante identificadores internos. Los archivos originales con información identificativa permanecerán fuera del repositorio público.

### 9.3. Calidad e integridad de los perfiles

Los perfiles actuales presentan campos incompletos y posibles duplicidades, especialmente en la información de contacto.

Esto puede dificultar la identificación inequívoca de un cliente cuando se integren nuevas fuentes.

**Mitigación:** se establecerá `cliente_id` como identificador interno único y se realizarán procesos de validación, deduplicación y normalización antes de incorporar los datos a la capa `gold`.

### 9.4. Integración de futuras fuentes

Las futuras ventas e interacciones pueden proceder de fuentes con estructuras diferentes a las actuales.

Si no existe un identificador común, podrían producirse problemas al relacionar una venta con el cliente correspondiente.

**Mitigación:** se utilizará `cliente_id` como identificador común dentro del modelo y se establecerán procesos de validación antes de integrar nuevas fuentes.

### 9.5. Riesgo de construir una Gold incompleta

Existe el riesgo de que la información disponible no permita construir todas las tablas previstas inicialmente.

Por ejemplo, sin un catálogo de productos no será posible completar correctamente la tabla `productos`, y sin fechas de ventas no será posible calcular las variables RFM.

**Mitigación:** la capa `gold` se construirá de forma incremental. Solo se incorporarán los datasets que puedan generarse a partir de información real y suficientemente fiable.

### 9.6. Riesgo de modelo predictivo poco representativo

Incluso disponiendo de un determinado número de transacciones, podría existir un desequilibrio entre clientes que realizan recompra y clientes que no la realizan.

También podría existir un histórico demasiado corto o concentrado en determinados tipos de clientes o productos.

En estas circunstancias, un modelo predictivo podría mostrar métricas aparentemente buenas sin generalizar correctamente a nuevos clientes.

**Mitigación:** antes de entrenar un modelo se analizará la distribución de la variable objetivo, la cantidad de ejemplos disponibles, la antigüedad del histórico y la representatividad de los datos.

Si estas condiciones no son suficientes, la predicción se mantendrá como funcionalidad futura.

### 9.7. Riesgo de evolución del modelo

El CRM está diseñado para crecer con nuevas ventas, clientes, productos e interacciones.

Los patrones de compra pueden cambiar con el tiempo y también pueden incorporarse nuevas categorías de productos o nuevas formas de interacción.

**Mitigación:** los procesos de transformación se mantendrán reproducibles y se podrán ejecutar nuevamente cuando se incorporen nuevos datos. Las reglas del modelo y las definiciones de las variables deberán documentarse para poder actualizarlas cuando sea necesario.

### 9.8. Qué ocurre si no se puede construir completamente la capa Gold

Si los datos disponibles no permiten construir todos los datasets inicialmente previstos, el proyecto no quedará bloqueado.

Se priorizará una versión funcional compuesta por:

1. Base estructurada y anonimizada de clientes.
2. Organización del catálogo de productos cuando esté disponible.
3. Registro estructurado de ventas cuando exista información real.
4. Segmentación de clientes basada en RFM cuando los datos lo permitan.
5. Dashboard para visualizar clientes, ventas y segmentos.

La predicción de recompra quedará como una extensión futura si el histórico disponible no permite desarrollarla con garantías.

### 9.9. Alternativa simplificada

En el escenario más limitado, si no se consigue suficiente histórico de ventas para realizar RFM o predicción, el núcleo del proyecto será el **CRM estructurado y el dashboard de seguimiento**, utilizando la información real disponible.

La incorporación progresiva de nuevas ventas permitirá ampliar posteriormente el histórico y habilitar nuevas funcionalidades analíticas.

De esta manera, el proyecto mantiene una funcionalidad útil incluso si la disponibilidad de datos no permite desarrollar inicialmente todos los componentes de inteligencia artificial previstos.

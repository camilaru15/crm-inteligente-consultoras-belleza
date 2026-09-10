# 04. Diseño del análisis y estrategia de modelado

## 1. Problema que se busca resolver

El proyecto busca mejorar el seguimiento comercial de las consultoras de belleza mediante la organización y análisis de la información de sus clientes y de su comportamiento de compra.

Actualmente, la información de los clientes puede encontrarse distribuida en contactos, perfiles y registros comerciales, lo que dificulta identificar de forma sistemática qué clientes necesitan atención, cuáles presentan mayor actividad de compra y qué clientes podrían requerir una acción de seguimiento.

El problema que se pretende resolver no consiste únicamente en almacenar información, sino en **transformar los datos disponibles en información útil para priorizar acciones comerciales**.

El usuario principal del sistema será la **consultora de belleza**, que podrá utilizar el CRM para conocer mejor a sus clientes, analizar su comportamiento y orientar sus acciones de seguimiento.

El análisis permitirá responder preguntas como:

* ¿Qué clientes han comprado recientemente?
* ¿Qué clientes presentan una mayor frecuencia de compra?
* ¿Qué clientes generan un mayor valor de ventas?
* ¿Qué perfiles de clientes presentan comportamientos similares?
* ¿Qué clientes deberían priorizarse para una acción de seguimiento?
* Cuando exista suficiente histórico, ¿qué clientes presentan una mayor probabilidad de realizar una recompra dentro del horizonte temporal definido?

El resultado esperado será un sistema que permita **priorizar y apoyar el seguimiento de clientes a partir de datos reales**, en lugar de depender únicamente de la memoria de la consultora o de revisiones manuales de sus contactos.

El núcleo inicial del proyecto estará compuesto por el CRM estructurado, el análisis RFM, la segmentación de clientes y un dashboard de seguimiento. La predicción de recompra se incorporará únicamente si el histórico real disponible permite construir y validar un modelo con suficiente rigor.

El proyecto se considerará útil si permite a la consultora identificar de forma clara los diferentes perfiles de clientes y obtener información accionable para decidir **a quién realizar seguimiento y por qué**.

## 2. Análisis de datos planteado y utilidad esperada

El análisis de datos se centrará inicialmente en comprender el comportamiento de compra de los clientes y en identificar patrones que puedan ayudar a la consultora a priorizar sus acciones comerciales.

El análisis se desarrollará de forma progresiva, comenzando por análisis descriptivos y de segmentación. La incorporación de modelos predictivos dependerá de la disponibilidad de un histórico real de transacciones suficiente para definir y validar adecuadamente la variable objetivo.

### 2.1 Preguntas de análisis

El sistema buscará responder, entre otras, las siguientes preguntas:

* ¿Cuántos clientes están registrados y qué información de perfil se dispone de cada uno?
* ¿Qué clientes han realizado compras recientemente?
* ¿Con qué frecuencia realizan compras los clientes?
* ¿Qué clientes presentan un mayor valor acumulado de compra?
* ¿Qué clientes llevan más tiempo sin realizar una compra?
* ¿Existen grupos de clientes con comportamientos de compra similares?
* ¿Qué perfiles de clientes presentan una mayor actividad comercial?
* ¿Qué clientes deberían priorizarse para realizar acciones de seguimiento?
* ¿Existen diferencias en el comportamiento de compra según características disponibles del perfil?
* Cuando exista suficiente histórico, ¿qué clientes presentan una mayor probabilidad de realizar una recompra dentro del horizonte temporal definido?

### 2.2 Análisis descriptivo y comparativo

En una primera fase se realizará un análisis descriptivo de la información disponible.

Se analizarán variables como:

* número de clientes;
* número de compras;
* frecuencia de compra;
* valor de las compras;
* fecha de última compra;
* productos adquiridos;
* distribución de clientes por características de perfil disponibles;
* evolución temporal de las ventas;
* distribución de las ventas por producto o categoría.

Este análisis permitirá conocer la estructura y calidad de los datos antes de realizar transformaciones o plantear modelos.

También se realizarán comparaciones entre grupos de clientes para identificar diferencias relevantes en su comportamiento de compra.

### 2.3 Análisis temporal

Siempre que existan fechas de transacción suficientes, se analizará la evolución temporal de las compras.

Se podrán estudiar aspectos como:

* evolución de las ventas;
* número de clientes activos por periodo;
* frecuencia de compra;
* periodos con mayor o menor actividad;
* tiempo transcurrido entre compras;
* comportamiento de clientes recurrentes frente a clientes con una única compra.

Este análisis será especialmente importante para estudiar posteriormente la recompra, ya que la definición de esta variable dependerá de la existencia de transacciones fechadas.

### 2.4 Segmentación mediante RFM

Se plantea utilizar el análisis RFM como una de las herramientas principales de segmentación.

Las dimensiones consideradas serán:

* **Recency:** tiempo transcurrido desde la última compra.
* **Frequency:** número de compras realizadas durante un periodo definido.
* **Monetary:** valor monetario acumulado de las compras.

A partir de estas variables se podrán identificar perfiles de clientes con diferentes niveles de actividad y valor comercial.

Por ejemplo, se podrán diferenciar clientes recientes y frecuentes de clientes que llevan un periodo prolongado sin comprar.

La segmentación permitirá pasar de una visión general de la cartera de clientes a una visión orientada a la acción comercial.

### 2.5 Análisis geográfico y de características del cliente

Cuando las variables estén disponibles y presenten suficiente cobertura, se podrán realizar análisis por ciudad y por características de perfil, como tipo de piel o tono de base.

Estos análisis tendrán carácter exploratorio y se utilizarán para comprobar si determinadas características están relacionadas con diferencias en el comportamiento de compra.

No se asumirán relaciones entre variables antes de comprobarlas mediante los datos disponibles.

### 2.6 Visualizaciones y KPI iniciales

Los principales resultados se integrarán posteriormente en un dashboard orientado a la consultora.

Entre los indicadores iniciales se contemplan:

* número total de clientes;
* clientes activos;
* número de compras;
* ventas acumuladas;
* ticket medio;
* frecuencia media de compra;
* recencia media;
* distribución de clientes por segmentos RFM;
* evolución temporal de las ventas;
* clientes prioritarios para seguimiento.

Los indicadores definitivos se ajustarán a la información que realmente pueda obtenerse del histórico de ventas.

### 2.7 Utilidad esperada del análisis

El análisis permitirá transformar los datos registrados en información útil para la toma de decisiones comerciales.

En particular, permitirá:

1. conocer mejor la cartera de clientes;
2. identificar clientes con diferentes niveles de actividad y valor;
3. detectar clientes que requieren seguimiento;
4. orientar las acciones comerciales según segmentos de clientes;
5. facilitar el seguimiento mediante indicadores y visualizaciones;
6. generar una base analítica adecuada para plantear posteriormente un modelo predictivo, si los datos disponibles lo permiten.

De esta forma, el análisis de datos constituye una parte central del proyecto y no únicamente una etapa previa al modelado. Si el histórico disponible no permite construir un modelo predictivo fiable, los resultados obtenidos mediante el CRM, el análisis RFM, la segmentación y el dashboard seguirán proporcionando una solución funcional y útil para la consultora.

## 3. Tipo de modelos que se van a plantear

El planteamiento de modelado estará condicionado por la disponibilidad y calidad del histórico real de transacciones. Antes de entrenar cualquier modelo se comprobará que existen suficientes compras fechadas, clientes con compras repetidas y ejemplos suficientes de recompra y no recompra.

El objetivo predictivo, si los datos lo permiten, será estimar la probabilidad de que un cliente realice una recompra dentro de un horizonte temporal previamente definido.

### 3.1 Tarea de modelado

La tarea principal que se plantea es un problema de **clasificación binaria**:

* **1:** el cliente realiza una recompra dentro del horizonte definido.
* **0:** el cliente no realiza una recompra dentro del horizonte definido.

El horizonte temporal no se establecerá de forma arbitraria. Se determinará a partir del comportamiento observado en el histórico disponible y de la lógica comercial del proyecto.

El modelo tendría como resultado una probabilidad de recompra para cada cliente, que posteriormente podría utilizarse para priorizar acciones de seguimiento.

### 3.2 Modelo baseline

Como referencia inicial se utilizará un modelo sencillo de **regresión logística**.

La regresión logística permitirá establecer una primera referencia de rendimiento y, además, facilita la interpretación de la relación entre las variables utilizadas y la probabilidad estimada de recompra.

El baseline será importante para comprobar si modelos más complejos aportan una mejora real respecto a una solución sencilla.

También se podrá utilizar, cuando corresponda, una regla de referencia basada en el comportamiento histórico de recompra para comprobar que el modelo predictivo aporta valor adicional frente a una estrategia comercial simple.

### 3.3 Modelos candidatos

Si el volumen y la calidad de los datos lo permiten, se compararán un número reducido de modelos:

**Regresión logística**

Será el modelo de referencia por su sencillez e interpretabilidad.

Ventajas:

* fácil de interpretar;
* adecuada para clasificación binaria;
* permite analizar la influencia de las variables;
* constituye un buen punto de comparación.

Limitaciones:

* puede tener dificultades para representar relaciones no lineales;
* su rendimiento puede verse limitado si existen interacciones complejas entre variables.

**Random Forest**

Se planteará como alternativa para capturar relaciones no lineales entre las características de los clientes.

Ventajas:

* permite modelar relaciones no lineales;
* puede trabajar con diferentes tipos de variables;
* proporciona información sobre la importancia de las características.

Limitaciones:

* menor interpretabilidad que la regresión logística;
* puede sobreajustarse si no se controla adecuadamente;
* requiere una cantidad de datos suficiente para obtener resultados estables.

**Gradient Boosting**

Se podrá evaluar como alternativa adicional si el volumen de datos disponible resulta suficiente.

Ventajas:

* puede capturar relaciones complejas;
* suele ofrecer un buen rendimiento en problemas de clasificación tabular;
* permite trabajar con interacciones entre variables.

Limitaciones:

* mayor complejidad;
* requiere un ajuste cuidadoso de hiperparámetros;
* puede sobreajustarse si el conjunto de datos es reducido.

No se plantea utilizar un número elevado de modelos. La comparación se limitará a alternativas razonables para el volumen, estructura y naturaleza de los datos disponibles.

### 3.4 Variables potenciales para el modelado

En caso de disponer de suficiente histórico, las variables de entrada podrán incluir información derivada de las transacciones, como:

* recencia;
* frecuencia de compra;
* valor monetario;
* número de productos adquiridos;
* categorías o tipos de productos adquiridos;
* tiempo medio entre compras;
* comportamiento reciente;
* características de perfil disponibles y previamente validadas.

Las variables utilizadas deberán representar información que estaría disponible en el momento en que la consultora necesita realizar la predicción.

### 3.5 Alternativa si no existe suficiente información para predecir

Si el histórico real no contiene suficientes ejemplos para construir y validar un modelo predictivo de forma fiable, no se forzará el entrenamiento de un modelo.

En ese escenario, el proyecto tendrá como solución principal:

* CRM estructurado;
* análisis descriptivo;
* análisis RFM;
* segmentación de clientes;
* reglas de priorización;
* dashboard de seguimiento.

La priorización podrá realizarse mediante reglas basadas en variables como recencia, frecuencia y valor de compra, siempre que estas puedan calcularse correctamente a partir de datos reales.

La predicción de recompra quedará documentada como una ampliación futura que podrá incorporarse cuando exista un histórico suficiente.

### 3.6 Criterio general de adecuación

La elección del modelo no se realizará únicamente en función de obtener la métrica más alta.

Se tendrá en cuenta conjuntamente:

* rendimiento predictivo;
* comparación con el baseline;
* capacidad de generalización;
* estabilidad de los resultados;
* interpretabilidad;
* volumen y calidad de los datos;
* utilidad práctica para la consultora.

Por tanto, el modelo final será seleccionado únicamente si demuestra aportar un valor suficiente frente a una alternativa sencilla y puede validarse correctamente con datos reales.

## 4. Datos de entrada del análisis y los modelos

Los análisis y modelos se realizarán a partir de los datos estructurados en la capa Gold definida en la Entrega 3.

La información disponible actualmente permite trabajar principalmente con datos de clientes y sus características de perfil. El histórico de transacciones necesario para realizar análisis completos de comportamiento de compra y, especialmente, para construir un modelo de predicción de recompra deberá incorporarse posteriormente a partir de registros reales de ventas.

Por este motivo, se diferenciarán los datos disponibles actualmente de los datos necesarios para la fase predictiva.

### 4.1 Datos disponibles actualmente

Los datos disponibles contienen información de clientes y perfiles, incluyendo campos como:

* identificador del cliente;
* nombre;
* teléfono;
* tipo de piel;
* tono de base;
* ciudad.

Estos datos permitirán construir y validar inicialmente la estructura del CRM y realizar análisis exploratorios sobre la información de los clientes.

Los datos identificativos, como nombre y teléfono, no se utilizarán directamente en los análisis publicados ni se incluirán en el repositorio público. Para el desarrollo se utilizará un identificador interno y anonimizado del cliente.

### 4.2 Datos necesarios para el análisis comercial

Para construir el análisis de comportamiento de compra será necesario disponer de un histórico real de ventas estructurado.

La entidad principal será la tabla `ventas`, con una granularidad de **una fila por transacción o línea de venta**, según el nivel de detalle que pueda obtenerse de la fuente original.

Entre los campos previstos se encuentran:

* `id_venta`;
* `id_cliente`;
* `id_producto`;
* `fecha_venta`;
* cantidad;
* importe;
* categoría o tipo de producto, cuando esté disponible.

La tabla `clientes` se relacionará con `ventas` mediante `id_cliente`, mientras que `productos` se relacionará mediante `id_producto`.

### 4.3 Variables derivadas

A partir del histórico de ventas podrán construirse variables agregadas para el análisis y, si procede, para el modelo predictivo.

Entre ellas:

* número total de compras;
* fecha de última compra;
* días desde la última compra;
* importe total comprado;
* importe medio por compra;
* frecuencia de compra;
* número de productos adquiridos;
* tiempo medio entre compras;
* comportamiento de compra reciente;
* puntuaciones RFM.

Estas variables se calcularán utilizando únicamente información disponible hasta el momento en el que se realice el análisis o la predicción, evitando utilizar información futura.

### 4.4 Datos de entrada del modelo predictivo

Si el histórico disponible permite construir un modelo de recompra, el conjunto de entrada estará formado por las características disponibles antes del momento de predicción.

Las principales variables candidatas serán las derivadas del comportamiento histórico del cliente:

* recencia;
* frecuencia;
* valor monetario;
* número de compras anteriores;
* tiempo entre compras;
* productos o categorías adquiridas;
* comportamiento reciente;
* características de perfil que presenten suficiente cobertura y utilidad.

La variable objetivo será construida posteriormente a partir de las compras posteriores al momento de referencia, siguiendo el horizonte de recompra definido.

Por tanto, la información utilizada como entrada y la información utilizada para definir el resultado estarán temporalmente separadas.

### 4.5 Variables excluidas

No se utilizarán como variables predictoras los datos identificativos cuyo único propósito sea identificar al cliente, como:

* nombre;
* número de teléfono;
* identificadores personales no anonimizados.

Tampoco se utilizarán variables que incorporen información posterior al momento en el que se pretende realizar la predicción, ya que podrían producir **fuga de información (data leakage)** y generar resultados artificialmente buenos.

Las variables de perfil, como tipo de piel, tono de base o ciudad, solo se incorporarán al modelo si presentan suficiente cobertura y se demuestra que pueden aportar información útil sin introducir sesgos o problemas de calidad.

### 4.6 Granularidad y clave principal

La granularidad dependerá de la entidad analizada:

* `clientes`: una fila por cliente;
* `productos`: una fila por producto;
* `ventas`: una fila por transacción o línea de venta;
* `interacciones`: una fila por interacción registrada;
* `clientes_rfm`: una fila por cliente y periodo de cálculo;
* `segmentacion_clientes`: una fila por cliente y segmentación asignada.

La clave principal de la entidad `clientes` será `id_cliente`, mientras que `id_venta` identificará las ventas y `id_producto` identificará los productos.

Las tablas derivadas de RFM y segmentación utilizarán `id_cliente` junto con el periodo de cálculo cuando sea necesario.

### 4.7 Información disponible en el momento de la predicción

Una condición fundamental será que el modelo solo utilice información que la consultora habría podido conocer en el momento en que se genera la predicción.

Por ejemplo, para estimar si un cliente realizará una recompra después de una determinada fecha, se podrán utilizar sus compras anteriores a esa fecha, pero no las compras realizadas posteriormente.

Este criterio permitirá evitar fuga de información y obtener una evaluación más realista del comportamiento del modelo ante nuevos casos.

### 4.8 Situación actual de los datos

En el momento actual, la información disponible permite avanzar en la estructura del CRM y en la preparación del modelo de datos, pero no garantiza todavía la existencia de un histórico suficiente para entrenar un modelo predictivo de recompra.

Por ello, antes del modelado se realizará una comprobación de:

* número de transacciones disponibles;
* número de clientes con compras repetidas;
* profundidad temporal del histórico;
* distribución de las compras;
* cantidad de casos de recompra y no recompra;
* cobertura y calidad de las variables.

Si estas condiciones no son suficientes, se mantendrán como núcleo del proyecto el CRM, el análisis RFM, la segmentación y el dashboard, dejando el modelo predictivo como ampliación futura.

## 5. Datos de salida y forma de consumo

Los resultados del sistema estarán orientados a facilitar la interpretación del comportamiento de los clientes y apoyar la toma de decisiones comerciales por parte de la consultora.

Las salidas se dividirán en resultados analíticos, resultados de segmentación y, únicamente si los datos lo permiten, resultados predictivos.

### 5.1 Resultados del análisis

El análisis generará indicadores y métricas que permitan conocer el comportamiento general de la cartera de clientes.

Entre los principales resultados se contemplan:

* número de clientes;
* clientes activos;
* número de compras;
* ventas acumuladas;
* ticket medio;
* frecuencia de compra;
* recencia;
* evolución temporal de las ventas;
* distribución de clientes por segmentos.

Estos resultados se presentarán principalmente mediante tablas, indicadores y visualizaciones dentro de un dashboard.

### 5.2 Resultado de la segmentación RFM

Para cada cliente se podrá generar una clasificación basada en sus valores de Recencia, Frecuencia y Valor Monetario.

El resultado tendrá una granularidad de **cliente**, permitiendo asociar a cada `id_cliente`:

* puntuación de recencia;
* puntuación de frecuencia;
* puntuación monetaria;
* puntuación RFM;
* segmento asignado.

La segmentación permitirá identificar grupos de clientes con comportamientos diferentes y facilitar la definición de acciones comerciales.

Por ejemplo, un segmento de clientes con compras recientes y frecuentes podría recibir un tratamiento diferente al de clientes que llevan un periodo prolongado sin comprar.

### 5.3 Priorización de clientes

A partir de los resultados del análisis y de la segmentación se podrá generar una lista de clientes priorizados para seguimiento.

La priorización podrá basarse inicialmente en reglas derivadas de variables como:

* recencia;
* frecuencia;
* valor de compra;
* segmento RFM;
* comportamiento reciente.

Esta salida tendrá como objetivo transformar el análisis en una acción concreta para la consultora.

### 5.4 Resultado del modelo predictivo

Si el histórico real disponible permite desarrollar y validar un modelo de recompra, la salida principal del modelo será una **probabilidad estimada de recompra** para cada cliente.

El resultado podrá contener:

| Campo                   | Descripción                                     |
| ----------------------- | ----------------------------------------------- |
| `id_cliente`            | Identificador anonimizado del cliente           |
| `probabilidad_recompra` | Probabilidad estimada de realizar una recompra  |
| `clasificacion`         | Recompra estimada / no recompra estimada        |
| `periodo_prediccion`    | Horizonte temporal utilizado para la predicción |
| `nivel_prioridad`       | Nivel de prioridad para seguimiento             |

La probabilidad se utilizará como apoyo a la decisión y no como una certeza sobre el comportamiento futuro del cliente.

### 5.5 Forma de consumo

Los resultados serán consumidos principalmente a través de un **dashboard del CRM**.

La consultora podrá utilizarlo para:

* consultar la situación general de su cartera;
* identificar segmentos de clientes;
* localizar clientes que requieren seguimiento;
* analizar la evolución de sus ventas;
* consultar indicadores comerciales;
* priorizar acciones de contacto;
* y, si existe un modelo predictivo validado, consultar qué clientes presentan una mayor probabilidad estimada de recompra.

El dashboard deberá presentar los resultados de forma sencilla y comprensible, evitando que la consultora tenga que interpretar directamente el código o los modelos utilizados.

### 5.6 Interpretabilidad de los resultados

Los resultados deberán poder interpretarse de forma clara.

En el caso de la segmentación RFM, la explicación estará basada directamente en las variables de recencia, frecuencia y valor monetario.

En el caso de un modelo predictivo, además de mostrar la probabilidad estimada, se procurará proporcionar información sobre las principales variables que han contribuido al resultado, siempre que el modelo seleccionado permita obtener esta explicación de forma adecuada.

El sistema no presentará la predicción como una decisión automática, sino como una herramienta de apoyo para que la consultora pueda decidir qué clientes priorizar y qué acción comercial realizar.

### 5.7 Salida mínima viable

Si no existe suficiente histórico para validar un modelo predictivo, la salida mínima viable del proyecto seguirá estando formada por:

* CRM estructurado;
* indicadores comerciales;
* segmentación RFM;
* priorización de clientes;
* dashboard de seguimiento.

Esta solución permitirá entregar valor incluso sin incorporar inicialmente una predicción de recompra.

## 6. Estrategia para diseñar y seleccionar el modelo

La estrategia de modelado se desarrollará de forma progresiva, comenzando por la preparación de los datos y la definición de la variable objetivo y continuando con la comparación de diferentes alternativas de modelado.

El proceso estará condicionado por la cantidad, calidad y profundidad temporal del histórico real de transacciones disponible.

### 6.1 Preparación de los datos

Antes de entrenar cualquier modelo se realizará una revisión del conjunto de datos Gold para comprobar:

* existencia de valores nulos;
* registros duplicados;
* consistencia de fechas;
* valores atípicos;
* coherencia de las categorías;
* cantidad de transacciones;
* número de clientes con compras repetidas;
* profundidad temporal del histórico;
* distribución de la variable objetivo.

Las variables categóricas se transformarán cuando sea necesario y las variables numéricas podrán escalarse dependiendo del modelo utilizado.

Las transformaciones realizadas deberán poder reproducirse mediante un proceso automatizado de preparación de datos.

### 6.2 Definición de la variable objetivo

El objetivo predictivo será determinar si un cliente realiza una recompra dentro del horizonte temporal definido.

La variable objetivo será construida utilizando las transacciones posteriores al momento de referencia, mientras que las variables predictoras se calcularán exclusivamente con información anterior a dicho momento.

Antes de entrenar el modelo se comprobará que existen suficientes ejemplos de ambas clases:

* clientes que realizan recompra;
* clientes que no realizan recompra.

Si alguna de las clases presenta una cantidad insuficiente de observaciones, se reconsiderará la viabilidad del modelado predictivo.

### 6.3 Construcción del baseline

Se establecerá primero un baseline sencillo que permita conocer el rendimiento mínimo que debe superar un modelo predictivo.

Como referencia principal se utilizará la regresión logística.

También podrán utilizarse reglas sencillas basadas en el comportamiento histórico del cliente, por ejemplo, utilizando información de recencia o segmentación, cuando resulte adecuado.

El objetivo será evitar seleccionar un modelo complejo únicamente porque obtiene un resultado aparentemente bueno sin demostrar una mejora respecto a una alternativa sencilla.

### 6.4 Comparación de modelos candidatos

Cuando los datos sean suficientes, se compararán los modelos definidos en la sección anterior:

1. regresión logística;
2. Random Forest;
3. Gradient Boosting.

Todos los modelos se evaluarán utilizando las mismas particiones de datos y criterios de evaluación para permitir una comparación justa.

No se incorporarán modelos adicionales salvo que exista una justificación relacionada con las características de los datos o con una necesidad concreta del proyecto.

### 6.5 Prevención de fuga de información

Una parte fundamental del proceso será evitar que información futura llegue al conjunto de variables utilizado para realizar la predicción.

Las transformaciones que aprendan parámetros a partir de los datos, como escalado o imputación, se ajustarán únicamente utilizando los datos correspondientes al entrenamiento.

Las variables derivadas de las compras posteriores al momento de predicción no podrán utilizarse como variables de entrada.

De esta manera se busca evitar que el modelo obtenga información que no estaría disponible en una situación real.

### 6.6 Criterios para seleccionar el modelo

La selección del modelo no dependerá exclusivamente de una única métrica.

Se tendrán en cuenta:

* rendimiento predictivo;
* capacidad de generalización;
* comparación con el baseline;
* estabilidad de los resultados;
* complejidad;
* interpretabilidad;
* calidad y volumen de los datos;
* utilidad para la consultora.

En un problema de recompra será especialmente importante valorar la capacidad del modelo para identificar correctamente a los clientes con mayor probabilidad de recompra, sin generar un número excesivo de falsas prioridades.

### 6.7 Regla de selección final

El modelo final será seleccionado únicamente si demuestra una mejora suficientemente clara respecto al baseline y mantiene un comportamiento estable durante la validación.

Entre dos modelos con resultados similares se priorizará el modelo más sencillo e interpretable, siempre que cumpla los requisitos de rendimiento.

Por tanto, no se seleccionará automáticamente el modelo más complejo ni el que presente la métrica máxima en un único conjunto de datos.

### 6.8 Estrategia si el modelo no resulta adecuado

Si ninguno de los modelos candidatos supera de forma suficiente al baseline, o si el volumen de datos no permite realizar una validación fiable, no se considerará que exista un modelo predictivo válido.

En ese caso, el proyecto mantendrá como solución principal:

* análisis descriptivo;
* RFM;
* segmentación;
* reglas de priorización;
* dashboard.

La estrategia permitirá incorporar posteriormente un modelo predictivo cuando se disponga de un histórico de ventas suficiente y de una variable objetivo que pueda definirse y validarse correctamente.

## 7. Estrategia de validación y evaluación

La evaluación del modelo se diseñará teniendo en cuenta la naturaleza temporal del problema de predicción de recompra. El objetivo será comprobar si el modelo puede generalizar a clientes y periodos posteriores a los utilizados durante su entrenamiento.

La estrategia definitiva dependerá de la cantidad y profundidad temporal del histórico real disponible.

### 7.1 División de los datos

Siempre que exista suficiente histórico, se priorizará una división temporal de los datos.

La información más antigua se utilizará para entrenamiento y validación, mientras que un periodo posterior se reservará como conjunto de prueba final.

De esta forma se busca reproducir una situación real en la que el modelo utiliza información histórica para realizar predicciones sobre compras futuras.

No se utilizarán aleatoriamente datos futuros dentro del conjunto de entrenamiento cuando esto pueda generar información sobre el comportamiento posterior del cliente.

### 7.2 Entrenamiento y validación

El conjunto de entrenamiento se utilizará para ajustar los modelos candidatos.

Dentro de este conjunto se podrá utilizar validación cruzada cuando el volumen y la estructura temporal de los datos lo permitan.

En caso de que la naturaleza temporal de los datos haga más apropiada una estrategia basada en periodos, se utilizarán particiones temporales para evaluar la estabilidad del modelo.

Las transformaciones necesarias para preparar los datos se ajustarán únicamente con la información correspondiente al entrenamiento de cada partición.

### 7.3 Conjunto de prueba

Se reservará un conjunto de prueba que no será utilizado durante el entrenamiento ni para seleccionar el modelo.

Este conjunto representará información posterior y permitirá realizar una evaluación final del modelo seleccionado.

El resultado obtenido en este conjunto será utilizado para estimar de forma más realista el comportamiento esperado del modelo ante nuevos datos.

### 7.4 Prevención de fuga de información

Se prestará especial atención a la fuga de información.

Para cada predicción se garantizará que las variables de entrada se calculen únicamente con información disponible antes del momento de referencia.

Por ejemplo, si se quiere predecir la recompra después de una determinada fecha, no se podrán utilizar como variables de entrada compras realizadas posteriormente.

También se evitará calcular previamente estadísticas o transformaciones utilizando conjuntamente datos de entrenamiento y prueba.

### 7.5 Métricas de evaluación

La evaluación utilizará varias métricas para evitar depender de un único indicador.

Entre las métricas consideradas se encuentran:

* **Accuracy:** proporción total de predicciones correctas.
* **Precision:** proporción de clientes identificados como compradores que realmente realizan una recompra.
* **Recall:** proporción de los clientes que realmente recompran y que son identificados por el modelo.
* **F1-score:** equilibrio entre precision y recall.
* **ROC-AUC:** capacidad del modelo para distinguir entre clientes que realizan recompra y aquellos que no.

La métrica prioritaria se determinará según el objetivo comercial y la distribución de las clases observada en los datos.

Si existe un desequilibrio importante entre clientes que recompran y que no recompran, no se utilizará accuracy como único criterio de evaluación.

### 7.6 Comparación con el baseline

Los resultados de cada modelo se compararán con el baseline definido anteriormente.

La finalidad será comprobar si el modelo aporta una mejora real respecto a una estrategia sencilla.

Se registrarán las métricas obtenidas por cada alternativa y se analizarán las diferencias entre modelos.

Un modelo no se considerará adecuado únicamente por obtener una métrica elevada, sino por demostrar una mejora consistente y útil frente a la referencia.

### 7.7 Análisis de errores

Además de las métricas globales, se analizarán los errores del modelo.

Se estudiarán especialmente:

* falsos positivos: clientes clasificados como compradores que finalmente no recompran;
* falsos negativos: clientes que realizan una recompra pero no fueron identificados correctamente.

Este análisis permitirá valorar las consecuencias prácticas de los errores.

Por ejemplo, un falso positivo puede provocar que la consultora dedique tiempo a contactar a un cliente que finalmente no compre, mientras que un falso negativo puede representar una oportunidad comercial que no fue priorizada.

### 7.8 Criterio mínimo de aceptación

Antes de definir un umbral definitivo de aceptación se analizará el comportamiento del baseline y la distribución real de la variable objetivo.

El modelo deberá:

* superar de forma razonable al baseline;
* mantener resultados estables en los conjuntos de validación y prueba;
* evitar diferencias excesivas entre entrenamiento y prueba;
* mostrar un comportamiento coherente en el análisis de errores;
* y proporcionar un resultado que pueda utilizarse de forma práctica por la consultora.

No se establecerá un valor de métrica artificialmente alto como requisito previo si todavía no se conoce el volumen, distribución y dificultad real del problema.

### 7.9 Alternativa si el modelo no supera la validación

Si el modelo no consigue superar de forma suficiente al baseline, presenta un comportamiento inestable o los datos no permiten realizar una evaluación fiable, no se incorporará como componente principal del sistema.

En ese caso, se utilizará como solución analítica:

* segmentación RFM;
* reglas de priorización;
* indicadores comerciales;
* dashboard de seguimiento.

La predicción de recompra podrá quedar como una línea futura de desarrollo, condicionada a la incorporación de un histórico de transacciones más amplio y representativo.

## 8. Riesgos y alternativas

El principal riesgo del proyecto está relacionado con la disponibilidad y calidad del histórico real de transacciones. La existencia de un número elevado de clientes no garantiza por sí misma que exista información suficiente para desarrollar un modelo predictivo de recompra.

Por este motivo, los riesgos se analizarán antes de realizar el modelado y se establecerán alternativas para mantener la utilidad del proyecto aunque la predicción no resulte viable.

### 8.1 Insuficiencia de histórico de ventas

El riesgo principal es disponer de pocas transacciones fechadas, pocos clientes con compras repetidas o un periodo histórico demasiado corto.

Esto impediría construir de forma fiable la variable objetivo de recompra y podría provocar que un modelo aparentemente válido no generalizara correctamente a nuevos casos.

**Alternativa:**

Si el histórico no es suficiente, el proyecto se centrará en:

* CRM estructurado;
* análisis descriptivo;
* análisis RFM;
* segmentación de clientes;
* reglas de priorización;
* dashboard comercial.

La predicción de recompra se planteará como una ampliación futura cuando exista suficiente histórico real.

### 8.2 Definición de la recompra

Otro riesgo es no disponer de una definición suficientemente clara de qué se considera una recompra.

Para poder realizar un modelo supervisado será necesario establecer un momento de referencia y un horizonte temporal posterior dentro del cual se considere que el cliente ha vuelto a comprar.

**Alternativa:**

La definición se establecerá a partir del histórico real y se documentará antes de entrenar el modelo. Si los datos no permiten definir un horizonte con suficiente evidencia, no se utilizará la predicción como componente principal.

### 8.3 Desequilibrio entre clases

Puede existir una diferencia importante entre el número de clientes que realizan una recompra y los que no la realizan.

Un conjunto de datos muy desequilibrado puede hacer que determinadas métricas, especialmente accuracy, proporcionen una visión poco representativa del rendimiento.

**Alternativa:**

Se analizará la distribución de la variable objetivo y se utilizarán métricas como precision, recall, F1-score y ROC-AUC.

Si fuera necesario, se estudiarán estrategias apropiadas para tratar el desequilibrio, evitando generar artificialmente patrones que no representen el comportamiento real.

### 8.4 Calidad de los datos

Los datos pueden presentar:

* valores nulos;
* duplicados;
* formatos de fecha inconsistentes;
* categorías escritas de diferentes formas;
* valores atípicos;
* información incompleta de los perfiles;
* errores de identificación de clientes;
* falta de correspondencia entre clientes, productos y ventas.

Estos problemas pueden afectar tanto al análisis como al rendimiento de los modelos.

**Alternativa:**

Se realizará un proceso de validación y limpieza antes de generar las tablas Gold y antes del entrenamiento.

Los problemas que no puedan resolverse de forma fiable se documentarán y las variables afectadas podrán excluirse del análisis o modelado.

### 8.5 Fuga de información

Existe el riesgo de utilizar accidentalmente información posterior al momento en que se realiza la predicción.

Esto produciría resultados artificialmente buenos y no representativos de una situación real.

**Alternativa:**

Las variables predictoras se construirán exclusivamente con información disponible antes del momento de referencia y se utilizará una estrategia de validación temporal cuando el histórico lo permita.

### 8.6 Cambios en el comportamiento de compra

Los patrones de compra pueden cambiar con el tiempo debido a campañas comerciales, temporadas, cambios de productos o modificaciones en el comportamiento de los clientes.

Un modelo entrenado con información antigua podría perder capacidad predictiva cuando cambien estos patrones.

**Alternativa:**

Se analizará la evolución temporal de las compras y se comprobará el rendimiento del modelo sobre periodos posteriores.

Si se detecta una pérdida importante de rendimiento, se documentará como una limitación y se podrá plantear una actualización periódica del modelo cuando exista nuevo histórico.

### 8.7 Sesgo de cobertura

Los datos pueden representar únicamente una parte de los clientes o de las ventas de una consultora.

Por ejemplo, si determinadas compras o interacciones no quedan registradas, el comportamiento observado puede no representar completamente la actividad comercial.

**Alternativa:**

Se documentará el alcance real de los datos y no se generalizarán los resultados más allá de la población representada por el histórico disponible.

### 8.8 Privacidad y uso de datos reales

Los datos de clientes pueden contener información identificativa, como nombres o teléfonos.

El uso de estos datos requiere especial atención para evitar que información personal termine en el repositorio público o sea utilizada innecesariamente durante el análisis.

**Alternativa:**

Los datos utilizados en el repositorio público serán anonimizados y se utilizarán identificadores internos de cliente.

Los datos identificativos originales no formarán parte del conjunto de datos público utilizado para reproducir el proyecto.

### 8.9 Modelo que no supera al baseline

Existe la posibilidad de que ninguno de los modelos candidatos proporcione una mejora suficiente respecto al baseline.

En ese caso, incorporar un modelo predictivo añadiría complejidad sin aportar un beneficio demostrado.

**Alternativa:**

Se mantendrá como solución principal el enfoque analítico basado en:

**CRM → análisis descriptivo → RFM → segmentación → priorización → dashboard.**

La predicción de recompra quedará como una funcionalidad futura que podrá incorporarse cuando los datos permitan demostrar una mejora real.

### 8.10 Datos insuficientes para construir la capa Gold

También existe el riesgo de que determinados campos necesarios para construir las tablas Gold no estén disponibles en la fuente real.

Esto puede afectar especialmente a información como fechas de compra, productos, cantidades o importes.

**Alternativa:**

La capa Gold se construirá únicamente con información disponible y validada.

Si una entidad o variable no puede construirse con suficiente calidad, se documentará la limitación y se adaptará el alcance del análisis.

El proyecto priorizará una solución más sencilla pero respaldada por datos reales frente a una solución más compleja basada en supuestos o datos simulados.

### 8.11 Estrategia general ante los riesgos

La estrategia general será mantener un enfoque incremental.

El proyecto comenzará por los componentes que pueden sustentarse con los datos disponibles:

1. organización de la información de clientes;
2. estructuración del histórico de ventas cuando esté disponible;
3. análisis descriptivo;
4. RFM;
5. segmentación;
6. dashboard;
7. predicción de recompra, únicamente si los datos permiten definir, entrenar y validar el modelo correctamente.

De esta manera, la falta de datos suficientes para la predicción no invalida el proyecto completo, sino que limita de forma explícita el alcance de la parte predictiva.

El criterio principal será priorizar la **validez, trazabilidad y utilidad de los resultados** frente a la incorporación de modelos complejos sin suficiente evidencia.

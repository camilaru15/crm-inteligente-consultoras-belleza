# Entrega 02 - Selección de idea de proyecto y análisis de datos necesarios

## 1. Idea seleccionada

### Problema que resuelve

El proyecto seleccionado consiste en desarrollar un Sistema Inteligente de Seguimiento y Análisis de Ventas dirigido a consultoras de belleza. Actualmente, muchas consultoras gestionan la información de sus clientes mediante listas de contactos, hojas de cálculo o aplicaciones de mensajería, lo que dificulta realizar un seguimiento adecuado de las compras, identificar oportunidades de venta y mantener una comunicación personalizada con cada cliente. Esta situación puede generar pérdida de oportunidades comerciales, disminuir la fidelización y hacer que parte de las decisiones se basen principalmente en la experiencia personal y no en el análisis sistemático de los datos.

### Solución planteada

La propuesta consiste en desarrollar una plataforma que centralice la información de los clientes y sus compras, permitiendo analizar su comportamiento comercial. El sistema permitirá registrar clientes, productos, ventas e interacciones, consultar el historial de cada cliente, calcular indicadores de comportamiento y realizar segmentaciones que faciliten la toma de decisiones comerciales.

Como evolución del sistema, y únicamente si el histórico real disponible contiene suficientes transacciones y ejemplos de diferentes comportamientos de compra, se podrá desarrollar un modelo predictivo orientado a estimar la probabilidad de recompra. De esta forma, la utilización de técnicas de aprendizaje automático estará condicionada a la disponibilidad y calidad de los datos, evitando construir un modelo que no pueda generalizar a nuevos clientes.

### MVP del proyecto final

El Producto Mínimo Viable consistirá en una aplicación web capaz de registrar clientes y nuevas ventas, consultar el historial de compras, calcular indicadores comerciales mediante análisis RFM, segmentar clientes y visualizar los principales resultados mediante un dashboard interactivo.

El sistema estará diseñado para incorporar nuevos clientes y transacciones de forma continua, permitiendo que la base de datos crezca progresivamente.

La predicción de recompra se considerará una funcionalidad adicional del MVP únicamente si el análisis del histórico real demuestra que existe suficiente información para definir y validar el objetivo predictivo. En caso contrario, la predicción quedará como una funcionalidad futura, manteniendo como núcleo del proyecto el CRM, el análisis RFM, la segmentación y el dashboard.

---

# 2. Datos necesarios

Para desarrollar el proyecto será necesario trabajar con información relacionada con clientes, productos, transacciones e interacciones comerciales.

Actualmente se dispone de información básica de clientes y perfiles, pero los datos disponibles no contienen por sí solos un histórico completo de transacciones fechadas. Por este motivo, antes de desarrollar un modelo predictivo será necesario comprobar la disponibilidad y calidad del histórico real de compras.

## Información del cliente

Las principales variables previstas son:

* Identificador interno del cliente.
* Nombre, únicamente cuando sea necesario para la gestión interna y siempre anonimizado en la versión académica.
* Edad, cuando esté disponible y resulte pertinente.
* Ciudad.
* Tipo de piel.
* Tono de base.
* Fecha de registro.

Los números telefónicos y otros datos directamente identificativos no serán necesarios para los análisis y serán eliminados, anonimizados o sustituidos por identificadores internos en la versión académica.

## Información de productos

* Identificador del producto.
* Nombre o referencia del producto.
* Categoría.
* Precio.
* Cantidad disponible, cuando sea necesaria para la gestión comercial.
* Duración estimada del producto, cuando pueda obtenerse de una fuente fiable y sea relevante para el análisis de recompra.

## Información de las transacciones

Para analizar el comportamiento de compra será necesario disponer, como mínimo, de:

* Identificador de la transacción.
* Identificador del cliente.
* Fecha de compra.
* Producto adquirido.
* Categoría del producto.
* Cantidad comprada.
* Valor de la compra.

Estos datos permitirán reconstruir el historial de compras de cada cliente y calcular variables relacionadas con su comportamiento.

## Información de seguimiento e interacciones

Como información deseable se contempla:

* Fecha del último contacto.
* Medio de contacto.
* Tipo de interacción.
* Productos de interés.
* Respuesta a promociones o campañas.
* Observaciones comerciales no sensibles.

Estas variables podrán utilizarse posteriormente para enriquecer la segmentación y las recomendaciones de seguimiento.

## Variables derivadas

A partir de los datos anteriores se podrán calcular variables como:

* Número total de compras.
* Frecuencia de compra.
* Tiempo desde la última compra.
* Valor acumulado de compras.
* Ticket promedio.
* Número de categorías adquiridas.
* Categoría de producto más frecuente.
* Recencia.
* Frecuencia.
* Valor monetario.
* Segmento RFM.

En caso de disponer de suficiente histórico, también podrá definirse una variable objetivo relacionada con la recompra.

## Definición de recompra

Para utilizar la recompra como objetivo predictivo será necesario establecer una definición medible y adecuada al comportamiento real observado en los datos.

Se considerará recompra cuando un cliente realice una nueva compra después de una compra anterior dentro de un horizonte temporal previamente definido.

El horizonte temporal, por ejemplo 30, 60 o 90 días, no se establecerá arbitrariamente. Se determinará después de analizar los intervalos reales entre compras disponibles en el histórico.

Posteriormente se comprobará si existe un número suficiente de casos de clientes que realizan recompra y de clientes que no la realizan dentro del período seleccionado.

Si el histórico no contiene suficientes ejemplos de ambos comportamientos, no se considerará adecuado entrenar un modelo predictivo de recompra para el proyecto final.

### Granularidad

La unidad principal de análisis será la transacción de compra. Cada compra realizada por un cliente constituirá un registro independiente, permitiendo reconstruir el historial comercial de cada cliente.

Para determinados análisis también se utilizará una granularidad por cliente, agregando las transacciones para calcular variables como recencia, frecuencia y valor monetario.

### Profundidad histórica

La profundidad histórica dependerá de la información real disponible.

Actualmente se dispone principalmente de información de clientes y perfiles, por lo que será necesario comprobar qué histórico real de ventas puede recuperarse y digitalizarse.

La antigüedad del histórico será especialmente importante para determinar si existe información suficiente para estudiar los ciclos de compra y definir adecuadamente la variable de recompra.

Además del histórico disponible, la base de datos podrá crecer progresivamente mediante el registro de nuevas ventas e interacciones durante el desarrollo del proyecto.

### Volumen esperado

Actualmente se dispone de varios cientos de registros de clientes, pero este volumen no puede considerarse por sí mismo suficiente para entrenar un modelo de predicción de recompra.

El volumen útil para el modelo dependerá principalmente del número de transacciones fechadas, del número de clientes con varias compras y de la existencia de suficientes ejemplos de recompra y no recompra.

Por este motivo, antes de aplicar aprendizaje automático se realizará una auditoría del histórico disponible.

### Datos imprescindibles

Para el núcleo de análisis comercial:

* Identificador del cliente.
* Fecha de compra.
* Producto comprado.
* Cantidad.
* Valor de la compra.

Para la predicción de recompra, además, será imprescindible disponer de suficientes transacciones históricas fechadas y de información que permita determinar correctamente el resultado de recompra o no recompra.

### Datos deseables

* Edad.
* Ciudad.
* Tipo de piel.
* Tono de base.
* Preferencias.
* Historial de interacciones.
* Respuesta a campañas comerciales.
* Duración estimada de los productos.

---

# 3. Fuentes de datos previstas

La principal fuente de información será una base de datos propia procedente de la actividad comercial de una consultora independiente de productos de belleza.

Actualmente se dispone de:

* Una base de clientes.
* Información de contacto.
* Características del cliente, como tipo de piel y tono de base.
* Información de ciudad.

Estos datos constituyen el punto de partida para estructurar el CRM, pero no sustituyen a un histórico de transacciones.

La principal fuente que deberá completarse será el histórico real de ventas, incluyendo fechas, productos y valores de las transacciones. La disponibilidad de este histórico determinará la viabilidad de desarrollar la funcionalidad predictiva.

Durante el proyecto también podrán registrarse nuevas ventas e interacciones en una estructura de datos organizada, permitiendo que el sistema crezca progresivamente.

### Formato previsto

Los datos iniciales pueden encontrarse en formatos como Excel y CSV. Posteriormente se organizarán en una estructura de base de datos relacional para facilitar su consulta, actualización y análisis.

### Disponibilidad histórica

La disponibilidad del histórico de compras deberá ser comprobada antes de iniciar el modelado predictivo.

Se evaluarán:

* Número de transacciones disponibles.
* Fechas disponibles.
* Número de clientes con más de una compra.
* Intervalos entre compras.
* Porcentaje de registros incompletos.
* Existencia de casos de recompra y no recompra.

### Riesgos relacionados con las fuentes

* Algunos registros históricos pueden estar incompletos.
* Parte de las compras antiguas podrían no estar digitalizadas.
* Pueden existir inconsistencias entre clientes y transacciones.
* Puede ser necesario realizar procesos de limpieza y normalización.
* El histórico disponible puede no ser suficientemente amplio para desarrollar un modelo predictivo fiable.
* Los datos personales de clientes reales requieren medidas específicas de protección.

No se utilizarán datos simulados ni conjuntos de datos públicos de comercios de otro contexto para entrenar el modelo predictivo final, ya que sus patrones de compra podrían no representar adecuadamente el comportamiento de las consultoras de belleza.

---

# 4. Consideraciones de privacidad y protección de datos

El proyecto parte de información correspondiente a clientes reales, por lo que será necesario aplicar medidas de protección de datos durante todo el desarrollo.

En la versión académica del proyecto:

* Los nombres serán anonimizados o eliminados cuando no sean necesarios.
* Los números telefónicos serán eliminados o sustituidos por identificadores internos.
* No se publicará información que permita identificar directamente a los clientes.
* El repositorio público no contendrá datos personales reales.
* Los datos utilizados para demostraciones deberán estar anonimizados y, cuando sea necesario, podrán utilizarse datos de ejemplo únicamente para probar el funcionamiento técnico de la aplicación, sin utilizarlos para entrenar el modelo predictivo final.
* Los datos reales se utilizarán únicamente cuando exista autorización para su tratamiento con fines académicos.

También se evitará incorporar información personal que no sea necesaria para resolver el problema planteado.

Los principales riesgos éticos y legales están relacionados con la identificación de clientes, el uso no autorizado de información personal y la exposición de datos en el repositorio público.

---

# 5. Viabilidad inicial del proyecto

El proyecto es técnicamente viable porque existe una base inicial de clientes y perfiles que permite comenzar la construcción del CRM y estructurar el sistema de información.

Sin embargo, la viabilidad de la funcionalidad predictiva debe evaluarse de manera independiente. Disponer de varios cientos de clientes no implica disponer de suficientes observaciones para predecir la recompra.

Por este motivo, una de las primeras actividades del proyecto será realizar una auditoría del histórico real de transacciones para determinar:

* Cuántas transacciones fechadas existen.
* Cuántos clientes tienen compras repetidas.
* Cuánto tiempo transcurre entre compras.
* Qué horizonte temporal permite definir una recompra de forma razonable.
* Si existen suficientes ejemplos de recompra y no recompra.
* Si los datos tienen la calidad y completitud necesarias para el modelado.

Si el histórico demuestra que existe información suficiente, se podrá desarrollar y validar un modelo predictivo de recompra.

Si el histórico resulta limitado, el núcleo del proyecto será el CRM con registro estructurado de ventas, análisis RFM, segmentación de clientes y dashboard. La predicción de recompra quedará como una funcionalidad futura que podrá incorporarse cuando el sistema haya acumulado suficiente histórico real.

El principal riesgo del proyecto es, por tanto, la disponibilidad limitada de transacciones históricas. La estrategia para reducir este riesgo será diseñar desde el principio una estructura que permita incorporar nuevas ventas de manera continua, de modo que la base de datos pueda crecer progresivamente sin tener que rediseñar el sistema.

En conjunto, el proyecto resulta viable para el desarrollo académico siempre que el alcance se adapte a la evidencia proporcionada por los datos. El objetivo no será forzar la utilización de un modelo predictivo, sino demostrar que las técnicas de Ciencia de Datos utilizadas son adecuadas para la información realmente disponible.

# Entrega 2 - Selección de idea de proyecto y análisis de datos necesarios

## 1. Idea seleccionada

### Problema que resuelve

El proyecto seleccionado consiste en desarrollar un Sistema Inteligente para la Predicción de Recompras y Automatización del Seguimiento Comercial dirigido a consultoras de belleza. Actualmente, muchas consultoras gestionan la información de sus clientes mediante listas de contactos, hojas de cálculo o aplicaciones de mensajería, lo que dificulta realizar un seguimiento adecuado de las compras, identificar oportunidades de venta y mantener una comunicación personalizada con cada cliente. Esta situación genera pérdida de oportunidades comerciales, disminuye la fidelización y hace que gran parte de las decisiones se basen únicamente en la experiencia personal y no en el análisis de datos.

### Solución planteada

La propuesta consiste en desarrollar una plataforma que centralice la información de los clientes y utilice técnicas de Ciencia de Datos para analizar su comportamiento de compra. El sistema permitirá almacenar información de cada cliente, registrar compras e interacciones, segmentar clientes según sus características y construir un modelo predictivo capaz de estimar la probabilidad de recompra. Con esta información será posible generar recomendaciones y recordatorios personalizados, facilitando la toma de decisiones comerciales basadas en datos.

### MVP del proyecto final

El Producto Mínimo Viable consistirá en una aplicación web capaz de registrar clientes, almacenar el historial de compras, visualizar indicadores comerciales mediante un dashboard interactivo y ejecutar un modelo predictivo que estime qué clientes tienen mayor probabilidad de realizar una nueva compra. El sistema permitirá además generar recomendaciones de seguimiento comercial y estará diseñado para incorporar nuevos clientes y transacciones de forma continua, mejorando progresivamente el rendimiento de los modelos conforme aumente el volumen de información disponible.

---

# 2. Datos necesarios

Para desarrollar el proyecto será necesario trabajar con información relacionada con clientes, productos e historial de compras.

Las principales variables consideradas son:

## Información del cliente

- Identificador del cliente
- Nombre (anonimizado para el proyecto)
- Edad (cuando esté disponible)
- Ciudad
- Número telefónico (anonimizado)
- Tipo de piel
- Tono de base
- Fecha de registro

## Información comercial

- Fecha de compra
- Producto adquirido
- Categoría del producto
- Valor de la compra
- Cantidad comprada
- Método de pago
- Estado del pedido

## Información de seguimiento

- Fecha del último contacto
- Medio de contacto
- Respuesta a promociones
- Productos de interés
- Observaciones

## Variables derivadas

Durante el análisis también se calcularán variables como:

- Número total de compras
- Frecuencia de compra
- Tiempo desde la última compra
- Valor acumulado de compras
- Ticket promedio
- Probabilidad estimada de recompra

### Granularidad

La unidad de análisis será la transacción de compra. Cada compra realizada por un cliente constituirá un registro independiente, permitiendo reconstruir el historial completo de cada cliente.

### Profundidad histórica

Inicialmente se utilizará la información histórica disponible de clientes y posteriormente la base de datos crecerá de manera continua incorporando nuevos clientes, compras e interacciones registradas durante el desarrollo del proyecto.

### Volumen esperado

Actualmente se dispone de una base inicial de varios cientos de clientes reales. A medida que avance el proyecto se espera ampliar el conjunto de datos mediante nuevos registros y datos históricos de ventas, alcanzando un volumen suficiente para aplicar técnicas de segmentación y modelos predictivos.

### Datos imprescindibles

- Identificador del cliente
- Fecha de compra
- Producto comprado
- Valor de la compra

### Datos deseables

- Edad
- Ciudad
- Tipo de piel
- Preferencias
- Historial de interacciones
- Respuesta a campañas comerciales

---

# 3. Fuentes de datos previstas

La principal fuente de información será una base de datos propia obtenida durante la actividad comercial de una consultora independiente de productos de belleza.

Actualmente se dispone de:

- Base de clientes.
- Información de contacto.
- Características del cliente (tipo de piel, tono de base, entre otras).
- Registros comerciales que servirán como punto de partida para construir el histórico de compras.

Durante el proyecto esta información será enriquecida mediante el registro continuo de nuevas ventas e interacciones.

Además, podrán utilizarse conjuntos de datos públicos relacionados con ventas minoristas para validar técnicas de análisis o comparar resultados, siempre que sean compatibles con el objetivo del proyecto.

Los datos serán almacenados inicialmente en formato Excel y CSV y posteriormente migrados a una base de datos relacional para facilitar su gestión.

### Riesgos identificados

- Algunos registros históricos pueden estar incompletos.
- Parte de las compras antiguas podrían no estar digitalizadas.
- Será necesario realizar procesos de limpieza y normalización de los datos.
- El modelo predictivo requerirá suficiente histórico de compras para alcanzar un buen rendimiento.

---

# 4. Consideraciones de privacidad y protección de datos

El proyecto utilizará información correspondiente a clientes reales, por lo que se adoptarán medidas para garantizar la protección de datos personales.

En la versión académica:

- Los nombres serán anonimizados.
- Los números telefónicos serán eliminados o sustituidos por identificadores internos.
- No se publicará información que permita identificar personas.
- El repositorio únicamente contendrá datos anonimizados o sintéticos cuando sea necesario.

El tratamiento de la información tendrá exclusivamente fines académicos y de investigación.

---

# 5. Viabilidad inicial del proyecto

La viabilidad del proyecto se considera alta, ya que se dispone de una base inicial de clientes reales que permitirá comenzar el desarrollo sin depender exclusivamente de fuentes externas.

La calidad de los datos deberá mejorarse mediante procesos de limpieza, normalización y enriquecimiento progresivo conforme se registren nuevas compras e interacciones. Este crecimiento continuo constituye una de las principales fortalezas del proyecto, ya que permitirá que los modelos predictivos mejoren su capacidad conforme aumente el volumen de información disponible.

El principal riesgo identificado es la limitada disponibilidad de un histórico amplio de compras durante las primeras etapas del desarrollo. Como alternativa, se contempla complementar el entrenamiento inicial mediante datos simulados o conjuntos de datos públicos de ventas, siempre diferenciándolos claramente de la información real utilizada en el sistema.

En conjunto, el proyecto resulta viable desde el punto de vista técnico y de disponibilidad de datos, y puede desarrollarse de manera realista durante el curso, incorporando nuevas funcionalidades y mejorando sus modelos de forma incremental.
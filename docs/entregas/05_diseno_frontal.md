# Entrega 5 - Diseño del frontal y experiencia de usuario

## 1. Resumen de la solución y del usuario

El proyecto **CRM Inteligente para Consultoras de Belleza** tiene como objetivo facilitar la gestión y el seguimiento de clientes mediante la centralización de la información disponible y la incorporación progresiva de análisis sobre el comportamiento comercial.

El usuario principal es la **consultora de belleza**, que necesita consultar de forma rápida la información de sus clientes, conocer sus características y preferencias y utilizar estos datos para organizar mejor el seguimiento comercial.

La necesidad principal que aborda el frontal es facilitar tareas como:

- localizar un cliente;
- consultar su información y características;
- filtrar clientes según diferentes atributos;
- identificar clientes que requieren seguimiento;
- consultar los análisis disponibles;
- realizar acciones sobre el cliente, como programar un seguimiento, enviar un mensaje, registrar una compra o añadir una nota.

El producto se plantea como una **aplicación web operativa de tipo CRM**, complementada con capacidades analíticas y, cuando los datos disponibles lo permitan, funcionalidades de segmentación y predicción.

El resultado principal para la consultora será disponer de una visión organizada de su cartera de clientes que le permita pasar de la consulta de información a una acción concreta de seguimiento.

Actualmente los datos disponibles contienen información de perfil de los clientes, como ciudad, tipo de piel y tono de base, pero no incluyen un histórico de ventas suficientemente estructurado para construir todavía un modelo fiable de predicción de recompra. Por este motivo, las funcionalidades relacionadas con historial de compras, RFM y predicción se representan en el mockup como funcionalidades futuras o condicionadas a la disponibilidad de datos de ventas.

---

## 2. Imagen mockup del frontal

El siguiente mockup representa la pantalla principal propuesta para el CRM Inteligente.

![Mockup del frontal](/assets/05_mockup_frontal.png)

La pantalla principal se ha diseñado siguiendo una estructura orientada a la operación diaria de la consultora.

En la parte superior se encuentra el buscador general y la información de la usuaria. En el lateral izquierdo se sitúa la navegación principal de la aplicación.

La zona central presenta el resumen de clientes y la tabla de clientes, incluyendo opciones de búsqueda y filtrado. La zona derecha contiene el **Asistente inteligente**, que contextualiza la información del cliente seleccionado y presenta los análisis disponibles y las acciones que puede realizar la consultora.

El diseño también diferencia visualmente entre funcionalidades disponibles con los datos actuales y funcionalidades futuras que requieren información adicional. De esta forma, el historial de compras, RFM y la predicción de recompra aparecen como funcionalidades condicionadas a la disponibilidad de un histórico de ventas.

---

# 3. Justificación del diseño

## 3.1. Utilidad y valor de la solución

El frontal está diseñado para resolver una necesidad operativa concreta: **facilitar a la consultora la consulta, organización y seguimiento de su cartera de clientes**.

La información disponible actualmente puede encontrarse dispersa entre diferentes fuentes y formatos. Centralizarla en una única interfaz permite reducir el tiempo necesario para localizar información y facilita que la consultora pueda utilizar los datos disponibles antes de realizar una acción comercial.

La pantalla principal prioriza la información que resulta más útil para la actividad diaria:

- número de clientes registrados;
- número de perfiles con información disponible;
- ciudades;
- tipos de piel registrados;
- listado de clientes;
- características principales del cliente seleccionado;
- análisis disponibles;
- acciones de seguimiento.

Esta información se ha priorizado frente a otros elementos más técnicos que no son necesarios para la actividad cotidiana de la consultora.

Por ejemplo, no se muestran directamente métricas técnicas del modelo, variables internas o información de implementación. Estos elementos podrían formar parte de una vista técnica o de detalle si en fases posteriores se desarrolla un modelo predictivo.

El diseño busca convertir la información en una acción. Por ejemplo, la consultora puede seleccionar un cliente, consultar sus características y, desde el mismo frontal, realizar acciones como:

- **Programar seguimiento**
- **Enviar mensaje**
- **Registrar compra**
- **Añadir nota**

De esta manera, el análisis y la información disponible no quedan separados de la actividad comercial, sino que sirven como apoyo para decidir qué hacer a continuación.

---

## 3.2. Flujo de usuario

El flujo principal previsto para la consultora es el siguiente:

### 1. Punto de entrada

La usuaria accede al CRM y encuentra un resumen de su cartera de clientes.

La pantalla inicial muestra información general y permite identificar rápidamente el estado de la cartera.

### 2. Búsqueda o selección

La consultora puede localizar un cliente utilizando el buscador o consultar directamente el listado.

También puede utilizar filtros por atributos disponibles, como:

- ciudad;
- tipo de piel;
- tono de base;
- segmento.

### 3. Consulta del cliente

Una vez seleccionado un cliente, el frontal muestra su información disponible y sus principales características.

La información se presenta de forma resumida para evitar que la consultora tenga que revisar diferentes fuentes.

### 4. Procesamiento y análisis

El sistema utiliza la información estructurada disponible para mostrar los análisis que pueden realizarse en ese momento.

Con los datos actuales se pueden utilizar principalmente características de perfil y segmentaciones basadas en la información disponible.

Las funcionalidades que requieren histórico de compras quedan condicionadas a la incorporación de datos de ventas.

### 5. Resultado

El resultado para la consultora es una visión contextualizada del cliente seleccionado y de los análisis disponibles.

El panel de asistencia inteligente resume la información relevante y ayuda a identificar las posibles acciones siguientes.

### 6. Acción

A partir de la información mostrada, la consultora puede:

- programar un seguimiento;
- enviar un mensaje;
- registrar una compra;
- añadir una nota.

Estas acciones permiten conectar directamente la consulta de información con la gestión comercial.

### 7. Excepciones

Si faltan datos de un cliente, el sistema deberá indicarlo de forma clara en lugar de completar la información de manera automática sin evidencia.

Si una funcionalidad necesita información que todavía no existe, como el histórico necesario para calcular RFM o predecir la recompra, se mostrará como no disponible y se indicará el motivo.

Si en el futuro se incorpora un modelo predictivo y este no dispone de suficiente información o presenta una confianza insuficiente, el sistema deberá evitar presentar la predicción como una certeza y podrá mostrar que el resultado no es concluyente.

---

## 3.3. Experiencia de usuario

### Jerarquía visual

La interfaz utiliza una jerarquía clara para que la consultora pueda identificar rápidamente:

1. dónde se encuentra dentro del CRM;
2. qué clientes tiene disponibles;
3. qué cliente está seleccionado;
4. qué información puede consultar;
5. qué acciones puede realizar.

La información operativa se sitúa en el centro de la pantalla, mientras que el panel lateral derecho concentra la asistencia y las acciones.

### Simplicidad

Se evita mostrar una gran cantidad de métricas o información técnica en la pantalla principal.

La intención es que la consultora pueda utilizar el sistema sin necesidad de conocimientos específicos de Data Science o Machine Learning.

La información técnica más detallada se podría reservar para vistas específicas de análisis.

### Legibilidad y consistencia

Se utilizan componentes visuales consistentes para botones, filtros, tarjetas, etiquetas y estados.

Los diferentes colores utilizados en etiquetas y estados permiten distinguir visualmente situaciones como clientes activos, potenciales o inactivos.

Los botones utilizan textos descriptivos para que la acción sea comprensible sin depender únicamente de iconos.

### Contexto y confianza

La aplicación diferencia entre información disponible y funcionalidades que todavía requieren datos adicionales.

En particular, el mockup no presenta una probabilidad de recompra como si fuese un resultado disponible actualmente.

La predicción de recompra se plantea como una funcionalidad futura que solamente se incorporará cuando exista suficiente histórico real de transacciones y ejemplos adecuados para entrenar y validar el modelo.

### Control del usuario

La consultora mantiene el control sobre las acciones propuestas.

El asistente puede mostrar sugerencias, pero la decisión final de realizar una acción corresponde a la usuaria.

Las acciones como enviar un mensaje, registrar una compra o programar un seguimiento deben ser iniciadas o confirmadas por la consultora.

### Feedback del sistema

El frontal incluye estados visuales para indicar información disponible, funcionalidades condicionadas y acciones.

En una futura implementación se incorporarán también mensajes de confirmación, indicadores de carga y mensajes de error comprensibles para informar al usuario sobre el resultado de sus acciones.

### Accesibilidad y adaptación

La interfaz utiliza textos claros, botones diferenciados y una estructura visual consistente.

La implementación final deberá adaptar el diseño a diferentes tamaños de pantalla, manteniendo especialmente accesibles las funciones de búsqueda, consulta y seguimiento.

---

# 4. Presentación de resultados y explicabilidad

El resultado principal del frontal será inicialmente una **visión organizada y contextualizada de cada cliente**, complementada con los análisis que puedan realizarse a partir de los datos disponibles.

En la situación actual, estos resultados pueden incluir:

- información del perfil;
- características registradas;
- segmentación basada en la información disponible;
- indicadores generales de la cartera.

Cuando exista un histórico de ventas suficientemente completo, el producto podrá incorporar progresivamente:

- historial de compras;
- análisis RFM;
- segmentación basada en comportamiento de compra;
- predicción de recompra.

En el caso de incorporar un modelo predictivo, el resultado no se mostrará únicamente como una etiqueta o una probabilidad aislada. Se acompañará de contexto que permita interpretar el resultado y conocer sus limitaciones.

La aplicación deberá diferenciar entre:

- información observada en los datos;
- resultados calculados mediante análisis;
- estimaciones realizadas por un modelo.

De esta manera, una predicción será presentada como una **estimación**, no como una certeza.

También se evitará utilizar una predicción para justificar automáticamente una acción comercial. La consultora podrá revisar la información disponible y decidir si realiza o no el seguimiento propuesto.

## IA generativa como capa de explicación

La IA generativa no forma parte de la funcionalidad predictiva actual del mockup.

Si se incorpora posteriormente como parte del asistente inteligente, su función será principalmente **resumir o explicar información y resultados previamente obtenidos por el sistema**.

Las explicaciones generadas deberán basarse exclusivamente en datos y resultados disponibles dentro del CRM. No deberán inventar causas, características o comportamientos que no estén respaldados por los datos.

La IA generativa se utilizaría, por tanto, como una capa de interacción y explicación y no como sustituto del análisis estadístico o del modelo predictivo.

---

# 5. Alcance del MVP

El MVP se plantea de forma progresiva para mantener un alcance realista y coherente con los datos disponibles.

### Funcionalidades que forman parte del núcleo del MVP

- Gestión y consulta de clientes.
- Visualización de información de perfil.
- Búsqueda de clientes.
- Filtros por características disponibles.
- Visualización de información de la cartera.
- Registro y consulta de características de clientes.
- Estructuración de los datos para futuras funcionalidades analíticas.
- Interfaz orientada al seguimiento comercial.

### Elementos representados visualmente en el mockup

El mockup representa además funcionalidades que forman parte de la evolución prevista del producto:

- asistente inteligente;
- historial de compras;
- análisis RFM;
- predicción de recompra;
- recomendaciones basadas en comportamiento de compra.

Estas funcionalidades aparecen diferenciadas porque requieren disponer de un histórico de ventas real y suficientemente estructurado.

### Tecnología prevista

Para la implementación final se prevé utilizar una aplicación web conectada con la capa de datos y análisis desarrollada durante el proyecto.

La arquitectura podrá integrar:

- Python para el procesamiento y análisis de datos;
- una base de datos o almacenamiento estructurado para la información del CRM;
- herramientas de visualización y/o una aplicación web para el frontal;
- modelos de Machine Learning cuando exista suficiente histórico de ventas;
- una capa de IA generativa únicamente si aporta una utilidad concreta y puede mantenerse la trazabilidad con los datos y resultados del sistema.

El mockup representa, por tanto, la visión funcional del producto final, mientras que la implementación del MVP se limitará a las funcionalidades que puedan desarrollarse y validarse de forma realista con los datos disponibles.

El objetivo es que el sistema pueda evolucionar desde un CRM estructurado y útil para la gestión diaria hacia funcionalidades analíticas y predictivas a medida que se disponga de un histórico comercial suficiente.
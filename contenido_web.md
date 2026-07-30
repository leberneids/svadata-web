# Contenido de la web — SVA Data

> **Cómo funciona:** edita cualquier texto de este documento (los valores, no las etiquetas en negrita tipo `**Titular:**`). Cuando acabes, dile a Claude «aplica contenido_web.md» y volcará los cambios al `index.html`. Las secciones van en el mismo orden que la página. Lo que está marcado _(vacío)_ es un hueco que puedes rellenar o dejar vacío.

---

> **Páginas:** la web tiene dos páginas — `index.html` (portada: secciones 1–7) y `servicios.html` (¿Quién somos? + Cómo empezamos + Contacto). El botón «Servicios» de la navegación lleva a la segunda.

## Barra de navegación _(igual en las dos páginas)_

- **Enlace 1:** ¿Qué hacemos? _(lleva a la sección «Qué hacemos» de la portada)_
- **Enlace 2:** Servicios _(lleva a servicios.html)_
- **Botón:** Hablemos

---

## 1 · Hero (portada)

- **Chip superior:** El Hub de Datos de Planta
- **Titular (dos líneas fijas):** Todos tus datos `[palabra rotatoria]` ⏎ en un solo sitio.
- **Palabras rotatorias** _(en negrita, navy)_**:** operativos · de planta · de máquinas · de sensores · de órdenes de producción · mantenimiento · calidad
- **Subtitular (lead):** En tiempo real, con histórico, y listo para decidir.
- **Párrafo:** Conecta cada máquina y cada sistema **una sola vez**, y usa esos datos donde hacen falta: en la pantalla de planta, en dashboards, Excel, la IA. Un **Hub de Datos de Planta**, un sitio, todos tus datos, ordenados.
- **Botón primario:** Cómo empezamos
- **Botón secundario:** Ver por qué

**Etiquetas del diagrama (cajas alrededor de SVA):**
ERP · Máquinas · Sensores · Robots · MES · Agentes de IA · Calidad · Histórico

- **Caja central:** SVA — Todos tus datos en un sitio.

### Tres pilares (debajo del hero)

1. **Sin tocar nada** — Extraemos los datos de las máquinas y los sistemas que ya tienes. No cambiamos tu forma de trabajar.
2. **Todos tus datos, en un solo sitio** — _(vacío)_
3. **Toma decisiones, cada mes. Mide los cambios en los procesos, busca órdenes defectuosas, relaciona defectos de calidad con sensores…** — Cada mes, con los datos delante, te ayudamos a extraer el valor de tus datos.

---

## 2 · Cita

> «Los sistemas de control hacen funcionar las máquinas. Nosotros hacemos funcionar las decisiones.»

---

## 3 · El problema

- **Eyebrow:** El problema
- **Titular:** Diferentes softwares para cada departamento: ERP, MES, MOM, SCADA, mantenimiento.
- **Párrafo:** Cada software tiene su función, pero la analítica nunca se ha hecho dentro de los softwares. Hay que extraer los datos, ordenarlos, unirlos — si no, la información se pierde en un exporte, un Excel, la memoria de alguien. Finanzas dice una cosa, producción otra, mantenimiento otra, calidad otra — y nadie sabe cuál es la verdad.

**Diagrama «Hoy» (cajas):** ERP · MES · Excels · Máquinas · Sensores · Calidad
**Diagrama «Con SVA» (cajas):** ERP · MES · Calidad · Máquinas · Sensores · Robots — centro: SVA, una sola capa, tuya

- **Pie de sección:** **Conecta una vez. Decide siempre.** Cada fuente se conecta una sola vez a la capa — y cualquier pregunta se responde cruzándolas todas.

---

## 4 · En lo que creemos

- **Eyebrow:** En lo que creemos

1. **Visualizar lo que ocurre en tu planta puede abrirte los ojos.** — Tu gestión sabe lo que debería pasar; tus máquinas, lo que pasa.
2. **Tus datos ya existen. Están encerrados.** — Cada ERP, cada MES, MOM, SCADA intentan encerrarte. ¿Por qué no un sitio donde acceder a todo?
3. **Un panel de números no gana dinero.** — Una decisión a tiempo, sí. Por eso no entregamos un dashboard y nos vamos: lo trabajamos contigo, cada mes — somos tu equipo de analítica.
4. **Medir no debería ser un proyecto.** — Nada de implantaciones de meses: en marcha en semanas, sin parar producción y sin cambiar cómo trabaja tu gente.

---

## 5 · Qué hacemos

- **Eyebrow:** Qué hacemos
- **Titular:** Capturamos los datos de tu empresa y los convertimos en decisiones.
- **Párrafo:** Tu fábrica ya genera datos por el simple hecho de trabajar. No son una sola cosa: son cuatro familias, y cada una se captura distinto, se guarda distinto y responde a una pregunta distinta. Mezclarlas es donde descarrila la mayoría de proyectos de datos — en la primera reunión:

### Las cuatro familias de datos

1. **01 · Máquina (MDE)** — **Lo que hace la máquina**
   Ciclos, estados, tiempos de marcha, paros, velocidades, códigos de alarma.
   _Fuente:_ Sale del control (CNC, PLC), de señales digitales o de un servidor OPC UA — sin tocar nada.
2. **02 · Operación (BDE)** — **Lo que se está fabricando**
   Estado de las órdenes, fichaje de operario, consumo de material, motivos de paro.
   _Fuente:_ Sale del terminal de planta, del lector de códigos — o del apunte del operario.
3. **03 · Proceso** — **En qué condiciones**
   Temperaturas, presiones, pares de apriete, caudales, dimensiones.
   _Fuente:_ Sale de sensores, equipos de medida y galgas en línea — los que ya tienes o los que añadimos.
4. **04 · Calidad** — **Cómo salió**
   Resultados de inspección, categorías de defecto, mediciones SPC.
   _Fuente:_ Sale de la tridimensional (CMM), sistemas de visión, controles manuales, laboratorio.

### Banda azul (cruce)

- **Título:** El valor no está en recoger — está en cruzar.
- **Texto:** Una parada (máquina) + la orden que corría (operación) + la temperatura de ese rato (proceso) + el lote que salió mal (calidad), sobre la misma línea de tiempo. Ahí aparece la causa — y el euro. Eso es lo que montamos.

### Línea de cierre

- **Pregunta:** ¿Por qué hoy no se aprovechan?
- **Motivos:** Cada dato vive en su silo · Nada apunta a la orden de trabajo · Se apuntan a mano, tarde y a trozos · Nadie es dueño del conjunto

---

## 6 · Integración de datos

- **Eyebrow:** Integración de datos
- **Titular:** Nos conectamos a todo lo que ya tienes — y extraemos los datos.
- **Párrafo:** Máquinas, sensores, calidad, logística, tu ERP y tu MES: todo acaba en una sola base de datos unificada. Y de ahí salen los casos de uso.

**Fuentes (columna izquierda del diagrama):**

- Máquinas — estado · ciclos · paradas
- Sensores — temperatura · consumo
- Control de calidad — medidas · defectos
- RFID / código de barras — lote · trazabilidad
- Packaging — formato · conteo
- (píldoras arriba) ERP · MES 

**Centro del diagrama:** Hub de Datos de Planta — base de datos unificada

**Casos de uso (panel derecho):**

1. Conectividad de planta
2. OEE y visibilidad de producción
3. Gestión energética
4. Chat de IA con tus datos
5. Trazabilidad de lote y calidad
6. Integración planta · ERP
7. Integración máquina · MES

- **Pie de sección:** **Cada fuente se ordena para que todos los datos estén en el mismo sitio.** Los casos de uso se activan por fases — empezando por el que más te duele.

---

## 7 · Tu Excel (ilustración «Obtener datos»)

- **Eyebrow:** Sin aprender nada nuevo
- **Titular:** Abres Excel, le das a «Obtener datos» — y ahí está tu planta.
- **Párrafo:** El hub no es un programa cerrado: es una **base de datos estándar**. Cualquier herramienta que sepa leer una — Excel, Power BI, tu ERP — ve las mismas tablas: producción, paradas, energía, calidad. Sin exportes, sin esperar a que alguien te pase el informe.

**Ilustración (Navegador):**

- **Base de datos:** sva_planta
- **Tablas:** produccion · paradas · alarmas · energia · calidad
- **Vistas:** v_oee_turno (seleccionada) · v_paradas_pareto · v_consumo_energia
- **Nota bajo la vista previa:** 1.248 filas · actualizado hace 2 min

- **Pie de sección:** **El mismo número para todos.** La tabla que gestión abre en su Excel es la misma que alimenta el dashboard de planta — actualizada sola, sin copiar y pegar.

---

## 9 · ¿Quién somos? _(en servicios.html)_

- **Eyebrow:** ¿Quién somos?
- **Titular:** Somos tu equipo de datos, experto en fabricación — por menos de lo que cuesta un data analyst.
- **Sub-eyebrow:** Tres partes

1. **01 · El pipeline — Pipelines de datos probados en grandes multinacionales**
   Datos en tiempo real, histórico y datos de empresa — sin tocar nada de lo que funciona.
2. **02 · El acceso — Un sitio donde tu equipo accede a los datos**
   Jefes de producción, calidad, logística: un solo sitio, una verdad — sin extraer datos de aquí y de allí para cruzarlos.
3. **03 · Las sesiones — Sesiones semanales y mensuales**
   Análisis y automatización sobre tus datos: qué pasó, qué tocar — y qué dio lo del mes pasado.

- **Banda de cierre:** _(vacío)_

---

## 8 · Cómo empezamos _(en servicios.html)_

- **Eyebrow:** _(vacío)_
- **Titular:** No te pedimos que nos creas: medimos.
- **Píldora (precio):** 1.000 € · un mes
- **Párrafo:** Cada fábrica tiene su problema: paradas, merma, calidad, energía. Investigamos y generamos dashboards, informes automatizados, alarmas, bases de datos donde acceder a tus datos — y al cabo de un mes decides.

### Los cuatro pasos

1. **Día 1–2 — Miramos tu fábrica**
   Qué te duele y dónde están los datos: máquinas, ERP, calidad, energía — lo que haya.
2. **Semana 1 — Tus datos, juntos**
   Un sitio donde acceder a todos tus datos — todo junto, por primera vez. Solo lectura: no tocamos nada.
3. **Día 30 — Tu número** _(tarjeta destacada en azul)_
   Observamos: dashboards, avisos, exportes — la visualización de los análisis. Medido, no estimado.
4. **La decisión — ¿Te gusta? Seguimos**
   Y si no, el informe te lo quedas igual.

- **Pie de sección:** **El informe trae dos cosas:** lo que ya hemos encontrado en tus datos, y la analítica que esos datos permiten a partir de aquí — qué preguntas podrás responder si seguimos.


---

## 10 · Contacto _(en servicios.html)_

- **Titular:** ¿Quieres saber tu número?
- **Párrafo:** Un mes con tus datos, 1.000 €, y decides con el número delante. El informe te lo quedas, sigas o no.
- **Botón:** Escríbenos

---

## Pie de página

- **Nombre:** Lluís Barnadas
- **Rol:** Ingeniero de procesos · lluis.barnadas@svaservice.es
- **Línea legal:** © 2026 SVA Data
- **Lema:** Tu planta, tus datos.

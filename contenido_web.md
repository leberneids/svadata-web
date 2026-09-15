# Contenido de la web — svadata.com

Edita aquí cualquier texto y dile a Claude **«aplica contenido_web.md»**: lo vuelca al
HTML. No hace falta tocar código.

**Reglas de este fichero**

1. Si el HTML y este fichero discrepan, **gana el HTML**. Este documento se actualiza en el
   **mismo commit** que el HTML, nunca en uno posterior — la versión anterior llevaba meses
   desincronizada (numeración 7→9→8, palabras del rotor que ya no existían, etiquetas de un
   diagrama sustituido) y dejó de ser fiable.
2. Cada apartado lleva **el `id` real de la sección** entre paréntesis, para poder localizar
   la deriva con `grep`.
3. El repositorio `svadata-web` es **público**. No escribas aquí nombres de clientes,
   precios negociados ni estrategia.

---

## Barra de navegación

- **Enlaces:** Producto (`index.html#modulos`) · Servicios (`servicios.html`)
- **Botón:** Hablemos → correo

---

## 1 · Hero (`header.hero`)

- **Chip:** El Hub de Datos de Planta
- **Titular:** Todos tus datos *[palabra que rota]* en un solo sitio.
- **Palabras que rotan** (las define el `<script>` al final de `index.html`, 5 en total):
  operativos · de máquinas · de sensores · de órdenes · de mantenimiento
- **Entradilla:** En tiempo real, con histórico, y lista para decidir.
- **Párrafo:** Conectamos tus máquinas, tus sensores y tu ERP a **una sola base de datos**.
  Tu equipo la ve en el portal, en los tableros y en su propio Excel.
- **Botón primario:** Ver el producto → `#producto`
- **Botón secundario:** Cómo empezamos → `servicios.html#empezamos`
- **Línea de datos:** Siete protocolos de máquina · una base de datos · lectura, nunca escritura.
- **Ilustración:** la isométrica de la planta. **Generada** por `assets/build_hero_iso.py`
  — no se edita a mano, se regenera.

**Tres columnas:**

| Título | Texto |
|---|---|
| Sin tocar nada | Leemos el control. No cambiamos el programa, ni la red, ni cómo trabaja tu gente. |
| Todo en un sitio | Máquina, proceso, calidad y ERP sobre la misma línea de tiempo. |
| Cada mes, contigo | Una sesión al mes con los datos delante: qué cambió y qué tocar. |

---

## 2 · El problema (`#problema`)

- **Eyebrow:** El problema
- **Titular:** Diferentes softwares para cada departamento: ERP, MES, MOM, SCADA, mantenimiento.
- **Párrafo:** Cada uno resuelve lo suyo y guarda sus datos donde le conviene. Nadie cruza la
  parada con la orden que corría, ni el defecto con la temperatura de ese rato. La respuesta
  acaba en un exporte, un Excel y la memoria de alguien.
- **Diagrama:** dos columnas, «Hoy» (todo conectado con todo) y «Con SVA» (todo contra una
  capa). Etiquetas: ERP · MES · Excels · Máquinas · Sensores · Calidad · Robots; caja central
  **SVA / una sola capa, tuya**.
- **Pie:** **Conecta una vez. Decide siempre.** Cada fuente entra una sola vez — y cualquier
  pregunta se responde cruzándolas todas.

---

## 3 · El producto (`#producto`)

- **Eyebrow:** El producto
- **Titular:** Esto es lo que ve tu gente el lunes a las seis.
- **Párrafo:** El portal es una web dentro de la red de la planta: sin instalar nada en los
  puestos, sin licencia por usuario, y sin escribir jamás en el control.
- **Captura:** `portal-planta.webp`
- **Pie (obligatorio, no quitar):** **Capturas reales del portal con datos sintéticos**
  (CNC-01…CNC-08, septiembre de 2026). El producto es el que ves; los números de estas
  capturas, no.

> El pie es la condición para poder enseñar capturas: son del producto real, con datos
> inventados. Si algún día se enseñan datos de un cliente, hace falta su permiso por escrito.

---

## 4 · Cinco piezas (`#modulos`)

- **Eyebrow:** Cómo está hecho
- **Titular:** Cinco piezas.
- **Párrafo:** Cada una responde una pregunta distinta y todas leen la misma base de datos.
  No son módulos que se compren por separado: es un solo sistema, y la interfaz que aparece
  aquí es la que se instala.

### 01 · Conectar
- **Frase:** Cada máquina, cada señal, en la misma base de datos.
- **Texto:** Leemos el control directamente: FANUC por FOCAS, DMG MORI por MTConnect, OPC UA,
  Modbus TCP, S7, robots FANUC y Universal Robots. Un colector por planta, a 1 Hz, solo lectura.
- **Etiquetas:** Máquina (MDE) · Operación (BDE) · Proceso · Calidad
- **Diagrama:** fuentes → base de datos → casos de uso. La lista de casos de uso del dibujo
  es: Conectividad de planta · OEE y visibilidad de producción · Gestión energética · Chat de
  IA con tus datos · Trazabilidad de lote y calidad · Integración planta · ERP · Desgaste de
  herramienta.

### 02 · Supervisar
- **Frase:** La nave entera en una pantalla, cada diez segundos.
- **Texto:** Planta dibuja tu croquis real: estado, programa en curso, husillo y horas en
  marcha. Las alarmas se agrupan por máquina y, sobre todo, por las que se repiten.
- **Nota:** La utilización se mide contra las **horas de turno declaradas**, no contra el
  reloj: una máquina que produce sola de madrugada puede pasar del 100 %, y ese es justo el
  dato que buscas.
- **Captura:** `portal-alarmas.webp`

### 03 · Analizar
- **Frase:** Dónde se fue el tiempo, con el denominador a la vista.
- **Texto:** Reparto del tiempo, día a día, top de paros, ciclos, override y desgaste de
  herramienta. Los informes semanales y mensuales se generan solos.
- **Nota:** Los paros se **miden** solos; el motivo todavía lo pones tú. La captura por
  operario en planta está en el backlog, no en el producto.
- **Capturas:** `portal-analisis.webp` y `portal-herramientas.webp`
- **Pie:** **El cambio de plaquita no lo anuncia el control.** Lo deducimos del salto en el
  corrector de la herramienta cuando el operario la vuelve a medir — y de ahí sale la vida
  típica y el aviso antes de que falle.

### 04 · Integrar
- **Frase:** Es una base de datos, no un programa cerrado.
- **Texto:** Las mismas tablas que ve el portal las abre tu Excel o tu Power BI, con un rol de
  solo lectura. Sin exportes y sin copiar y pegar.
- **Nota:** Y tu **ERP** entra en el mismo sitio: órdenes, artículos y lotes sobre la misma
  línea de tiempo que la máquina. Cruzar la orden con lo que hizo la máquina es lo que
  convierte los datos en euros.
- **Diagrama:** la maqueta de Excel abriendo «Obtener datos» contra la base de datos.

### 05 · Preguntar
- **Frase:** Tus datos, tus planos y tus pautas, en el mismo índice.
- **Texto:** Preguntas en castellano sobre tu propia planta. Las pautas, los manuales y las
  hojas de proceso se indexan junto a la telemetría, así que la respuesta cita la máquina y
  la orden de las que sale.
- **Nota:** El conocimiento que hoy vive en la cabeza de dos personas pasa a estar donde
  cualquiera puede preguntarlo — y sigue siendo tuyo, dentro de tu base de datos.
- **Diagrama:** documentos + histórico + órdenes → índice único → respuesta citada.

### Banda de cierre de la sección
- **Título:** El valor no está en recoger — está en cruzar.
- **Texto:** Una parada, la orden que corría y la temperatura de ese rato son tres datos
  sueltos. Juntos, sobre la misma línea de tiempo, son la respuesta a por qué se paró.

---

## 5 · La instalación (`#estado`)

- **Eyebrow:** La instalación
- **Titular:** Una caja, una base de datos, una puerta.
- **Párrafo:** Todo corre dentro de tu planta. No hay nube obligatoria, no hay agente en los
  PC de nadie, y ningún dato sale de tu red si tú no quieres.

| # | Título | Texto |
|---|---|---|
| 01 · En la planta | Un mini-PC industrial | Del tamaño de un libro, en el armario. Habla con los controles por la red que ya tienes y no toca la configuración de ninguna máquina. |
| 02 · Los datos | Una base de datos estándar | PostgreSQL con extensión de series temporales. Un año de histórico, y un usuario de solo lectura para todo lo que consulte. |
| 03 · El acceso | Una sola puerta | El portal y los tableros se abren desde cualquier navegador de tu red, con certificado. Ningún otro servicio queda expuesto. |

**Cifras** (sustituyen al caso de éxito que todavía no se puede enseñar; todas verificables
en el repositorio del producto):

| Cifra | Texto |
|---|---|
| 1 Hz | sondeo al control, sin cargarlo |
| 10 s | refresco de la vista de planta |
| 365 días | de histórico en la caja |
| 0 | escrituras al control, por diseño |

---

## 6 · Cierre (`#empezar`)

- **Banda:** Tu planta, tus datos, tu base de datos.
- **Botón primario:** Ver una demo del portal → correo
- **Botón secundario:** Cómo empezamos → `servicios.html#empezamos`

---

## Pie de página

- Lluís Barnadas · Ingeniero de procesos · correo
- © 2026 SVA Data · Tu planta, tus datos.

---

# Página «Servicios» (`servicios.html`)

## ¿Quién somos? (`#quien-somos`)
- **Titular:** Somos tu equipo de datos, experto en fabricación — por menos de lo que cuesta
  un data analyst.
- **Tres partes:** 01 · El pipeline · 02 · El acceso · 03 · Las sesiones

## Cómo empezamos (`#empezamos`)
- **Titular:** No te pedimos que nos creas: medimos.
- **Precio:** 1.000 € · un mes
- **Pasos:** Día 1–2 Miramos tu fábrica · Semana 1 Tus datos, juntos · Día 30 Tu número ·
  La decisión ¿Te gusta? Seguimos
- **Captura:** `portal-informe.webp`
- **Pie:** El informe trae dos cosas: lo que ya hemos encontrado en tus datos, y la analítica
  que esos datos permiten.
- **Banda:** Un panel de números no gana dinero. Lo que lo gana es la decisión que sale de él.

## Contacto (`#contacto`)
- **Titular:** ¿Quieres saber tu número?
- **Botones:** Ver una demo del portal · Escríbenos

---

# Capturas

Todas se regeneran con **un comando**, contra el portal real con datos sintéticos:

```bash
~/.venvs/web-fetch/bin/python assets/build_shots.py
```

El runbook completo (levantar el stack, sembrar los datos) está en
`02_Projects/00_Guias/03_desplegar_web_svadata.md`.

| Fichero | Origen | Dónde aparece |
|---|---|---|
| `portal-planta.webp` | `/planta`, recorte `.page` | `#producto` |
| `portal-alarmas.webp` | `/alarmas` | módulo 02 |
| `portal-analisis.webp` | `/analisis?p=mes` | módulo 03 |
| `portal-herramientas.webp` | `/maquinas/cnc-01?vista=herramientas&p=30`, recorte a la tabla | módulo 03 |
| `portal-informe.webp` | `/informes` | `servicios.html` |
| `og-planta.png` | `/planta`, 1200×630 | `og:image` de las dos páginas |

**Sello de fecha:** el pie de `#producto` dice «septiembre de 2026». Cuando se regeneren las
capturas, actualiza el mes — así se ve si están viejas en lugar de disimularlo.

---

# Afirmaciones y su estado

Lo que la web promete, y qué hay detrás. Mantener esta tabla al día es lo que permite escribir
con seguridad: si algo baja de categoría, el texto cambia **antes** que la conversación con el
cliente.

| Afirmación en la web | Estado |
|---|---|
| FANUC por FOCAS, DMG MORI por MTConnect, robots FANUC y Universal Robots | En producción — hay un colector para cada uno |
| OPC UA | En producción, vía UMH Core |
| Modbus TCP · S7 | Soportados por la capa de conexión; **todavía sin desplegar en cliente** |
| Planta, Alarmas, Análisis, Informes | En producción |
| Vida y desgaste de herramienta | En producción |
| Excel / Power BI contra la base de datos | En producción |
| El motivo de cada paro | **No**: se mide el paro, no la causa. La web lo dice explícitamente |
| Integración con el ERP | Diseñada; primera implantación en curso |
| Preguntar en castellano (módulo 05) | **En desarrollo** — decidido presentarlo como capacidad; no hay pantalla que enseñar todavía |

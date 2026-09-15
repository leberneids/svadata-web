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
4. **No se habla de bases de datos, protocolos ni de cómo está hecho por dentro.** Lo que se
   vende es el portal: lo que el cliente ve y decide con ello. La única «base de datos» que
   queda en la página es la del menú de Excel, porque es el menú real de Excel.

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
- **Párrafo:** Máquinas, sensores y ERP en **un solo sitio**. Tu equipo lo ve en el portal,
  en los tableros y en su propio Excel.
- **Botón primario:** Ver el producto → `#producto`
- **Botón secundario:** Cómo empezamos → `servicios.html#empezamos`
- **Línea de datos:** En vivo y con histórico · sin instalar nada en los puestos · sin tocar tus máquinas.
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
- **Párrafo:** Cada uno guarda sus datos donde le conviene, y nadie cruza la parada con la
  orden que corría. La respuesta acaba en un exporte, un Excel y la memoria de alguien.
- **Diagrama:** dos columnas, «Hoy» (todo conectado con todo) y «Con SVA» (todo contra una
  capa). Etiquetas: ERP · MES · Excels · Máquinas · Sensores · Calidad · Robots; caja central
  **SVA / una sola capa, tuya**.
- **Pie:** **Conecta una vez. Decide siempre.** Cada fuente entra una vez; cualquier pregunta
  se responde cruzándolas todas.

---

## 3 · El producto (`#producto`)

- **Eyebrow:** El producto
- **Titular:** Esto es lo que ve tu gente el lunes a las seis.
- **Párrafo:** Una web dentro de la red de la planta: sin instalar nada en los puestos, sin
  licencia por usuario, y sin escribir jamás en el control.
- **Captura:** `portal-planta.webp`
- **Sin pie.** (Retirado el 2026-09-15: las capturas son del producto real con datos de
  demostración, como las de cualquier software.)

> Lo que sí sigue en pie: las capturas **nunca** llevan datos de un cliente. Se generan
> contra el taller sintético. Enseñar los de un cliente exigiría su permiso por escrito.

---

## 4 · Cinco piezas (`#modulos`)

- **Eyebrow:** Cómo está hecho
- **Titular:** Cinco piezas.
- **Párrafo:** Cada una responde una pregunta distinta y todas miran los mismos datos. No se
  compran por separado: la interfaz que ves aquí es la que se instala.

### 01 · Conectar
- **Frase:** Cada máquina, cada señal, en el mismo sitio.
- **Texto:** Tus máquinas, tengan los años que tengan, y los sistemas que ya usas. Sin tocar
  programas, sin tocar la red y sin que nadie apunte nada a mano.

> **Sin lista de protocolos, a propósito** (2026-09-15). Aquí se vende el portal, no la
> fontanería. La pregunta «¿te conectas a mi máquina?» se responde en la visita, no en la web.
- **Etiquetas:** Máquina (MDE) · Operación (BDE) · Proceso · Calidad
- **Diagrama:** fuentes → el hub → casos de uso. La lista de casos de uso del dibujo
  es: Conectividad de planta · OEE y visibilidad de producción · Gestión energética · Chat de
  IA con tus datos · Trazabilidad de lote y calidad · Integración planta · ERP · Desgaste de
  herramienta.

### 02 · Supervisar
- **Frase:** La nave entera en una pantalla, cada diez segundos.
- **Texto:** Tu croquis real: estado, programa en curso, husillo y horas en marcha. Las
  alarmas, agrupadas por máquina y por las que se repiten.
- **Nota:** La utilización va contra las **horas de turno declaradas**, no contra el reloj:
  una máquina que produce sola de madrugada pasa del 100 %.
- **Captura:** `portal-alarmas.webp`

### 03 · Analizar
- **Frase:** Dónde se fue el tiempo, con el denominador a la vista.
- **Texto:** Reparto del tiempo, día a día, top de paros, ciclos, override y desgaste de
  herramienta. Los informes se generan solos.
- **Nota:** Los paros se **miden** solos; el motivo todavía lo pones tú.
- **Capturas:** `portal-analisis.webp` y `portal-herramientas.webp`
- **Sin pie.** El *cómo* se deduce el cambio de plaquita **no se cuenta en la web**: se ve el
  resultado en la captura y ya. Es nuestro, no material de marketing.

### 04 · Integrar
- **Frase:** Tus datos salen cuando los necesitas.
- **Texto:** Lo mismo que ves en el portal lo abres en tu Excel o en tu Power BI, actualizado
  solo. Sin exportes y sin copiar y pegar.
- **Nota:** Tu **ERP** entra en el mismo sitio: órdenes, artículos y lotes sobre la línea de
  tiempo de la máquina. Cruzar la orden con lo que hizo la máquina es lo que convierte datos
  en euros.
- **Diagrama:** la maqueta de Excel abriendo «Obtener datos» contra tus datos de planta.

### 05 · Preguntar
- **Frase:** Tus datos, tus planos y tus pautas, en el mismo índice.
- **Texto:** Preguntas en castellano. Las pautas, los manuales y las hojas de proceso se
  indexan junto a la telemetría, así que la respuesta cita la máquina y la orden.
- **Diagrama:** documentos + histórico + órdenes → índice único → respuesta citada.

### Banda de cierre de la sección
- **Título:** El valor no está en recoger — está en cruzar.
- **Texto:** Una parada, la orden que corría y la temperatura de ese rato son tres datos
  sueltos. Juntos, sobre la misma línea de tiempo, son la respuesta a por qué se paró.

---

## 5 · La instalación (`#estado`)

- **Eyebrow:** La instalación
- **Titular:** Una caja en tu planta, y poco más.
- **Párrafo:** Todo se queda dentro de tu nave. Sin nube obligatoria.

| # | Título | Texto |
|---|---|---|
| 01 · En la planta | Un mini-PC industrial | Habla con los controles por la red que ya tienes, sin tocar su configuración. |
| 02 · Los datos | Un año de histórico | Todo lo que pasa queda guardado y es tuyo, sin que nadie tenga que apuntarlo. |
| 03 · El acceso | Una sola puerta | Portal y tableros desde cualquier navegador de tu red, y nada más expuesto. |

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

- **Banda:** Tu planta, tus datos, en un solo sitio.
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
| FANUC por FOCAS, DMG MORI por MTConnect, robots FANUC y Universal Robots | En producción — pero **no se nombran en la web** (2026-09-15) |
| OPC UA | En producción, vía UMH Core — tampoco se nombra |
| Modbus TCP · S7 | Soportados por la capa de conexión; **todavía sin desplegar en cliente** |
| Planta, Alarmas, Análisis, Informes | En producción |
| Vida y desgaste de herramienta | En producción |
| Excel / Power BI contra los datos de planta | En producción |
| El motivo de cada paro | **No**: se mide el paro, no la causa. La web lo dice explícitamente |
| Integración con el ERP | Diseñada; primera implantación en curso |
| Preguntar en castellano (módulo 05) | **En desarrollo** — decidido presentarlo como capacidad; no hay pantalla que enseñar todavía |

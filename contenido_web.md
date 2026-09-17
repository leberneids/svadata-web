# Contenido de la web — svadata.com

Edita aquí cualquier texto y dile a Claude **«aplica contenido_web.md»**: lo vuelca al
HTML. No hace falta tocar código.

**Reglas de este fichero**

1. Si el HTML y este fichero discrepan, **gana el HTML**. Este documento se actualiza en el
   **mismo commit** que el HTML, nunca en uno posterior — la versión anterior llevaba meses
   desincronizada y dejó de ser fiable.
2. Cada apartado lleva **el `id` real de la sección** entre paréntesis, para poder localizar
   la deriva con `grep`.
3. El repositorio `svadata-web` es **público**. No escribas aquí nombres de clientes,
   precios negociados ni estrategia.
4. **No se habla de bases de datos, protocolos ni de cómo está hecho por dentro.** Lo que se
   vende es el portal: lo que el cliente ve y decide con ello. La única «base de datos» que
   queda en la página es la del menú de Excel, porque es el menú real de Excel.
5. **Una sola página** (2026-09-17). La web se envía a clientes por correo y tiene que
   leerse de arriba abajo en cinco minutos. `servicios.html` ya no existe como página: es
   una redirección a `/#empezamos` para no romper enlaces antiguos. La estructura de venta
   es la misma que el deck «Tres niveles» de `04_Teams/04_Sales/`: Ver · Cruzar · Preguntar.
   No inventar otra nomenclatura (ni siglas de producto): un cliente que ve la web y luego
   el deck tiene que reconocer lo mismo.

---

## Barra de navegación

- **Enlaces:** Producto (`#niveles`) · Empezar (`#empezamos`)
- **Botón:** Hablemos → correo

---

## 1 · Hero (`header.hero`)

- **Chip:** El Hub de Datos de Planta
- **Titular:** Todos tus datos *[palabra que rota]* en un solo sitio.
- **Palabras que rotan** (las define el `<script>` al final de `index.html`, 5 en total):
  operativos · de máquinas · de sensores · de órdenes · de mantenimiento
- **Entradilla:** Sabe qué pasa en tu planta ahora mismo, y cuánto te cuesta.
  *(Es la portada del deck: vende resultado, no lugar. Sustituye a «En tiempo real, con
  histórico, y lista para decidir».)*
- **Párrafo:** Máquinas, sensores y ERP en **un solo sitio**. Tu equipo lo ve en el portal,
  en los tableros y en su propio Excel.
- **Botón primario:** Ver el producto → `#producto`
- **Botón secundario:** Cómo empezamos → `#empezamos`
- **Línea de datos:** En vivo y con histórico · sin instalar nada en los puestos · sin tocar tus máquinas.
- **Ilustración:** la isométrica de la planta. **Generada** por `assets/build_hero_iso.py`
  — no se edita a mano, se regenera.

> **Fuera los tres pilares** bajo el hero (2026-09-17): decían lo mismo que la sección
> «Sin riesgo». Cada garantía se dice una vez.

---

## 2 · El problema (`#problema`)

- **Eyebrow:** El problema
- **Titular:** Un software por departamento, y nadie cruza los datos.
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
- **Sin pie.** Las capturas son del producto real con datos de demostración; **nunca** llevan
  datos de un cliente. Enseñar los de un cliente exigiría su permiso por escrito.

---

## 4 · Tres niveles (`#niveles`)

Sustituye a «Cinco piezas» (2026-09-17). Las piezas no desaparecen: son las viñetas de
cada nivel. Cambio de modelo, no solo de texto: antes la web decía «no se compran por
separado»; ahora **se contrata por niveles y cada uno incluye el anterior**, igual que en el
deck.

- **Eyebrow:** Tres niveles
- **Titular:** Empiezas viendo tu planta, sigues sabiendo cuánto te cuesta y acabas
  preguntando a tus datos.
- **Párrafo:** Se contrata por niveles y cada uno incluye el anterior. Nadie empieza por el
  tercero.

Cada nivel tiene la misma anatomía: etiqueta · título · **para quién** · texto · lista ·
nota honesta · **la pregunta que responde** · figura.

### Nivel 1 · Ver (`#nivel-1`)
- **Título:** Tu planta, en directo.
- **Para quién:** Para quien hoy no sabe qué hacen sus máquinas si no está delante.
- **Texto:** Nos conectamos a tus máquinas, tengan los años que tengan, y montamos tu centro
  de control. Sin tocar programas, sin tocar la red y sin que nadie apunte nada a mano.
- **Lista:**
  - La nave entera en una pantalla: qué produce, qué está parado y desde cuándo.
  - Histórico de marchas y paradas por máquina: reparto del tiempo y top de paros.
  - Las alarmas de todas las máquinas en una sola pantalla, agrupadas por máquina y por las que se repiten.
  - Vida y desgaste de herramienta, máquina a máquina.
  - Informes semanales y mensuales que llegan solos.
  - Tus datos en tu Excel con «Obtener datos», siempre al día.
- **Nota:** Los paros se **miden** solos; el motivo todavía lo pones tú.
- **Pregunta:** ¿Qué está pasando y cuánto tiempo pierdo?
- **Figuras:** `portal-analisis.webp` y, debajo, la maqueta de Excel abriendo «Obtener
  datos» contra tus datos de planta.

> **Sin lista de protocolos, a propósito.** Aquí se vende el portal, no la fontanería. La
> pregunta «¿te conectas a mi máquina?» se responde en la visita, no en la web.

### Nivel 2 · Cruzar (`#nivel-2`)
- **Título:** Planta y gestión: el coste real.
- **Para quién:** Para quien tiene ERP o MES y quiere que los números de planta y de
  oficina cuadren.
- **Texto:** ¿Ya tienes ERP? Se queda donde está: lo leemos. Órdenes, referencias y
  materiales entran sobre la línea de tiempo de la máquina.
- **Lista:**
  - Todo lo del nivel 1.
  - Tiempo real de máquina por orden de fabricación.
  - Ciclo real frente al del escandallo, por referencia.
  - Coste por pieza real y margen por referencia.
  - Lo que cuesta cada parada, en euros.
  - El informe que hoy montáis exportando de tres sistemas, hecho solo.
- **Nota:** Cada ERP es distinto: el primer cruce con un ERP nuevo lleva su tiempo.
- **Pregunta:** ¿Cuánto me cuesta de verdad cada pieza?
- **Figura:** tabla «Margen por referencia», marcada **«Ejemplo ilustrativo · datos
  inventados»** (las mismas cinco filas del deck). Es tabla y no captura porque la
  integración con el ERP todavía no tiene pantalla que enseñar. Fila destacada REF-0875:
  «tarda un 55 % más de lo previsto: cada pieza que sale pierde dinero».

> **Nunca escribir aquí «planificación», «gestión de operaciones» ni «pronósticos».** Eso es
> la definición de un MES; SVA lee el MES y el ERP, no los sustituye ni planifica.

### Nivel 3 · Preguntar (`#nivel-3`)
- **Título:** Tu asistente de planta.
- **Para quién:** Para quien ya tiene sus datos ordenados y quiere respuestas sin esperar a
  un informe.
- **Texto:** ERP, MES, calidad, herramientas y almacén entran en el mismo sitio, con
  histórico. Preguntas en castellano y la respuesta cita la máquina y la orden.
- **Lista:**
  - Todo lo del nivel 2.
  - Preguntas en lenguaje normal, cuando las necesitas.
  - Las pautas, los manuales y las hojas de proceso, indexados junto a los datos.
  - Cada respuesta te enseña de dónde sale el número.
- **Nota:** La IA solo responde bien si los datos de debajo están ordenados. Por eso es el
  nivel 3, y no el 1.
- **Pregunta:** ¿Qué quiero saber hoy?
- **Figura:** diagrama documentos + histórico + órdenes → índice único → respuesta citada.

### Banda de cierre de la sección
- **Título:** El valor no está en recoger — está en cruzar.
- **Texto:** Una parada, la orden que corría y la temperatura de ese rato son tres datos
  sueltos. Juntos, sobre la misma línea de tiempo, son la respuesta a por qué se paró.

---

## 5 · Sin riesgo (`#sin-riesgo`)

Funde los antiguos «tres pilares» del hero, «La instalación» y «Las sesiones» de la
página de servicios. Cada garantía, una vez.

- **Eyebrow:** Sin riesgo
- **Titular:** Una caja en tu planta, y poco más.
- **Párrafo:** Un mini-PC industrial en la red que ya tienes, con un año de histórico
  dentro. Todo se queda en tu nave, sin nube obligatoria.

| # | Título | Texto |
|---|---|---|
| 01 · No tocamos nada | Solo leemos | No programamos tus máquinas, no cambiamos tu red ni tus sistemas, y nunca escribimos en el control. |
| 02 · Tus datos son tuyos | Viven en tu planta | Los ves desde cualquier navegador de tu red, y nada más queda expuesto. Si un día lo dejas, te los quedas. |
| 03 · Cada mes, contigo | Una sesión con los datos delante | Un ingeniero de procesos revisa los números contigo: qué cambió y qué tocar. |

> **Fuera la fila de cifras** (1 Hz · 10 s · 365 días · 0 escrituras), 2026-09-17: eran
> «cómo está hecho», y la regla 4 lo prohíbe. «Un año de histórico» y «nunca escribimos en
> el control» sobreviven como texto.

---

## 6 · Cómo empezamos (`#empezamos`)

Venía de `servicios.html`; ahora está en la página principal.

- **Titular:** No te pedimos que nos creas: medimos.
- **Píldora:** Un mes  *(sin precio: no se publican precios)*
- **Párrafo:** Cada fábrica tiene su problema: paradas, merma, calidad, energía. Ponemos la
  caja en tus máquinas clave, te dejamos montados los tableros y los informes, y
  al cabo de un mes decides.
- **Pasos:**
  - Día 1–2 · Miramos tu fábrica · Qué te duele y dónde están los datos: máquinas, ERP,
    calidad, energía. Lo que haya.
  - Semana 1 · Tus datos, juntos · Tus máquinas en directo y un sitio donde verlo todo junto,
    por primera vez. Solo lectura: no tocamos nada.
  - Día 30 · Tu número *(destacado)* · Un informe con lo que hemos encontrado en tus datos.
    Medido, no estimado.
  - La decisión · ¿Te gusta? Seguimos · Y si no, el informe te lo quedas igual.
- **Captura:** `portal-informe.webp`
- **Pie:** El informe trae dos cosas: lo que ya hemos encontrado en tus datos, y las
  preguntas que podrás responder si seguimos.

> **Nada de precios en la web** (2026-09-15). Ni cifras, ni rangos, ni «desde». El precio se
> habla en la visita, con la fábrica delante.

---

## 7 · Contacto (`#contacto`)

- **Titular:** ¿Quieres saber tu número?
- **Párrafo:** Un mes con tus datos, y decides con el número delante. El informe te lo quedas, sigas o no.
- **Botones:** Ver una demo del portal · Escríbenos (los dos → correo)

---

## Pie de página

- Lluís Barnadas · Ingeniero de procesos · correo
- © 2026 SVA Data · Tu planta, tus datos.

---

# Lo que se quitó el 2026-09-17 y por qué

| Fuera | Por qué |
|---|---|
| Página `servicios.html` («Quién somos» + «Cómo empezamos») | Una sola página que se pueda enviar. «Cómo empezamos» pasa a la principal; «Quién somos» era otra forma de decir lo de «Sin riesgo». Queda una redirección. |
| Sección «Cinco piezas» | Sustituida por «Tres niveles», la misma estructura que el deck. Las piezas son ahora viñetas. |
| Diagrama «fuentes → hub → casos de uso» (pieza 01) | Repetía el diagrama de «El problema» con más palabras. |
| Capturas `portal-alarmas.webp` y `portal-herramientas.webp` | Una captura por nivel; alarmas y herramientas quedan como viñetas del nivel 1. Los ficheros se conservan y se siguen regenerando. |
| Etiquetas «Máquina (MDE) · Operación (BDE) · Proceso · Calidad» | Jerga. |
| Tres pilares del hero | Duplicaban «Sin riesgo». |
| Fila de cifras (1 Hz, 10 s, 365 días, 0) | Cómo está hecho. |
| Banda «Tu planta, tus datos, en un solo sitio» + botones al final | Duplicaba el contacto. |
| Banda «Un panel de números no gana dinero…» | Bonita, pero una banda más antes del contacto. |

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
| `portal-analisis.webp` | `/analisis?p=mes` | nivel 1 |
| `portal-informe.webp` | `/informes` | `#empezamos` |
| `portal-alarmas.webp` | `/alarmas` | *(no se usa en la web desde 2026-09-17; se conserva)* |
| `portal-herramientas.webp` | `/maquinas/cnc-01?vista=herramientas&p=30`, recorte a la tabla | *(ídem)* |
| `og-planta.png` | `/planta`, 1200×630 | `og:image` |

---

# Afirmaciones y su estado

Lo que la web promete, y qué hay detrás. Mantener esta tabla al día es lo que permite escribir
con seguridad: si algo baja de categoría, el texto cambia **antes** que la conversación con el
cliente.

| Afirmación en la web | Estado |
|---|---|
| FANUC por FOCAS, DMG MORI por MTConnect, robots FANUC y Universal Robots | En producción — pero **no se nombran en la web** |
| OPC UA | En producción, vía UMH Core — tampoco se nombra |
| Modbus TCP · S7 | Soportados por la capa de conexión; **todavía sin desplegar en cliente** |
| Planta, Alarmas, Análisis, Informes (nivel 1) | En producción |
| Aviso de alarmas de máquina al móvil o al correo | **No existe** (2026-09-17): lo único que avisa al móvil es la salud de la caja (ntfy), y avisa a SVA, no al cliente. Por eso la web **no lo promete**; el borrador de copy del 16-09 lo decía y se quitó |
| Vida y desgaste de herramienta (nivel 1) | En producción |
| Excel / Power BI contra los datos de planta (nivel 1) | En producción |
| El motivo de cada paro | **No**: se mide el paro, no la causa. La web lo dice explícitamente |
| Cruce con el ERP: tiempo por orden, ciclo real vs escandallo, coste por pieza, margen (nivel 2) | Diseñado; **primera implantación en curso**. La figura es una tabla de ejemplo, no una captura, por eso |
| Coste de cada parada en euros (nivel 2) | Sale del cruce anterior más una tarifa hora del cliente; misma situación |
| Preguntar en castellano (nivel 3) | **En desarrollo** — se presenta como capacidad; no hay pantalla que enseñar todavía |

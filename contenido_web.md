# Contenido de la web — svadata.com

Edita aquí cualquier texto y dile a Claude **«aplica contenido_web.md»**: lo vuelca al
HTML. No hace falta tocar código.

**Reglas de este fichero**

1. Si el HTML y este fichero discrepan, **gana el HTML**. Se actualiza en el **mismo commit**
   que el HTML, nunca en uno posterior.
2. Cada apartado lleva **el `id` real de la sección** entre paréntesis, para localizar la
   deriva con `grep`.
3. El repositorio `svadata-web` es **público**. Ni nombres de clientes, ni precios, ni
   estrategia.
4. **No se habla de bases de datos, protocolos ni de cómo está hecho por dentro.** Se vende
   lo que el cliente ve y decide con ello.
5. **Nada de precios.** Ni cifras, ni rangos, ni «desde». El precio se habla en la visita.
6. **Una sola página.** `servicios.html` es una redirección a `/#empezamos`; por eso la
   sección de cierre lleva ese `id` y no se le puede cambiar.

---

## Dirección visual (2026-09-28)

«Plano técnico»: **franjas alternas azul / blanco** en vez de una página oscura continua.
Sustituye a la dirección oscura del 2026-09-22 (commit `c5a798f`).

- Azul `#0B1B4D` (hero `#071235`), acento `#2F5BFF` y **ámbar `#FFB020` solo para señalar**:
  marcadores, cotas y llamadas, nunca superficies. Sigue rompiendo la regla de marca
  «monocromo navy sin acento»; `07_SVA_brand_design/` todavía describe la identidad anterior.
- Display en **Source Serif**, cuerpo en **Plus Jakarta Sans**, etiquetas y todo lo que es
  dato en **JetBrains Mono**.
- Las **maquetas del portal van dibujadas en SVG**, no capturadas: nítidas a cualquier
  tamaño. El marco lleva la paleta de la web; **los estados de máquina llevan los colores
  del portal real** (verde en marcha, azul en espera, amarillo pausa, naranja inactiva, rojo
  parada, gris sin señal). Si el portal cambia de colores, se cambian aquí.

---

## Barra de navegación

- **Enlaces:** Plataforma (`#plataforma`) · Producto (`#producto`) · Soluciones (`#usos`) ·
  Sectores (`#sectores`)
- **Botón:** Hablemos → correo

---

## 1 · Hero (`#top`)

- **Chip:** Hub de datos de planta
- **Titular:** Deja de suponer. / Empieza a ver.
  *(Dos golpes cortos, registro publicitario. Sustituye a «Todos tus datos operativos en un
  solo sitio», que era una descripción, no un titular.)*
- **Párrafo:** Un solo sitio donde entra todo lo que pasa en tu fábrica y del que sale
  cualquier respuesta que necesites.
  *(Las metaetiquetas `og:description` y el JSON-LD conservan la versión larga, con
  «máquinas, calidad, órdenes, energía».)*
- **Botones:** Ver la plataforma → `#plataforma` · Pedir una demo → correo
- **Diagrama:** esquema de izquierda a derecha. **Ocho fuentes** a la izquierda (Máquinas ·
  Sensores · Calidad · Órdenes · Mantenimiento · Energía · Almacén · Operarios), **SVA** en
  el centro con su resplandor, y cinco salidas a la derecha (Planta en vivo · Análisis ·
  Informes · Excel · Power BI · IA para tu planta). Cables curvos; solo se mueven los pulsos.
- **Fuera del esquema, a propósito (2026-09-28):** la lista Fuentes / Refresco / Histórico /
  Escrituras, el «recoge · guarda · escribe» de la caja, la cota «8 fuentes · 1 sitio ·
  cualquier respuesta», la llamada «01 — en tu nave», los puntos fijos y todo el ámbar.
- **Fondo:** resplandor azul difuminado detrás del esquema.

> El mensaje ya no es «monitorizamos máquinas» sino **«somos el sitio donde entra todo»**.
> Por eso desapareció la isométrica con las CNC.

---

## 2 · Cinta de fabricantes

- **Etiqueta:** Nos conectamos a lo que ya tienes
- **Nombres:** FANUC · Siemens · Heidenhain · Mitsubishi · Fagor · Okuma · DMG MORI · Mazak ·
  Haas · Doosan · Hurco · Brother · Universal Robots · ABB · KUKA · Omron · Beckhoff ·
  Allen-Bradley

> **Nombres en tipografía, nunca sus logos.** Son marcas registradas: usarlas sugiere que
> esas empresas te respaldan. Si algún día hay acuerdo de partner firmado, entonces sí — y
> con su kit de marca.

---

## 2b · La empresa entera (`#empresa`) — EN PRUEBA, rama `prueba-isometrico`

Sección en azul profundo, entre la cinta de fabricantes y «La plataforma».

- Sin eyebrow.
- **Titular:** Toda la empresa, en un sitio.
- **Párrafo:** Descubre con preguntas.
- **Ilustración:** isométrica animada. Seis salas sueltas (Administración · Oficina técnica ·
  Mantenimiento · Calidad · Almacén) alrededor de la Fábrica, que es la nave grande. De cada
  sala sube un flujo a la capa SVA; sobre la capa, una persona pregunta y un chat responde.
  Generada por script; solo se mueven los datos.
- **Chat (se puede desplazar), tres preguntas:**
  1. ¿Por qué paró ayer CNC-03? → parada de 4 h 12 min por la alarma SP9001 (SSPA:01 MOTOR
     OVERHEAT).
  2. ¿Qué significa esa alarma? → según el manual: sobrecalentamiento del motor de husillo, y
     qué revisar.
  3. ¿Cuándo se hizo el último servicio técnico? → fecha e intervención, de los partes.

| Etiqueta | Sala | Texto |
|---|---|---|
| La sala principal | Fábrica | Estado, ciclos, paros y alarmas de cada máquina, leídos del control sin tocar el programa. |
| Órdenes | Oficina técnica | Qué orden y qué programa corría en cada momento. |
| Costes | Administración | El sistema de gestión que ya usas: referencias, escandallos y costes. |
| Medidas | Calidad | Medidas y defectos, atados a la pieza y a la máquina. |
| Intervenciones | Mantenimiento | Qué se reparó, cuándo y cuánto estuvo parada. |
| Material | Almacén | Lo que entra y sale, junto a lo que se fabrica. |

> Al entrar esta sección, «La plataforma» pasa a fondo blanco y «Producto» a gris claro, para
> que las franjas sigan alternando.
>
> **Por verificar antes de publicar:** el significado de SP9001 y la referencia del manual
> (B-65285) están citados de memoria. Partes, fechas y horas son inventados.

---

## 3 · La plataforma (`#plataforma`)

- **Eyebrow:** La plataforma
- **Titular:** Conecta una vez. Responde siempre.
- **Párrafo:** Cuatro pasos, y a partir del segundo cada pregunta nueva ya no es un proyecto
  nuevo.

| # | Paso | Texto |
|---|---|---|
| 01 | Conectar | Leemos lo que ya tienes: máquinas de cualquier edad, sensores, calidad y tu sistema de gestión. Sin tocar programas ni redes. |
| 02 | Unificar | Todo con el mismo nombre y la misma hora. Una parada y la orden que corría dejan de ser dos datos sueltos. |
| 03 | Usar | Pantallas, alarmas, informes y tu Excel de siempre. Cada equipo entra por donde le conviene, a lo mismo. |
| 04 | Preguntar | Con los datos ordenados se les puede preguntar en castellano, y la respuesta cita de dónde sale. |

---

## 4 · Producto (`#producto`)

- **Titular:** Empiezas viendo. Acabas preguntando.
- Sin eyebrow y sin párrafo. **No se habla de niveles** (2026-09-28): tres bloques seguidos,
  cada uno con título · frase · lista · maqueta.

### «Tu planta, en directo.»
Qué produce, qué está parado y desde cuándo. Sin llamar a nadie y sin que nadie apunte nada
a mano.
La nave entera en una pantalla · Reparto del tiempo y top de paros · Alarmas agrupadas por
las que se repiten · Vida y desgaste de herramienta.
**Maqueta:** Planta · en vivo (tiles con los colores de estado del portal).

### «Nos conectamos a todos tus sistemas.»
Indexamos y ordenamos los datos. Para que tú puedas decidir.
Tiempo real de máquina por orden · Ciclo real frente al del escandallo · Coste por pieza y
margen por referencia · Lo que cuesta cada parada, en euros.
**Maqueta:** Análisis · el mes, con el reparto en los **seis estados** del portal (En marcha ·
En espera · Pausa · Inactiva · Parada · Sin señal) y su leyenda en píldoras.

### «Creamos una IA con tus datos.»
Tus pautas, tus manuales y tus hojas de proceso, indexados junto a lo que cuentan las
máquinas. Preguntas en castellano y te enseña de dónde sale la respuesta.
Preguntas en lenguaje normal · El saber de la casa, dentro · Cada respuesta cita máquina y
orden.
**Maqueta:** Pregunta · el asistente. Dos preguntas de ejemplo sobre CNC-03 (por qué hizo
menos piezas; cuánto ha costado), con las fuentes citadas debajo de cada respuesta.

> **Nunca escribir «planificación» ni «gestión de operaciones».** Eso es un MES; SVA lee el
> MES y el ERP, no los sustituye.

---

## 5 · Soluciones (`#usos`)

**Titular:** Lo que te piden el primer día

Visibilidad · Paros · Utilización · Herramienta · Alarmas · Informes · Capacidad · Energía,
cada uno con su título y una línea.

- **Informes:** «Informes automatizados» — Sin pelearte con el equipo de datos.

---

## 6 · Por equipo (`#equipos`)

**Titular:** La misma verdad, desde cada silla

Dirección · Producción · Mantenimiento · Calidad · Planta · Informática.

---

## 7 · Por sector (`#sectores`)

**Titular:** Industria pequeña y mediana
**Párrafo:** Empresas donde el turno lo dirige la experiencia de tres personas. No hay
departamento de datos, y no hace falta.

Talleres de mecanizado · Proveedores de automoción · Metalurgia y estampación · Plástico e
inyección · Bienes de equipo · Alimentación y envasado.

---

## 8 · Cierre (`#empezamos`)

- **Titular:** Un mes con tus datos.
- **Párrafo:** Miramos tu fábrica, conectamos lo que haya y te sientas delante de tu número.
  Te lo quedas, sigas con nosotros o no.
- **Botones:** Pedir una demo · Quiero saber mi número

> **El `id` es obligatorio:** `servicios.html` redirige a `/#empezamos`.

---

## Maquetas

Las tres maquetas de `#producto` son SVG escritos dentro de `index.html`; no hay comando
que las regenere. Llevan un taller sintético (CNC-01…09), nunca datos de un cliente.

`assets/img/portal-*.webp` y `assets/build_shots.py` son de la versión anterior y ya no se
usan en la página. `og-planta.png` sigue siendo la imagen para redes.

Runbook de despliegue: `02_Projects/00_Guias/03_desplegar_web_svadata.md`.

---

## Lo que se perdió en este cambio

La versión anterior (commit `a5dbba1`) tenía cosas que esta no, y se quitaron **a sabiendas**
al aprobar la página nueva. Si alguna hace falta, están en el historial:

- El «para quién» de cada nivel.
- Las notas honestas («los paros se miden solos; el motivo lo pones tú», «cada ERP es
  distinto»).
- La tabla «Margen por referencia» con la fila REF-0875.
- Las secciones «Sin riesgo» y el detalle de «Cómo empezamos» (Día 1-2 · Semana 1 · Día 30).
- La sección «La instalación» (mini-PC, histórico, una sola puerta) y su fila de cifras.

---

## Afirmaciones y su estado

| Afirmación | Estado |
|---|---|
| Conexión a máquinas de cualquier marca y edad | En producción para FANUC, MTConnect, OPC UA y robots; el resto vía la capa de conexión, **sin desplegar en cliente** |
| Planta, alarmas, análisis, herramienta, informes | En producción |
| Excel / Power BI contra los datos de planta | En producción |
| El motivo de cada paro | **No**: se mide el paro, no la causa |
| Cruce con el ERP (órdenes, escandallo, coste) | Diseñado; primera implantación en curso |
| Preguntar en castellano | En el portal, sobre los datos de máquina |
| Respuestas que citan el manual de la máquina y los partes de mantenimiento (chat de `#empresa`) | **No todavía** — visión |
| Datos de almacén, calidad y mantenimiento en la capa (`#empresa`) | **No desplegado en cliente**; hoy en producción solo máquinas |
| Documentos de la casa indexados (pautas, manuales) y coste en euros en las respuestas | **No todavía** — la maqueta del asistente los enseña como visión; dependen de indexar documentos y del cruce con el ERP |

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

## Dirección visual (2026-09-22)

Cambio grande: la web pasa de **clara y monocroma** a **oscura con azul eléctrico**. Es una
decisión deliberada tomada mirando a UMH, y **rompe dos reglas antiguas de marca** («light
only», «monocromo navy sin acento»). Si se toca `07_SVA_brand_design/`, que refleje esto —
esa carpeta todavía describe la identidad anterior.

- Fondo `#070E24`, acento `#3B6BFF`, segunda nota cian `#27D2F5` solo para el dato en
  movimiento.
- Display en **Source Serif** a 64 px. Se probaron y descartaron *Instrument Serif*
  (contraste de revista de moda, astas que se rompen en oscuro) y *Newsreader* (remates
  caligráficos, aire literario). Lo profesional es el serif neutro.
- Cuerpo en **Plus Jakarta Sans**, etiquetas en **JetBrains Mono**. Switzer queda fuera de
  la web: la dirección aprobada se vio con Jakarta.
- Las **capturas del portal** van sobre las únicas secciones claras de la página. Son lo
  único con color propio y por eso destacan.

---

## Barra de navegación

- **Enlaces:** Plataforma (`#plataforma`) · Niveles (`#niveles`) · Soluciones (`#usos`) ·
  Sectores (`#sectores`)
- **Botón:** Hablemos → correo

---

## 1 · Hero (`#top`)

- **Chip:** Hub de datos de planta
- **Titular:** Deja de suponer. / Empieza a ver.
  *(Dos golpes cortos, registro publicitario. Sustituye a «Todos tus datos operativos en un
  solo sitio», que era una descripción, no un titular.)*
- **Párrafo:** Un solo sitio donde entra todo lo que pasa en tu fábrica — máquinas, calidad,
  órdenes, energía — y del que sale cualquier respuesta que necesites.
- **Botones:** Ver la plataforma → `#plataforma` · Pedir una demo → correo
- **Diagrama:** hub radial. Ocho fuentes en corona (Máquinas · Sensores · Calidad · Órdenes ·
  Mantenimiento · Energía · Almacén · Operarios), SVA en el centro y pulsos de datos viajando
  por los radios hacia dentro. **Generado** por el script de construcción, no a mano.

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

## 3 · La plataforma (`#plataforma`)

- **Eyebrow:** La plataforma
- **Titular:** Conecta una vez. Responde siempre.
- **Párrafo:** Cuatro pasos, y a partir del segundo cada pregunta nueva ya no es un proyecto
  nuevo.

| # | Paso | Texto |
|---|---|---|
| 01 | Conectar | Leemos lo que ya tienes. Máquinas de cualquier edad, sensores, calidad y tu sistema de gestión. Sin tocar programas ni redes. |
| 02 | Unificar | Todo queda con el mismo nombre y la misma hora. Una parada y la orden que corría dejan de ser dos datos sueltos. |
| 03 | Usar | Pantallas, alarmas, informes y tu Excel de siempre. Cada equipo entra por donde le conviene, a lo mismo. |
| 04 | Preguntar | Cuando los datos están ordenados, se les puede preguntar en castellano y la respuesta cita de dónde sale. |

---

## 4 · Tres niveles (`#niveles`)

Sección clara. Cada nivel: etiqueta · título · frase · lista · captura. Se contrata por
niveles y cada uno incluye el anterior.

### Nivel 1 · Ver — «Tu planta, en directo.»
Qué produce, qué está parado y desde cuándo. Sin llamar a nadie y sin que nadie apunte nada
a mano.
La nave entera en una pantalla · Reparto del tiempo y top de paros · Alarmas agrupadas por
las que se repiten · Vida y desgaste de herramienta · Informes semanales y mensuales solos.
**Captura:** `portal-planta.webp`

### Nivel 2 · Cruzar — «Planta y gestión, el coste real.»
Tu ERP se queda donde está: lo leemos. Órdenes y referencias caen sobre la línea de tiempo
de la máquina.
Tiempo real de máquina por orden · Ciclo real frente al del escandallo · Coste por pieza y
margen por referencia · Lo que cuesta cada parada, en euros.
**Captura:** `portal-analisis.webp`

### Nivel 3 · Preguntar — «Tu asistente de planta.»
Las pautas, los manuales y las hojas de proceso, indexados junto a los datos. Preguntas y te
enseña la fuente.
Preguntas en lenguaje normal · El saber de la casa, dentro · Cada respuesta cita máquina y
orden.
**Captura:** `portal-herramientas.webp`

> **Nunca escribir «planificación» ni «gestión de operaciones».** Eso es un MES; SVA lee el
> MES y el ERP, no los sustituye.

---

## 5 · Soluciones (`#usos`)

**Titular:** Lo que te piden el primer día

Visibilidad · Paros · Utilización · Herramienta · Alarmas · Informes · Capacidad · Energía,
cada uno con su título y una línea.

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

## Capturas

Se regeneran con un comando contra el portal real y datos sintéticos:

```bash
~/.venvs/web-fetch/bin/python assets/build_shots.py
```

Runbook completo: `02_Projects/00_Guias/03_desplegar_web_svadata.md`.
Nunca llevan datos de un cliente.

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
| Cruce con el ERP (nivel 2) | Diseñado; primera implantación en curso |
| Preguntar en castellano (nivel 3) | **En desarrollo** — se presenta como capacidad, no hay pantalla que enseñar |

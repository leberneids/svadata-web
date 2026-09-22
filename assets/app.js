/* ============================================================================
   Movimiento. Tres cosas y nada más: aparecer al hacer scroll, contar las
   cifras, y marcar en qué módulo estás. Sin librerías — todo con
   IntersectionObserver, que el navegador ya trae.

   Si el visitante pide menos animación (prefers-reduced-motion) no se anima
   nada: los contadores saltan a su valor final y los bloques ya están
   visibles por CSS.
   ========================================================================== */
(function () {
  'use strict';

  var quieto = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. aparecer al entrar en pantalla ---------------------------------
     El retardo escalonado va en CSS (.rv-d1…d5); aquí solo se añade la clase.
     Se deja de observar cada elemento en cuanto entra: una vez visto, visto. */
  var rv = document.querySelectorAll('.rv');
  if (quieto || !('IntersectionObserver' in window)) {
    rv.forEach(function (el) { el.classList.add('in'); });
  } else {
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    rv.forEach(function (el) { obs.observe(el); });
  }

  /* ---- 2. contadores ------------------------------------------------------
     Arrancan al verse, no al cargar: contar mientras nadie mira es tirar el
     efecto. easeOutCubic para que frene al final en vez de cortarse seco. */
  function contar(el) {
    var fin = parseInt(el.getAttribute('data-count'), 10) || 0;
    if (quieto || fin === 0) { el.textContent = String(fin); return; }
    var ini = performance.now(), dur = 1100;
    (function paso(ahora) {
      var t = Math.min((ahora - ini) / dur, 1);
      var e = 1 - Math.pow(1 - t, 3);
      el.textContent = String(Math.round(fin * e));
      if (t < 1) requestAnimationFrame(paso);
    })(ini);
  }

  var nums = document.querySelectorAll('[data-count]');
  if (quieto || !('IntersectionObserver' in window)) {
    nums.forEach(contar);
  } else {
    var obsN = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { contar(e.target); obsN.unobserve(e.target); }
      });
    }, { threshold: 0.9 });
    nums.forEach(function (el) { obsN.observe(el); });
  }

  /* ---- 3. raíl de la plataforma ------------------------------------------
     Marca el módulo en pantalla. La franja de detección es la banda central
     del viewport: así el activo cambia cuando el módulo llega al medio, que
     es donde el ojo está, y no cuando asoma por abajo. */
  var mods = [].slice.call(document.querySelectorAll('.mod'));
  var links = {};
  document.querySelectorAll('.rail a').forEach(function (a) {
    links[a.getAttribute('href').slice(1)] = a;
  });

  if (mods.length && 'IntersectionObserver' in window) {
    var visibles = new Set();
    var obsM = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) visibles.add(e.target.id); else visibles.delete(e.target.id);
      });
      // El primero en orden de documento de los que se ven: evita el
      // parpadeo cuando dos módulos cortan la franja a la vez.
      var activo = mods.map(function (m) { return m.id; })
                       .filter(function (id) { return visibles.has(id); })[0];
      Object.keys(links).forEach(function (id) {
        links[id].classList.toggle('on', id === activo);
      });
    }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
    mods.forEach(function (m) { obsM.observe(m); });
  }

  /* ---- 4. pulsos del hub ------------------------------------------------
     Los <animateMotion> son SMIL: `prefers-reduced-motion` en CSS no los para,
     así que se retiran a mano. */
  if (quieto) {
    document.querySelectorAll('.hub-svg animateMotion').forEach(function (a) {
      a.parentNode && a.parentNode.removeChild(a.parentNode);
    });
  }

  /* ---- 5. el ancla del nav pegajoso --------------------------------------
     scroll-margin-top en CSS resuelve el salto; esto solo cierra el menú
     mental de "he pulsado y no ha pasado nada" dando foco al destino. */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function () {
      var d = document.getElementById(a.getAttribute('href').slice(1));
      if (d) { d.setAttribute('tabindex', '-1'); setTimeout(function () { d.focus({ preventScroll: true }); }, 420); }
    });
  });
})();

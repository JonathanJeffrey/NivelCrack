(function () {
  const nav = document.querySelector('.page-layout__nav');
  if (!nav) return;

  const top = nav.querySelector('.site-nav__top');
  const inner = nav.querySelector('.site-nav__inner');
  if (!top || !inner) return;

  if (!inner.id) inner.id = 'site-nav-panel';

  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'nav-mobile-toggle';
  btn.setAttribute('aria-label', 'Toggle menu');
  btn.setAttribute('aria-expanded', 'false');
  btn.setAttribute('aria-controls', inner.id);
  btn.innerHTML = '<span class="nav-mobile-toggle__icon" aria-hidden="true"></span><span class="nav-mobile-toggle__badge" aria-hidden="true"></span>';

  const logo = top.querySelector('.nav-brand__logo');
  if (logo && logo.nextSibling) {
    top.insertBefore(btn, logo.nextSibling);
  } else {
    top.appendChild(btn);
  }

  btn.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', String(isOpen));
  });

  const mq = window.matchMedia('(min-width: 769px)');
  const onChange = (e) => {
    if (e.matches) {
      nav.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
    }
  };
  if (mq.addEventListener) mq.addEventListener('change', onChange);
  else mq.addListener(onChange);
})();

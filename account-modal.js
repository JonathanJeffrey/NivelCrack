(function () {
  /* ---- Build modal DOM ---- */
  var overlay = document.createElement('div');
  overlay.className = 'account-overlay';
  overlay.id = 'account-overlay';
  overlay.hidden = true;
  overlay.innerHTML = '' +
    '<div class="account-overlay__backdrop" id="account-backdrop"></div>' +
    '<div class="account-overlay__panel" role="dialog" aria-modal="true" aria-label="Sign in">' +
      '<header class="account-overlay__header">' +
        '<span class="account-overlay__title">Sign In</span>' +
        '<button type="button" class="account-overlay__close" id="account-close" aria-label="Close">Close</button>' +
      '</header>' +
      '<form class="account-form" id="account-form">' +
        '<div class="account-form__fields">' +
          '<div class="account-form__group">' +
            '<label class="account-form__label" for="account-email">Email</label>' +
            '<input class="account-form__input" type="email" id="account-email" name="email" autocomplete="email" placeholder="you@example.com" spellcheck="false" required />' +
          '</div>' +
          '<div class="account-form__group">' +
            '<label class="account-form__label" for="account-password">Password</label>' +
            '<input class="account-form__input" type="password" id="account-password" name="password" autocomplete="current-password" required />' +
          '</div>' +
        '</div>' +
        '<button type="submit" class="btn btn--primary btn--md btn--block">Sign In</button>' +
        '<div class="account-overlay__links">' +
          '<a href="#" class="account-form__link">Create Account</a>' +
          '<a href="#" class="account-form__link">Forgot Password?</a>' +
        '</div>' +
      '</form>' +
    '</div>';

  document.body.appendChild(overlay);

  /* ---- Open / Close ---- */
  var backdrop = document.getElementById('account-backdrop');
  var closeBtn = document.getElementById('account-close');

  function open() {
    overlay.hidden = false;
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        overlay.classList.add('is-open');
        var emailInput = document.getElementById('account-email');
        if (emailInput && window.innerWidth > 768) emailInput.focus();
      });
    });
  }

  function close() {
    overlay.classList.remove('is-open');
    setTimeout(function () { overlay.hidden = true; }, 250);
  }

  closeBtn.addEventListener('click', close);
  backdrop.addEventListener('click', close);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !overlay.hidden) close();
  });

  /* Prevent default form submission (mockup) */
  document.getElementById('account-form').addEventListener('submit', function (e) {
    e.preventDefault();
  });

  /* ---- Wire up Account triggers ---- */
  document.querySelectorAll('[data-account-trigger]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      open();
    });
  });
})();

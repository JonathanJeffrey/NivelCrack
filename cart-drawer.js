/* Universal cart side-drawer. Injects markup, intercepts [data-cart-trigger] clicks. */
var CartDrawer = (function () {
  var overlay, backdrop, closeBtn, cartItems, cartSubtotal, injected = false;

  var DRAWER_CSS =
    '.cart-overlay{position:fixed;top:0;left:0;right:0;bottom:0;z-index:100;}' +
    '.cart-overlay__backdrop{position:absolute;inset:0;background:rgba(0,0,0,0.15);opacity:0;transition:opacity var(--dur-med) var(--ease);}' +
    '.cart-overlay.is-open .cart-overlay__backdrop{opacity:1;}' +
    '.cart-drawer--slide{position:fixed;top:0;right:0;height:100dvh;width:25vw;max-width:25vw;transform:translateX(100%);transition:transform var(--dur-med) var(--ease);z-index:101;}' +
    '.cart-overlay.is-open .cart-drawer--slide{transform:translateX(0);}' +
    '.cart-drawer__empty{font-family:var(--font-body);font-size:11px;font-weight:var(--weight-medium);text-transform:uppercase;letter-spacing:var(--tracking-label);color:var(--color-text-secondary);margin:0;padding:var(--space-3) 0;text-align:center;}' +
    '@media (max-width: 768px){.cart-drawer--slide{width:100vw;max-width:100vw;}}';

  var DRAWER_HTML =
    '<div class="cart-overlay" id="cart-overlay" hidden>' +
      '<div class="cart-overlay__backdrop" id="cart-backdrop"></div>' +
      '<aside class="cart-drawer cart-drawer--slide" id="cart-drawer" aria-label="Shopping cart">' +
        '<header class="cart-drawer__header">' +
          '<button type="button" class="cart-drawer__close" id="cart-close" aria-label="Close cart">Close</button>' +
        '</header>' +
        '<div class="cart-drawer__items" id="cart-items"></div>' +
        '<footer class="cart-drawer__footer">' +
          '<div class="cart-drawer__subtotal">' +
            '<span class="cart-drawer__subtotal-label">Subtotal</span>' +
            '<span class="cart-drawer__subtotal-value" id="cart-subtotal">0.00 USD</span>' +
          '</div>' +
          '<p class="cart-drawer__note">Exchange or refund due to size is not acceptable so please check the size chart carefully before ordering.</p>' +
          '<p class="cart-drawer__note">The customs duties and VAT are not included so please check the conditions of your country before purchasing.</p>' +
          '<button type="button" class="btn btn--primary btn--lg btn--block">Check Out</button>' +
        '</footer>' +
      '</aside>' +
    '</div>';

  function inject() {
    if (injected) return;
    injected = true;

    var style = document.createElement('style');
    style.textContent = DRAWER_CSS;
    document.head.appendChild(style);

    var wrapper = document.createElement('div');
    wrapper.innerHTML = DRAWER_HTML;
    document.body.appendChild(wrapper.firstElementChild);

    overlay = document.getElementById('cart-overlay');
    backdrop = document.getElementById('cart-backdrop');
    closeBtn = document.getElementById('cart-close');
    cartItems = document.getElementById('cart-items');
    cartSubtotal = document.getElementById('cart-subtotal');

    closeBtn.addEventListener('click', close);
    backdrop.addEventListener('click', close);
  }

  function escapeAttr(s) {
    return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function render() {
    inject();
    var items = CartStore.getItems();
    cartItems.innerHTML = '';
    if (!items.length) {
      var empty = document.createElement('p');
      empty.className = 'cart-drawer__empty';
      empty.textContent = 'Your cart is empty';
      cartItems.appendChild(empty);
      cartSubtotal.textContent = '0.00 USD';
      return;
    }
    items.forEach(function (ci, idx) {
      var el = document.createElement('article');
      el.className = 'cart-item';
      el.innerHTML = '' +
        '<div class="cart-item__image"><img src="' + escapeAttr(ci.img) + '" alt="' + escapeAttr(ci.name) + '" width="1000" height="1000" /></div>' +
        '<div class="cart-item__details">' +
          '<span class="cart-item__name">' + escapeAttr(ci.name) + '</span>' +
          '<span class="cart-item__variant">Size: ' + escapeAttr(ci.size) + '</span>' +
          '<div class="cart-item__qty">' +
            '<div class="cart-item__qty-controls">' +
              '<button type="button" class="cart-item__qty-btn" data-dir="down" aria-label="Decrease quantity">\u2013</button>' +
              '<span class="cart-item__qty-value">' + ci.qty + '</span>' +
              '<button type="button" class="cart-item__qty-btn" data-dir="up" aria-label="Increase quantity">+</button>' +
            '</div>' +
            '<span class="cart-item__price">' + (ci.price * ci.qty).toFixed(2) + ' USD</span>' +
          '</div>' +
        '</div>';
      cartItems.appendChild(el);

      el.querySelectorAll('.cart-item__qty-btn').forEach(function (qBtn) {
        qBtn.addEventListener('click', function () {
          var current = CartStore.getItems();
          var q = current[idx].qty;
          if (qBtn.getAttribute('data-dir') === 'up') q++;
          else if (q > 1) q--;
          else { CartStore.removeItem(idx); render(); return; }
          CartStore.updateItem(idx, q);
          render();
        });
      });
    });
    cartSubtotal.textContent = CartStore.subtotal().toFixed(2) + ' USD';
  }

  function open() {
    inject();
    render();
    overlay.hidden = false;
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        overlay.classList.add('is-open');
      });
    });
  }

  function close() {
    if (!overlay) return;
    overlay.classList.remove('is-open');
    setTimeout(function () { overlay.hidden = true; }, 250);
  }

  function init() {
    inject();
    document.addEventListener('click', function (e) {
      var trigger = e.target.closest('[data-cart-trigger]');
      if (trigger) {
        e.preventDefault();
        open();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  return { open: open, close: close, render: render };
})();

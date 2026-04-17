/* Shared cart state via localStorage */
var CartStore = (function () {
  var KEY = 'nvlcrk_cart';

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || []; }
    catch (e) { return []; }
  }

  function save(items) {
    localStorage.setItem(KEY, JSON.stringify(items));
    updateBadges();
  }

  function getItems() { return load(); }

  function addItem(item) {
    var items = load();
    /* If same product+size exists, increment qty */
    for (var i = 0; i < items.length; i++) {
      if (items[i].name === item.name && items[i].size === item.size) {
        items[i].qty += item.qty;
        save(items);
        return;
      }
    }
    items.push(item);
    save(items);
  }

  function updateItem(index, qty) {
    var items = load();
    if (qty <= 0) items.splice(index, 1);
    else items[index].qty = qty;
    save(items);
  }

  function removeItem(index) {
    var items = load();
    items.splice(index, 1);
    save(items);
  }

  function totalQty() {
    return load().reduce(function (n, item) { return n + item.qty; }, 0);
  }

  function subtotal() {
    return load().reduce(function (n, item) { return n + item.price * item.qty; }, 0);
  }

  function updateBadges() {
    var count = totalQty();
    document.querySelectorAll('.site-nav__link[href="cart.html"]').forEach(function (el) {
      el.textContent = 'Cart (' + count + ')';
    });
  }

  /* Update badges on load */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateBadges);
  } else {
    updateBadges();
  }

  return {
    getItems: getItems,
    addItem: addItem,
    updateItem: updateItem,
    removeItem: removeItem,
    totalQty: totalQty,
    subtotal: subtotal,
    updateBadges: updateBadges
  };
})();

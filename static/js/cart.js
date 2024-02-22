// cart.js
document.addEventListener('DOMContentLoaded', function() {
  function addToCart(productId, price) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let found = cart.find(item => item.id === productId);
    if (found) {
      found.quantity += 1;
    } else {
      cart.push({ id: productId, quantity: 1, price: price });
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
  }

  function updateCartCount() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let count = cart.reduce((acc, item) => acc + item.quantity, 0);
    document.getElementById('cart-count').innerText = count;
  }

  function clearCart() {
    localStorage.removeItem('cart');
    updateCartCount();
    renderCartItems();
  }

  function renderCartItems() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = '';
    let totalPrice = 0;

    cart.forEach(item => {
      let row = document.createElement('tr');
      row.innerHTML = `
      <td>${item.id}</td>
      <td>${item.quantity}</td>
      <td>${item.price} USD</td>
      <td><button onclick="removeFromCart('${item.id}')" class="btn btn-danger">&times;</button></td>
    `;
      cartItemsContainer.appendChild(row);
      totalPrice += item.quantity * item.price;
    });

    document.getElementById('total-price').innerText = totalPrice;
  }

  function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let newCart = cart.filter(item => item.id !== productId);
    localStorage.setItem('cart', JSON.stringify(newCart));
    renderCartItems();
    updateCartCount();
  }

  window.addToCart = addToCart;
  window.updateCartCount = updateCartCount;
  window.clearCart = clearCart;
  window.renderCartItems = renderCartItems;
  window.removeFromCart = removeFromCart;

  updateCartCount();
  renderCartItems();
});

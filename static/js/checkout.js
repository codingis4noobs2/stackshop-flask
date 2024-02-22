// checkout.js
function confirmOrder() {
    alert('Order submitted. Thank you for shopping with us!');
    window.location.href = '/';
    return false;
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let totalCount = cart.reduce((acc, item) => acc + item.quantity, 0);
    let totalPrice = cart.reduce((acc, item) => acc + (item.quantity * item.price), 0).toFixed(2);
  
    document.getElementById('cart-count').innerText = totalCount;
    document.getElementById('total-price').innerText = totalPrice;
  });
  


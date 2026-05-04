// ==========================================
//  ArtisanHub — JavaScript principal
// ==========================================

// --- Panier (côté client, simple) ---
let cartCount = 0;

function addToCart() {
  cartCount++;
  const el = document.getElementById('cartCount');
  if (el) el.textContent = cartCount;
}

// --- Filtre catégories (catalogue) ---
function setCat(el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
}

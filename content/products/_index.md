---
title: "products"
showTitle: true
params:
  disableList: true
cascade:
  showList: false
---
<style>
/* PAGE LAYOUT */
.prose {
  max-width: 750px !important;
  margin: 0 auto !important;
  padding-top: 10vh !important;
  text-align: center !important;
}
.max-w-prose {
  max-width: 750px !important;
}
/* TITLE (REAL CONGO H1) */
main > header {
  max-width: 820px !important;
  margin: 0 auto !important;
  text-align: center !important;
  display: block !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}
/* TITLE SPACING */
h1.mt-0 {
  margin-top: 0rem !important;
}
/* TITLE STYLE */
header h1,
h1.mt-0.text-4xl.font-extrabold {
  text-align: left !important;
  font-weight: 300 !important;
  font-size: 3rem;
  color: #333333 !important;
  letter-spacing: -0.02em;
  margin-bottom: 0rem !important;
}
/* BODY TEXT */
.prose p {
  font-weight: 300;
  font-size: 1.2rem;
  line-height: 1.4;
  margin: 0 0 1.2rem 0;
  color: #333333;
}
/* CLEAN SPACING */
.prose > * {
  margin-top: 0 !important;
}
.prose hr,
section.prose.mt-10 {
  display: none !important;
}
/* BACK LINK */
#back-link {
  position: fixed !important;
  top: 2.75rem !important;
  left: 275px !important;
  font-size: 0.875rem !important;
  font-weight: 300 !important;
  z-index: 1000 !important;
  transition: opacity 0.2s ease !important;
}
#back-link a,
#back-link a:visited,
#back-link a:hover,
#back-link a:active,
#back-link a:focus {
  color: #333333 !important;
  text-decoration: none !important;
  border-bottom: none !important;
  box-shadow: none !important;
}
#back-link a:hover {
  color: #000000 !important;
  text-decoration: none !important;
  border-bottom: none !important;
  box-shadow: none !important;
}
/* NAV CLEANUP */
nav a {
  text-decoration: none !important;
}
#back-link a {
  all: unset;
  color: #333333;
  cursor: pointer;
}
nav a,
nav a:visited {
  color: #333333 !important;
  text-decoration: none !important;
}
header nav a:hover {
  color: #000000 !important;
  text-decoration: none !important;
  border-bottom: none !important;
  box-shadow: none !important;
}

#main-content section:nth-of-type(2) {
  display: none !important;
}

/* FILTER */
.filter-bar {
  max-width: 1100px;
  margin: -4vh auto;
  padding: 0rem 0 0;
  display: flex;
  justify-content: flex-start;
}

.filter-dropdown {
  position: relative;
}

.filter-toggle {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 300;
  letter-spacing: 0.1em;
  text-transform: none;
  color: #888888;
  padding: 0;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  transition: color 0.15s;
}

.filter-toggle:hover {
  color: #333333;
}

.filter-toggle .arrow {
  font-size: 0.65rem;
  transition: transform 0.2s;
  display: inline-block;
}

.filter-toggle.open .arrow {
  transform: rotate(180deg);
}

.filter-menu {
  display: none;
  position: absolute;
  left: calc(100% + 1rem);
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  padding: 0;
  z-index: 50;
  white-space: nowrap;
  box-shadow: none;
}

.filter-menu.open {
  display: block;
}

.filter-option {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.75rem 0.4rem 0;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 300;
  letter-spacing: 0.05em;
  color: #333333;
  white-space: nowrap;
  user-select: none;
}

.filter-option input[type="checkbox"] {
  appearance: none;
  width: 11px;
  height: 11px;
  border: 1px solid #cccccc;
  background: #ffffff;
  cursor: pointer;
  flex-shrink: 0;
  position: relative;
  top: 0;
}

.filter-option input[type="checkbox"]:checked {
  background: #333333;
  border-color: #333333;
}

/* PRODUCTS GRID */
.products-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  padding: .75rem 0 4rem;
  max-width: 1100px;
  margin: 0 auto;
  text-align: left;
}

.product-card {
  text-decoration: none !important;
  color: #333333 !important;
  display: flex;
  flex-direction: column;
  gap: .25rem;
  border-bottom: none !important;
  box-shadow: none !important;
  transition: opacity 0.2s;
}

.product-card.hidden {
  display: none;
}

.product-card:hover .product-name {
  text-decoration: none;
}

.product-card:hover {
  color: #333333 !important;
  background: none !important;
  box-shadow: none !important;
  border-bottom: none !important;
  outline: none !important;
}

.product-card:hover .product-image img {
  opacity: 0.85;
  transition: opacity 0.2s ease;
}

.product-image img {
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  background: #f5f5f5;
  display: block;
}

.product-name {
  font-family: 'Inter', sans-serif;
  font-weight: 300;
  font-size: 0.5rem;
  margin: 0;
  color: #333333;
}

.product-descriptor {
  font-family: 'Inter', sans-serif;
  font-weight: 300;
  font-size: 0.5rem;
  color: #888888;
  margin: 0;
}

.products-grid .product-name {
  font-size: 1.2rem !important;
  margin: 0 !important;
}

.products-grid .product-descriptor {
  font-size: 1rem !important;
  margin: 0 !important;
}

.products-grid .product-image {
  margin-bottom: 0 !important;
}

.products-grid .product-name {
  margin-top: -1.5rem !important;
}

.product-card:hover img {
  transform: scale(1.02);
  transition: all 0.25s ease;
}

/* MOBILE */
@media (max-width: 1024px) {
  #back-link {
    left: 1.25rem !important;
  }
}

@media (max-width: 768px) {
  main > header {
    padding-left: 1rem !important;
  }
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
    padding: 0.5rem 1rem 3rem;
  }
  .filter-bar {
    padding: 1.5rem 1rem 0;
  }
  .products-grid .product-name {
    font-size: 0.85rem !important;
  }
  .products-grid .product-descriptor {
    font-size: 0.75rem !important;
  }
}

footer hr {
  display: none !important;
}
</style>

<div id="back-link"><a href="/">← partihaus</a></div>

<div class="filter-bar">
  <div class="filter-dropdown">
    <button class="filter-toggle" id="filterToggle">
      categories <span class="arrow">▾</span>
    </button>
    <div class="filter-menu" id="filterMenu">
      <label class="filter-option">
        <input type="checkbox" value="tabletop" checked> tabletop
      </label>
      <label class="filter-option">
        <input type="checkbox" value="atmosphere" checked> atmosphere
      </label>
      <label class="filter-option">
        <input type="checkbox" value="utility" checked> utility
      </label>
    </div>
  </div>
</div>

<div class="products-grid" id="productsGrid">

  <a class="product-card" href="/products/section-bowl/" data-category="atmosphere">
    <div class="product-image">
      <img src="/images/products/section-bowl.jpg" alt="Form & Refine Section Bowl" loading="lazy">
    </div>
    <p class="product-name">section bowl</p>
    <p class="product-descriptor">solid european oak</p>
  </a>

  <a class="product-card" href="/products/kaiser-idell-lamp/" data-category="atmosphere">
    <div class="product-image">
      <img src="/images/products/kaiser-lamp.jpg" alt="Kaiser Idell Table Lamp" loading="lazy">
    </div>
    <p class="product-name">kaiser idell table lamp</p>
    <p class="product-descriptor">bauhaus steel, high-gloss finish</p>
  </a>

  <a class="product-card" href="/products/kubus-candleholder/" data-category="atmosphere">
    <div class="product-image">
      <img src="/images/products/kubus-candleholder.jpg" alt="Kubus Candleholder" loading="lazy">
    </div>
    <p class="product-name">kubus candleholder</p>
    <p class="product-descriptor">architectural steel design</p>
  </a>

  <a class="product-card" href="/products/emma-french-press/" data-category="utility">
    <div class="product-image">
      <img src="/images/products/emma-french-press.jpg" alt="Stelton Emma French Press" loading="lazy">
    </div>
    <p class="product-name">emma french press</p>
    <p class="product-descriptor">lacquered steel with beechwood handle</p>
  </a>

  <a class="product-card" href="/products/alfredo-salt-pepper/" data-category="tabletop">
    <div class="product-image">
      <img src="/images/products/alfredo-salt-pepper.jpg" alt="Georg Jensen Alfredo Salt & Pepper Mills" loading="lazy">
    </div>
    <p class="product-name">alfredo salt & pepper mills</p>
    <p class="product-descriptor">mirror-polished stainless steel</p>
  </a>

  <a class="product-card" href="/products/blomus-alpha-carafe/" data-category="utility">
    <div class="product-image">
      <img src="/images/products/blomus-decantor.jpg" alt="blomus Alpha decanting carafe" loading="lazy">
    </div>
    <p class="product-name">blomus alpha decanting carafe</p>
    <p class="product-descriptor">hand-blown glass, stainless steel</p>
  </a>

  <a class="product-card" href="/products/iittala-kartio-tumbler" data-category="tabletop">
    <div class="product-image">
      <img src="/images/products/iittala-Kartio-Tumbler.jpg" alt="iittala Kartio Tumbler" loading="lazy">
    </div>
    <p class="product-name">iittala kartio tumbler</p>
    <p class="product-descriptor">lead-free molded glass</p>
  </a>

  <a class="product-card" href="/products/turning-tray/" data-category="atmosphere">
    <div class="product-image">
      <img src="/images/products/turning-tray.jpg" alt="Finn Juhl Turning Tray" loading="lazy">
    </div>
    <p class="product-name">finn juhl turning Tray</p>
    <p class="product-descriptor">teak frame, dual-tone laminate</p>
  </a>

  <a class="product-card" href="/products/pantone-mug/" data-category="tabletop">
    <div class="product-image">
      <img src="/images/products/pantone-mug.jpg" alt="Pantone Mug" loading="lazy">
    </div>
    <p class="product-name">pantone mug</p>
    <p class="product-descriptor">color-matched ceramic</p>
  </a>

</div>

<script>
(function() {
  const toggle = document.getElementById('filterToggle');
  const menu = document.getElementById('filterMenu');
  const checkboxes = menu.querySelectorAll('input[type="checkbox"]');

  toggle.addEventListener('click', function(e) {
    e.stopPropagation();
    const isOpen = menu.classList.toggle('open');
    toggle.classList.toggle('open', isOpen);
  });

  document.addEventListener('click', function() {
    menu.classList.remove('open');
    toggle.classList.remove('open');
  });

  menu.addEventListener('click', function(e) {
    e.stopPropagation();
  });

  function applyFilter() {
    const active = Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    document.querySelectorAll('.product-card').forEach(function(card) {
      const cat = card.getAttribute('data-category');
      card.classList.toggle('hidden', !active.includes(cat));
    });

    if (active.length === 0) {
      document.querySelectorAll('.product-card').forEach(function(card) {
        card.classList.remove('hidden');
      });
    }
  }

  checkboxes.forEach(function(cb) {
    cb.addEventListener('change', applyFilter);
  });

  // Hide back link on scroll
  window.addEventListener('scroll', function() {
    const backLink = document.getElementById('back-link');
    if (window.scrollY > 50) {
      backLink.style.opacity = '0';
      backLink.style.pointerEvents = 'none';
    } else {
      backLink.style.opacity = '1';
      backLink.style.pointerEvents = 'auto';
    }
  });

})();
</script>

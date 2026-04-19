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
.prose {
  max-width: 750px !important;
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
  margin-top: 8rem !important;
}
/* TITLE STYLE */
header h1,
h1.mt-0.text-4xl.font-extrabold {
  text-align: center !important;
  font-weight: 300 !important;
  font-size: 3rem;
  color: #333333 !important;
  letter-spacing: -0.02em;
  margin-bottom: -6rem !important;
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
  left: 200px !important;
  font-size: 0.875rem !important;
  font-weight: 300 !important;
  z-index: 100 !important;
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
.divider {
  margin: 0 0.2rem;
  opacity: .75;
}
.prose p.center-line {
  font-weight: 600 !important;
  letter-spacing: 0.02em;
}

#main-content section:nth-of-type(2) {
  display: none !important;
}

/* PRODUCTS GRID */
.products-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  padding: 2.5rem 0;
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
}

.products-grid .product-descriptor {
  font-size: 1rem !important;
}

.products-grid .product-name {
  margin: 0 !important;
}

.products-grid .product-descriptor {
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

@media (max-width: 768px) {
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div id="back-link"><a href="/">← partihaus</a></div>

<div class="products-grid">

  <!-- ROW 1 -->

  <a class="product-card" href="/products/kontra-fruit-bowl/">
    <div class="product-image">
      <img src="/images/products/kontra-bowl.jpg" alt="Stelton Kontra Fruit Bowl" loading="lazy">
    </div>
    <p class="product-name">Kontra Fruit Bowl</p>
    <p class="product-descriptor">wood and stainless steel</p>
  </a>

  <a class="product-card" href="/products/kaiser-idell-lamp/">
    <div class="product-image">
      <img src="/images/products/kaiser-lamp.jpg" alt="Kaiser Idell Table Lamp" loading="lazy">
    </div>
    <p class="product-name">Kaiser Idell Table Lamp</p>
    <p class="product-descriptor">bauhaus steel, high-gloss finish</p>
  </a>

  <a class="product-card" href="/products/kubus-candleholder/">
    <div class="product-image">
      <img src="/images/products/kubus-candleholder.jpg" alt="Kubus Candleholder" loading="lazy">
    </div>
    <p class="product-name">Kubus Candleholder</p>
    <p class="product-descriptor">architectural steel design</p>
  </a>


  <!-- ROW 2 -->

  <a class="product-card" href="/products/emma-french-press/">
    <div class="product-image">
      <img src="/images/products/emma-french-press.jpg" alt="Stelton Emma French Press" loading="lazy">
    </div>
    <p class="product-name">Emma French Press</p>
    <p class="product-descriptor">steel with beechwood handle</p>
  </a>

  <a class="product-card" href="/products/barbry-salt-pepper-mills/">
    <div class="product-image">
      <img src="/images/products/barbry-salt-pepper.jpg" alt="Barbry Salt and Pepper Mills" loading="lazy">
    </div>
    <p class="product-name">Barbry Salt & Pepper Mills</p>
    <p class="product-descriptor">polished stainless steel</p>
  </a>

  <a class="product-card" href="/products/blomus-alpha-carafe/">
    <div class="product-image">
      <img src="/images/products/blomus-decantor.jpg" alt="blomus Alpha decanting carafe" loading="lazy">
    </div>
    <p class="product-name">Blomus Alpha decanting carafe</p>
    <p class="product-descriptor">minimal curved glass</p>
  </a>


  <!-- ROW 3 -->

  <a class="product-card" href="/products/iittala-kartio-tumbler">
    <div class="product-image">
      <img src="/images/products/iittala-Kartio-Tumbler.jpg" alt="iittala Kartio Tumbler" loading="lazy">
    </div>
    <p class="product-name">iittala Kartio Tumbler</p>
    <p class="product-descriptor">Clear Medium Glass (Set of 8) </p>
  </a>

  <a class="product-card" href="/products/turning-tray/">
    <div class="product-image">
      <img src="/images/products/turning-tray.jpg" alt="Finn Juhl Turning Tray" loading="lazy">
    </div>
    <p class="product-name">Turning Tray</p>
    <p class="product-descriptor">dual-tone laminated wood</p>
  </a>

  <a class="product-card" href="/products/pantone-mug/">
    <div class="product-image">
      <img src="/images/products/pantone-mug.jpg" alt="Pantone Mug" loading="lazy">
    </div>
    <p class="product-name">Pantone Mug</p>
    <p class="product-descriptor">color-matched ceramic</p>
  </a>

</div>


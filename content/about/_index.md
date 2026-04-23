---
title: "about"
showTitle: true
---
<style>
.prose {
  max-width: 720px !important;
  margin: 0 auto !important;
  padding-top: 10vh !important;
  padding-right: 0 !important;
  text-align: left !important;
}
.max-w-prose {
  max-width: 620px !important;
}
main > header {
  max-width: 820px !important;
  margin: 0 auto !important;
  text-align: left !important;
  display: block !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}
h1.mt-0 {
  margin-top: 0rem !important;
}
header h1,
h1.mt-0.text-4xl.font-extrabold {
  text-align: left !important;
  font-weight: 300 !important;
  font-size: 3rem !important;
  color: #333333 !important;
  letter-spacing: -0.02em;
  margin-bottom: 0rem !important;
}
.prose p {
  font-weight: 300;
  font-size: 1.05rem;
  line-height: 1.6;
  margin: 0 0 0.75rem 0;
  color: #333333;
}
.prose > * {
  margin-top: 0 !important;
}
.prose hr,
section.prose.mt-10 {
  display: none !important;
}
nav a {
  text-decoration: none !important;
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
  text-align: center !important;
  margin: 1.5rem 0 !important;
  padding-right: 0 !important;
}
footer hr {
  display: none !important;
}
@media (max-width: 768px) {
  main > header {
    padding-left: 1rem !important;
  }
  .prose {
    max-width: 100% !important;
    padding: 6vh 1.25rem 0 !important;
  }
}
</style>

the name comes from architecture. *parti* is the simplest possible diagram of a design idea — the concept stripped to its core before anything else is added. *haus* is home, and a quiet reference to the Bauhaus, which spent a century proving that the objects you live with should be both useful and beautiful

*partihaus* curates from that same conviction — objects with a clear *parti* and selected for function, form, and longevity.

<p class="center-line">timeless over trendy <span class="divider">·</span> quality over imitation <span class="divider">·</span> intentional design</p>

this collection is for those who think about design — and those who gift them.

<script>
document.addEventListener('DOMContentLoaded', function() {
  var nav = document.querySelector('header nav') || document.querySelector('nav');
  if (nav) {
    nav.style.cssText = 'display:flex; align-items:center; width:100%; justify-content:space-between;';
    var backItem = document.createElement('li');
    backItem.style.cssText = 'list-style:none;';
    backItem.innerHTML = '<a href="/" style="color:#333333; text-decoration:none; font-size:0.875rem; font-weight:300;">← partihaus</a>';
    nav.insertBefore(backItem, nav.firstChild);
  }
});
</script>

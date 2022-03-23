import re
html = r'<a href="/collections/pasture-raised-beef/products/grass-fed-non-gmo-corn-fed-ground-beef-patties">          \n      <img src="//cdn.shopify.com/s/files/1/0914/6382/products/IMG_4144_Beef_patties_web_large.jpg?v=1576169110" alt="Ground beef 4 oz Patties  (100 % grass fed)" />\n    </a>\n  </div>\n\n  <div class="details">\n    <a href="/collections/pasture-raised-beef/products/grass-fed-non-gmo-corn-fed-ground-beef-patties" class="clearfix">\n      <h4 class="title">Ground beef 4 oz Patties  (100 % grass fed)</h4>\n\n      <span class="price">\n      \n      \n        \n        $ 9.99\n      \n      </span>\n  \n      <span class="shopify-product-reviews-badge" data-id="1544567491"></span>\n    </a>'
match = re.findall(r"<a.*?<h4 class=\"title\">(.*?)</h4>.*?<span class=\"price\".*?((?:[0-9]{1,2}\.[0-9]{2}).*?)</span>.*?</a>", html)
print('')
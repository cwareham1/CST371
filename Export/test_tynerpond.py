import unittest
import tynerpond

class TynerTest(unittest.TestCase):

    def test_regex_rawlist_nosavings(self):
        tyner = tynerpond.Tyner()
        tyner.html = r'<a href="/collections/pasture-raised-beef/products/grass-fed-non-gmo-corn-fed-ground-beef-patties">          \n      <img src="//cdn.shopify.com/s/files/1/0914/6382/products/IMG_4144_Beef_patties_web_large.jpg?v=1576169110" alt="Ground beef 4 oz Patties  (100 % grass fed)" />\n    </a>\n  </div>\n\n  <div class="details">\n    <a href="/collections/pasture-raised-beef/products/grass-fed-non-gmo-corn-fed-ground-beef-patties" class="clearfix">\n      <h4 class="title">Ground beef 4 oz Patties  (100 % grass fed)</h4>\n\n      <span class="price">\n      \n      \n        \n        $ 9.99\n      \n      </span>\n  \n      <span class="shopify-product-reviews-badge" data-id="1544567491"></span>\n    </a>'
        tyner.regex()
        self.assertEqual(tyner.rawlist, [('Ground beef 4 oz Patties  (100 % grass fed)', '9.99\\n      \\n      ')])

    def test_regex_rawlist_withsavings(self):
        tyner = tynerpond.Tyner()
        tyner.html = r'<a href="/collections/pasture-raised-beef/products/top-sirloin-steak-100-grass-fed-65-75-lbs">          \n      <img src="//cdn.shopify.com/s/files/1/0914/6382/products/IMG_4119_Beef_sirloinsteak_web_large.jpg?v=1566226256" alt="Top Sirloin Steak (100% Grass-Fed)" />\n    </a>\n  </div>\n\n  <div class="details">\n    <a href="/collections/pasture-raised-beef/products/top-sirloin-steak-100-grass-fed-65-75-lbs" class="clearfix">\n      <h4 class="title">Top Sirloin Steak (100% Grass-Fed)</h4>\n\n      <span class="price">\n      \n      \n        \n          <del>$ 15.77</del>\n        \n        $ 13.77\n      \n      </span>\n  \n      <span class="shopify-product-reviews-badge" data-id="5062303107"></span>\n    </a>'
        tyner.regex()
        self.assertEqual(tyner.rawlist,[('Top Sirloin Steak (100% Grass-Fed)','15.77</del>\\n        \\n        $ 13.77\\n      \\n      ')])

    def test_regex_rawlist_noname(self):
        tyner = tynerpond.Tyner()
        tyner.html = r'<a href="/collections/pasture-raised-beef/products/top-sirloin-steak-100-grass-fed-65-75-lbs">          \n      <img src="//cdn.shopify.com/s/files/1/0914/6382/products/IMG_4119_Beef_sirloinsteak_web_large.jpg?v=1566226256" alt="Top Sirloin Steak (100% Grass-Fed)" />\n    </a>\n  </div>\n\n  <div class="details">\n    <a href="/collections/pasture-raised-beef/products/top-sirloin-steak-100-grass-fed-65-75-lbs" class="clearfix">\n      <h4 class="title"></h4>\n\n      <span class="price">\n      \n      \n        \n          <del>$ 15.77</del>\n        \n        $ 13.77\n      \n      </span>\n  \n      <span class="shopify-product-reviews-badge" data-id="5062303107"></span>\n    </a>'
        tyner.regex()
        self.assertEqual(tyner.rawlist,[('','15.77</del>\\n        \\n        $ 13.77\\n      \\n      ')])

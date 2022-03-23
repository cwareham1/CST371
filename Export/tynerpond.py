import re
# pylint: disable=line-too-long

class Tyner:

    def __init__(self, html=None):
        self.rawlist = None
        self.namelist = None
        self.prices = None
        self.savings = None
        self.html = html

    def regex(self):
        #regex
        self.rawlist = re.findall(
            r"<a.*?<h4 class=\"title\">(.*?)</h4>.*?<s1,2}\.[0-9]{2}).*?)</span>.*?</a>" #pan class=\"price\".*?((?:[0-9]{
            , self.html)

    def make_temp_lists(self):
        #make temp lists
        self.namelist = []
        self.prices = []
        self.savings = []
        for i in self.rawlist:
            self.namelist.append(i[0])
            self.prices.append(i[1])
            self.savings.append(None)

    def clean_product_names(self):
        #clean product names
        for i,_ in enumerate(self.namelist):
            self.namelist[i]  = re.search(r"[a-zA-Z\s\u2019\~\/\,\$\.\%\u002D\(\)\u20130-9]*", self.namelist[i]).group(0)

    def clean_prices_and_savings(self):
        #clean prices and savings
        for i,_ in enumerate(self.prices):
            numlist = re.findall(r"([0-9]{1,2}\.[0-9]{2}\.{0,5}).*?([0-9]{1,2}\.[0-9]{2}\.{0,5})*?", self.prices[i])
            self.prices[i] = numlist[0]
            if len(numlist) == 2:
                self.savings[i] = numlist[1]

    def prep_data(self):
        #wrapper method
        self.regex()
        self.make_temp_lists()
        self.clean_product_names()
        self.clean_prices_and_savings()

        
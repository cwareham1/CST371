import requests
import re
import csv

class Product:

    def __init__(self, name, price, savings):
        self.name = name
        self.price = price
        self.savings = savings
        self.bythepound = None
        self.hassavings = None

    def isBythepound(self):
        if re.search(r"lb", self.price):
            self.bythepound = True
        else:
            self.bythepound = False

    def cleanPrice(self):
        self.price = float(re.search(r"[0-9]{1,2}\.[0-9]{2}", self.price).group(0))

    def createSavings(self):
        if re.search(r"[0-9]{1,2}\.[0-9]{2}", self.savings):
            self.hassavings = True
        else:
            self.hassavings = False

    def typeSavings(self):
        if not self.hassavings:
            self.savings = float(0)
        else:
            float(self.savings)


    
# get the HTML first
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://joesbutchershop.com'
page = requests.get(url, headers=headers)
Html = page.text


# regex heavy lifting
rawlist = re.findall(
    r"<p>([a-zA-Z\s\u2019\u002D\(\)\u20130-9]*).*?<strong>.*?([0-9]{1,2}\.[0-9]{2}.{0,5}).*?</strong>(?:.*?([0-9]{1,2}\.[0-9]{2})*.*?)*</p>"
    ,Html)


def main():

# create products
    prodlist = []
    for item in rawlist:
        prodlist.append(
            Product(name=item[0], price=item[1], savings=item[2]))

    for product in prodlist:
        product.isBythepound()
        product.cleanPrice()
        product.createSavings()
        product.typeSavings()

# write csv file
    with open('joesproducts.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Price', 'By the pound?', 'Has savings?', 'Savings']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for object in prodlist:
            writer.writerow({'Name': object.name, 'Price': object.price, 
            'By the pound?': object.bythepound, 'Has savings?': object.hassavings, 'Savings': object.savings})

main()
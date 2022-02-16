import re
import requests
import csv

class Product:

    def __init__(self, name, price, savings):
        self.name = name
        self.price = price
        self.savings = savings

    def hasSavings(self):
        if self.savings:
            return True
        else:
            return False


# get the HTML first
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://tynerpondfarm.com/collections/in-stock'
page = requests.get(url, headers=headers)
Html = str(page.content)

#regex
rawlist = re.findall(
    r"<a.*?<h4 class=\"title\">(.*?)</h4>.*?<span class=\"price\".*?((?:[0-9]{1,2}\.[0-9]{2}).*?)</span>.*?</a>"
    , Html)


def main():
    #make temp lists
    prodlist = []
    prices = []
    savings = []
    for i in rawlist:
        prodlist.append(i[0])
        prices.append(i[1])
        savings.append(None)

    #clean product names
    for i in range(len(prodlist)):
        prodlist[i]  = re.search(r"[a-zA-Z\s\u2019\~\/\,\$\.\%\u002D\(\)\u20130-9]*", prodlist[i]).group(0)

    #clean prices and savings
    for i in range(len(prices)):
        numlist = re.findall(r"([0-9]{1,2}\.[0-9]{2}\.{0,5}).*?([0-9]{1,2}\.[0-9]{2}\.{0,5})*?", prices[i])
        prices[i] = numlist[0]
        if len(numlist) == 2:
            savings[i] = numlist[1]

    #make product objects
    products = []
    for i in range(len(prodlist)):
        products.append(Product(prodlist[i], prices[i], savings[i]))

    # write csv file
        with open('tynerproducts.csv', 'w', newline='') as file:
            fieldnames = ['Name', 'Price', 'Has savings?', 'Savings']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for object in products:
                writer.writerow({'Name': object.name, 'Price': object.price,
                'Has savings?': object.hasSavings(), 'Savings': object.savings})
main()
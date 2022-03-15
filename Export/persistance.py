import logging
import csv
import requests

#create logger object
logging.basicConfig(filename="loginfo.log",
 format='%(asctime)s %(message)s',filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#http get class
class PageGet:

    def __init__(self, url, company):

        self.url = url
        self.company =  company
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            page = requests.get(url, headers=headers)
            self.html = str(page.content)
            logger.info(self.company, 'webpage recieved')
        except:
            logger.error(self.company, 'webpage NOT recieved')

#product class
class Product:

    def __init__(self, name=None, price=None, savings=None):
        self.name = name
        self.price = price
        self.savings = savings
        if self.savings:
            self.hassavings = True
        else:
            self.hassavings = False

#product list class
class ProductList(Product):

    def __init__(self):
        super().__class__
        self.productlist = list()

#persistance class to export data to CSV
class PersistToDatabase(ProductList):

    def __init__(self, filename):
        super().__class__

        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['Name', 'Price', 'Has savings?', 'Savings']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                for object in self.productlist:
                    writer.writerow({'Name': object.name, 'Price': object.price,
                    'Has savings?': object.hassavings, 'Savings': object.savings})

                    logger.info(filename, 'created')

        except:
            logger.error(filename, 'NOT created')


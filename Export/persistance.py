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

    def __init__(self, url=None, company=None):
        self.url = url
        self.company =  str(company)
        self.html = None

    def http_get(self):
        #try:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(self.url, headers=headers)
        self.html = str(page.content)
            #logger.info(self.company, "webpage recieved")
        #except:
            #logger.error(self.company, 'webpage NOT recieved')'''

#product class
class Product:
    def __init__(self, name=None, price=None, savings=None, domain=None):
        self.name = name
        self.price = price
        self.savings = savings
        self.domain = domain
        if self.savings:
            self.hassavings = True
        else:
            self.hassavings = False


class PersistToDatabase:

    def __init__(self, filename=None):
        self.filename = str(filename)


    def persist(self, prod_list : list):
        try:
            with open(self.filename, 'w', newline='', encoding='UTF-8') as file:
                fieldnames = ['Name', 'Price', 'Has savings?', 'Savings', 'Domain']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                for i in prod_list:
                    writer.writerow({'Name': i.name, 'Price': i.price,
                    'Has savings?': i.hassavings, 'Savings': i.savings,
                    'Domain': i.domain})

                    logger.info(self.filename, 'persisted')
        # pylint: disable=bare-except
        except:
            logger.error(self.filename, 'NOT persisted')

print('')


#main
import Export.persistance
import Export.tynerpond
import Export.joesshop

tyGet = Export.persistance.PageGet(
    url='https://tynerpondfarm.com/collections/pasture-raised-beef', company='Tyner')
jsGet = Export.persistance.PageGet(url='https://joesbutchershop.com/', company= 'Joes')

tyGet.http_get()
jsGet.http_get()

productsTy = Export.tynerpond.regex(tyGet.html)
productsJs = Export.joesshop.regex(jsGet.html)

'''
for i in productsJs:
    stuff.productlist.append(
        name=i[0], price=i[1], savings=i[2], domain='Joes')
'''
print('')

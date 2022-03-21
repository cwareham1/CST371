#main
import Export.persistance
import Export.tynerpond
import Export.joesshop

product_list = []

#Tyner pond farm
ty_get = Export.persistance.PageGet(
    url='https://tynerpondfarm.com/collections/pasture-raised-beef', company='Tyner')
ty_get.http_get()
tyner = Export.tynerpond.Tyner(ty_get.html)
tyner.prep_data()

for i,_ in enumerate(tyner.namelist):
    product_list.append(Export.persistance.Product(
        name=tyner.namelist[i],
        price=tyner.prices[i],
        savings=tyner.savings[i],
        domain='Tyner'))

#Joes butcher shop

#export last
exporter = Export.persistance.PersistToDatabase(filename='products.csv')
exporter.persist(product_list)


print('')

#main
import Export.persistance
import Export.tynerpond
import Export.joesshop

product_list = []

#Tyner pond farm
ty_get = Export.persistance.PageGet(
    url='https://tynerpondfarm.com/collections/pasture-raised-beef', company='Tyner')
ty_get.http_get()
ty_list = Export.tynerpond.regex(ty_get.html)
for i,_ in enumerate(ty_list[0]):
    product_list.append(
        Export.persistance.Product(
            name=ty_list[0][i],
            price=ty_list[1][i][0],
            savings=ty_list[2][i],
            domain='Tyner')
    )
    if product_list[i].savings:
        product_list[i].savings = product_list[i].savings[0]
exporter = Export.persistance.PersistToDatabase(filename='products.csv')
exporter.persist(product_list)

#Joes butcher shop


print('')

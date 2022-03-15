#main
import Export.persistance
import Export.tynerpond
import Export.joesshop

tyGet = Export.persistance.PageGet('https://tynerpondfarm.com/collections/pasture-raised-beef', 'Tyner')
Export.tynerpond.intialParse(tyGet.html)


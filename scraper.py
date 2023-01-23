import requests
from stores.intertoys import get_intertoys_store_stock
from stores.toychamp import get_toychamp_store_stock

# Part to look for, also called Artikel Nummer
partNumberIntertoys = 1990609
# Also called bestelcode
partNumberToychamp = '01662672'

toychamp_stock = get_toychamp_store_stock(partNumberToychamp)
intertoys_stock = get_intertoys_store_stock(partNumberIntertoys)

if intertoys_stock:
    for item in intertoys_stock:
        print(f"{item['store']} - {item['stock']}")
else:
    print('Something went wrong retrieving Intertoys store stock.')

if toychamp_stock:
    for item in toychamp_stock:
        print(f"{item['store']} - {item['stock']}")
else:
    print('Something went wrong retrieving Toychamp store stock.')

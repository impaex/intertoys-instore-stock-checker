import requests
from stores.intertoys import get_intertoys_store_stock

# Part to look for, also called Artikel Nummer
partNumberIntertoys = 1990609

stock = get_intertoys_store_stock(partNumberIntertoys)

if stock:
    for item in stock:
        print(f"{item['storeNumber']} - {item['stock']}")
else:
    print('Something went wrong retrieving Intertoys store stock.')

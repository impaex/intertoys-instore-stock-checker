import requests
from bs4 import BeautifulSoup


def get_toychamp_store_stock(part_number):
    """
    This function takes in the partNumber (Bestelcode) as described on the product page on Toychamp.
    Returns list of dicts {'store': 'stock'} if request was successful, returns
    """
    # Store product page
    # So far only 24 stores in the Netherlands
    url = f'https://www.toychamp.nl/producten/open/{part_number}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 '
                      'Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = []
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find_all('table')[1]
        for entry in table.find_all('tr'):
            all_data = entry.find_all('td')
            location = all_data[0].text.strip()
            availability = all_data[1].text.strip()
            data.append({'store': location, 'stock': availability})
        return data
    else:
        return None

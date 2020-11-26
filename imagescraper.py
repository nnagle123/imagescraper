import requests
from bs4 import BeautifulSoup
import os

# url = 'https://www.airbnb.ca/s/Chala--Peru/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Chala%2C%20Peru&place_id=ChIJrUNxvJaBFZERktj1LKqaZXw&source=structured_search_input_header&search_type=autocomplete_click'

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except: 
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.find_all('img')

    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

imagedown('https://www.airbnb.ca/s/Bora~Bora--French-Polynesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJK6Wf3FO8vXYRWcWLFrt275s&query=Bora-Bora%2C%20French%20Polynesia&checkin=2021-01-06&checkout=2021-01-27&adults=2&source=search_blocks_selector_p1_flow&search_type=search_query', 'bora-bora')

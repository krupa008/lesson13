import requests
from bs4 import BeautifulSoup

url = 'https://www.onlinetrade.ru/catalogue/igry_dlya_nintendo_switch-c4094/nintendo/igra_dlya_nintendo_switch_super_mario_3d_world_bowser_s_fury_045496426927-2443870.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='catalog__displayedItem__actualPrice')


for n, i in enumerate(items, start=1):
    itemName = i.find('h1', class_='productPage__card').text.strip()

    itemPrice = i.find('h1', class_='productPage__card').text.strip()
    
    print(f'{n}:  {itemPrice} за {itemName}')
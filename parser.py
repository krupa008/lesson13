import requests
from bs4 import BeautifulSoup

url = 'https://www.onlinetrade.ru/catalogue/igry_dlya_nintendo_switch-c4094/nintendo/igra_dlya_nintendo_switch_super_mario_3d_world_bowser_s_fury_045496426927-2443870.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='catalog__displayedItem__actualPrice')

parsed_data = []

for item in items: 
    
    item_name = item.find('h1', class_='productPage__card').text.strip()
    
    parsed_data.append(item_name: "item")
print(parsed_data)
# para debuggar:  flask run --debug
import requests
from bs4 import BeautifulSoup

def get_brawler_stats(map_name):
    # URL alvo com o nome do mapa. Modifique conforme o site de dados
    url = f"https://brawlify.com/maps/detail/{map_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Ajuste a lógica de scraping conforme a estrutura da página
        stats = []
        brawler_elements = soup.find_all('div', class_='d-flex justify-content-center p-1')
        for brawler in brawler_elements:
            id = brawler.find('img')['src'].split('/')[-1].replace('.png', '').strip()
            use_rate = brawler.find('div', class_='text-primary small').get_text().replace('#', '').strip() if brawler.find('div', class_='text-primary small') else None
            star_rate = brawler.find('div', class_='text-orange small').get_text().replace('%', '').strip() if brawler.find('div', class_='text-orange small') else None

            stats.append({
                'brawler': id,
                'useRate': use_rate,
                'starRate': star_rate
            })
        return stats
    else:
        return None

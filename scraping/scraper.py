# scraping/scraper.py
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
        for brawler in soup.select('#brawlers>.row .justify-content-center>.d-flex .justify-content-center .p-1'):
            name = brawler.select_one('.name').text
            win_rate = brawler.select_one('.win-rate').text
            use_rate = brawler.select_one('.use-rate').text
            stats.append({
                'name': name,
                'win_rate': win_rate,
                'use_rate': use_rate
            })
        return stats
    else:
        return None

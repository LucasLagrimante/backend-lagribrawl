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
        # `brawler_elements` is a list that contains all the elements in the HTML content that have
        # the class name 'd-flex justify-content-center p-1'. These elements likely represent the
        # brawlers' statistics on the webpage for a specific map.
        brawler_elements = soup.find_all('div', class_='d-flex justify-content-center p-1')
        for brawler in brawler_elements:
            # Check if the brawler element has the 'src' attribute to avoid null pointer
            # references
            if brawler.find('img') and 'src' in brawler.find('img').attrs:
                id = brawler.find('img')['src'].split('/')[-1].replace('.png', '').strip()
            else:
                id = None

            # Check if the brawler element has the 'small' class to avoid null pointer
            # references
            if brawler.select("div[class*='small']"):
                win_rate = brawler.select("div[class*='small']")[1].get_text().replace('%', '').strip()
            else:
                win_rate = None

            # Check if the brawler element has the 'text-primary small' class to avoid null pointer
            # references
            if brawler.find('div', class_='text-primary small'):
                use_rate = brawler.find('div', class_='text-primary small').get_text().replace('#', '').strip()
            else:
                use_rate = None

            # Check if the brawler element has the 'text-orange small' class to avoid null pointer
            # references
            if brawler.find('div', class_='text-orange small'):
                star_rate = brawler.find('div', class_='text-orange small').get_text().replace('%', '').strip()
            else:
                star_rate = None

            stats.append({
                'brawler': int(id) if id else None,
                'useRate': int(use_rate) if use_rate else None,
                'winRate': float(win_rate) if win_rate else None,
                'starRate': float(star_rate) if star_rate else None
            })
        
        return {'data': stats}
    else:
        return {'data': None}

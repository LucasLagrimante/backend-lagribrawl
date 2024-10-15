# para debuggar:  flask run --debug
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from scraping.scraper import get_brawler_stats
from cachetools import TTLCache, cached

app = Flask(__name__)
#CORS(app)
CORS(app, origins=['https://lucaslagrimante.github.io'])

# Configurando um cache com tamanho máximo de 100 itens e tempo de expiração de 1 hora
cache = TTLCache(maxsize=100, ttl=3600)

# Função para buscar estatísticas dos brawlers, com cache aplicado
@cached(cache)
def fetch_brawler_stats(map_name):
    return get_brawler_stats(map_name)

@app.route('/api/brawlers', methods=['GET'])
def brawler_stats():
    map_name = request.args.get('map_name')
    if not map_name:
        return jsonify({'error': 'Map name is required'}), 400

    # Usando a função com cache
    stats = fetch_brawler_stats(map_name)
    if stats:
        return jsonify(stats)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
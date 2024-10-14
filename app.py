# app.py
from flask import Flask, jsonify, request
from scraping.scraper import get_brawler_stats
import os

app = Flask(__name__)

@app.route('/api/brawlers', methods=['GET'])
def brawler_stats():
    map_name = request.args.get('map_name')
    if not map_name:
        return jsonify({'error': 'Map name is required'}), 400

    stats = get_brawler_stats(map_name)
    if stats:
        return jsonify(stats)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    # O Render definirá a porta através da variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))  # Porta padrão para desenvolvimento
    app.run(host='0.0.0.0', port=port)

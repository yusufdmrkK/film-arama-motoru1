import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Ortam değişkeninden (Docker tarafından sağlanacak) API anahtarını al
OMDB_API_KEY = os.environ.get('OMDB_API_KEY') 
if not OMDB_API_KEY:
    # Anahtar bulunamazsa uyarı ver
    print("HATA: OMDB_API_KEY ortam değişkeni ayarlanmadı!")

@app.route('/search')
def search_movie():
    # URL'den 'title' parametresini al
    title = request.args.get('title') 
    
    if not title:
        return jsonify({"error": "Lütfen bir 'title' parametresi belirtin."}), 400

    # OMDb API'ye istek gönderme
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={title}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # HTTP hatalarını kontrol et
        data = response.json()
        
        # Sadece arama sonuçlarını (Search listesini) döndür
        if data.get('Search'):
            return jsonify(data['Search'])
        else:
            return jsonify({"message": f"'{title}' için sonuç bulunamadı."})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API'ye ulaşılamadı: {e}"}), 500

# Flask uygulamasını çalıştırma
if __name__ == "__main__":
    # Güvenlik nedeniyle host: 0.0.0.0, Docker'da çalışmak için gereklidir.
    app.run(host='0.0.0.0', port=5000)

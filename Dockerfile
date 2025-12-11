# Temel imaj olarak Python'un küçük ve hafif sürümünü kullan
FROM python:3.9-slim

# Çalışma dizinini /app olarak ayarla
WORKDIR /app

# requirements.txt dosyasını kopyala
COPY requirements.txt requirements.txt

# Gerekli kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Geri kalan kodları (app.py) kopyala
COPY . .

# Uygulamanın dinlediği portu belirt
EXPOSE 5000

# Konteyner başlatıldığında uygulamayı çalıştırma komutu
CMD ["python", "app.py"]

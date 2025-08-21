 Real-Time OpenCV Filters (CLAHE + Canny)

Gerçek zamanlı görüntü işleme pipeline'ı. `m` ile mod değiştir, `f` ile tam ekrana geç, `+/-` ile ölçekle, `q` ile çık.

## Kurulum
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
Çalıştırma
bash
Kopyala
Düzenle
python src/main.py --source 0 --start-mode gaussian --show-fps
Klavye
m: mod değiştir

f: tam ekran / pencere modu

+ / -: ölçek (pencere modunda)

q: çıkış

Lisans
MIT

markdown
Kopyala
Düzenle

> İpucu: Kapatma çiti (```) **tek başına bir satırda** olmalı; önünde/arkasında boşluk veya karakter kalmasın.

## 2) VS Code/Notepad ile yapmak istersen
- `README.md`’yi aç → **tamamını** yukarıdaki metinle değiştir → **UTF-8** olarak kaydet →  
  `git add README.md && git commit -m "fix: README fences" && git push`.

Bundan sonra başlıklar normal, kod blokları sadece komutlar için görünecek. İstersen demo GIF bölümünü de ekleyelim; ffmpeg komutunu README’ye yerleştiririm.







ChatGPT’ye sor

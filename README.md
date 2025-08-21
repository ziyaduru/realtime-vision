# Real-Time OpenCV Filters (CLAHE + Canny)

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

yaml
Kopyala
Düzenle
3) Editörün üstündeki **Preview** sekmesinde kontrol et (gri kutularda sadece komutlar kalmalı).  
4) Aşağıda **Commit changes** → **Commit**.

> İpucu: Kod blokları **açılırken de kapanırken de** üç ters tırnak (```) tek başına bir satırda olmalı; önünde/arkasında boşluk/karakter olmasın.

---

## Alternatif (yerelden Notepad ile)
PowerShell’de:
```powershell
cd C:\Users\tunah\Documents\GitHub\realtime-vision
notepad README.md

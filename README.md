# Real-Time OpenCV Filters (CLAHE + Canny)

Gerçek zamanlı görüntü işleme pipeline'ı. `m` ile mod değiştir, `f` ile tam ekrana geç, `+/-` ile ölçekle, `q` ile çık.

## Kurulum
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Çalıştırma
    python src/main.py --source 0 --start-mode gaussian --show-fps

## Parametreler
- `--source`: 0 (kamera) veya video yolu
- `--start-mode`: none | gaussian | median | gaussian_canny | median_canny
- `--k`: kernel (varsayılan 5)
- `--t1` / `--t2`: Canny eşikleri
- `--scale`: 0.2–3.0 (pencere modunda)
- `--fullscreen`: tam ekran
- `--show-fps`: FPS yazısı

## Klavye
- `m`: mod değiştir
- `f`: tam ekran / pencere modu
- `+` / `-`: ölçek (pencere modunda)
- `q`: çıkış

## Lisans
MIT

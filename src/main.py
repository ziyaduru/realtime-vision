import cv2
import numpy as np
import time
import argparse

MODES = ["none", "gaussian", "median", "gaussian_canny", "median_canny"]

def ensure_odd(x: int) -> int:
    return x if x % 2 == 1 else x + 1

def apply_clahe_L(bgr, clahe_obj):
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)
    L2 = clahe_obj.apply(L)
    lab2 = cv2.merge([L2, A, B])
    return cv2.cvtColor(lab2, cv2.COLOR_LAB2BGR)

def process_frame(frame, mode, k, t1, t2, clahe):
    out = frame
    if mode == "gaussian":
        out = cv2.GaussianBlur(out, (ensure_odd(k), ensure_odd(k)), 0)
        out = apply_clahe_L(out, clahe)
    elif mode == "median":
        out = cv2.medianBlur(out, ensure_odd(k))
        out = apply_clahe_L(out, clahe)
    elif mode == "gaussian_canny":
        gauss = cv2.GaussianBlur(frame, (ensure_odd(k), ensure_odd(k)), 0)
        gauss = apply_clahe_L(gauss, clahe)
        gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, t1, t2)
        base = gauss.copy()
        mask = edges != 0
        base[mask] = (0, 255, 0)
        out = base
    elif mode == "median_canny":
        median = cv2.medianBlur(frame, ensure_odd(k))
        median = apply_clahe_L(median, clahe)
        gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, t1, t2)
        base = median.copy()
        mask = edges != 0
        base[mask] = (0, 255, 0)
        out = base
    return out

def run(source, start_mode, k, t1, t2, scale, fullscreen, clahe_clip, clahe_grid, show_fps):
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise SystemExit(f"Kaynak aÃ§Ä±lamadÄ±: {source}")
    win = "kamera"
    cv2.namedWindow(win, cv2.WINDOW_NORMAL)

    if fullscreen:
        cv2.setWindowProperty(win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    clahe = cv2.createCLAHE(clipLimit=clahe_clip, tileGridSize=(clahe_grid, clahe_grid))

    mode_idx = MODES.index(start_mode) if start_mode in MODES else 0
    is_fullscreen = fullscreen
    fs_applied = False
    pressed_m = False

    last_t = time.perf_counter()
    fps = 0.0

    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break

        now = time.perf_counter()
        dt = now - last_t
        last_t = now
        inst_fps = (1.0 / dt) if dt > 0 else 0.0
        fps = fps * 0.9 + inst_fps * 0.1

        current_mode = MODES[mode_idx]
        out = process_frame(frame, current_mode, k, t1, t2, clahe)

        cv2.putText(out, f"Mode: {current_mode} (m)  k={k}  Canny=({t1},{t2})",
                    (10, 28), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2, cv2.LINE_AA)

        disp = out
        if not is_fullscreen and scale != 1.0:
            H, W = out.shape[:2]
            disp = cv2.resize(out, (int(W * scale), int(H * scale)), interpolation=cv2.INTER_AREA)

        if show_fps:
            text = f"{fps:4.1f} FPS"
            font = cv2.FONT_HERSHEY_COMPLEX
            font_scale = 0.6
            th = 2
            (tw, th_text), _ = cv2.getTextSize(text, font, font_scale, th)
            H, W = disp.shape[:2]
            x = max(10, W - tw - 10)
            y = max(10 + th_text, H - 10)
            cv2.rectangle(disp, (x-6, y-th_text-6), (x+tw+6, y+6), (0,0,0), thickness=-1)
            cv2.putText(disp, text, (x, y), font, font_scale, (255,255,255), th, cv2.LINE_AA)

        cv2.imshow(win, disp)

        if not fs_applied:
            target = cv2.WINDOW_FULLSCREEN if is_fullscreen else cv2.WINDOW_NORMAL
        try:
            cv2.setWindowProperty(win, cv2.WND_PROP_FULLSCREEN, target)
        except Exception:
            pass
        fs_applied = True

        key = cv2.waitKey(1) & 0xFF
        if key == ord('m') and not pressed_m:
            mode_idx = (mode_idx + 1) % len(MODES)
            pressed_m = True
        elif key != ord('m'):
            pressed_m = False

        if key == ord('q'):
            break
        if key == ord('f'):
            is_fullscreen = not is_fullscreen
            fs_applied = False
        if not is_fullscreen:
            if key in (ord('+'), ord('=')):
                scale = min(3.0, scale * 1.1)
            elif key in (ord('-'), ord('_')):
                scale = max(0.2, scale / 1.1)

    cap.release()
    cv2.destroyAllWindows()

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="0", help="0 (kamera) ya da video yolu")
    p.add_argument("--start-mode", default="none", choices=MODES)
    p.add_argument("--k", type=int, default=5)
    p.add_argument("--t1", type=int, default=40)
    p.add_argument("--t2", type=int, default=80)
    p.add_argument("--scale", type=float, default=1.0)
    p.add_argument("--fullscreen", action="store_true")
    p.add_argument("--clahe-clip", type=float, default=2.5)
    p.add_argument("--clahe-grid", type=int, default=6)
    p.add_argument("--show-fps", action="store_true")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    src = int(args.source) if str(args.source).isdigit() else args.source
    run(src, args.start_mode, args.k, args.t1, args.t2,
        args.scale, args.fullscreen, args.clahe_clip, args.clahe_grid, args.show_fps)

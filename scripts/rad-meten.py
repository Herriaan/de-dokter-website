#!/usr/bin/env python3
"""Meet de segmentgrenzen van het draairad (draairad.png).

Bepaalt middelpunt + straal via de alpha-bbox, sampelt radiaal en detecteert
grenzen via de hoek-gradient (mediaan over meerdere radii om bottel-graphics-
ruis te onderdrukken). Schrijft een overlay-PNG ter visuele controle.

BELANGRIJK: de rad heeft 23 segmenten, maar de ruwe gradient kan een VALSE
grens vinden midden in een graphic-druk segment (bewezen: ~114° in het
"Rocketshot Sour"-segment). Verifieer de output altijd visueel tegen de
overlay/segment-montages. De DEFINITIEVE, handmatig geverifieerde grenzen +
prijslabels staan in `index.html` (SEG_START + prizes). Draai dit script
alleen opnieuw als het rad-beeld (assets/img/draairad.png) verandert.
"""
import sys, numpy as np
from PIL import Image, ImageDraw

SRC = sys.argv[1] if len(sys.argv) > 1 else "assets/img/draairad.png"
OVERLAY_OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/rad-overlay.png"
src_img = Image.open(SRC)
alpha = np.asarray(src_img.split()[-1]) if src_img.mode == "RGBA" else None
img = src_img.convert("RGB")
arr = np.asarray(img).astype(np.int32)
H, W, _ = arr.shape

# --- center + radius via alpha (wheel = opaque, corners = transparant) ---
if alpha is not None:
    mask = alpha > 128
else:
    mask = arr.max(axis=2) > 45
ys, xs = np.where(mask)
minx, maxx, miny, maxy = xs.min(), xs.max(), ys.min(), ys.max()
cx, cy = (minx + maxx) / 2.0, (miny + maxy) / 2.0
R = min(maxx - minx, maxy - miny) / 2.0
print(f"beeld {W}x{H}  center=({cx:.1f},{cy:.1f})  R={R:.1f}  bbox=({minx},{miny},{maxx},{maxy})")

# --- radiaal sampelen ---
N = 2880  # 0.125 graden
radii = np.arange(0.34, 0.93, 0.015) * R
angs = np.deg2rad(np.arange(N) * 360.0 / N)  # CW vanaf top
# sample kleur per (hoek, radius)
samp = np.zeros((N, len(radii), 3))
for j, r in enumerate(radii):
    xs = np.clip((cx + r * np.sin(angs)).round().astype(int), 0, W - 1)
    ys = np.clip((cy - r * np.cos(angs)).round().astype(int), 0, H - 1)
    samp[:, j, :] = arr[ys, xs, :]

# hoek-gradient per radius, dan MEDIAAN over radii (robuust tegen lokale graphics)
span = 8  # ~1 graad
def circ_shift(a, s):
    return np.roll(a, -s, axis=0)
diff = np.abs(circ_shift(samp, span) - samp).sum(axis=2)  # (N, radii)
grad = np.median(diff, axis=1)  # (N,)
# lichte smoothing
k = 5
kern = np.ones(k) / k
grad_s = np.convolve(np.concatenate([grad[-k:], grad, grad[:k]]), kern, "same")[k:-k]

# --- 24 pieken met minimale onderlinge afstand ---
minsep = int(N / 24 * 0.55)  # ~8.25 graden
order = np.argsort(-grad_s)
chosen = []
for k_ in order:
    if all(min(abs(c - k_), N - abs(c - k_)) >= minsep for c in chosen):
        chosen.append(int(k_))
    if len(chosen) >= 24:
        break
chosen.sort()
bounds = [round(c * 360.0 / N, 2) for c in chosen]
widths = [round((bounds[(i + 1) % 24] - bounds[i]) % 360, 2) for i in range(24)]
print("aantal grenzen:", len(bounds))
print("grenzen (CW vanaf top):", bounds)
print("breedtes:", widths, " som=", round(sum(widths), 2))

# --- overlay ter controle ---
ov = img.copy()
dr = ImageDraw.Draw(ov)
for b in bounds:
    th = np.deg2rad(b)
    dr.line([(cx, cy), (cx + R * 1.01 * np.sin(th), cy - R * 1.01 * np.cos(th))],
            fill=(255, 0, 0), width=3)
dr.line([(cx, cy - R * 0.2), (cx, cy - R * 1.05)], fill=(255, 255, 0), width=4)  # pointer top
ov.save(OVERLAY_OUT)
print("overlay ->", OVERLAY_OUT)

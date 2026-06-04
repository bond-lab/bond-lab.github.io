#!/usr/bin/env python3

from math import cos, sin, pi
from pathlib import Path
import sys
from PIL import Image, ImageDraw

# ----------------------------
# Config
# ----------------------------

SIZE = 1024
CENTER = SIZE // 2

OUTER_MARGIN = 40
RING_WIDTH = 72      # thick ring (your latest preference)

PADDING = 100        # space between stars and ring
STAR_SCALE = 2.60    # enlarged stars


# ----------------------------
# Australian flag geometry
# ----------------------------

W = 1.0
center_fly_x = 1.5 * W
center_fly_y = 0.5 * W

stars_flag = [
    ("Alpha",   center_fly_x,         1 - 1/6,      7, 1/14),
    ("Beta",    center_fly_x - 1/4,   0.5 - 1/16,   7, 1/14),
    ("Gamma",   center_fly_x,         1/6,          7, 1/14),
    ("Delta",   center_fly_x + 2/9,   0.5 - 31/240, 7, 1/14),
    ("Epsilon", center_fly_x + 1/10,  0.5 + 1/24,   5, 1/24),
]


# ----------------------------
# CLI handling
# ----------------------------

out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "southern_cross_kamon.png"
svg_path = out_dir / "southern_cross_kamon.svg"
ico_path = out_dir / "southern_cross_kamon.ico"


# ----------------------------
# Geometry helpers
# ----------------------------

ring_radius = CENTER - OUTER_MARGIN
usable_radius = ring_radius - PADDING

max_extent = 0.0
for _, x, y, _, outer_d in stars_flag:
    dx = abs(x - center_fly_x)
    dy = abs(y - center_fly_y)
    r = outer_d / 2
    max_extent = max(max_extent, dx + r, dy + r)

scale = usable_radius / max_extent


def star_points(cx, cy, points, r_outer, r_inner, rotation_deg=-90):
    pts = []
    rotation = pi * rotation_deg / 180.0
    step = pi / points

    for i in range(points * 2):
        angle = rotation + i * step
        r = r_outer if i % 2 == 0 else r_inner
        x = cx + r * cos(angle)
        y = cy + r * sin(angle)
        pts.append((x, y))

    return pts


# ----------------------------
# Render PNG
# ----------------------------

img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# ring
draw.ellipse(
    (OUTER_MARGIN, OUTER_MARGIN, SIZE - OUTER_MARGIN, SIZE - OUTER_MARGIN),
    outline="black",
    width=RING_WIDTH,
)

# stars
for _, x, y, points, outer_d in stars_flag:
    dx = (x - center_fly_x) * scale
    dy = (y - center_fly_y) * scale

    cx = CENTER + dx
    cy = CENTER + dy

    r_outer = (outer_d / 2) * scale * STAR_SCALE
    r_inner = r_outer * (4/9)

    pts = star_points(cx, cy, points, r_outer, r_inner)
    draw.polygon(pts, fill="black")

# save PNG + ICO
img.save(png_path)
img.save(ico_path, sizes=[(256,256), (128,128), (64,64), (32,32)])


# ----------------------------
# Render SVG
# ----------------------------

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">',
    f'  <rect width="100%" height="100%" fill="white"/>',
    f'  <circle cx="{CENTER}" cy="{CENTER}" r="{ring_radius}" fill="none" stroke="black" stroke-width="{RING_WIDTH}"/>'
]

for _, x, y, points, outer_d in stars_flag:
    dx = (x - center_fly_x) * scale
    dy = (y - center_fly_y) * scale

    cx = CENTER + dx
    cy = CENTER + dy

    r_outer = (outer_d / 2) * scale * STAR_SCALE
    r_inner = r_outer * (4/9)

    pts = star_points(cx, cy, points, r_outer, r_inner)

    path = "M " + " ".join(
        [f"{pts[0][0]:.2f},{pts[0][1]:.2f}"] +
        [f"L {px:.2f},{py:.2f}" for px, py in pts[1:]]
    ) + " Z"

    svg_parts.append(f'  <path d="{path}" fill="black"/>')

svg_parts.append("</svg>")

with open(svg_path, "w") as f:
    f.write("\n".join(svg_parts))


# ----------------------------
# Done
# ----------------------------

print("Created:")
print(" ", png_path)
print(" ", svg_path)
print(" ", ico_path)

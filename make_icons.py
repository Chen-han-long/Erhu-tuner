#!/usr/bin/env python3
"""生成 PWA 图标（需 Pillow）"""
from PIL import Image, ImageDraw, ImageFont
import os

SIZE = 512
OUT = "icons"
os.makedirs(OUT, exist_ok=True)

img = Image.new("RGBA", (SIZE, SIZE), (10, 10, 40, 255))
draw = ImageDraw.Draw(img)

# 背景圆
draw.ellipse([20, 20, SIZE-20, SIZE-20], fill=(20, 20, 60, 255), outline=(255, 215, 0, 255), width=6)

# 文字
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", 80)
except:
    font = ImageFont.load_default()

text = "🎻"
draw.text((SIZE//2, SIZE//2), text, font=font, fill=(255,215,0,255), anchor="mm")

for s in [192, 512]:
    img.save(os.path.join(OUT, f"icon-{s}.png"), "PNG")
print("Done")

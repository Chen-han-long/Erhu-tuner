from PIL import Image, ImageDraw, ImageFont
import os

OUT = "icons"
os.makedirs(OUT, exist_ok=True)

def make_icon(size, path):
    img = Image.new("RGBA", (size, size), (26, 26, 46, 255))
    d = ImageDraw.Draw(img)

    # 圆形底
    m = size // 10
    d.ellipse([m, m, size - m, size - m], fill=(45, 45, 80, 255), outline=(255, 215, 0, 255), width=max(size//64, 2))

    # 二胡简笔画：两根弦 + 琴筒
    cx = size // 2
    # 琴筒（椭圆）
    r = size // 5
    d.ellipse([cx - r, size//2 - r//2, cx + r, size//2 + r//2], fill=(120, 80, 50, 255))
    # 琴杆
    bar_w = max(size//40, 2)
    d.rectangle([cx - bar_w, size//6, cx + bar_w, size//2 + r//2], fill=(160, 110, 60, 255))
    # 内外弦（两根细线）
    for offset in (-bar_w*2, bar_w*2):
        x = cx + offset
        d.line([(x, size//6), (x, size//2 + r//3)], fill=(220, 220, 220, 255), width=max(size//120, 1))

    # 文字
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", size//8)
    except Exception:
        font = ImageFont.load_default()
    text = "二胡调音"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((size - tw)//2, size - size//4 - th//2), text, fill=(255, 215, 0, 255), font=font)

    img.save(path, "PNG")
    print("saved", path)

make_icon(192, f"{OUT}/icon-192.png")
make_icon(512, f"{OUT}/icon-512.png")

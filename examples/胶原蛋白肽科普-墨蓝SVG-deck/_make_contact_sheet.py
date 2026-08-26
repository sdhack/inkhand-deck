"""Contact sheet builder for 胶原蛋白肽科普-墨蓝SVG-deck (7 pages, 9:16).

本地 SVG + 无头 Chrome 渲染版本（无水印 / 不花 credits / 风格锁死）。
Reads 7 renamed PNGs from the deck folder and assembles a 4x2 grid:
  Row 1: P1-P4   Row 2: P5-P7 + note slot
Each cell: thumbnail (9:16) + caption (page title + 墨仔 role).
Writes: contact-sheet-墨蓝SVG.png
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

DECK = Path(r"D:/Users/Gao Ming/Documents/WB抖音视频号抓取260815/胶原蛋白肽科普-墨蓝SVG-deck")

PAGES = [
    ("01-封面.png", "P1 封面",   "墨仔端天平掂量问题"),
    ("02-争论.png", "P2 争论",   "墨仔居中当裁判"),
    ("03-误区.png", "P3 误区",   "墨仔两臂举 X 猪蹄/面膜"),
    ("04-真相.png", "P4 真相",   "墨仔喂细胞 · 刺激自造胶原"),
    ("05-证据.png", "P5 证据",   "墨仔坐地记笔记 + 共识 21RCT"),
    ("06-避坑.png", "P6 避坑",   "墨仔举警示牌指伪科技"),
    ("07-落点.png", "P7 落点",   "墨仔右下签名 + 三判断"),
]

# 9:16 thumb
THUMB_W = 360
THUMB_H = 640
PAD = 24
COLS = 4
TITLE_H = 110
FOOTER_H = 180
GRID_W = COLS * THUMB_W + (COLS + 1) * PAD
GRID_H = 2 * THUMB_H + 3 * PAD
SHEET_W = GRID_W
SHEET_H = TITLE_H + GRID_H + FOOTER_H + 24   # +24 clean gap before footer

PAPER = (251, 250, 245)   # #FBFAF5
INK = (52, 70, 94)        # #34465E
INK_BLUE = (35, 56, 107)  # #23386B
SOFT = (180, 188, 198)
NOTE_BG = (244, 239, 230)
WARN = (200, 80, 60)

# Try to find a CJK font; fallback to default
def get_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ]
    for f in candidates:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

font_title  = get_font(30, bold=True)
font_sub    = get_font(18)
font_page   = get_font(20, bold=True)
font_role   = get_font(15)
font_footer = get_font(15)
font_note   = get_font(16, bold=True)

sheet = Image.new("RGB", (SHEET_W, SHEET_H), PAPER)
draw = ImageDraw.Draw(sheet)

# Title
draw.text((PAD, 24), "胶原蛋白肽科普 · 墨蓝墨仔 SVG 竖版 deck", font=font_title, fill=INK_BLUE)
draw.text((PAD, 64), "inkhand-deck · 7P · 9:16 · 本地 SVG + Chrome 无头渲染 · 无水印",
          font=font_sub, fill=INK)
draw.line([(PAD, 100), (PAD + 360, 100)], fill=(160, 200, 230), width=2)

# Grid
for idx, (fname, page_lbl, role_lbl) in enumerate(PAGES):
    row = idx // COLS
    col = idx % COLS
    x = PAD + col * (THUMB_W + PAD)
    y = TITLE_H + PAD + row * (THUMB_H + PAD)
    img = Image.open(DECK / fname).convert("RGB")
    img.thumbnail((THUMB_W, THUMB_H), Image.LANCZOS)
    # center within cell
    cx = x + (THUMB_W - img.width) // 2
    cy = y + (THUMB_H - img.height) // 2
    sheet.paste(img, (cx, cy))
    # caption strip below thumb
    cap_y = y + THUMB_H + 4
    draw.text((x, cap_y), page_lbl, font=font_page, fill=INK_BLUE)
    draw.text((x, cap_y + 26), role_lbl, font=font_role, fill=INK)

# Note slot (P8 position)
row, col = 1, 3
x = PAD + col * (THUMB_W + PAD)
y = TITLE_H + PAD + row * (THUMB_H + PAD)
note_box = Image.new("RGB", (THUMB_W, THUMB_H), NOTE_BG)
nd = ImageDraw.Draw(note_box)
nd.rectangle([(0, 0), (THUMB_W - 1, THUMB_H - 1)], outline=SOFT, width=2)
nd.text((18, 18), "注意事项", font=font_note, fill=INK_BLUE)
notes = [
    "· 本地渲染链路：",
    "  SVG → Chrome 无头",
    "  1080×1920 一次性出图",
    "  无水印 / 不花 credits",
    "",
    "· 风格锁（hex 锁死）：",
    "  #23386B 墨身体",
    "  #34465E 墨线",
    "  #A3C9A8 绿芽",
    "  #E07B39 墨芯",
    "  #FBFAF5 纸",
    "",
    "· 字：STKaiti/Kaiti",
    "  楷体手写感（Windows）",
    "",
    "· 小瑕疵：",
    "  P3 猪蹄/面膜 label",
    "  被大红 X 覆盖一点点",
    "  不影响阅读，可微调",
    "  X 位置避让。",
]
ly = 50
for line in notes:
    color = WARN if line.startswith("•") and ("瑕疵" in line or "重复" in line) else INK
    nd.text((18, ly), line, font=font_footer, fill=color)
    ly += 22
sheet.paste(note_box, (x, y))

# Footer
fy = TITLE_H + GRID_H + 24
draw.line([(PAD, fy - 6), (SHEET_W - PAD, fy - 6)], fill=SOFT, width=1)
draw.text((PAD, fy + 6),
          "源文案: 抖音-胶原蛋白肽科普-口播-2608262214.md  |  生产: 本地 SVG (1080×1920) + Chrome --headless  |  用途: 抖音口播配图 / 视频封面拼图",
          font=font_footer, fill=INK)
draw.text((PAD, fy + 30),
          "墨蓝主题: #23386B body · #34465E line · #FBFAF5 paper  |  墨仔签名: 软墨泪滴 + sage 芽 + 红橙墨芯 + 死鱼眼",
          font=font_footer, fill=INK)
draw.text((PAD, fy + 54),
          "对比上一版 ImageGen: 无水印 ✓ / 不花 credits ✓ / 文字精确 ✓ / 风格锁死 ✓ / 批量可控 ✓",
          font=font_footer, fill=INK_BLUE)

out = DECK / "contact-sheet-墨蓝SVG.png"
sheet.save(out, "PNG", optimize=True)
print(f"saved: {out}  size={sheet.size}  bytes={out.stat().st_size}")

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm

# A4縦のCanvasを準備 --- (*1)
w, h = portrait(A4)
cv = canvas.Canvas('hougansi.pdf', pagesize=(w, h))
# 方眼紙のマスを計算 --- (*2)
rsize = 12*mm  # マスのサイズ
margin_x, margin_y = (10*mm, 10*mm)
count_x = int((w - margin_x*2) / rsize)
count_y = int((h - margin_y*2) / rsize)
top_x = int((w - count_x*rsize) / 2)
top_y = margin_y
bottom_x = top_x + count_x * rsize
bottom_y = top_y + count_y * rsize

# ヘッダに英数文字を描画 --- (*3)
cv.setFont("Times-Roman", 10)
cv.drawString(top_x, bottom_y+5, "A4 Graph Paper 12mm")
# 線の色をRGBで指定 --- (*4)
cv.setStrokeColorRGB(0.4, 0.6, 0.8)
# 線のサイズを指定
cv.setLineWidth(1)
# 方眼紙の線を描画 --- (*5)
for y in range(count_y+1):
  ry = y * rsize + top_y
  cv.line(top_x, ry, bottom_x, ry)
for x in range(count_x+1):
  rx = x * rsize + top_x
  cv.line(rx, top_y, rx, bottom_y)
# ファイルに保存
cv.showPage()
cv.save()

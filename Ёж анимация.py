import math
import graph

graph.canvasSize(1000, 700)
def trg(x, y, f):
    x3 = X + ((x - 400) * math.cos(F[0] / 57.296) - (y - 450) * math.sin(F[0] / 57.296))*Size        # F, f - углы поворота ежа и эллипса
    y = Y + ((x - 400) * math.sin(F[0] / 57.296) + (y - 450) * math.cos(F[0] / 57.296))*Size
    x = x3
    f -= F[0]
    x1 = 50 * Size * math.sin((5 + f)/57)
    x2 = 50 * Size * math.sin((-5 + f)/57)
    y1 = 50 * Size * math.cos((5 + f)/57)
    y2 = 50 * Size * math.cos((-5 + f)/57)
    return graph.polygon([(x, y),(x + x1, y + y1),(x + x2, y + y2)])

def el(x, y, a, b, f):
    x1 = X + ((x - 400)*math.cos(F[0] / 57.296) - (y - 450)*math.sin(F[0] / 57.296))*Size
    y = Y + ((x - 400)*math.sin(F[0] / 57.296) + (y - 450)*math.cos(F[0] / 57.296))*Size
    x = x1
    a *= Size
    b *= Size
    f += F[0]
    el = []
    for i in range(360):
        m = a*math.cos(i/57.296)
        n = b*math.sin(i/57.296)
        el.append((x + m*math.cos(f/57.296) - n*math.sin(f/57.296), y + m*math.sin(f/57.296) + n*math.cos(f/57.296)))
    return graph.polygon(el)


def Esh():
    for ob in yozh:
        graph.deleteObject(ob)
    if t[0] < 100:
        F[0] +=1
        t[0] +=1
    graph.penColor(200, 200, 200)
    graph.penSize(1)

    graph.brushColor(100,100,100)
    yozh.append(el(470, 460, 7, 5, 0))
    yozh.append(el(400, 450, 70, 25, 0))
    yozh.append(el(458, 469, 9, 5, 0))
    yozh.append(el(345, 469, 12, 5, 0))
    yozh.append(el(330, 460, 10, 5, 0))
    graph.penColor(0,0,0)
    graph.brushColor(50,50,50)
    yozh.append(trg(310, 420, 50))
    yozh.append(trg(305, 430, 60))
    yozh.append(trg(310, 420, 50))
    yozh.append(trg(315, 410, 50))
    yozh.append(trg(330, 390, 50))
    yozh.append(trg(345, 390, 50))
    yozh.append(trg(332, 390, 20))
    yozh.append(trg(340, 392, 20))
    yozh.append(trg(350, 384, 20))
    yozh.append(trg(360, 386, 20))
    yozh.append(trg(370, 386, 20))
    yozh.append(trg(380, 387, 20))
    yozh.append(trg(390, 389, 20))
    yozh.append(trg(400, 392, 20))
    yozh.append(trg(410, 396, 20))
    yozh.append(trg(420, 400, 20))
    yozh.append(trg(430, 405, -20))
    yozh.append(trg(425, 420, -20))
    yozh.append(trg(317, 405, 20))
    yozh.append(trg(325, 416, 20))
    yozh.append(trg(335, 399, 20))
    yozh.append(trg(345, 388, 20))
    yozh.append(trg(355, 391, 20))
    yozh.append(trg(365, 395, 20))
    yozh.append(trg(370, 400, 20))
    yozh.append(trg(385, 405, 20))
    yozh.append(trg(390, 410, 20))
    yozh.append(trg(400, 415, -20))
    yozh.append(trg(410, 390, -20))
    yozh.append(trg(420, 390, -20))
    yozh.append(trg(332, 390, 20))
    yozh.append(trg(335, 392, 20))
    yozh.append(trg(345, 384, 20))
    yozh.append(trg(355, 386, 20))
    yozh.append(trg(360, 386, 20))
    yozh.append(trg(365, 387, 20))
    yozh.append(trg(370, 389, 20))
    yozh.append(trg(380, 392, 20))
    yozh.append(trg(390, 396, 20))
    yozh.append(trg(400, 400, 20))
    yozh.append(trg(410, 405, 20))
    yozh.append(trg(420, 415, 20))
    yozh.append(trg(455, 405, 20))
    yozh.append(trg(445, 405, 20))
    yozh.append(trg(440, 400, 20))
    yozh.append(trg(450, 405, 20))
    yozh.append(trg(435, 400, 20))
    yozh.append(trg(465, 405, -20))
    yozh.append(trg(460, 400, -20))
    yozh.append(trg(470, 405, -20))
    yozh.append(trg(455, 400, -20))

    graph.penColor(200,200,200)
    graph.brushColor(100,100,100)
    yozh.append(el(471, 445, 18, 10, 0))
    graph.brushColor("black")
    yozh.append(el(471, 444, 3, 3, 0))
    yozh.append(el(480, 441, 3, 3, 0))
    yozh.append(el(489, 445, 2, 2, 0))
    graph.brushColor("white")
    yozh.append(el(390, 400, 20, 8, -70))
    graph.brushColor(200, 120,60)
    yozh.append(el(340, 410, 14, 18, 0))
    graph.brushColor("red")
    yozh.append(el(430, 410, 19, 20, 0))
    yozh.append(el(398, 380, 8, 25, -70))
    graph.brushColor("white")
    yozh.append(el(396, 382, 2, 3, -60))
    yozh.append(el(385, 380, 1, 2, -80))
    yozh.append(el(410, 380, 2, 2, 0))
    yozh.append(el(415, 387, 1, 2, -70))
    yozh.append(el(391, 375, 1, 3, -70))
    yozh.append(el(379, 374, 2, 3, -60))

    graph.brushColor(50, 50, 50)
    graph.penColor("black")

    yozh.append(trg(328, 385, 20))
    graph.brushColor(200, 120,60)
    graph.penColor("grey")
    yozh.append(el(355, 415, 14, 18, 0))

    graph.brushColor(50, 50, 50)
    graph.penColor("black")
    yozh.append(trg(340, 420, 20))
    yozh.append(trg(345, 420, 20))
    yozh.append(trg(350, 420, 20))
    yozh.append(trg(355, 420, 20))
    yozh.append(trg(360, 420, 20))
    yozh.append(trg(330, 417, 20))
    yozh.append(trg(333, 414, 20))
    yozh.append(trg(365, 425, 20))
    yozh.append(trg(370, 425, 20))

    yozh.append(trg(400, 420, 0))
    yozh.append(trg(410, 424, 0))
    yozh.append(trg(400, 400, 0))
    yozh.append(trg(390, 420, 0))
    yozh.append(trg(380, 400, 0))
    yozh.append(trg(385, 390, 0))
    yozh.append(trg(370, 393, 0))
    yozh.append(trg(393, 395, 0))
    yozh.append(trg(420, 399, 0))
    yozh.append(trg(433, 400, 0))
    yozh.append(trg(440, 390, 0))
    yozh.append(trg(365, 410, 0))

    yozh.append(trg(405, 420, -20))
    yozh.append(trg(410, 420, -20))
    yozh.append(trg(420, 425, -20))
    yozh.append(trg(425, 420, -20))
    yozh.append(trg(430, 425, -20))
    yozh.append(trg(435, 420, -20))
    yozh.append(trg(440, 425, -20))
    yozh.append(trg(445, 425, -20))
    yozh.append(trg(450, 420, -20))
    yozh.append(trg(455, 415, -20))
    yozh.append(trg(460, 410, -20))
    yozh.append(trg(460, 420, -20))
    yozh.append(trg(465, 415, -20))

X = 200
Y = 300
Size = 1.5
F = [-50]
t = [0]
yozh = []

graph.brushColor(150, 150, 150)
graph.rectangle(0, 350, 500, 600)
graph.brushColor(100, 200, 140)
graph.rectangle(0, 0, 500, 350)
graph.brushColor(250, 200, 0)
graph.rectangle(0, 0, 30, 380)
graph.rectangle(340, 0, 390, 385)
graph.rectangle(460, 0, 490, 420)
graph.rectangle(50, 0, 150, 600)

graph.onTimer(Esh, 50)

graph.run()































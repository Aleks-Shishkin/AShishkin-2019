import graph
import math

graph.canvasSize(1000, 700)
def trg(x, y, f):
    x3 = X + ((x - 400) * math.cos(F / 57.296) - (y - 450) * math.sin(F / 57.296))*Size
    y = Y + ((x - 400) * math.sin(F / 57.296) + (y - 450) * math.cos(F / 57.296))*Size
    x = x3
    f -= F
    x1 = 50 * Size * math.sin((5 + f)/57)
    x2 = 50 * Size * math.sin((-5 + f)/57)
    y1 = 50 * Size * math.cos((5 + f)/57)
    y2 = 50 * Size * math.cos((-5 + f)/57)
    graph.polygon([(x, y),(x + x1, y + y1),(x + x2, y + y2)])

def el(x, y, a, b, f):
    x1 = X + ((x - 400)*math.cos(F / 57.296) - (y - 450)*math.sin(F / 57.296))*Size
    y = Y + ((x - 400)*math.sin(F / 57.296) + (y - 450)*math.cos(F / 57.296))*Size
    x = x1
    a *= Size
    b *= Size
    f += F
    el = []
    for i in range(360):
        m = a*math.cos(i/57.296)
        n = b*math.sin(i/57.296)
        el.append((x + m*math.cos(f/57.296) - n*math.sin(f/57.296), y + m*math.sin(f/57.296) + n*math.cos(f/57.296)))
    graph.polygon(el)


def Esh():
    graph.penColor(200, 200, 200)
    graph.penSize(1)

    graph.brushColor(100,100,100)
    el(470, 460, 7, 5, 0)
    el(400, 450, 70, 25, 0)
    el(458, 469, 9, 5, 0)
    el(345, 469, 12, 5, 0)
    el(330, 460, 10, 5, 0)
    graph.penColor(0,0,0)
    graph.brushColor(50,50,50)
    trg(310, 420, 50)
    trg(305, 430, 60)
    trg(310, 420, 50)
    trg(315, 410, 50)
    trg(330, 390, 50)
    trg(345, 390, 50)
    trg(332, 390, 20)
    trg(340, 392, 20)
    trg(350, 384, 20)
    trg(360, 386, 20)
    trg(370, 386, 20)
    trg(380, 387, 20)
    trg(390, 389, 20)
    trg(400, 392, 20)
    trg(410, 396, 20)
    trg(420, 400, 20)
    trg(430, 405, -20)
    trg(425, 420, -20)
    trg(317, 405, 20)
    trg(325, 416, 20)
    trg(335, 399, 20)
    trg(345, 388, 20)
    trg(355, 391, 20)
    trg(365, 395, 20)
    trg(370, 400, 20)
    trg(385, 405, 20)
    trg(390, 410, 20)
    trg(400, 415, -20)
    trg(410, 390, -20)
    trg(420, 390, -20)
    trg(332, 390, 20)
    trg(335, 392, 20)
    trg(345, 384, 20)
    trg(355, 386, 20)
    trg(360, 386, 20)
    trg(365, 387, 20)
    trg(370, 389, 20)
    trg(380, 392, 20)
    trg(390, 396, 20)
    trg(400, 400, 20)
    trg(410, 405, 20)
    trg(420, 415, 20)
    trg(455, 405, 20)
    trg(445, 405, 20)
    trg(440, 400, 20)
    trg(450, 405, 20)
    trg(435, 400, 20)
    trg(465, 405, -20)
    trg(460, 400, -20)
    trg(470, 405, -20)
    trg(455, 400, -20)

    graph.penColor(200,200,200)
    graph.brushColor(100,100,100)
    el(471, 445, 18, 10, 0)
    graph.brushColor("black")
    el(471, 444, 3, 3, 0)
    el(480, 441, 3, 3, 0)
    el(489, 445, 2, 2, 0)
    graph.brushColor("white")
    el(390, 400, 20, 8, -70)
    graph.brushColor(200, 120,60)
    el(340, 410, 14, 18, 0)
    graph.brushColor("red")
    el(430, 410, 19, 20, 0)
    el(398, 380, 8, 25, -70)
    graph.brushColor("white")
    el(396, 382, 2, 3, -60)
    el(385, 380, 1, 2, -80)
    el(410, 380, 2, 2, 0)
    el(415, 387, 1, 2, -70)
    el(391, 375, 1, 3, -70)
    el(379, 374, 2, 3, -60)

    graph.brushColor(50, 50, 50)
    graph.penColor("black")

    trg(328, 385, 20)
    graph.brushColor(200, 120,60)
    graph.penColor("grey")
    el(355, 415, 14, 18, 0)

    graph.brushColor(50, 50, 50)
    graph.penColor("black")
    trg(340, 420, 20)
    trg(345, 420, 20)
    trg(350, 420, 20)
    trg(355, 420, 20)
    trg(360, 420, 20)
    trg(330, 417, 20)
    trg(333, 414, 20)
    trg(365, 425, 20)
    trg(370, 425, 20)

    trg(400, 420, 0)
    trg(410, 424, 0)
    trg(400, 400, 0)
    trg(390, 420, 0)
    trg(380, 400, 0)
    trg(385, 390, 0)
    trg(370, 393, 0)
    trg(393, 395, 0)
    trg(420, 399, 0)
    trg(433, 400, 0)
    trg(440, 390, 0)
    trg(365, 410, 0)

    trg(405, 420, -20)
    trg(410, 420, -20)
    trg(420, 425, -20)
    trg(425, 420, -20)
    trg(430, 425, -20)
    trg(435, 420, -20)
    trg(440, 425, -20)
    trg(445, 425, -20)
    trg(450, 420, -20)
    trg(455, 415, -20)
    trg(460, 410, -20)
    trg(460, 420, -20)
    trg(465, 415, -20)

X = 200
Y = 300
Size = 1.5
F = -50

graph.brushColor(150, 150, 150)
graph.rectangle(0, 350, 500, 600)
graph.brushColor(100, 200, 140)
graph.rectangle(0, 0, 500, 350)
graph.brushColor(250, 200, 0)
graph.rectangle(0, 0, 30, 380)
graph.rectangle(340, 0, 390, 385)
graph.rectangle(460, 0, 490, 420)
graph.rectangle(50, 0, 150, 600)

Esh()

graph.run()

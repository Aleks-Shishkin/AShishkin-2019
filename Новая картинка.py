from graph import *

windowSize(900,1400)
canvasSize(792,1200)
def leps(a,b,x0,y0):
	x=2*a
	y=b
	l=[(x0,y0+b)]
	for i in range(a):
		x-=1
		y=((1-x**2/(a**2))*b**2)**0.5
		l.append((x+x0,y+y0))
	for i in range(a):
		x-=1
		y=((1-x**2/(a**2))*b**2)**0.5
		l.append((x+x0,y+y0))
	for i in range(a):
		x+=1
		y=-((1-x**2/(a**2))*b**2)**0.5
		l.append((x+x0,y+y0))
	for i in range(a):
		x+=1
		y=-((1-x**2/(a**2))*b**2)**0.5
		l.append((x+x0,y+y0))
	polygon(l)

def dom(x,y):
	p3=[(15+x,22+y), (171+x,22+y), (171+x,736+y), (15+x,736+y)]
	polygon(p3)
def okno(x,y):
	p5=[(320+x,880+y),(340+x,880+y),(340+x,890+y), (320+x,890+y)]
	polygon(p5)

penColor("#b7c4c8")
brushColor("#b7c4c8")
p1=[(0,0),(792,0),(792,710), (0,710)]
polygon(p1)

penColor("#536c67")
brushColor("#536c67")
p2 = [(0, 715), (792, 715), (792, 1200), (0,1200)]
polygon(p2)

penColor("#b7c8c4")
brushColor("#b7c8c4")
circle(370, 1500, 650)

penColor("#93a7ac")
brushColor("#93a7ac")

dom(0,0)
penColor("#93aca7")
brushColor("#93aca7")
dom(198,40)
penColor("#b7c8c4")
brushColor("#b7c8c4")
dom(105,100)
penColor("#dbe3e2")
brushColor("#dbe3e2")
dom(590,0)
penColor("#6f918a")
brushColor("#6f918a")
dom(505,120)

penColor("#00ccff")
brushColor("#00ccff")
p3=[(260,900),(533,900),(533,930), (260,930)]
polygon(p3)
p4=[(310,900),(410,900),(410,870), (310,870)]
polygon(p4)
penColor("#d5f6ff")
brushColor("#d5f6ff")
okno(0,0)
okno(50,0)
penColor("#00222b")
brushColor("#00222b")
p6=[(260,925),(260,915),(230,915), (230,925)]
polygon(p6)
penColor("#a8baba")
brushColor("#a8baba")

run()
import tkinter as tk
import time
import math
from random import randrange as rnd, choice


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('900x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self):
        self.x = 30
        self.y = 400
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.hit = 0
        self.color = choice(['blue', 'green', 'red', 'orange', 'grey'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def get_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def hittest(self, obj):
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 < (obj.r + self.r) ** 2 :
            return True
        else:
            return False

    def move(self):
        self.vy -= 1
        if self.x > 900 or self.x < 0 :
            self.vx = - self.vx
            self.hit +=1
        if self.y > 600 or self.y <0 :
            self.vy = - self.vy
            self.hit +=1
        self.x += self.vx
        self.y -= self.vy
        self.get_coords()
        canv.itemconfig(self.id, fill=self.color)
        if self.hit > 5 :
            canv.delete(self.id)
            balls.remove(self)


class mortira():
    def __init__ (self):
        self.power = 50
        self.on = 0
        self.ang = 0
        self.id = canv.create_line(30,400,80,400,width = 20) 

    def fire_start(self, event):
        self.on = 1

    def fire_end(self, event):
        """Вылет мяча"""
        global balls, fire
        fire += 1
        new_ball = ball()
        if abs(event.y - 400) < 10*abs(event.x - 30):
                self.ang = math.atan((event.y - 400) / (event.x - 30))
        else:
                self.ang = abs(event.y - 400)/(event.y - 400)*math.atan(10)
        new_ball.vx = self.power * math.cos(self.ang)
        new_ball.vy = - self.power * math.sin(self.ang)
        balls += [new_ball]
        self.on = 0
        self.power = 50

    def targetting(self, event=0):
        """Прицеливание"""
        if event:
            if abs(event.y - 400) < 10*abs(event.x - 30):
                self.ang = math.atan((event.y - 400) / (event.x - 30))
            else:
                self.ang = abs(event.y - 400)/(event.y - 400)*math.atan(10)
        if self.on:
            canv.itemconfig(self.id, fill='green')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 30, 400,
                    30 + max(self.power, 50) * math.cos(self.ang),
                    400 + max(self.power, 50) * math.sin(self.ang)
                    )

    def power_grow(self):
        if self.on:
            if self.power < 100:
                self.power += 1
            canv.itemconfig(self.id, fill='green')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 0
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """Появляется новая цель. """
        self.live = 1
        x = self.x = rnd(300, 880)
        y = self.y = rnd(100, 570)
        r = self.r = rnd(2, 50)
        color = self.color = choice(['red', 'grey'])

        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        canv.coords(self.id, -10, -10, 0, 0)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t3 = target()
screen3 = canv.create_text(400, 300, text='', font='28')
m1 = mortira()
fire = 0
balls = []


def new_game(event=''):
    global mortira, t1, screen1, balls, fire
    t3.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', m1.fire_start)
    canv.bind('<ButtonRelease-1>', m1.fire_end)
    canv.bind('<Motion>', m1.targetting)
    while t3.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t3) and t3.live:
                t3.live = 0
                t3.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen3, text='Количество выстрелов для уничтожения: ' + str(fire))
        canv.update()
        time.sleep(0.04)
        m1.targetting()
        m1.power_grow()
    canv.itemconfig(screen3, text='')
    canv.delete(mortira)
    root.after(670, new_game)


new_game()

root.mainloop()

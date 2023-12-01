from screen import Screen
import math

dragObj = False
def clickCallback(event):
    global dragObj

    distance = math.sqrt((event.x - x)**2 + (event.y - y)**2)
    if distance <= 60:
        dragObj = True

def releaseCallback(event):
    global dragObj
    global physics
    global vy

    dragObj = False
    physics = True
    vy = 0

def dragCallback(event):
    global dragObj
    global physics
    global x
    global y

    if dragObj:
        physics = False
        x = event.x
        y = event.y
    else:
        physics = True

screen = Screen(clickCallback, releaseCallback, dragCallback)
x = screen.SCR_WIDTH/2
y = screen.SCR_HEIGHT/2
physics = True
vx = 3
vy = 1

r = 20
# elasticity
ey = -1.5
ex = -1
# f is proportional to rho and proportional to v^2
rho = 10
const = 0.001
f = const * rho
while True:
    if physics:
        x += vx
        y += vy 
        vy+=screen.FRAME_TIME*9.81
        if (y + r >= screen.SCR_HEIGHT and vy>0) or (y - r <= 0 and vy<0):
            vy /= ey
        if (x + r >= screen.SCR_WIDTH and vx>0) or (x - r <= 0 and vx<0):
            vx *= ex
        if (abs(vx) > 0.01):
            vx -= f*vx*vx
        if (abs(vy) > 0.01):
            vy -= f*vy*vy
        if (abs(vy) < 0.01):
            vx = vx * 0.99
            vy = 0
        if (abs(vx) < 0.01):
            vx = 0
    screen.drawCircle(x, y, r, outline='black', fill=None, width = 3)

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()

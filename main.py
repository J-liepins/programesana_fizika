from screen import Screen
import math
import time

dragObj = False
saved_vx = 0
saved_vy = 0
prev_mouse_pos = (0, 0)
prev_time = time.time()
def clickCallback(event):
    global dragObj

    distance = math.sqrt((event.x - x)**2 + (event.y - y)**2)
    if distance <= r + w/2:
        dragObj = True
def releaseCallback(event):
    global dragObj
    global physics
    global vy
    global vx
    global saved_vx
    global saved_vy

    dragObj = False
    physics = True
    vy = saved_vy
    vx = saved_vx

def dragCallback(event):
    global dragObj
    global physics
    global x
    global y
    global prev_mouse_pos
    global prev_time
    global saved_vx
    global saved_vy

    if dragObj:
        physics = False
        x = event.x
        y = event.y
        current_time = time.time()
        elapsed_time = current_time - prev_time
        if elapsed_time > 0:
            saved_vx = 0.005*((event.x - prev_mouse_pos[0])/ elapsed_time)
            saved_vy = 0.005*((event.y - prev_mouse_pos[1])/ elapsed_time)
        prev_mouse_pos = (event.x, event.y)
        prev_time = current_time
    else:
        physics = True

screen = Screen(clickCallback, releaseCallback, dragCallback)
x = screen.SCR_WIDTH/2
y = screen.SCR_HEIGHT/2
physics = True
vx = 10
vy = 1

w = 3
r = 20
# elasticity
ey = -1.5
ex = -1.5
# f is proportional to rho and proportional to v^2
rho = 25
const = 0.0001
f = const * rho
while True:
    if physics:
        x += vx
        y += vy 
        vy+=screen.FRAME_TIME*9.81
        if (y + r >= screen.SCR_HEIGHT and vy>0) or (y - r <= 0 and vy<0):
            vy /= ey
        if (x + r >= screen.SCR_WIDTH and vx>0) or (x - r <= 0 and vx<0):
            vx /= ex
        if (abs(vx) > 0.01):
            vx = vx/abs(vx) * (abs(vx) - abs(f*vx))
        if (abs(vy) > 0.01):
            vy = vy/abs(vy) * (abs(vy) - abs(f*vy))
        if (abs(vy) < 0.01):
            vy = 0
        if (abs(vx) < 0.01):
            vx = 0
        print(vx, x)
    screen.drawCircle(x, y, r, outline='black', fill=None, width = w)

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()

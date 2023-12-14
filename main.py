from screen import Screen

screen = Screen()
def on_canvas_click(event):
    x = event.x
    y = event.y

x = 0
y = 0
vx = 10
vy = 1

r = 20
# elasticity
ey = -1.5
ex = -1.5
# f is proportional to rho and proportional to v^2
rho = 10
const = 0.001
f = const * rho
while True:
    x += vx
    y += vy 
    vy+=screen.FRAME_TIME*1
    if (y + r >= screen.SCR_HEIGHT and vy>0) or (y - r <= 0 and vy<0):
        vy /= ey
    if (x + r >= screen.SCR_WIDTH and vx>0) or (x - r <= 0 and vx<0):
        vx /= ex
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

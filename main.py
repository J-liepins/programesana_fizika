from screen import Screen

screen = Screen()
x = screen.SCR_WIDTH/2
y = screen.SCR_HEIGHT/2
vx = 2
vy = 1
while True:
    x += vx
    y += vy 
    vy+=screen.FRAME_TIME*9.81
    if (y >= screen.SCR_HEIGHT and vy>0) or (y <= 0 and vy<0):
        vy /= -1.2
    if (x >= screen.SCR_WIDTH and vx>0) or (x <= 0 and vx<0):
        vx *= -1
    # screen.drawLine([x - 5,y - 5, x + 5, y + 5])
    screen.drawCircle(x, y, 20, outline='black', fill=None, width = 5)

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()

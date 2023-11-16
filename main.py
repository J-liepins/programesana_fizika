from screen import Screen

screen = Screen()
x = 0
y = 0
vx = 1
vy = 1
while True:
    x += vx
    y += vy
    if y == screen.SCR_HEIGHT or y == 0:
        vy *= -1
    if x == screen.SCR_WIDTH or x == 0:
        vx *= -1
    # screen.drawLine([x - 5,y - 5, x + 5, y + 5])
    screen.drawCircle(x, y, 20, outline='black', fill=None, width = 5)

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()

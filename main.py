from screen import Screen

screen = Screen()
x = 0
y = 0
vx = 1
vy = 1
while True:
    x += vx
    y += vy
    # Draw line at x1 = 0  y1 = 0  x2 = 100  y2 = 100
    if y == screen.SCR_HEIGHT or y == 0:
        vy *= -1
    if x == screen.SCR_WIDTH or x == 0:
        vx *= -1
    screen.drawLine([x - 10,y - 10, x, y])

    # Draw stuff and delete old lines
    screen.mainloop()

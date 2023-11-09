from screen import Screen

screen = Screen()

i = 1
while True:
    i += 1
    
    # Draw line at x1 = 0  y1 = 0  x2 = 100  y2 = 100
    screen.drawLine([0, 0, 100, 100, 200, 100])

    # Draw stuff and delete old lines
    screen.mainloop()

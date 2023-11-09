from screen import Screen

screen = Screen()

i = 1
while True:
    i += 1
    screen.drawLine([0, 0, i, i])
    screen.mainloop()
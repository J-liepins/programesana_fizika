import math
from screen import Screen
from physics import PhysicsObject

dragObj = None
def clickCallback(event):
    global dragObj

    for obj in objs:
        distance = math.sqrt((event.x - obj.x)**2 + (event.y - obj.y)**2)
        if distance <= 60:
            dragObj = obj

def releaseCallback(event):
    global dragObj
    global objs
    dragObj.physics = True
    dragObj = None
    for obj in objs:
        obj.vy = 0

def dragCallback(event):
    global dragObj

    if dragObj is not None:
        dragObj.physics = False
        dragObj.x = event.x
        dragObj.y = event.y

screen = Screen(clickCallback, releaseCallback, dragCallback)
objs = [
    PhysicsObject(sx=100, sy=100),
    PhysicsObject(sx=300, sy=300)
]

while True:
    for obj in objs:
        obj.physics_update()
        screen.drawCircle(obj.x, obj.y, PhysicsObject.r, outline='black', fill=None, width = 3)

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()

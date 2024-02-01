import math
import random
from tkinter import messagebox
from screen import Screen
from physics_object import PhysicsObject
import time

dragObj = None
prev_mouse_pos = (0, 0)
prev_time = time.time()
def clickCallback(event):
    global dragObj


    for obj in objs:
        distance = math.sqrt((event.x - obj.x)**2 + (event.y - obj.y)**2)
        if distance <= PhysicsObject.r + 3/2:
            dragObj = obj

def releaseCallback(event):
    global dragObj
    global objs
    dragObj.physics = True
    dragObj = None
    

def dragCallback(event):
    global dragObj
    global prev_mouse_pos
    global prev_time
    global dragObj

    if dragObj is not None:
        dragObj.physics = False
        dragObj.x = event.x
        dragObj.y = event.y
       


        current_time = time.time()
        elapsed_time = current_time - prev_time
        if elapsed_time > 0:
            dragObj.vx = 0.005*((event.x - prev_mouse_pos[0])/ elapsed_time)
            dragObj.vy = 0.005*((event.y - prev_mouse_pos[1])/ elapsed_time)
        prev_mouse_pos = (event.x, event.y)
        prev_time = current_time

def rightClickCallback(event):
    global objs
    global screen
    # Get the values from the entry boxes
    vx_str = screen.entry_x.get()
    vy_str = screen.entry_y.get()

    # Check if either vx_str or vy_str is empty
    if vx_str == '' or vy_str == '':
        # Display an error message and return
        messagebox.showerror('Error', "Please enter values for vx and vy.")
        return
    vx_value = float(vx_str)
    vy_value = float(vy_str)
    objs.append(PhysicsObject(sx=event.x, sy=event.y, svx=vx_value, svy=vy_value))  # Create object with vx and vy values
    
screen = Screen(clickCallback, releaseCallback, dragCallback, rightClickCallback)


objs = [
PhysicsObject(sx=random.randint(0,1080), sy=random.randint(0,720)),
PhysicsObject(sx=random.randint(0,1080), sy=random.randint(0,720))
]


while True:
    for obj in objs:
        obj.physics_update(objs)
        screen.drawCircle(obj.x, obj.y, PhysicsObject.r, outline='black', fill=None, width = 3)

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()
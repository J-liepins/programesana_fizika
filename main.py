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
        if distance <= obj.r + 3/2:
            dragObj = obj

def releaseCallback(event):
    global dragObj
    global objs
    if dragObj is not None:
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

def generate_new_ball(existing_balls, click_x, click_y, min_distance=50):
    # Find the existing ball closest to the click position
    closest_ball = None
    min_distance_sq = float('inf')
    for ball in existing_balls:
        distance_sq = (click_x - ball.x)**2 + (click_y - ball.y)**2
        if distance_sq < min_distance_sq:
            closest_ball = ball
            min_distance_sq = distance_sq
    
    # Generate coordinates for the new ball next to the closest ball
    new_x = closest_ball.x + random.randint(-min_distance, min_distance)
    new_y = closest_ball.y + random.randint(-min_distance, min_distance)
    
    # Ensure the new coordinates are within the screen bounds
    new_x = max(min(new_x, Screen.SCR_WIDTH - 2*min_distance), 2*min_distance)
    new_y = max(min(new_y, Screen.SCR_HEIGHT - 2*min_distance), 2*min_distance)
    
    return new_x, new_y

def rightClickCallback(event):
    global objs
    global screen
    global other_obj
    
    

    # Get the values from the entry boxes
    vx_str = screen.entry_x.get()
    vy_str = screen.entry_y.get()
    r_str = screen.entry_r.get()
    m_str = screen.entry_m.get()
    


    # Check if either vx_str or vy_str is empty
    if vx_str == '' or vy_str == '' or r_str == '' or m_str == '':
        # Display an error message and return
        messagebox.showerror('Error', "Ievadiet visas vērtības")
        return
   
    vx_value = float(vx_str)
    vy_value = float(vy_str)
    r_value = float(r_str)
    m_value = float(m_str)

    # Generate new coordinates for the ball
    new_x, new_y = event.x, event.y
    
    # Check for overlap with existing balls
    overlap = False
    for ball in objs:
        distance = math.sqrt((new_x - ball.x)**2 + (new_y - ball.y)**2)
        if distance <= ball.r + r_value:
            overlap = True
            break
    
    # If there is overlap, generate new coordinates next to the closest ball
    if overlap:
        new_x, new_y = generate_new_ball(objs, event.x, event.y)

    objs.append(PhysicsObject(sx=new_x, sy=new_y, svx=vx_value, svy=vy_value, sr=r_value, sm=m_value))  # Create object with vx and vy valu
def resetCallback(event):
    global objs
    objs.clear()
     
screen = Screen(clickCallback, releaseCallback, dragCallback, rightClickCallback, resetCallback)
objs = [
PhysicsObject(sx=random.randint(0,1080), sy=random.randint(0,360)),
PhysicsObject(sx=random.randint(0,1080), sy=random.randint(0,360))
]


while True:
    for obj in objs:
        obj.physics_update(objs)
        screen.drawCircle(obj.x, obj.y, obj.r, outline='black', fill=None, width = 3)

    g_str = screen.slider_g.get()
    g_value = float(g_str)
    PhysicsObject.g = g_value
    ex_str = screen.slider_ex.get()
    ex_value = float(ex_str)*(-1)
    PhysicsObject.ex = ex_value
    ey_str = screen.slider_ey.get()
    ey_value = float(ey_str)*(-1)
    PhysicsObject.ey = ey_value
    f_str = screen.slider_f.get()
    f_value = float(f_str)
    PhysicsObject.f = f_value
    gf_str = screen.slider_gf.get()
    gf_value = float(gf_str)
    PhysicsObject.gf = gf_value
    eb_str = screen.slider_eb.get()
    eb_value = float(eb_str)
    PhysicsObject.eb = eb_value

    # Canvas outline
    screen.drawLine([0, 0, Screen.SCR_WIDTH, 0, Screen.SCR_WIDTH, Screen.SCR_HEIGHT, 0, Screen.SCR_HEIGHT, 0, 0])
    # Draw stuff and delete old lines
    screen.mainloop()
    
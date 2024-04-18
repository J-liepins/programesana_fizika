import tkinter as tk
from tkinter import Canvas, Entry
from tkinter import *
import time
import pyautogui 
class Screen:
    # Get with Screen.SCR_WIDTH or Screen.SCR_HEIGHT
    x,y = pyautogui.size()
    SCR_WIDTH = x
    SCR_HEIGHT = y
    # Seconds between frames for 60fps
    FRAME_TIME = 0.01666

    def __init__(self, clickCallback, releaseCallback, dragCallback, rightClickCallback, resetCallback):
        # Create window
        self.window = tk.Tk()
        self.window.attributes("-fullscreen", True)
        # Add canvas
        self.canvas = Canvas(self.window, width = Screen.SCR_WIDTH, height = Screen.SCR_HEIGHT)
        self.canvas.place(x = 0, y = 0)
        #self.canvas.grid(row=0, columnspan=15)

        # Canvas event callbacks
        self.canvas.bind('<Button-1>', clickCallback)
        self.canvas.bind('<Button-3>', rightClickCallback)
        self.canvas.bind('<ButtonRelease-1>', releaseCallback)
        self.canvas.bind('<B1-Motion>', dragCallback)
        self.window.bind('r', resetCallback)
        
        # Array of canvas lines to delete
        self.canvas_elements = []

        # Get last frame time
        self.last_update = Screen.getTime()  

        # Add entry boxes
        self.label1 = tk.Label(self.window, text="vx")
        self.label1.grid(row=1, column=0)

        self.entry_x = Entry(self.window)
        self.entry_x.insert(0, "0")
        self.entry_x.grid(row=1, column=1)

        self.label2 = tk.Label(self.window, text="vy")
        self.label2.grid(row=2, column=0)

        self.entry_y = Entry(self.window)
        self.entry_y.insert(0, "0")
        self.entry_y.grid(row=2, column=1)

        self.label3 = tk.Label(self.window, text="r")
        self.label3.grid(row=3, column=0)

        self.entry_r = Entry(self.window)
        self.entry_r.insert(0, "20")
        self.entry_r.grid(row=3, column=1)

        self.label4 = tk.Label(self.window, text="m")
        self.label4.grid(row=4, column=0)

        self.entry_m = Entry(self.window)
        self.entry_m.insert(0, "5")
        self.entry_m.grid(row=4, column=1)

        self.label5 = tk.Label(self.window, text="g")
        self.label5.grid(row=5, column=0)

        self.slider_g = tk.Scale(self.window, from_=0, to=20, orient=HORIZONTAL, resolution = 0.01)
        self.slider_g.set(1)
        self.slider_g.grid(row=5, column=1)

        self.label6 = tk.Label(self.window, text="elasticity x")
        self.label6.grid(row=1, column=2)

        self.slider_ex = tk.Scale(self.window, from_=0, to=1, orient=HORIZONTAL, resolution = 0.01)
        self.slider_ex.set(1)
        self.slider_ex.grid(row=1, column=3)

        self.label7 = tk.Label(self.window, text="elasticity y")
        self.label7.grid(row=2, column=2)

        self.slider_ey = tk.Scale(self.window, from_=0, to=1, orient=HORIZONTAL, resolution = 0.01)
        self.slider_ey.set(1)
        self.slider_ey.grid(row=2, column=3)

        self.label8 = tk.Label(self.window, text="gaisa pretestība")
        self.label8.grid(row=3, column=2)

        self.slider_f = tk.Scale(self.window, from_=0, to=1, orient=HORIZONTAL, resolution = 0.01)
        self.slider_f.set(0)
        self.slider_f.grid(row=3, column=3)

        self.label9 = tk.Label(self.window, text="berze")
        self.label9.grid(row=4, column=2)

        self.slider_gf = tk.Scale(self.window, from_=0, to=1, orient=HORIZONTAL, resolution = 0.01)
        self.slider_gf.set(1)
        self.slider_gf.grid(row=4, column=3)

        self.label10 = tk.Label(self.window, text="elasticity b")
        self.label10.grid(row=5, column=2)

        self.slider_eb = tk.Scale(self.window, from_=0, to=1, orient=HORIZONTAL, resolution = 0.01)
        self.slider_eb.set(1)
        self.slider_eb.grid(row=5, column=3)


        # Ignore this
        super().__init__()

    def getTime():
        return time.time()

    def mainloop(self):
        # Update window
        self.window.update_idletasks()
        self.window.update()
        
        # Delete old lines
        while len(self.canvas_elements) > 0:
            line_id = self.canvas_elements.pop()
            self.canvas.delete(line_id)

        # Now time
        time_now = Screen.getTime()
        # Time since last update
        delta_time = time_now - self.last_update
        # Time to wait for 60fps
        time_to_wait = Screen.FRAME_TIME - delta_time
        # If not negative, then wait it
        # if (time_to_wait > 0): time.sleep(time_to_wait)
        # Update last_update time
        self.last_update = Screen.getTime() 
         

    def drawLine(self, points, color = 'black', width = 3):
        # Draw line and add id to be deleted next frame
        canvas_line_id = self.canvas.create_line(points, fill=color, width=width)
        self.canvas_elements.append(canvas_line_id)

    def drawCircle(self, x, y, radius = 10, fill = None, outline = 'black', width = 10):
        # Draw circle and add id to be deleted next frame
        canvas_circle_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=fill, outline=outline, width=width)
        self.canvas_elements.append(canvas_circle_id)


import tkinter as tk
from tkinter import Canvas, Entry, Button, messagebox
import time


class Screen:
    # Get with Screen.SCR_WIDTH or Screen.SCR_HEIGHT
    SCR_WIDTH = 1080
    SCR_HEIGHT = 720
    
    # Seconds between frames for 60fps
    FRAME_TIME = 0.01666

    def __init__(self, clickCallback, releaseCallback, dragCallback, rightClickCallback):
        # Create window
        self.window = tk.Tk()
        
        # Add canvas
        self.canvas = Canvas(self.window, width=Screen.SCR_WIDTH, height=Screen.SCR_HEIGHT)
        self.canvas.pack()

        # Canvas event callbacks
        self.canvas.bind('<Button-1>', clickCallback)
        self.canvas.bind('<Button-3>', rightClickCallback)
        self.canvas.bind('<ButtonRelease-1>', releaseCallback)
        self.canvas.bind('<B1-Motion>', dragCallback)
        
        # Array of canvas lines to delete
        self.canvas_elements = []

        # Get last frame time
        self.last_update = Screen.getTime()  

        # Add entry boxes
        self.entry_x = Entry(self.window)
        self.entry_y = Entry(self.window)
        self.entry_x.pack(side=tk.LEFT)
        self.entry_y.pack(side=tk.LEFT)

        # Add submit button
        self.submit_button = Button(self.window, text="Submit", command=self.submit_data)
        self.submit_button.pack(side=tk.LEFT)     

        # Ignore this
        super().__init__()

    def submit_data(self):
        # Get the values from the entry boxes
        x_value = self.entry_x.get()
        y_value = self.entry_y.get()
        messagebox.showinfo('Submitted', "Your data is submitted successfully!" + x_value + y_value) 
        self.entry_x.delete(0, 'end') 
        self.entry_y.delete(0, 'end')

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

import tkinter as tk
from tkinter import Canvas
import time

class Screen:
    # Get with Screen.SCR_WIDTH or Screen.SCR_HEIGHT
    SCR_WIDTH = 1080
    SCR_HEIGHT = 720
    
    # Seconds between frames for 60fps
    FRAME_TIME = 0.01666

    def __init__(self):
        # Create window
        self.window = tk.Tk()
        
        # Add canvas
        self.canvas = Canvas(self.window, width=Screen.SCR_WIDTH, height=Screen.SCR_HEIGHT)
        self.canvas.pack()
        
        # Array of canvas lines to delete
        self.canvas_elements = []

        # Get last frame time
        self.last_update = Screen.getTimeMs()        

        # Ignore this
        super().__init__()

    def getTimeMs():
        return round(time.time() * 1000)

    def mainloop(self):
        # Update window
        self.window.update_idletasks()
        self.window.update()
        
        # Delete old lines
        while len(self.canvas_elements) > 0:
            line_id = self.canvas_elements.pop()
            self.canvas.delete(line_id)

        # Now time
        time_now = Screen.getTimeMs()
        # Time since last update
        delta_time = time_now - self.last_update
        # Time to wait for 60fps
        time_to_wait = Screen.FRAME_TIME - delta_time
        # If not negative, then wait it
        # if (time_to_wait > 0): time.sleep(time_to_wait)
        # Update last_update time
        self.last_update = Screen.getTimeMs()

    def drawLine(self, points, color = 'black', width = 3):
        # Draw line and add id to be deleted next frame
        canvas_line_id = self.canvas.create_line(points, fill=color, width=width)
        self.canvas_elements.append(canvas_line_id)

    def drawCircle(self, x, y, radius = 10, fill = None, outline = 'black', width = 10):
        # Draw circle and add id to be deleted next frame
        canvas_circle_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=fill, outline=outline, width=width)
        self.canvas_elements.append(canvas_circle_id)

    
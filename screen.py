import tkinter as tk
from tkinter import Canvas

class Screen:
    # Get with Screen.SCR_WIDTH or Screen.SCR_HEIGHT
    SCR_WIDTH = 1080
    SCR_HEIGHT = 720

    def __init__(self):
        # Create window
        self.window = tk.Tk()
        
        # Add canvas
        self.canvas = Canvas(self.window, width=Screen.SCR_WIDTH, height=Screen.SCR_HEIGHT)
        self.canvas.pack()
        
        # Array of canvas lines to delete
        self.canvas_lines = []

        # Ignore this
        super().__init__()

    def mainloop(self):
        # Update window
        self.window.update_idletasks()
        self.window.update()
        
        # Delete old lines
        for line_id in self.canvas_lines:
            self.canvas.delete(line_id)

    def drawLine(self, points, color = 'black', width = 10):
        # Draw line and add id to be deleted next frame
        canvas_line_id = self.canvas.create_line(points, fill=color, width=width)
        self.canvas_lines.append(canvas_line_id)
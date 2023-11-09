import tkinter as tk
from tkinter import Canvas

class Screen:
    SCR_WIDTH = 1080
    SCR_HEIGHT = 720

    def __init__(self):
        self.window = tk.Tk()
        self.canvas = Canvas(self.window, width=Screen.SCR_WIDTH, height=Screen.SCR_HEIGHT)
        self.canvas.pack()
        self.canvas_lines = []
        super().__init__()

    def mainloop(self):
        self.window.update_idletasks()
        self.window.update()
        for line_id in self.canvas_lines:
            self.canvas.delete(line_id)

    def drawLine(self, points, color = 'black', width = 2):
        canvas_line_id = self.canvas.create_line(points, fill=color, width=width)
        self.canvas_lines.append(canvas_line_id)
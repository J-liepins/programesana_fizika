import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Some test text")
label.pack()
window.mainloop()
while y > 0:
ay = -g
y += vy * dt # use old vy to calculate new y
vy += ay * dt # use old ay to calculate new vy
t += dt
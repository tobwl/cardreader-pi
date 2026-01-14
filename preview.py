import tkinter as tk
from PIL import Image, ImageTk
import render
import importlib

SCALE = 3
REFRESH_MS = 1000

fake_stats = {
    "uptime": "03 : 02 : 04",
    "wifi": 2,
    "busy": True
}

config = {
    "font": "C:/Windows/Fonts/segoeui.ttf", 
    "font_bold": "C:/Windows/Fonts/segoeuib.ttf"
}

root = tk.Tk()
root.title("E-Ink Preview")

label = tk.Label(root)
label.pack()

def update_preview():
    global tk_img
    importlib.reload(render)

    img = render.render_screen(fake_stats, config)

    # Scale up for visibility
    img = img.resize((img.width * SCALE, img.height * SCALE), Image.NEAREST)
    
    tk_img = ImageTk.PhotoImage(img)

    label.config(image=tk_img)

    root.after(REFRESH_MS, update_preview)

update_preview()
root.mainloop()
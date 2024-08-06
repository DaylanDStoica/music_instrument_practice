
# Develop GUI module 


import tkinter as tk
def create_window(
        window_width = 300,
        window_height = 300,
        window_offsetx = 100,
        window_offsety = 100,
    ):
    # window = tk.Tk()
    # window.title("Hello World")
    root = tk.Tk()
    root.mainloop()
    root.minsize(200, 200)
    root.maxsize(500,500)
    # window_width = 300
    # window_height = 300
    # window_offsetx = 100
    # window_offsety = 100
    # root.geometry("300x300+100+100")
    root.geometry("%sx%s+%s+%s" % ( window_width, window_height, window_offsetx, window_offsety))

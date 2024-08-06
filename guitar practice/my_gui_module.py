
# Develop GUI module 


import tkinter as tk

class MyWindowClass:
    def __init__( self,
        window_width = 300,
        window_height = 300,
        window_offsetx = 100,
        window_offsety = 100,
        title = "guitar chord practice"
        ):
        
        self.window_width = window_width
        self.window_height = window_height
        self.window_offsetx = window_offsetx
        self.window_offsety = window_offsety
        self.title = title
        
    def create_window(self):
        # window = tk.Tk()
        # window.title("Hello World")
        root = tk.Tk()
        root.minsize(200, 200)
        root.maxsize(500,500)

        root.geometry("%sx%s+%s+%s" % ( self.window_width, self.window_height, self.window_offsetx, self.window_offsety))
        root.title(self.title) # set label of window
        root.mainloop() # keep this line at the bottom
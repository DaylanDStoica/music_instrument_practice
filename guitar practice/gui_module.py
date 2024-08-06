
# Develop GUI module 


import tkinter as tk
def create_window():
    # window = tk.Tk()
    # window.title("Hello World")
    root = tk.Tk()
    root.mainloop()
    root.minsize(200, 200)
    root.maxsize(500,500)
    root.geometry("300x300+100+100")


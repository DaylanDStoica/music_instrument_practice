
import guitar_chord_practice as guitar



'''
TODO: build main, to take in command args
for duration of wait hold times, and if there should be button input to continue"
'''

'''
TODO: develop GUI 
'''

import tkinter as tk
def create_window():
    # window = tk.Tk()
    # window.title("Hello World")
    root = tk.Tk()
    root.mainloop()
    root.minsize(200, 200)
    root.maxsize(500,500)
    root.geometry("300x300+100+100")


def main():
    # guitar.provided_chord_holds(2, True)
    create_window()


main()



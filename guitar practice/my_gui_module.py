
# Develop GUI module 


import tkinter as tk

import guitar_chord_practice as gc_prac
from time import sleep
import random

CHORD_TEXT_FILE = "guitar_chords_tab.txt"

        


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
        

    def next_chord(self):
        pass

    def create_window(self):
        # window = tk.Tk()
        # window.title("Hello World")
        root = tk.Tk()
        root.minsize(200, 200)
        root.maxsize(500,500)

        root.geometry("%sx%s+%s+%s" % ( self.window_width, self.window_height, self.window_offsetx, self.window_offsety))
        root.title(self.title) # set label of window

        root.title("guitar chords")

        frame = tk.Frame(root)
        frame.grid()

        tk.Button(frame, text="Next chord", command=self.next_chord()).grid(column=0, row=0)
        tk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)


        self.window = root

        root.mainloop() # keep this line at the bottom
        
        

    def gui_provided_chord_holds ( self, time_gaps = 1.0 , wait_for_input = False):
        # every X seconds (time_gaps), print a new chord to play
        # repeat until exit program, Ctrl+Q
        chord_file_access = open(CHORD_TEXT_FILE, 'r')
        # chords = chord_file_access.split('\n')
        chords = chord_file_access.read().splitlines()
        # print(" running from the chord list of : ")
        # print("         ", chords)

        # create the window
        self.create_window()
        # set the grid for displaying the window
        frame = tk.Frame(self.window, padding = 10)
        frame.grid()
        tk.ttk.Label(frame, text = " running from the chord list of :        %s" % chords).grid( column=0, row = 0)

        while ( True):
            sleep(time_gaps)
            if wait_for_input: # wait for user input before generating next chord
                # input("Button press when ready: ")
                tk.ttk.Button (frame, text="Next chord").grid(column=3, row=0)
            rand_chord = random.choice(chords)
            # print( rand_chord, " chord" )
            tk.ttk.Label(self.window, text = "%s  chord" % rand_chord)

            self.window.mainloop()
        # TODO: change command line prints to text within the GUI window
        # self.window.mainloop()

    def learning_gui_window(self):
        # for learning how the gui interactions work, comment out while testing
        root = tk.Tk()
        root.title("Hello world!")
        root.geometry("400x400")
        # frm = tk.Frame(root, padding = 10)
        frm = tk.Frame(root)
        frm.grid()
        tk.Label(frm, text="Hello World!").grid(column=0, row=0)
        tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        root.mainloop() 

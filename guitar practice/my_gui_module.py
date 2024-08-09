
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
        
    def create_window(self):
        # window = tk.Tk()
        # window.title("Hello World")
        root = tk.Tk()
        root.minsize(200, 200)
        root.maxsize(500,500)

        root.geometry("%sx%s+%s+%s" % ( self.window_width, self.window_height, self.window_offsetx, self.window_offsety))
        root.title(self.title) # set label of window
        root.mainloop() # keep this line at the bottom

        self.window = root


    def gui_provided_chord_holds ( self, time_gaps = 1.0 , wait_for_input = False):
        # every X seconds (time_gaps), print a new chord to play
        # repeat until exit program, Ctrl+Q
        chord_file_access = open(CHORD_TEXT_FILE, 'r')
        # chords = chord_file_access.split('\n')
        chords = chord_file_access.read().splitlines()
        print(" running from the chord list of : ")
        print("         ", chords)
        while ( True):
            sleep(time_gaps)
            if wait_for_input: # wait for user input before generating next chord
                input("Button press when ready: ")
            rand_chord = random.choice(chords)
            print( rand_chord, " chord" )

        # TODO: change command line prints to text within the GUI window
        self.window.mainloop()
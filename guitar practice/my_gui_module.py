
# Develop GUI module 


import tkinter as tk

import guitar_chord_practice as gc_prac
from time import sleep
import random

CHORD_TEXT_FILE = "guitar_chords_tab.txt"

        
current_chord_label = ""
chord_label = tk.Tk

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
        self.chord_label_text = ""
        
        

    def next_chord(self, chord_list):
        # for the next button on the gui window, 
        # display the next randomly chosen chord in the window
        chord_choice = random.choice(chord_list)

        global current_chord_label
        current_chord_label = chord_choice
        self.chord_label_text = chord_choice
        # self.window_frame.
        # tk.Label(self.window_frame, text = self.chord_label).grid(column=1, row=3)
        # self.chord_label.config(text = self.chord_label_text)

        self.chord_label.config(text = self.chord_label_text)
        # self.chord_label.config(text = current_chord_label)
        # return chord_choice
        self.window.mainloop()


    def next_chord2(self):
        
        filename = open(CHORD_TEXT_FILE, 'r')
        chords = filename.read().splitlines()
        
        chord_choice = random.choice(chords)
        self.chord_label_text = chord_choice

        # return chord_choice
        global current_chord_label 
        current_chord_label= chord_choice
        # self.chord_label.config(text = self.chord_label_text)
        self.chord_label = current_chord_label
        print("new chord selected and inputted: " + chord_choice)
        filename.close()
        return chord_choice

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


        self.window = root
        self.window_frame = frame

        filename = open(CHORD_TEXT_FILE, 'r')
        chords = filename.read().splitlines()
        
        tk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
        chord_label = tk.Label(frame, text = self.chord_label_text)
        chord_label.grid(column=1, row=3)
        self.chord_label = chord_label
        

        next_button = tk.Button(frame, text="Next chord", 
                                # command=self.next_chord(chords)).grid(column=0, row=0)
        )
        # next_button.config(command=self.next_chord(chords))
        next_button.config(
            command=chord_label.config(text = self.next_chord2()))
        next_button.grid(row=1,column=1)

        junk_button = tk.Button(frame, text="print junk", command=print(" junk button pressed")).grid(row=4)

        # chord_label.config(text = self.chord_label_text)

        
        # self.window = root
        # self.window_frame = frame
        # self.next_button = next_button
        
        # chord_label.pack()

        root.mainloop() # keep this line at the bottom
        # TODO: find place for mainloop, to allow 'next chord' button to change visible text
        
        

    # def gui_provided_chord_holds ( self, time_gaps = 1.0 , wait_for_input = False):
    #     # every X seconds (time_gaps), print a new chord to play
    #     # repeat until exit program, Ctrl+Q
    #     chord_file_access = open(CHORD_TEXT_FILE, 'r')
    #     # chords = chord_file_access.split('\n')
    #     chords = chord_file_access.read().splitlines()
    #     # print(" running from the chord list of : ")
    #     # print("         ", chords)

    #     # create the window
    #     self.create_window()
    #     # set the grid for displaying the window
    #     frame = tk.Frame(self.window, padding = 10)
    #     frame.grid()
    #     tk.ttk.Label(frame, text = " running from the chord list of :        %s" % chords).grid( column=0, row = 0)

    #     while ( True):
    #         sleep(time_gaps)
    #         if wait_for_input: # wait for user input before generating next chord
    #             # input("Button press when ready: ")
    #             tk.ttk.Button (frame, text="Next chord").grid(column=3, row=0)
    #         rand_chord = random.choice(chords)
    #         # print( rand_chord, " chord" )
    #         tk.ttk.Label(self.window, text = "%s  chord" % rand_chord)

    #         self.window.mainloop()
    #     # TODO: change command line prints to text within the GUI window
    #     # self.window.mainloop()

    # def learning_gui_window(self):
    #     # for learning how the gui interactions work, comment out while testing
    #     root = tk.Tk()
    #     root.title("Hello world!")
    #     root.geometry("400x400")
    #     # frm = tk.Frame(root, padding = 10)
    #     frm = tk.Frame(root)
    #     frm.grid()
    #     tk.Label(frm, text="Hello World!").grid(column=0, row=0)
    #     tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    #     root.mainloop() 

    def create_window2(self):

        root = tk.Tk()
        root.minsize(200, 200)
        root.maxsize(500,500)

        root.geometry("%sx%s+%s+%s" % ( self.window_width, self.window_height, self.window_offsetx, self.window_offsety))
        root.title(self.title) # set label of window

        root.title("guitar chords")

        # frame = tk.Frame(root)
        # frame.grid()


        self.window = root
        # self.window_frame = frame

        # filename = open(CHORD_TEXT_FILE, 'r')
        # chords = filename.read().splitlines()
        
        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        chord_label = tk.Label(root, text = self.chord_label_text)
        self.chord_label = chord_label
        # self.next_chord(chords)

        next_button = tk.Button(root, text="Next chord", command=self.next_chord2())

        next_button.pack()
        quit_button.pack()
        chord_label.pack()

        # root.mainloop()
        return root
    


class MyNiceWindowClass:
    def __init__(self):
        print("nice window made")
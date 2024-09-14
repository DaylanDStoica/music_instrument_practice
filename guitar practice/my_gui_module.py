
# Develop GUI module 


from nicegui import ui, app

# import guitar_chord_practice as gc_prac
from time import sleep
import random


CHORD_TEXT_FILE = "guitar_chords_tab.txt"

# return the string of a chord and fret counts, randomly chosen from the list of chords
def get_random_chord():
    filename = open(CHORD_TEXT_FILE, 'r')
    chords_list = filename.read().splitlines()
    chord_choice = random.choice(chords_list)

    filename.close()

    return chord_choice 

class MyNiceWindowClass:
    def __init__(self):
        print("nice window made")
        self.auto_rotation_bool = False # variable for choose the method of new chord display.
        # False: user must manually press button to call for next Chord
        # True: new chord will be presented automatically after set seconds
        self.chord_time = 3

    def auto_run_chords(self):
        # to be run when the AutoRequest toggle is set to on
        # every x seconds, send up a message of a random chord
        
        # create a thread for handling the time passing and chord calling
        pass

    def set_chord_time(self, new_timer):
        self.chord_time = new_timer
    def create_window(self):
        ui.label("Instrument practice > Guitar Practice > chords")

        # using the notification attribute to create refreshing chord requests
        new_chord_string = get_random_chord()
        next_button = ui.button("Next Chord", on_click=lambda: 
                                # ui.notify(new_chord_string) )
                                ui.notify(get_random_chord()) )
        
        #shutdown button, shuts off connection to browser page
        # acts as a server shutoff
        ui.button("end connection", on_click=app.shutdown)

        # TODO: develop boolean tracking for the toggle switch
        auto_rotation_bool = ui.toggle({1: "Auto request" , 0: "Click for new request" }) # 1 = True for auto-rotate,0 = False for auto-rotate, manual rotation
        self.auto_rotation_bool = auto_rotation_bool
        print(self.auto_rotation_bool)
        # Auto request, on: generate new message every X seconds
        # Click for new request, on: wait for "Next Chord" button press to display new message
        # both off: show nothing until a choice is made.

        ui.run(reload=False) # reload=False to allow app program server shutdown


from PySide6 import QtGui
class MyQtWindowClass:
    def __init__(self):
        print("creating a qt window")

    def create_window(self):
        pass
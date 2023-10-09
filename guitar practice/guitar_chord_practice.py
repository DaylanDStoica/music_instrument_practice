
# contains practice examples for practicing guitar pieces 

import random
from time import sleep
def random_chord_holds( time_gaps = 1.0 , wait_for_input = False):
    # every X seconds (time_gaps), print a new chord to play
    # repeat until exit program, Ctrl+Q
    chords = "E A D C G E_minor A_minor D_minor C7 G7 E7 A7 D7 F B7".split()
    print(" running from the chord list of : ")
    print("         ", chords)
    while ( True):
        sleep(time_gaps)
        if wait_for_input: # wait for user input before generating next chord
            input("Button press when ready: ")
        rand_chord = random.choice(chords)
        print( rand_chord, " chord" )


random_chord_holds(2, True)

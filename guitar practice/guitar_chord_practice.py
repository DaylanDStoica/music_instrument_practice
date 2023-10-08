
# contains practice examples for practicing guitar pieces 

import random
from time import sleep
def random_chord_holds( time_gaps = 1.0 ):
    # every X seconds (time_gaps), print a new chord to play
    # repeat until exit program, Ctrl+Q
    chords = ["C", "Dm", "C sharp"]
    while ( True):
        sleep(time_gaps)

        rand_chord = random.choice(chords)
        print( rand_chord, " chord" )


random_chord_holds(2)

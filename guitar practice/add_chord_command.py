CHORD_TEXT_FILE = "guitar_chords_tab.txt"

chord_name = "" 
fret_placement = "XXXXXX" # 6 chars, representing the fret of each string 

file_access = open(CHORD_TEXT_FILE, 'a')
def addChordToFile( chord_and_fret_string): 
    #f = open( CHORD_TEXT_FILE, 'a') #append to the file
    # chord_and_fret = input("chord name, fret: ")
    
    # parse the string for placement
    chord_name, fret_placement = chord_and_fret_string.split() 
    in_string = chord_name + " = " + fret_placement
    
    file_access.write(in_string) 
    
    
def loopAddChords():
    chord_and_fret = input("chord_name fret: ")
    while( chord_and_fret != ""): # while the string is not empty
        addChordToFile(chord_and_fret)
        
    file_access.close()
    
loopAddChords()
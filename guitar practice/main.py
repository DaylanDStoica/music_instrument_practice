
import guitar_chord_practice as guitar



'''
TODO: build main, to take in command args
for duration of wait hold times, and if there should be button input to continue"
'''

'''
TODO: develop GUI 
'''

import my_gui_module as gui

#this main will use the MyNiceWindow class, using NiceGUI
# from nicegui import ui
# import my_gui_module as gui
def main2():
    # # ui.label("hello world")

    # ui.label("guitar practice : chords")

    # ui.run()
    
    my_nice_window = gui.MyNiceWindowClass()
    my_nice_window.create_window()
    my_nice_window.window_loop()

main2()

#this main will use QT gui, 
def main3():
    my_qt_window = gui.MyQtWindowClass()
    my_qt_window.create_window()


# main3()
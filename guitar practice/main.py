
import guitar_chord_practice as guitar



'''
TODO: build main, to take in command args
for duration of wait hold times, and if there should be button input to continue"
'''

'''
TODO: develop GUI 
'''

import my_gui_module as gui
def main():
    # guitar.provided_chord_holds(2, True)
    # gui.create_window()
    MyWindow = gui.MyWindowClass()
    MyWindow.create_window()
    # MyWindow.create_window2()

    # MyWindow.display_chord()
    # MyWindow.gui_provided_chord_holds()
    # while(True):
    # MyWindow.create_window()
    # MyWindow.window.mainloop()

    # # MyWindow.create_window()
    # MyWindow.window.mainloop()
    # # MyWindow.create_window()
    # MyWindow.window.mainloop()
    # # MyWindow.create_window()
    # MyWindow.window.mainloop()

    # TODO: setup conditional loop for the random chord displayer
    # window_body = MyWindow.create_window()
    # window_body.mainloop()
    print("create window")

# main()


#this main will use the MyNiceWindow class, using NiceGUI
# from nicegui import ui
# import my_gui_module as gui
def main2():
    # # ui.label("hello world")

    # ui.label("guitar practice : chords")

    # ui.run()
    
    my_nice_window = gui.MyNiceWindowClass()
    my_nice_window.create_window()

main2()

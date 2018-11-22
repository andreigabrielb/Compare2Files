import Tkinter # Library for UI 
import random  # import for random genaration 

def random_number():
    #This function returns a random number
    my_random = random.randint(1, 10)
    dice_thrown.configure(text = "Chance was: " + str(my_random))

"""
def generate_UI():
    #This function will genarate all of the UI elements for this application
    main_window = Tkinter.Tk("Main")

    MyTitle = Tkinter.Label(main_window, SystemExit="Generate random number")
    MyTitle.pack()

    generate_button = Tkinter.Button(main_window, text = "Generate", command  = random_number)
    generate_button.pack()

    main_window.mainloop()
"""

main_window = Tkinter.Tk()

MyTitle = Tkinter.Label(main_window, SystemExit="Generate random number")
MyTitle.pack()
"""
generate_button = Tkinter.Button(main_window, text = "Generate", command  = random_number)
generate_button.pack()

dice_throw = Tkinter.Label(main_window)
dice_throw.pack()
"""
main_window.mainloop()
